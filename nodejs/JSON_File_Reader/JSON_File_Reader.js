/*
Write a program that reads a JSON file (data.json) 
and prints the content to the console.
*/


const fs = require('fs');
const path = require('path');

// Define the file name
const fileName = "data.json";


// Define the fila path
const filePath = path.join(__dirname, fileName);


// Read the JSON file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  try {
    // Parse the JSON data
    const jsonData = JSON.parse(data);
    // Print the content to the console
    console.log(jsonData);
  } catch (error) {
    console.error('Error parsing JSON data:', error);
  }
});
