import { useState } from 'react';

export default function ProductModal({ product, onSave, onClose, isAdmin = false }) {
  const [formData, setFormData] = useState(
    product || {
      name: '',
      category: '',
      price: '',
      stock_quantity: 0,
      min_limit: 10,
    }
  );

  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: name === 'price' ? parseFloat(value) : name === 'stock_quantity' || name === 'min_limit' ? parseInt(value) : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name || !formData.category || !formData.price) {
      setError('All fields are required');
      return;
    }
    onSave(formData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md">
        <h2 className="text-2xl font-bold mb-4">{product ? 'Edit' : 'Create'} Product</h2>

        {error && <div className="bg-red-100 text-red-700 p-3 rounded mb-4">{error}</div>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium">Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              disabled={!isAdmin}
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Category</label>
            <input
              type="text"
              name="category"
              value={formData.category}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              disabled={!isAdmin}
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Price</label>
            <input
              type="number"
              name="price"
              value={formData.price}
              onChange={handleChange}
              step="0.01"
              className="w-full border rounded px-3 py-2"
              disabled={!isAdmin}
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Stock</label>
            <input
              type="number"
              name="stock_quantity"
              value={formData.stock_quantity}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              disabled={!isAdmin}
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Minimum Limit</label>
            <input
              type="number"
              name="min_limit"
              value={formData.min_limit}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              disabled={!isAdmin}
            />
          </div>

          <div className="flex gap-2 justify-end">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border rounded hover:bg-gray-100"
            >
              Cancel
            </button>
            {isAdmin && (
              <button
                type="submit"
                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
              >
                Save
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}
