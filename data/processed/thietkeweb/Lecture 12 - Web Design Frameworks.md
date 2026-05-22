# Lecture 12 - Web Design Frameworks



<!-- page 2 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Contents
## 8.1. jQuery
## 8.2. Bootstrap


<!-- page 3 -->

# 8.1. jQuery

- jQuery Intro
- jQuery Syntax
- jQuery Selectors
- jQuery Events


<!-- page 4 -->

# jQuery Intro

- jQuery is a JavaScript Library.
- jQuery is a lightweight, "write less, do more", JavaScript library.
- jQuery takes a lot of common tasks that require many lines of JavaScript code to accomplish, and wraps them into methods that you can call with a single line of code.
- jQuery also simplifies a lot of the complicated things from JavaScript, like AJAX calls and DOM manipulation.

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide

What is your impression?


<!-- page 5 -->

# Adding jQuery to Your Web Pages

**Download the jQuery library from jQuery.com**
http://jquery.com/download/

**Or include jQuery from a CDN, like Google**

```html
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
```


<!-- page 6 -->

# jQuery Syntax

The jQuery syntax is tailor-made for selecting HTML elements and performing some action on the element(s).

Basic syntax is: **$(selector).action()**

- A $ sign to define/access jQuery
- A (selector) to "query (or find)" HTML elements
- A jQuery action() to be performed on the element(s)


<!-- page 7 -->

# jQuery Syntax

## Examples:
- `$(this).hide()` - hides the current element.
- `$("p").hide()` - hides all `<p>` elements.
- `$(".test").hide()` - hides all elements with class="test".
- `$("#test").hide()` - hides the element with id="test".


<!-- page 8 -->

# The Document Ready Event

This is to prevent any jQuery code from running before the document is finished loading (is ready).

Here are some examples of actions that can fail if methods are run before the document is fully loaded:

- Trying to hide an element that is not created yet
- Trying to get the size of an image that is not loaded yet

```javascript
$(document).ready(function(){

  // jQuery methods go here...

});
```


<!-- page 9 -->

# jQuery Selectors

jQuery selectors allow you to select and manipulate HTML element(s).

jQuery selectors are used to "find" (or select) HTML elements based on their name, id, classes, types, attributes, values of attributes and much more. It's based on the existing CSS Selectors, and in addition, it has some own custom selectors.


<!-- page 10 -->

# The element Selector

The jQuery element selector selects elements based on the element name.

You can select all `<p>` elements on a page like this:

`$("p")`

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_p


<!-- page 11 -->

# The #id Selector

The jQuery #id selector uses the id attribute of an HTML tag to find the specific element.

An id should be unique within a page, so you should use the #id selector when you want to find a single, unique element.

To find an element with a specific id, write a hash character, followed by the id of the HTML element:

`$("#test")`

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_id


<!-- page 12 -->

# The .class Selector

The jQuery .class selector finds elements with a specific class.

To find elements with a specific class, write a period character, followed by the name of the class:

`$(".test")`

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_class


<!-- page 13 -->

# jQuery Events

An event represents the precise moment when something happens.

Examples: moving a mouse over an element, selecting a radio button, clicking on an element

| Mouse Events | Keyboard Events | Form Events | Document/Window Events |
| :--- | :--- | :--- | :--- |
| click | keypress | submit | load |
| dblclick | keydown | change | resize |
| mouseenter | keyup | focus | scroll |
| mouseleave | | blur | unload |
