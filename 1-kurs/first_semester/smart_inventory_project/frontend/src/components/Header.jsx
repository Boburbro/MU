import { Link, useNavigate } from 'react-router-dom';
import { authService } from '../services/auth';

export default function Header() {
  const navigate = useNavigate();
  const user = authService.getCurrentUser();

  const handleLogout = () => {
    authService.logout();
    navigate('/login');
  };

  if (!authService.isAuthenticated()) {
    return null;
  }

  return (
    <header className="bg-blue-600 text-white shadow">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <div className="flex items-center gap-8">
          <h1 className="text-2xl font-bold">📦 Smart Inventory</h1>
          <nav className="flex gap-6">
            <Link to="/dashboard" className="hover:text-blue-200">Dashboard</Link>
            <Link to="/inventory" className="hover:text-blue-200">Inventory</Link>
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <span className="text-sm">
            {user?.username} <badge className="bg-blue-800 px-2 py-1 rounded text-xs ml-2">{user?.role}</badge>
          </span>
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-700 px-4 py-2 rounded"
          >
            Logout
          </button>
        </div>
      </div>
    </header>
  );
}
