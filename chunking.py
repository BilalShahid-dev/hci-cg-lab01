let items = ['5', '2', '9', '1', '7', '4', '6', '8'];
console.log("Ungrouped:", items.join(' '));

// Chunked items
let chunked = [['5', '2', '9'], ['1', '7', '4'], ['6', '8']];
console.log("Chunked:", chunked.map(c => c.join('')).join(' '));

// Explanation output
console.log("\nUngrouped is harder to remember.");
console.log("Chunked is easier because items are grouped into meaningful units.");