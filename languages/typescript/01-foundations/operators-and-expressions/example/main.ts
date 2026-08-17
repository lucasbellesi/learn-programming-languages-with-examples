// Module focus: Combining values through expressions and readable calculations.
// Why it matters: the example makes it possible to build expressions with correct precedence and
// explicit intent before the learner tackles the exercises.

const subtotal = 120;
const couponPercent = 10;
const isLoyalCustomer = true;
const couponDiscount = subtotal * (couponPercent / 100);
const loyaltyDiscount = isLoyalCustomer ? 5 : 0;
const finalTotal = subtotal - couponDiscount - loyaltyDiscount;
// The printed result shows whether the program can distinguish arithmetic, comparison, and
// logical operations.
console.log(`Subtotal: ${subtotal}`);
console.log(`Coupon discount: ${couponDiscount}`);
console.log(`Loyal customer: ${isLoyalCustomer}`);
console.log(`Final total: ${finalTotal}`);
export {};
