# Lecture 10 - JavaScript (cont.)



<!-- page 2 -->

# Contents

## 6.5. Loops and conditional statements
## 6.6. Functions
## 6.7. JavaScript Objects


<!-- page 3 -->

# 6.5. Loops and conditional statements

- **JavaScript For Loop**
- JavaScript For In
- JavaScript While Loop
- **JavaScript if, else, and else if**
- JavaScript Break and Continue


<!-- page 4 -->

# JavaScript For Loop

Loops can execute a block of code a number of times.

Loops are handy, if you want to run the same code over and over again, each time with a different value.

Instead of writing:
```javascript
text += cars[0] + "<br>";
text += cars[1] + "<br>";
text += cars[2] + "<br>";
text += cars[3] + "<br>";
text += cars[4] + "<br>";
text += cars[5] + "<br>";
```

You can write:
```javascript
for (let i = 0; i < cars.length; i++) {
  text += cars[i] + "<br>";
}
```
