const readline = require('readline');
const bcrypt = require("bcrypt")

const hashPassword = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


// to run : npm run hp
hashPassword.question("password : ", async (password) => {
    console.log(`hashed password : ${await bcrypt.hash(password,3)}`)
    hashPassword.close()
});