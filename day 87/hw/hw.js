function calculate(a, b, operation) {
    return operation(a, b);
}

// დამხმარე პატარა ფუნქციები (ლოგიკები)
const add = (x, y) => x + y;
const subtract = (x, y) => x - y;
const multiply = (x, y) => x * y;

// შემოწმება:
console.log(calculate(10, 5, add));      // დაიბეჭდება: 15
console.log(calculate(10, 5, subtract)); // დაიბეჭდება: 5
console.log(calculate(10, 5, multiply)); // დაიბეჭდება: 50




function multiplier(n) {
    return function(num) {
        return num * n;
    };
}

// შემოწმება:
const double = multiplier(2); // ახალი ფუნქციაა, რომელიც ყოველთვის ამრავლებს 2-ზე
const triple = multiplier(3); // ახალი ფუნქციაა, რომელიც ყოველთვის ამრავლებს 3-ზე

console.log(double(5)); // დაიბეჭდება: 10 (5 * 2)
console.log(triple(5)); // დაიბეჭდება: 15 (5 * 3)





function applyToArray(arr, fn) {
    let newArray = [];
    for (let i = 0; i < arr.length; i++) {
        newArray.push(fn(arr[i]));
    }
    return newArray;
}

// შემოწმება:
const numbers = [1, 2, 3, 4];
const square = x => x * x;

console.log(applyToArray(numbers, square)); // დაიბეჭდება: [1, 4, 9, 16]




function findFirst(arr, fn) {
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i])) {
            return arr[i]; // პირველივე დამთხვევაზე აბრუნებს ელემენტს და წყვეტს ციკლს
        }
    }
    return undefined;
}

// შემოწმება:
const nums = [1, 3, 7, 8, 11, 12];
const isEven = x => x % 2 === 0; // ეძებს ლუწ რიცხვს

console.log(findFirst(nums, isEven)); // დაიბეჭდება: 8 (რადგან 8 არის პირველი ლუწი რიცხვი მასივში)








function all(arr, fn) {
    for (let i = 0; i < arr.length; i++) {
        if (!fn(arr[i])) {
            return false; // თუ ერთმა მაინც არ დააკმაყოფილა პირობა, მაშინვე აბრუნებს false-ს
        }
    }
    return true; // თუ ციკლი დასრულდა და false არ გაეშვა, ე.ი. ყველა აკმაყოფილებს
}

// შემოწმება:
const list1 = [2, 4, 6, 8];
const list2 = [2, 4, 5, 8];
const checkEven = x => x % 2 === 0;

console.log(all(list1, checkEven)); // დაიბეჭდება: true (ყველა ლუწია)
console.log(all(list2, checkEven)); // დაიბეჭდება: false (რადგან 5 კენტია)







