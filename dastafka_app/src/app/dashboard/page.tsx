'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';

export default function UserDashboard() {
    const { user, logout, isLoading } = useAuth();
    const router = useRouter();
    const [orders, setOrders] = useState<any[]>([]);
    const [formData, setFormData] = useState({
        itemDescription: '',
        fromLocation: '',
        toLocation: '',
    });
    const [msg, setMsg] = useState({ type: '', content: '' });

    useEffect(() => {
        if (!isLoading && (!user || user.role !== 'user')) {
            router.push('/login');
        } else if (user && user.role === 'user') {
            fetchOrders();
        }
    }, [user, isLoading, router]);

    const fetchOrders = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch('/api/orders', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            const data = await res.json();
            if (data.success) {
                setOrders(data.orders);
            }
        } catch (err) {
            console.error(err);
        }
    };

    const handleCreateOrder = async (e: React.FormEvent) => {
        e.preventDefault();
        setMsg({ type: '', content: '' });

        try {
            const token = localStorage.getItem('token');
            const res = await fetch('/api/orders', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(formData),
            });

            const data = await res.json();

            if (data.success) {
                setMsg({ type: 'success', content: 'Order created successfully! Waiting for admin approval.' });
                setFormData({ itemDescription: '', fromLocation: '', toLocation: '' });
                fetchOrders();
            } else {
                setMsg({ type: 'error', content: data.error || 'Failed to create order' });
            }
        } catch (err) {
            setMsg({ type: 'error', content: 'Something went wrong' });
        }
    };

    if (isLoading || !user) return <div className="container" style={{ padding: '2rem' }}>Loading...</div>;

    return (
        <main>
            <nav style={{ padding: '1rem 0', borderBottom: '1px solid var(--bg-input)', backgroundColor: '#fff' }}>
                <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h2 style={{ fontSize: '1.25rem', fontWeight: '700' }}>User Dashboard</h2>
                    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                        <span>{user.name}</span>
                        <button onClick={logout} className="btn btn-outline" style={{ padding: '0.25rem 0.75rem', fontSize: '0.9rem' }}>
                            Logout
                        </button>
                    </div>
                </div>
            </nav>

            <div className="container" style={{ padding: '2rem 1.5rem' }}>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>

                    {/* Create Order Section */}
                    <div>
                        <div className="card">
                            <h3 style={{ marginBottom: '1.5rem', fontSize: '1.25rem' }}>Create New Order</h3>

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

                            <form onSubmit={handleCreateOrder}>
                                <div className="input-group">
                                    <label className="input-label">Item Description</label>
                                    <input
                                        type="text"
                                        className="form-input"
                                        placeholder="What are you sending?"
                                        value={formData.itemDescription}
                                        onChange={(e) => setFormData({ ...formData, itemDescription: e.target.value })}
                                        required
                                    />
                                </div>
                                <div className="input-group">
                                    <label className="input-label">Pickup Location (A)</label>
                                    <input
                                        type="text"
                                        className="form-input"
                                        placeholder="Address or Coordinates"
                                        value={formData.fromLocation}
                                        onChange={(e) => setFormData({ ...formData, fromLocation: e.target.value })}
                                        required
                                    />
                                </div>
                                <div className="input-group">
                                    <label className="input-label">Drop-off Location (B)</label>
                                    <input
                                        type="text"
                                        className="form-input"
                                        placeholder="Address or Coordinates"
                                        value={formData.toLocation}
                                        onChange={(e) => setFormData({ ...formData, toLocation: e.target.value })}
                                        required
                                    />
                                </div>
                                <button type="submit" className="btn btn-primary" style={{ width: '100%' }}>
                                    Request Delivery
                                </button>
                            </form>
                        </div>
                    </div>

                    {/* My Orders Section */}
                    <div>
                        <div className="card">
                            <h3 style={{ marginBottom: '1.5rem', fontSize: '1.25rem' }}>My Orders</h3>

                            {orders.length === 0 ? (
                                <div style={{ textAlign: 'center', color: 'var(--text-muted)', padding: '2rem 0' }}>
                                    No active orders found.
                                </div>
                            ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                                    {orders.map((order) => (
                                        <div key={order._id} style={{ padding: '1rem', border: '1px solid var(--bg-input)', borderRadius: 'var(--radius)' }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                                                <strong>{order.itemDescription}</strong>
                                                <span style={{
                                                    fontSize: '0.8rem',
                                                    padding: '0.2rem 0.5rem',
                                                    borderRadius: '99px',
                                                    backgroundColor:
                                                        order.status === 'pending_admin' ? '#fef3c7' :
                                                            order.status === 'approved' ? '#e0f2fe' :
                                                                order.status === 'picked_up' ? '#fce7f3' :
                                                                    order.status === 'delivered' ? '#dcfce7' : '#f3f4f6',
                                                    color:
                                                        order.status === 'pending_admin' ? '#b45309' :
                                                            order.status === 'approved' ? '#0369a1' :
                                                                order.status === 'picked_up' ? '#be185d' :
                                                                    order.status === 'delivered' ? '#15803d' : '#374151',
                                                }}>
                                                    {order.status.replace('_', ' ')}
                                                </span>
                                            </div>
                                            <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
                                                <div>From: {order.fromLocation?.address || 'N/A'}</div>
                                                <div>To: {order.toLocation?.address || 'N/A'}</div>
                                            </div>
                                            <div style={{ fontSize: '0.8rem', marginTop: '0.5rem', color: '#94a3b8' }}>
                                                {new Date(order.createdAt).toLocaleDateString()}
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>

                </div>
            </div>
        </main>
    );
}
