/*
Write a Node.js script that sends a GET request 
to http://example.com/search 
with query parameters query=Node.js and prints the response.
*/

const http = require('http');

// Define the URL with query parameters
const url = 'http://example.com/search?query=Node.js';

// Make a GET request
http.get(url, (response) => {
  let data = '';

  // When a chunk of data is received, concatenate it to the 'data' string
  response.on('data', (chunk) => {
    data += chunk;
  });

  // When the response is complete, print the accumulated data
  response.on('end', () => {
    console.log('Response body:');
    console.log(data);
  });
}).on('error', (error) => {
  console.error('Error:', error);
});



