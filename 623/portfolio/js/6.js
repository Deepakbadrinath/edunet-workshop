const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter count: ", (input) => {
    let n = parseInt(input),
        n1 = 0,
        n2 = 1;

    if (n > 0) {
        for (let i = 0; i < n; i++) {
            console.log(n1);
            [n1, n2] = [n2, n1 + n2];
        }
    } else {
        console.log("Enter a positive number.");
    }
    readline.close();
});