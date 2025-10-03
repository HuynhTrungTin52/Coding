export function square(num) {
    return num * num;
}

export function factorial(n) {
    if (n < 0) return "Không tính được";
    if (n === 0) return 1;
    return n * factorial(n - 1);
}

export function sumAll(...numbers) { 
    return numbers.reduce((acc, curr) => acc + curr, 0);
}