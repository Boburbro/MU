import Link from 'next/link';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Dastafka App - Fast Delivery',
};

export default function Home() {
  return (
    <main>
      <nav style={{ padding: '1.5rem 0', backgroundColor: 'var(--bg-card)', boxShadow: 'var(--shadow-sm)' }}>
        <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1 className="title" style={{ fontSize: '1.5rem', margin: 0 }}>Dastafka<span style={{ color: 'var(--text-main)' }}>.uz</span></h1>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <Link href="/login" className="btn btn-outline" style={{ padding: '0.5rem 1.25rem' }}>
              Login
            </Link>
            <Link href="/register" className="btn btn-primary" style={{ padding: '0.5rem 1.25rem' }}>
              Get Started
            </Link>
          </div>
        </div>
      </nav>

      <section style={{ padding: '5rem 0 3rem' }}>
        <div className="container" style={{ textAlign: 'center', maxWidth: '800px' }}>
          <span style={{ color: 'var(--primary)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '2px', fontSize: '0.9rem' }}>
            Fastest Delivery Service
          </span>
          <h1 style={{ fontSize: '3.5rem', fontWeight: '900', lineHeight: 1.2, margin: '1rem 0 1.5rem', color: 'var(--text-main)' }}>
            Deliver anything from <span className="title">Point A</span> to <span className="title">Point B</span>
          </h1>
          <p style={{ fontSize: '1.25rem', color: 'var(--text-muted)', marginBottom: '2.5rem', lineHeight: 1.6 }}>
            The easiest way to send packages, documents, or items across the city.
            Real-time tracking, secure couriers, and affordable rates.
          </p>
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <Link href="/register" className="btn btn-primary" style={{ fontSize: '1.1rem', padding: '1rem 2rem' }}>
              Start Shipping Now
            </Link>
            <Link href="/login" className="btn btn-outline" style={{ fontSize: '1.1rem', padding: '1rem 2rem' }}>
              I'm a Courier
            </Link>
          </div>
        </div>
      </section>

      <section style={{ padding: '3rem 0', backgroundColor: 'var(--bg-card)' }}>
        <div className="container">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
            <div className="card" style={{ border: '1px solid var(--bg-input)', boxShadow: 'none' }}>
              <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>📦</div>
              <h3 style={{ fontSize: '1.5rem', fontWeight: '700', marginBottom: '0.5rem' }}>Easy Request</h3>
              <p style={{ color: 'var(--text-muted)' }}>Simple form to specify pickup and drop-off locations with item details.</p>
            </div>
            <div className="card" style={{ border: '1px solid var(--bg-input)', boxShadow: 'none' }}>
              <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🛡️</div>
              <h3 style={{ fontSize: '1.5rem', fontWeight: '700', marginBottom: '0.5rem' }}>Secure & Admin Verified</h3>
              <p style={{ color: 'var(--text-muted)' }}>All couriers are verified. Orders are reviewed for safety before assignment.</p>
            </div>
            <div className="card" style={{ border: '1px solid var(--bg-input)', boxShadow: 'none' }}>
              <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🚚</div>
              <h3 style={{ fontSize: '1.5rem', fontWeight: '700', marginBottom: '0.5rem' }}>Fast Delivery</h3>
              <p style={{ color: 'var(--text-muted)' }}>Couriers nearby accept your request instantly and deliver in record time.</p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
