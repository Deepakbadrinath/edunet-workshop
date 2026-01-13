const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout });

rl.question("Enter a string: ", str => {
    const s = str.toLowerCase();
    const vowels = [...s].filter(c => "aeiou".includes(c)).length;
    const consonants = [...s].filter(c => c >= 'a' && c <= 'z' && !"aeiou".includes(c)).length;
    console.log(`Vowels: ${vowels}\nConsonants: ${consonants}`);
    rl.close();
});