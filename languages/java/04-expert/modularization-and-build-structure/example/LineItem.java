// A named domain type keeps item validation and item-level calculation in one source file.

record LineItem(String name, int quantity, double unitPrice) {
    LineItem {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("Item name is required.");
        }
        if (quantity < 0 || unitPrice < 0.0) {
            throw new IllegalArgumentException("Quantity and price cannot be negative.");
        }
    }

    double total() {
        return quantity * unitPrice;
    }
}
