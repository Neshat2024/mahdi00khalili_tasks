/*
In Node.js, environment variables 
are variables that are set outside of the application
but can be accessed within it. 
They are often used to configure settings, 
manage sensitive information, 
or provide runtime information to the application.
*/


// Check if the environment variable is set
if (process.env.API_KEY) {
    // If set, print its value
    console.log(`Value of API_KEY: ${process.env.API_KEY}`);
} else {
    // If not set, print a default message
    console.log("The environment variable API_KEY is not set.");
}


/* 
for running this code :

API_KEY=TEST_API_KEY_1234567890 node Environment_Variable_Reader.js


*/

