// document.addEventListener('contextmenu', event => event.preventDefault());

let message = "Hello";
message = 'Bye';
console.log(message)

const workday = 5;
console.log(workday)

let obj = null;
console.log(typeof obj); // object

let counter = 120;
console.log(typeof(counter)); // "number"

counter = false; 
console.log(typeof(counter)); // "boolean"

counter = "Hi";
console.log(typeof(counter)); // "string"

counter = "99.99";
console.log(typeof(counter)); 

let counter1;
console.log(counter);        // undefined
console.log(typeof counter); // undefined

let pageView = 900719925n;
console.log(typeof(pageView));

let contact = {
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    phone: '(408)-555-9999',
    address: {
        building: '4000',
        street: 'North 1st street',
        city: 'San Jose',
        state: 'CA',
        country: 'USA'
    }
}

console.log(contact.age); // undefined

console.log(contact['phone']); // '(408)-555-9999'
console.log(contact['email']); // 'john.doe@example.com'

console.log(typeof(null));