// Convert fixed text values into numbers and a boolean, then print a price.
// The exercises extend this idea to records read from standard input.

// Show how TypeScript starts from raw text and turns it into typed values on purpose.
const rawAge = "27";
const rawPrice = "14.50";
const rawMemberFlag = "true";
const age = Number.parseInt(rawAge, 10);
const price = Number.parseFloat(rawPrice);
const isMember = rawMemberFlag === "true";
if (Number.isNaN(age) || Number.isNaN(price)) {
    // getline preserves spaces in the name; operator >> extracts the numeric fields.
    console.log("Invalid sample input.");
} else {
    // Print a 10% member discount; toFixed controls display, not the stored value.
    const finalPrice = isMember ? price * 0.9 : price;
    console.log(`Age: ${age}`);
    console.log(`Original price: ${price.toFixed(2)}`);
    console.log(`Member discount applied: ${isMember}`);
    console.log(`Final price: ${finalPrice.toFixed(2)}`);
}
export {};
