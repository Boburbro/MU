import { NextResponse } from 'next/server';
import dbConnect from '@/lib/db';
import Order from '@/models/Order';
import jwt from 'jsonwebtoken';
import { headers } from 'next/headers';

const getCourierUser = async () => {
    const headersList = await headers();
    const authHeader = headersList.get('authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) return null;

    const token = authHeader.split(' ')[1];
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;
        if (decoded.role !== 'courier') return null;
        return decoded;
    } catch (error) {
        return null;
    }
};

export async function GET(req: Request) {
    try {
        await dbConnect();
        const courier = await getCourierUser();
        if (!courier) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        // 1. Available orders: Status 'approved' AND courierId is null
        const availableOrders = await Order.find({
            status: 'approved',
            courierId: null
        }).populate('userId', 'name').sort({ createdAt: -1 });

        // 2. My active orders: courierId is ME
        const myOrders = await Order.find({
            courierId: courier.userId
        }).populate('userId', 'name').sort({ updatedAt: -1 });

        return NextResponse.json({ success: true, availableOrders, myOrders });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
