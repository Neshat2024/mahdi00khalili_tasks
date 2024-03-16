/*
Create a script that prints all command line arguments passed to it.
*/

// Get the command line arguments
const args = process.argv;

// Remove the first two elements as they are not arguments we're interested in
const argumentsPassed = args.slice(2);

// Check if there are any arguments passed
if (argumentsPassed.length === 0) {
    console.log("No arguments passed.");
} else {
    // Print all the arguments passed
    console.log("Arguments passed:");
    argumentsPassed.forEach((arg, index) => {
        console.log(`${index + 1}: ${arg}`);
    });
}
