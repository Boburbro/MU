import { NextResponse } from 'next/server';
import dbConnect from '@/lib/db';
import Order from '@/models/Order';
import jwt from 'jsonwebtoken';
import { headers } from 'next/headers';

// Helper to get user from token
const getUserFromToken = async () => {
    const headersList = await headers();
    const authHeader = headersList.get('authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return null;
    }

    const token = authHeader.split(' ')[1];
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET!);
        return decoded as { userId: string, role: string };
    } catch (error) {
        return null;
    }
};

export async function POST(req: Request) {
    try {
        await dbConnect();
        const user = await getUserFromToken();

        if (!user) {
            return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
        }

        const body = await req.json();
        const { itemDescription, fromLocation, toLocation } = body;

        const order = await Order.create({
            userId: user.userId,
            itemDescription,
            fromLocation: { address: fromLocation }, // Simplified for now, expecting string
            toLocation: { address: toLocation },     // Simplified
            status: 'pending_admin',
        });

        return NextResponse.json({ success: true, order }, { status: 201 });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}

export async function GET(req: Request) {
    try {
        await dbConnect();
        const user = await getUserFromToken();

        if (!user) {
            return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
        }

        // If user is admin/courier, logic might differ, but for this specific route 
        // we might stick to "User's orders". 
        // Or we can leave this generic for "My Created Orders"
        const orders = await Order.find({ userId: user.userId }).sort({ createdAt: -1 });

        return NextResponse.json({ success: true, orders });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
