#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
    if (err1) {
        console.error(`Error reading ${sourceFilePath1}: ${err1}`);
        return;
    }

    // Read the content of the second source file
    fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
        if (err2) {
            console.error(`Error reading ${sourceFilePath2}: ${err2}`);
            return;
        }

        // Concatenate the content of the two source files
        const concatenatedContent = data1 + data2;

        // Write the concatenated content to the destination file
        fs.writeFile(destinationFilePath, concatenatedContent, 'utf8', (err3) => {
            if (err3) {
                console.error(`Error writing to ${destinationFilePath}: ${err3}`);
                return;
            }

            console.log(`Concatenation successful. Result saved to ${destinationFilePath}`);
        });
    });
});

