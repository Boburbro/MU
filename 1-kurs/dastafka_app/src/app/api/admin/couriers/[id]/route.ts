import { NextResponse } from 'next/server';
import dbConnect from '@/lib/db';
import User from '@/models/User';
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

        const user = await User.findByIdAndUpdate(
            params.id,
            { isVerified: true },
            { new: true }
        ).select('-password');

        if (!user) return NextResponse.json({ error: 'User not found' }, { status: 404 });

        return NextResponse.json({ success: true, user });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
