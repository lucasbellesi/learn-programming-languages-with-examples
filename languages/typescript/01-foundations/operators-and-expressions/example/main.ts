// Module focus: Combining values through expressions and readable calculations.
// Why it matters: practicing operators and expressions patterns makes exercises and checkpoints easier to reason about.

const subtotal = 120;
const couponPercent = 10;
const isLoyalCustomer = true;
const couponDiscount = subtotal * (couponPercent / 100);
const loyaltyDiscount = isLoyalCustomer ? 5 : 0;
const finalTotal = subtotal - couponDiscount - loyaltyDiscount;
// Report output values so learners can verify the operators and expressions result.
console.log(`Subtotal: ${subtotal}`);
console.log(`Coupon discount: ${couponDiscount}`);
console.log(`Loyal customer: ${isLoyalCustomer}`);
console.log(`Final total: ${finalTotal}`);
export {};
