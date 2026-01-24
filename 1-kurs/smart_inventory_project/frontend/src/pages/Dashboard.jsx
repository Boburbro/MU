import { useState, useEffect } from 'react';
import api from '../services/api';
import { authService } from '../services/auth';

export default function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [selectedProduct, setSelectedProduct] = useState('');
  const [loading, setLoading] = useState(true);
  const [products, setProducts] = useState([]);
  const user = authService.getCurrentUser();

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const res = await api.get('/dashboard/summary');
      setSummary(res.data);
      setLoading(false);
    } catch (err) {
      console.error(err);
      setLoading(false);
    }
  };

  const fetchProducts = async () => {
    try {
      const res = await api.get('/products');
      setProducts(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handlePredict = async () => {
    if (!selectedProduct) return;
    try {
      const res = await api.get('/ai/predict', { params: { product_id: selectedProduct } });
      setPrediction(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  if (loading) return <div className="p-8">Loading...</div>;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold mb-8">Dashboard</h2>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-600">Total Products</h3>
          <p className="text-4xl font-bold text-blue-600">{summary?.total_products || 0}</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-600">Low Stock</h3>
          <p className="text-4xl font-bold text-orange-600">{summary?.low_stock_count || 0}</p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-gray-600">Today's Sales</h3>
          <p className="text-4xl font-bold text-green-600">${summary?.today_sales?.total_revenue?.toFixed(2) || 0}</p>
          <p className="text-sm text-gray-500">{summary?.today_sales?.count} transactions</p>
        </div>
      </div>

      {/* Low Stock Products */}
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h3 className="text-xl font-bold mb-4">⚠️ Low Stock Alerts</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2 text-left">Product</th>
                <th className="px-4 py-2 text-left">Current Stock</th>
                <th className="px-4 py-2 text-left">Min Limit</th>
              </tr>
            </thead>
            <tbody>
              {summary?.low_stock_products?.map((p) => (
                <tr key={p.id} className="border-t hover:bg-gray-50">
                  <td className="px-4 py-2">{p.name}</td>
                  <td className="px-4 py-2">
                    <span className={p.stock < p.min_limit ? 'text-red-600 font-bold' : ''}>
                      {p.stock}
                    </span>
                  </td>
                  <td className="px-4 py-2">{p.min_limit}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* AI Prediction */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-xl font-bold mb-4">🤖 7-Day Sales Prediction</h3>
        <div className="flex gap-4 mb-6">
          <select
            value={selectedProduct}
            onChange={(e) => setSelectedProduct(e.target.value)}
            className="border rounded px-4 py-2 flex-1"
          >
            <option value="">Select a product...</option>
            {products.map((p) => (
              <option key={p.id} value={p.id}>{p.name}</option>
            ))}
          </select>
          <button
            onClick={handlePredict}
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            Predict
          </button>
        </div>

        {prediction && (
          <div className="border-t pt-4">
            <h4 className="font-bold mb-2">{prediction.product_name}</h4>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-gray-600">Current Stock</p>
                <p className="text-2xl font-bold">{prediction.current_stock}</p>
              </div>
              <div>
                <p className="text-sm text-gray-600">Predicted 7-Day Sales</p>
                <p className="text-2xl font-bold text-green-600">{prediction.prediction.total_7days}</p>
              </div>
              <div className="col-span-2">
                <p className="text-sm text-gray-600">Method</p>
                <p className="text-sm">{prediction.prediction.method} (Confidence: {prediction.prediction.confidence})</p>
              </div>
            </div>

            {prediction.prediction.daily_predictions && (
              <div className="mt-4">
                <p className="text-sm font-bold mb-2">Daily Predictions:</p>
                <div className="flex gap-1">
                  {prediction.prediction.daily_predictions.map((d, i) => (
                    <div key={i} className="flex-1">
                      <div className="bg-blue-200 h-12 rounded flex items-end justify-center pb-1 relative group">
                        <span className="text-xs font-bold">{d}</span>
                        <div className="absolute bottom-full bg-gray-800 text-white text-xs rounded p-1 mb-1 hidden group-hover:block whitespace-nowrap">
                          Day {i + 1}: {d} units
                        </div>
                      </div>
                      <p className="text-xs text-center mt-1">D{i + 1}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
