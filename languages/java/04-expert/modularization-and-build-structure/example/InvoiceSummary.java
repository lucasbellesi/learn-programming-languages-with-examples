// The immutable summary is the data contract between calculation and presentation modules.

record InvoiceSummary(double subtotal, double discountValue, double taxValue, double total) {
}
