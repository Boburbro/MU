'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';

export default function AdminDashboard() {
    const { user, logout, isLoading } = useAuth();
    const router = useRouter();
    const [couriers, setCouriers] = useState<any[]>([]);
    const [orders, setOrders] = useState<any[]>([]);
    const [msg, setMsg] = useState({ type: '', content: '' });

    useEffect(() => {
        if (!isLoading && (!user || user.role !== 'admin')) {
            router.push('/login');
        } else if (user && user.role === 'admin') {
            fetchData();
        }
    }, [user, isLoading, router]);

    const fetchData = async () => {
        try {
            const token = localStorage.getItem('token');
            const headers = { 'Authorization': `Bearer ${token}` };

            const [resCouriers, resOrders] = await Promise.all([
                fetch('/api/admin/couriers', { headers }),
                fetch('/api/admin/orders', { headers })
            ]);

            const dataCouriers = await resCouriers.json();
            const dataOrders = await resOrders.json();

            if (dataCouriers.success) setCouriers(dataCouriers.couriers);
            if (dataOrders.success) setOrders(dataOrders.orders);

        } catch (err) {
            console.error(err);
        }
    };

    const verifyCourier = async (id: string) => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`/api/admin/couriers/${id}`, {
                method: 'PUT',
                headers: { 'Authorization': `Bearer ${token}` }
            });
            const data = await res.json();
            if (data.success) {
                setMsg({ type: 'success', content: 'Courier verified successfully' });
                fetchData();
            } else {
                setMsg({ type: 'error', content: data.error });
            }
        } catch (err) {
            setMsg({ type: 'error', content: 'Failed to verify courier' });
        }
    };

    const updateOrderStatus = async (id: string, status: string) => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`/api/admin/orders/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ status })
            });
            const data = await res.json();
            if (data.success) {
                setMsg({ type: 'success', content: `Order ${status} successfully` });
                fetchData();
            } else {
                setMsg({ type: 'error', content: data.error });
            }
        } catch (err) {
            setMsg({ type: 'error', content: 'Failed to update order' });
        }
    };

    if (isLoading || !user) return <div className="container" style={{ padding: '2rem' }}>Loading...</div>;

    return (
        <main>
            <nav style={{ padding: '1rem 0', borderBottom: '1px solid var(--bg-input)', backgroundColor: '#fff' }}>
                <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h2 style={{ fontSize: '1.25rem', fontWeight: '700', color: 'var(--primary)' }}>Admin Portal</h2>
                    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                        <span>{user.name} (Admin)</span>
                        <button onClick={logout} className="btn btn-outline" style={{ padding: '0.25rem 0.75rem', fontSize: '0.9rem' }}>
                            Logout
                        </button>
                    </div>
                </div>
            </nav>

            <div className="container" style={{ padding: '2rem 1.5rem' }}>

                {msg.content && (
                    <div style={{
                        padding: '0.75rem',
                        borderRadius: 'var(--radius)',
                        marginBottom: '1rem',
                        backgroundColor: msg.type === 'error' ? '#fef2f2' : '#f0fdf4',
                        color: msg.type === 'error' ? 'var(--danger)' : 'var(--secondary)',
                        border: `1px solid ${msg.type === 'error' ? '#fecaca' : '#bbf7d0'}`
                    }}>
                        {msg.content}
                    </div>
                )}

                <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '2rem' }}>

                    <div className="card">
                        <h3 style={{ marginBottom: '1rem' }}>Pending Couriers (To Verify)</h3>
                        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                            <thead>
                                <tr style={{ borderBottom: '2px solid var(--bg-input)', textAlign: 'left' }}>
                                    <th style={{ padding: '0.75rem' }}>Name</th>
                                    <th style={{ padding: '0.75rem' }}>Email</th>
                                    <th style={{ padding: '0.75rem' }}>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {couriers.length === 0 ? (
                                    <tr>
                                        <td colSpan={3} style={{ padding: '1rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                                            No pending courier verifications.
                                        </td>
                                    </tr>
                                ) : (
                                    couriers.map((courier) => (
                                        <tr key={courier._id} style={{ borderBottom: '1px solid var(--bg-input)' }}>
                                            <td style={{ padding: '0.75rem' }}>{courier.name}</td>
                                            <td style={{ padding: '0.75rem' }}>{courier.email}</td>
                                            <td style={{ padding: '0.75rem' }}>
                                                <button
                                                    onClick={() => verifyCourier(courier._id)}
                                                    className="btn btn-primary"
                                                    style={{ padding: '0.25rem 1rem', fontSize: '0.9rem' }}
                                                >
                                                    Verify
                                                </button>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>

                    <div className="card">
                        <h3 style={{ marginBottom: '1rem' }}>Pending Orders (To Approve)</h3>
                        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                            <thead>
                                <tr style={{ borderBottom: '2px solid var(--bg-input)', textAlign: 'left' }}>
                                    <th style={{ padding: '0.75rem' }}>User</th>
                                    <th style={{ padding: '0.75rem' }}>Item</th>
                                    <th style={{ padding: '0.75rem' }}>Route</th>
                                    <th style={{ padding: '0.75rem' }}>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {orders.length === 0 ? (
                                    <tr>
                                        <td colSpan={4} style={{ padding: '1rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                                            No pending orders.
                                        </td>
                                    </tr>
                                ) : (
                                    orders.map((order) => (
                                        <tr key={order._id} style={{ borderBottom: '1px solid var(--bg-input)' }}>
                                            <td style={{ padding: '0.75rem' }}>{order.userId?.name || 'Unknown'}</td>
                                            <td style={{ padding: '0.75rem' }}>{order.itemDescription}</td>
                                            <td style={{ padding: '0.75rem', fontSize: '0.9rem' }}>
                                                <div>{order.fromLocation?.address}</div>
                                                <div>↓</div>
                                                <div>{order.toLocation?.address}</div>
                                            </td>
                                            <td style={{ padding: '0.75rem' }}>
                                                <div style={{ display: 'flex', gap: '0.5rem' }}>
                                                    <button
                                                        onClick={() => updateOrderStatus(order._id, 'approved')}
                                                        className="btn btn-primary"
                                                        style={{ padding: '0.25rem 0.75rem', fontSize: '0.9rem' }}
                                                    >
                                                        Approve
                                                    </button>
                                                    <button
                                                        onClick={() => updateOrderStatus(order._id, 'cancelled')}
                                                        className="btn btn-outline"
                                                        style={{ padding: '0.25rem 0.75rem', fontSize: '0.9rem', color: 'var(--danger)', borderColor: 'var(--danger)' }}
                                                    >
                                                        Reject
                                                    </button>
                                                </div>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>

                </div>
            </div>
        </main>
    );
}
