function isPerfectCube(num) {

    const cubeRoot = Math.cbrt(num);

    return Number.isInteger(cubeRoot);
}
const testNumbers = [27, 64, 10, 125, -8, 0];
testNumbers.forEach(n => {
    console.log(`${n} is a perfect cube: ${isPerfectCube(n)}`);
});