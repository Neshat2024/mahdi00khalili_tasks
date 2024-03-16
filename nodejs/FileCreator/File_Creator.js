/*
Develop a program that creates a file named test.txt
and writes "Hello, Node.js!" into it. 
If the file already exists, it should append the text instead.
*/

const fs = require("fs");
const path = require('path');


// Define the file name
const fileName = "test.txt";

// Text to write into the file
const textToWrite = "Hello, Node.js!\n";

// Define the fila path
const filePath = path.join(__dirname, fileName);

// Check if the file exists
fs.stat(filePath, (err, stats) => {
  if (err) {
    if (err.code === "ENOENT") {
      console.log("File does not exist.");
      // create the file and add textToWrite to it.
      fs.writeFile(filePath, textToWrite, (err) => {
        if (err) {
          console.error("Error writing to file:", err);
        } else {
          console.log("Text written to file successfully.");
        }
      });

      console.log("File is created successfully.");
    } else {
      // Other error occurred
      console.error("Error occurred while checking file existence:", err);
    }
  } else {
    // File exists
    console.log("File exists.");

    fs.appendFile(filePath, textToWrite, (err) => {
      if (err) {
        console.error("Error appending text to file:", err);
      } else {
        console.log("Text appended to file successfully.");
      }
    });
  }
});
