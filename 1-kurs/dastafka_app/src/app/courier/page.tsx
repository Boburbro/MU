'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';

export default function CourierDashboard() {
    const { user, logout, isLoading } = useAuth();
    const router = useRouter();
    const [availableOrders, setAvailableOrders] = useState<any[]>([]);
    const [myOrders, setMyOrders] = useState<any[]>([]);
    const [msg, setMsg] = useState({ type: '', content: '' });

    useEffect(() => {
        if (!isLoading && (!user || user.role !== 'courier')) {
            router.push('/login');
        } else if (user && user.role === 'courier') {
            fetchOrders();
        }
    }, [user, isLoading, router]);

    const fetchOrders = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch('/api/courier/orders', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            const data = await res.json();
            if (data.success) {
                setAvailableOrders(data.availableOrders);
                setMyOrders(data.myOrders);
            }
        } catch (err) {
            console.error(err);
        }
    };

    const handleAction = async (id: string, action: 'accept' | 'deliver') => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`/api/courier/orders/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ action })
            });
            const data = await res.json();
            if (data.success) {
                setMsg({ type: 'success', content: action === 'accept' ? 'Order accepted!' : 'Order delivered!' });
                fetchOrders();
            } else {
                setMsg({ type: 'error', content: data.error });
            }
        } catch (err) {
            setMsg({ type: 'error', content: 'Action failed' });
        }
    };

    if (isLoading || !user) return <div className="container" style={{ padding: '2rem' }}>Loading...</div>;

    return (
        <main>
            <nav style={{ padding: '1rem 0', borderBottom: '1px solid var(--bg-input)', backgroundColor: '#fff' }}>
                <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h2 style={{ fontSize: '1.25rem', fontWeight: '700', color: 'var(--secondary)' }}>Courier Dashboard</h2>
                    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                        <span>{user.name}</span>
                        <span style={{
                            fontSize: '0.8rem',
                            padding: '0.2rem 0.6rem',
                            backgroundColor: user.isVerified ? '#dcfce7' : '#fee2e2',
                            color: user.isVerified ? '#166534' : '#991b1b',
                            borderRadius: '99px'
                        }}>
                            {user.isVerified ? 'Verified' : 'Not Verified'}
                        </span>
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

                {!user.isVerified && (
                    <div style={{ backgroundColor: '#fff7ed', border: '1px solid #ffedd5', color: '#9a3412', padding: '1rem', borderRadius: 'var(--radius)', marginBottom: '2rem' }}>
                        <strong>Account Pending Verification:</strong> You cannot accept orders until an admin verifies your account. Please wait.
                    </div>
                )}

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>

                    {/* Available Jobs */}
                    <div className="card">
                        <h3 style={{ marginBottom: '1rem' }}>Available Orders / Market</h3>
                        <p style={{ color: 'var(--text-muted)', marginBottom: '1rem' }}>Orders approved by Admin.</p>

                        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                            {availableOrders.length === 0 ? (
                                <div style={{ color: 'var(--text-muted)', textAlign: 'center' }}>No available jobs nearby.</div>
                            ) : (
                                availableOrders.map(order => (
                                    <div key={order._id} style={{ padding: '1rem', border: '1px solid var(--bg-input)', borderRadius: 'var(--radius)' }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                                            <strong>{order.itemDescription}</strong>
                                            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{order.userId?.name}</span>
                                        </div>
                                        <div style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>
                                            {order.fromLocation?.address} → {order.toLocation?.address}
                                        </div>
                                        <button
                                            onClick={() => handleAction(order._id, 'accept')}
                                            disabled={!user.isVerified}
                                            className="btn btn-primary"
                                            style={{ width: '100%', opacity: !user.isVerified ? 0.5 : 1 }}
                                        >
                                            Accept Job
                                        </button>
                                    </div>
                                ))
                            )}
                        </div>
                    </div>

                    {/* My Active Deliveries */}
                    <div className="card">
                        <h3 style={{ marginBottom: '1rem' }}>My Deliveries</h3>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                            {myOrders.length === 0 ? (
                                <div style={{ color: 'var(--text-muted)', textAlign: 'center' }}>You have no active deliveries.</div>
                            ) : (
                                myOrders.map(order => (
                                    <div key={order._id} style={{ padding: '1rem', border: '1px solid var(--bg-input)', borderRadius: 'var(--radius)' }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                                            <strong>{order.itemDescription}</strong>
                                            <span style={{
                                                fontSize: '0.8rem',
                                                padding: '0.2rem 0.5rem',
                                                borderRadius: '99px',
                                                backgroundColor:
                                                    order.status === 'delivered' ? '#dcfce7' : '#fce7f3',
                                                color:
                                                    order.status === 'delivered' ? '#15803d' : '#be185d',
                                            }}>
                                                {order.status === 'picked_up' ? 'In Progress' : 'Delivered'}
                                            </span>
                                        </div>
                                        <div style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>
                                            {order.fromLocation?.address} → {order.toLocation?.address}
                                        </div>
                                        {order.status === 'picked_up' && (
                                            <button
                                                onClick={() => handleAction(order._id, 'deliver')}
                                                className="btn btn-primary" // Use success color ideally, reusing primary
                                                style={{ width: '100%', backgroundColor: 'var(--secondary)' }}
                                            >
                                                Mark Delivered
                                            </button>
                                        )}
                                    </div>
                                ))
                            )}
                        </div>
                    </div>

                </div>
            </div>
        </main>
    );
}
