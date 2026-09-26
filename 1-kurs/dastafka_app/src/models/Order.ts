import mongoose from 'mongoose';

const OrderSchema = new mongoose.Schema({
    userId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    courierId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        default: null,
    },
    itemDescription: {
        type: String,
        required: [true, 'Please provide a description of the item'],
    },
    fromLocation: {
        lat: Number,
        lng: Number,
        address: String,
    },
    toLocation: {
        lat: Number,
        lng: Number,
        address: String,
    },
    status: {
        type: String,
        enum: ['pending_admin', 'approved', 'picked_up', 'delivered', 'cancelled'],
        default: 'pending_admin',
    },
}, { timestamps: true });

export default mongoose.models.Order || mongoose.model('Order', OrderSchema);
