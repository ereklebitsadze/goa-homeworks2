let age = 18; // თავდაპირველი მნიშვნელობა
age = 20;     // მნიშვნელობის შეცვლა

console.log(age); // ტერმინალში დაიბეჭდება: 20


let text = "გამარჯობა";   // string
let num = 42;             // number
let isHappy = true;       // boolean
let emptyValue = null;    // null
let nonDefined;           // undefined

console.log(typeof text);       // "string"
console.log(typeof num);        // "number"
console.log(typeof isHappy);    // "boolean"
console.log(typeof emptyValue); // "object" -> (ეს არის JavaScript-ის ცნობილი ბაგი/თავისებურება, null-ზე აბრუნებს object-ს)
console.log(typeof nonDefined); // "undefined"



const name = "გიორგი";

name = "ალექსანდრე"; 
// 👉 რა მოხდება: პროგრამა გაჩერდება და ამოაგდებს შეცდომას: "TypeError: Assignment to constant variable."
// 👉 რატომ: იმიტომ, რომ const ქივორდით გამოცხადებული ცვლადი არის "მხოლოდ წაკითხვადი" (read-only) 
// და მისი მნიშვნელობის შეცვლა ინიციალიზაციის შემდეგ აკრძალულია.


console.log("Hello Giorga"); // სტრინგი
console.log(25);              // რიცხვი (ასაკი)
console.log(true);            // ბულეანი (boolean)


let x = 10;
console.log(x); // დაიბეჭდება: 10

x = x + 5; // გაზრდა 5-ით (იგივეა რაც x += 5)
console.log(x); // დაიბეჭდება: 15

x = "ten"; // მონაცემთა ტიპის შეცვლა სტრინგად
console.log(x); // დაიბეჭდება: ten




