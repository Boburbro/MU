import { Navigate } from 'react-router-dom';
import { authService } from '../services/auth';

export default function ProtectedRoute({ children, requiredRole = null }) {
  if (!authService.isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  if (requiredRole) {
    const user = authService.getCurrentUser();
    if (user?.role !== requiredRole && requiredRole !== '*') {
      return <Navigate to="/dashboard" replace />;
    }
  }

  return children;
}
