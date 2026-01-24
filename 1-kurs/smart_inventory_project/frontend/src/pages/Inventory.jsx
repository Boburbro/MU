import { useState, useEffect } from 'react';
import api from '../services/api';
import { authService } from '../services/auth';
import ProductModal from '../components/ProductModal';

export default function Inventory() {
  const user = authService.getCurrentUser();
  const isAdmin = user?.role === 'admin';
  const [products, setProducts] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showSaleModal, setShowSaleModal] = useState(false);
  const [saleData, setSaleData] = useState({ product_id: '', quantity_sold: '', total_price: '' });

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const res = await api.get('/products');
      setProducts(res.data);
      setLoading(false);
    } catch (err) {
      console.error(err);
      setLoading(false);
    }
  };

  const handleCreateClick = () => {
    setSelectedProduct(null);
    setShowModal(true);
  };

  const handleEditClick = (product) => {
    setSelectedProduct(product);
    setShowModal(true);
  };

  const handleSaveProduct = async (formData) => {
    try {
      if (selectedProduct) {
        await api.put(`/products/${selectedProduct.id}`, formData);
      } else {
        await api.post('/products', formData);
      }
      fetchProducts();
      setShowModal(false);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteProduct = async (id) => {
    if (!window.confirm('Delete this product?')) return;
    try {
      await api.delete(`/products/${id}`);
      fetchProducts();
    } catch (err) {
      console.error(err);
    }
  };

  const handleRecordSale = async (e) => {
    e.preventDefault();
    try {
      await api.post('/sales', {
        product_id: parseInt(saleData.product_id),
        quantity_sold: parseInt(saleData.quantity_sold),
        total_price: parseFloat(saleData.total_price),
      });
      setSaleData({ product_id: '', quantity_sold: '', total_price: '' });
      setShowSaleModal(false);
      fetchProducts();
      alert('Sale recorded successfully!');
    } catch (err) {
      alert(err.response?.data?.detail || 'Error recording sale');
    }
  };

  const handleQuantityChange = (e) => {
    const qty = parseInt(e.target.value);
    const product = products.find(p => p.id === parseInt(saleData.product_id));
    if (product && qty > 0) {
      setSaleData({
        ...saleData,
        quantity_sold: qty,
        total_price: (qty * product.price).toFixed(2)
      });
    }
  };

  if (loading) return <div className="p-8">Loading...</div>;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <h2 className="text-3xl font-bold">Inventory Management</h2>
        <div className="flex gap-2">
          {isAdmin && (
            <button
              onClick={handleCreateClick}
              className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
            >
              + Add Product
            </button>
          )}
          <button
            onClick={() => setShowSaleModal(true)}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            📊 Record Sale
          </button>
        </div>
      </div>

      {/* Products Table */}
      <div className="bg-white rounded-lg shadow overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-100 border-b">
            <tr>
              <th className="px-6 py-3 text-left">Name</th>
              <th className="px-6 py-3 text-left">Category</th>
              <th className="px-6 py-3 text-right">Price</th>
              <th className="px-6 py-3 text-right">Stock</th>
              <th className="px-6 py-3 text-right">Min</th>
              <th className="px-6 py-3 text-center">Status</th>
              <th className="px-6 py-3 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => {
              const isLowStock = product.stock_quantity < product.min_limit;
              return (
                <tr key={product.id} className="border-b hover:bg-gray-50">
                  <td className="px-6 py-3">{product.name}</td>
                  <td className="px-6 py-3 text-gray-600">{product.category}</td>
                  <td className="px-6 py-3 text-right font-semibold">${product.price.toFixed(2)}</td>
                  <td className="px-6 py-3 text-right">
                    <span className={isLowStock ? 'text-red-600 font-bold' : ''}>
                      {product.stock_quantity}
                    </span>
                  </td>
                  <td className="px-6 py-3 text-right">{product.min_limit}</td>
                  <td className="px-6 py-3 text-center">
                    {isLowStock ? (
                      <span className="bg-red-100 text-red-800 text-xs px-3 py-1 rounded">⚠️ Low</span>
                    ) : (
                      <span className="bg-green-100 text-green-800 text-xs px-3 py-1 rounded">✅ OK</span>
                    )}
                  </td>
                  <td className="px-6 py-3 text-center">
                    {isAdmin && (
                      <>
                        <button
                          onClick={() => handleEditClick(product)}
                          className="bg-blue-500 hover:bg-blue-700 text-white px-3 py-1 rounded mr-2"
                        >
                          Edit
                        </button>
                        <button
                          onClick={() => handleDeleteProduct(product.id)}
                          className="bg-red-500 hover:bg-red-700 text-white px-3 py-1 rounded"
                        >
                          Delete
                        </button>
                      </>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Product Modal */}
      {showModal && (
        <ProductModal
          product={selectedProduct}
          onSave={handleSaveProduct}
          onClose={() => setShowModal(false)}
          isAdmin={isAdmin}
        />
      )}

      {/* Sale Modal */}
      {showSaleModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-full max-w-md">
            <h2 className="text-2xl font-bold mb-4">Record Sale</h2>
            <form onSubmit={handleRecordSale} className="space-y-4">
              <div>
                <label className="block text-sm font-medium">Product</label>
                <select
                  value={saleData.product_id}
                  onChange={(e) => setSaleData({ ...saleData, product_id: e.target.value })}
                  className="w-full border rounded px-3 py-2"
                  required
                >
                  <option value="">Select product...</option>
                  {products.map((p) => (
                    <option key={p.id} value={p.id}>
                      {p.name} (Stock: {p.stock_quantity})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium">Quantity</label>
                <input
                  type="number"
                  value={saleData.quantity_sold}
                  onChange={handleQuantityChange}
                  className="w-full border rounded px-3 py-2"
                  min="1"
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium">Total Price</label>
                <input
                  type="number"
                  value={saleData.total_price}
                  className="w-full border rounded px-3 py-2 bg-gray-100"
                  readOnly
                  step="0.01"
                />
              </div>

              <div className="flex gap-2 justify-end">
                <button
                  type="button"
                  onClick={() => setShowSaleModal(false)}
                  className="px-4 py-2 border rounded hover:bg-gray-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
                >
                  Record Sale
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
