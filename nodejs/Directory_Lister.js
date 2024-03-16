/*

Create a script that lists all files 
and directories in the current directory.

*/


const fs = require('fs');

// Read the current directory
fs.readdir('.', (err, files) => {
  if (err) {
    console.error('Error reading directory:', err);
    return;
  }

  // Print files and directories
  console.log('Files and directories in the current directory:\n');
  files.forEach(file => {
    console.log(file);
  });
});


