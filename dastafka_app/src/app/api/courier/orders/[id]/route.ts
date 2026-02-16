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

export async function PUT(req: Request, { params }: { params: { id: string } }) {
    try {
        await dbConnect();
        const courier = await getCourierUser();
        if (!courier) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const body = await req.json();
        const { action } = body; // 'accept', 'pickup', 'deliver'

        const order = await Order.findById(params.id);
        if (!order) return NextResponse.json({ error: 'Order not found' }, { status: 404 });

        // Logic for actions
        if (action === 'accept') {
            if (order.status !== 'approved') return NextResponse.json({ error: 'Order not available' }, { status: 400 });
            if (order.courierId) return NextResponse.json({ error: 'Order already taken' }, { status: 400 });

            order.courierId = courier.userId;
            order.status = 'picked_up'; // Or separate 'assigned' status. Let's say 'picked_up' means "I am responsible now" for simplicity or add 'assigned'.
            // Wait, let's look at Schema.
            // Schema enum: ['pending_admin', 'approved', 'picked_up', 'delivered', 'cancelled']
            // So 'approved' -> 'picked_up' (on way to pickup? or actually picked up?)
            // Let's assume 'picked_up' means "Courier accepted and is handling it".
            order.status = 'picked_up';
        }
        else if (action === 'deliver') {
            if (order.courierId.toString() !== courier.userId) return NextResponse.json({ error: 'Not your order' }, { status: 403 });
            if (order.status !== 'picked_up') return NextResponse.json({ error: 'Order flow error' }, { status: 400 });

            order.status = 'delivered';
        } else {
            return NextResponse.json({ error: 'Invalid action' }, { status: 400 });
        }

        await order.save();

        return NextResponse.json({ success: true, order });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
