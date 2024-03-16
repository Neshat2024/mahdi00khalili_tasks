/*
Develop a program that copies the contents of source.txt
to destination.txt. If destination.txt does not exist, 
the program should create it.
*/





const fs = require('fs');
const path = require('path');

const sourceFilePath = path.join(__dirname, 'source.txt');
const destinationFilePath = path.join(__dirname, 'destination.txt');

// Read the contents of the source file
fs.readFile(sourceFilePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading source file:', err);
    return;
  }

  // Write the contents to the destination file
  fs.writeFile(destinationFilePath, data, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to destination file:', err);
      return;
    }
    console.log(`Contents of ${sourceFilePath} successfully copied to ${destinationFilePath}`);
  });
});
