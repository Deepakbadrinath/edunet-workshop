// write a javascript program to check given number is palindrome or notlet num = 121;
// function isPalindrome(str) {
//     return str === str.split("").reverse().join("");
// }
// console.log(isPalindrome("level")); // true
// console.log(isPalindrome("123454321")); // false

function printMultiplesSeries(count) {
    console.log("Multiples of 2 | Multiples of 5 | Multiples of 7");
    console.log("-----------------------------------------------");

    for (let i = 1; i <= count; i++) {

        let first = i * 2;
        let second = i * 5;
        let third = i * 7;

        console.log(`${first} \t\t ${second} \t\t ${third}`);
    }
}

printMultiplesSeries(5);