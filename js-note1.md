---
title: "JavaScript-study-note1"
date: 2017-04-26 14:25:43
categories:
- Study Notes
tags:
- Prgramming Language
- JavaScript
---

Reference(in Chinese): 
http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000

# Fundamentals

JS is usually embedded into ```<head>``` tag.
Functions for debugging:
```JavaScript
alert(); // pop up
console.log(); // print to console
```

## Basic gramma

```JavaScript
; // ended every line
{...}; // code block
// comment a line
/* comment 
one more 
lines */
```

## Types of variables

Number
```JavaScript
123; // integer
0.345; // float
1.234e3; // 1234 float
Nan; // not a number
Infinity; // infinity number
0xff; // base-16
// + - * / %(modulo) 
```
String
```JavaScript
'abc';
// or
"abc";
```

Boolean
```JavaScript
true;
false; // null undefined 0 NaN '': false
```

Comparison
```JavaScript
&&; // and
||; // or
!; // not
// > < >= <=
===; // equals (do not use '==')
isNaN(NaN); // true // check if NaN
// compare float
1 / 3 === (1 - 2 / 3); // false
Math.abs(1 / 3 - (1 - 2 / 3)) < 1e-9; // true
```

null, undefined
```JavaScript
null; // empty
undefined; // undefined
// Specially:
a == null;
// equals
a === null || a === undefined;
```

Array
```JavaScript
[1, 2, 3.14, 'Hello', null, true]; // recommended
new Array(1, 2, 3.14, 'Hello'); 
// index from 0
```

Object
```JavaScript
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
};
person.name; // 'Bob' // 'objectName.attributeName' to access attributeVale
```

Variable
```JavaScript
var $_a = 2; // can be only claimed once
b = 2; // global variable // not recommended // error in 'strict' mode
```

## String

```JavaScript
// '' or ""
"I'm OK"; 
'I\'m \"OK\"!'; // \t \n \\('\')
'\x41' // 'A'
'\u4e2d\u6587'; // unicode string // '中文'
`this is a 
multi-line string`; // `...` // from ES6
// concat
var j = 'Java';
var s = 'Script';
'Java' + 'Script'; // 'JavaScript'
`${j}${s}`; // 'JavaScript' // from ES6
// feature
j[0] // 'J'
j[0] = 'S';
j[0]; // 'J' // string is unchangable
// functions
j.length; // 4
j.toLowerCase(); // java
j.toUpperCase(); // JAVA
j.indexOf('J'); // 0
j.indexOf('S'); // -1
j.substring(0, 2); // Ja
j.substring(0, 6); // Java
j.substring(0); // Java
```

## Array

```JavaScript
var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6;
arr; // [1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // [1, 2]
var arr = [1, 2, 3];
arr[5] = 'x';
arr; // [1, 2, 3, undefined, undefined, 'x']
// functions
// indexOf
// slice // similar to substring of String
var arr_copy = arr.slice(); // specially: copy an array
arr_copy === arr; // false
// pop() // pop from tail
// push(...) // append to tail
// shift() // pop from head
// unshift(...) // push to head
// sort()
// reverse()
// splice(idx, numToDel, ...elePushedToIdx) // return the elements deleted
// concat // return new 1-dim cancat-ed array
// join // return new String by elements(change o String) and String
```

## Object

```JavaScript
var person = {
    name: 'J', // Obj.Attr: attrValue // recommended
    'school': 'No.1 Middle School' //Obj[Key]: Value
}; // ends in ';'

// functions
'name' in person; // true
'toString' in person; // true // inherity
person.hasOwnProperty('name'); // true
person.hasOwnProperty('toString'); // false
```

## Condition

```JavaScript
if () {
} else if () {
} else {
}
```

## Loop

```JavaScript
var x = 0;
for (var i=1; i<=10000; i++) {
    x = x + i;
}
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    alert(key); // 'name', 'age', 'city'
}
var a = ['A', 'B', 'C'];
for (var i in a) {
    alert(i); // '0', '1', '2'
    alert(a[i]); // 'A', 'B', 'C'
}
while (cond) {
}
do {
} while (cond); // judge cond after 'do'
```

## Map & Set
from ES6
```JavaScript
var m = new Map();
var s = new Set();
// Map
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
// functions
m.set(key, value);
m.has(key); // true or false
m.get(key); // value
m.delete(key); // delete [key, value] from map
// Set
var s = new Set([1,2,3,2,'3']);
s; // Set {1, 2, 3, '3'}
// functions
s.add(ele)
s.delete(ele)
```

## iterable
from ES6
```JavaScript
// iterable: Array, Map, Set
// for ... of iterate elements
'use strict';
var a = [1, 2, 3];
for (var x of a) {
}
// for ... in iterate attributes
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    alert(x); // '0', '1', '2', 'name'
}
// forEach iterate and call function
// from ES5.1
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    alert(element); // 'A', 'B', 'C'
    alert(index); // 0, 1, 2
    alert(array); // ['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']
});
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    alert(element); // 'A', 'B', 'C'
    alert(sameElement); // 'A', 'B', 'C'
    alert(set); // s, s, s
});
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
    alert(key);
    alert(map);
});
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    alert(element);
});
```
