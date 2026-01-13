// a=11
// if(a%2==0)
// {
//     console.log("even")
// }
// else{
//     console.log("odd")
// }

// 1.write a javascript program to print first even prime number
// 2.write a javascript program give is isHamston number or not
// 3.write a javascript program to check given number is perfect or not
// 4.write a javascript program to print hello if it is multiple of2 by if multiple 3 if multiple both 3&5 write tata bye bye 

//12jan write a javascript program to check given number is palindrome or not
//write a javascript program to prin series of 3 numbers where first number is multiple of 2 second number is multiple of 5 and third number is multiple of 7 
//write a javascript program to check given number is perfect or not
//write a javascript program to check given number is armstrong or not

// console.log("First even prime number:", 2);

//write a js program to print first 10 even prime numbers
function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= 20; i += 2) {
        if (i === 4) {
            console.log(i);
            return true;
        }
    }
    return false;
}
isPrime(10);