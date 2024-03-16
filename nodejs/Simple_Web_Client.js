/*
Develop a simple web client that makes a GET request 
to http://example.com and prints the response body to the console.
*/


const { log } = require('console');
const http = require('http');

// Define the URL
// const url = 'http://example.com';
const url = 'http://jsonplaceholder.typicode.com/posts/1';

// Make a GET request
http.get(url, (response) => {
    let body = '';
  
    // Concatenate data as it comes in
    response.on('data', (chunk) => {
        body += chunk;
    });
  
    // When the response is complete, print the data
    response.on('end', () => {
      console.log('Response body:');
      console.log(body);
    });
  }).on('error', (error) => {
    console.error('Error:', error);
  });

