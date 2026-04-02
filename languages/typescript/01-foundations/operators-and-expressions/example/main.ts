// This example shows combining values through expressions and readable calculations.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

const subtotal = 120;
const couponPercent = 10;
const isLoyalCustomer = true;
const couponDiscount = subtotal * (couponPercent / 100);
const loyaltyDiscount = isLoyalCustomer ? 5 : 0;
const finalTotal = subtotal - couponDiscount - loyaltyDiscount;
console.log(`Subtotal: ${subtotal}`);
console.log(`Coupon discount: ${couponDiscount}`);
console.log(`Loyal customer: ${isLoyalCustomer}`);
console.log(`Final total: ${finalTotal}`);
export {};
