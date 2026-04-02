// This example shows reading typed input carefully and turning raw text into values.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

// Show how TypeScript starts from raw text and turns it into typed values on purpose.
const rawAge = "27";
const rawPrice = "14.50";
const rawMemberFlag = "true";
const age = Number.parseInt(rawAge, 10);
const price = Number.parseFloat(rawPrice);
const isMember = rawMemberFlag === "true";
if (Number.isNaN(age) || Number.isNaN(price)) {
    console.log("Invalid sample input.");
} else {
    const finalPrice = isMember ? price * 0.9 : price;
    console.log(`Age: ${age}`);
    console.log(`Original price: ${price.toFixed(2)}`);
    console.log(`Member discount applied: ${isMember}`);
    console.log(`Final price: ${finalPrice.toFixed(2)}`);
}
export {};
