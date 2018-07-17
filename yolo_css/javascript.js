console.log('Hello World');
const name = "Charlie";
console.log(`Hello ${name} !`);

const age =16;
console.log(`You are ${age} years old!`);

if (age >= 18) {
  console.log("you can get your license");
} else if (age <15) {
  console.log ("you cannot get permit and you cannot vote");
} else {
  console.log ("you can get permit and not vote")
}

// line comment
/* block comment

//execute if expression is true
} else {
  // execute if expession is false
}
*/
function makeGreetMessage(name1, name2=null) {
  if (name2=null) {
    return `hello ${name1}`;
    console.log('This will not show up')
  } else {
  // code
  console.log(`Hello ${name1} and ${name2}`);
  }
}


function greet(name1,name2=null) {
  if (name1[0] !== "A"){

  }
}

greet ('Alice', 'Bob');

const multiplyBy3 = (x) => x * 3;
console.log(multiplyBy3(3));

setInterval(() => {
  console.log(new date());
}, 1000);

greet(name1, name2='null') {
  if (name2=null) {
    console.log(`Hello ${name}.`);
  } else {
  // code
  console.log(`Hello ${name1} and ${name2}`);
  }
}
