import { NextResponse } from 'next/server';
import dbConnect from '@/lib/db';
import Order from '@/models/Order';
import jwt from 'jsonwebtoken';
import { headers } from 'next/headers';

const getAdminUser = async () => {
    const headersList = await headers();
    const authHeader = headersList.get('authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) return null;

    const token = authHeader.split(' ')[1];
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;
        if (decoded.role !== 'admin') return null;
        return decoded;
    } catch (error) {
        return null;
    }
};

export async function PUT(req: Request, { params }: { params: { id: string } }) {
    try {
        await dbConnect();
        const admin = await getAdminUser();
        if (!admin) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const body = await req.json();
        const { status } = body; // 'approved' or 'rejected'/'cancelled'

        if (!orderStatusIsValid(status)) {
            return NextResponse.json({ error: 'Invalid status' }, { status: 400 });
        }

        const order = await Order.findByIdAndUpdate(
            params.id,
            { status },
            { new: true }
        );

        if (!order) return NextResponse.json({ error: 'Order not found' }, { status: 404 });

        return NextResponse.json({ success: true, order });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}

function orderStatusIsValid(status: string) {
    return ['approved', 'cancelled'].includes(status);
}
