# Lecture 4 - CSS



<!-- page 2 -->

# Contents

## 3.1. Introduction to CSS
## 3.2. Formatting text
## 3.3. Colors and background
## 3.4. CSS hyperlinks
## 3.5. CSS tables
## 3.6. CSS forms


<!-- page 3 -->

## 3.1. Introduction to CSS

CSS stands for **Cascading Style Sheets**

CSS describes how HTML elements are to be displayed on screen, paper, or in other media

CSS saves a lot of work. It can control the layout of multiple web pages all at once


<!-- page 4 -->

# How style sheets work

1. Start with a document that has been marked up in HTML.
2. Write style rules for how you'd like certain elements to look.
3. Attach the style rules to the document. When the browser displays the document, it follows your rules for rendering elements (unless the user has applied some mandatory styles, but we'll get to that later).


<!-- page 5 -->

# Marking Up the Document

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

Open the **cooking.html** in the course materials (**LWD5e_materials/ch11**) to see how the document looks by default.

---

## Cooking with Daniel from Nada Surf

I had the pleasure of spending a crisp, Spring day in Portsmouth, NH cooking and chatting with Daniel Lorca of the band Nada Surf as he prepared a gourmet, sit-down dinner for 28 pals.

When I first invited Nada Surf to be on the show, I was told that Daniel Lorca was the guy I wanted to talk to. Then Daniel emailed his response: "im way into it, but i don't want to talk about it, i wanna do it." After years of only having access to touring bands between their sound check and set, I've been doing a lot of talking about cooking with rockstars. To actually cook with a band was a dream come true.

### Six-hour Salad

Daniel prepared a salad of arugula, smoked tomatoes, tomato jam, and grilled avocado (it's as good as it sounds!). I jokingly called it "6-hour Salad" because that's how long he worked on it. The fresh tomatoes were slowly smoked over woodchips in the grill, and when they were softened, Daniel separated out the seeds which he reduced into a smoky jam. The tomatoes were cut into strips to put on the salads. As the day meandered, the avocados finally went on the grill after dark. I was on flashlight duty while Daniel checked for the perfect grill marks.

I wrote up a streamlined adaptation of his recipe that requires much less time and serves 6 people instead of fivetimes that amount.

### The Main Course

In addition to the smoky grilled salad, Daniel served tarragon cornish hens with a cognac cream sauce loaded with chanterelles and grapes, and wild rice with grilled ramps (wild garlicky leeks). Dinner was served close to midnight, but it was a party so nobody cared.

We left that night (technically, early the next morning) with full bellies, new cooking tips, and nearly 5 hours of footage. I'm considering renaming the show "Cooking with Nada Surf".


<!-- page 6 -->

# Write style rules

A style sheet is made up of one or more style instructions (called **style rules**) that describe how an element or group of elements should be displayed.

Each rule **selects** an element and **declares** how it should look.

`h1 { color: green; }`
`p { font-size: large; font-family: sans-serif; }`


<!-- page 7 -->

# Write style rules

The **selector** that identifies the element or elements to be affected, and the **declaration** that provides the rendering instructions

The declaration, in turn, is made up of a **property** (such as color) and its **value** (green), separated by a colon and a space

declaration
`selector { property: value; }`

declaration block
`selector {`
`  property1: value1;`
`  property2: value2;`
`  property3: value3;`
`}`


<!-- page 8 -->

# Test your knowledge

Identify the various parts of this style rule:

***blockquote { line-height: 1.5; }***

What is:
- Selector: \_\_\_\_\_\_\_\_
- Declaration: \_\_\_\_\_\_\_\_
- Property: \_\_\_\_\_\_\_\_
- Value: \_\_\_\_\_\_\_\_


<!-- page 9 -->

# Selectors

- **Simple selectors (select elements based on name, id, class)**
- Combinator selectors (select elements based on a specific relationship between them)
- Pseudo-class selectors (select elements based on a certain state)
- Pseudo-elements selectors (select and style a part of an element)
- Attribute selectors (select elements based on an attribute or attribute value)

https://www.w3schools.com/css/css_selectors.asp


<!-- page 10 -->

# Simple selectors

- The element selector selects HTML elements based on the element name.
- The id selector uses the id attribute of an HTML element to select a specific element.
    - The id of an element is unique within a page, so the id selector is used to select one unique element!
- The class selector selects HTML elements with a specific class attribute.
- The universal selector (*) selects all HTML elements on the page.
- The grouping selector selects all the HTML elements with the same style definitions.


<!-- page 11 -->

# Element selector

Here, all `<p>` elements on the page will be center-aligned, with a red text color:

```html
<!DOCTYPE html>
<html>
<head>
<style>
p {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<p>Every paragraph will be affected by the style.</p>
<p id="para1">Me too!</p>
<p>And me!</p>

</body>
</html>
```

Every paragraph will be affected by the style.
Me too!
And me!


<!-- page 12 -->

# The id selector

The CSS rule below will be applied to the HTML element with **id="para1"**:

```html
<!DOCTYPE html>
<html>
<head>
<style>
#para1 {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<p id="para1">Hello World!</p>
<p>This paragraph is not affected by the style.</p>

</body>
</html>
```

Hello World!
This paragraph is not affected by the style.


<!-- page 13 -->

BAV HỌC VIỆN NGÂN HÀNG BANKING ACADEMY OF VIETNAM

# The class selector

In this example the `<p>` element will be styled according to **class="center"** and to **class="large"**

```html
<!DOCTYPE html>
<html>
<head>
<style>
p.center {
  text-align: center;
  color: red;
}

p.large {
  font-size: 300%;
}
</style>
</head>
<body>

<h1 class="center">This heading will not be affected</h1>
<p class="center">This paragraph will be red and center-aligned.</p>
<p class="center large">This paragraph will be red, center-aligned, and in a large font-size.</p>

</body>
</html>
```

This heading will not be affected
This paragraph will be red and center-aligned.
This paragraph will be red, center-aligned, and in a large font-size.


<!-- page 14 -->

# The universal selector

The CSS rule below will affect every HTML element on the page:

```html
<!DOCTYPE html>
<html>
<head>
<style>
* {
  text-align: center;
  color: blue;
}
</style>
</head>
<body>

<h1>Hello world!</h1>

<p>Every element on the page will be affected by the style.</p>
<p id="para1">Me too!</p>
<p>And me!</p>

</body>
</html>
```

**Hello world!**
Every element on the page will be affected by the style.
Me too!
And me!


<!-- page 15 -->

# The group selector

In this example we have grouped the selectors

```html
<!DOCTYPE html>
<html>
<head>
<style>
h1, h2, p {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1>Hello World!</h1>
<h2>Smaller heading!</h2>
<p>This is a paragraph.</p>

</body>
</html>
```

Hello World!
Smaller heading!
This is a paragraph.


<!-- page 16 -->

# Exercise 4-1

Do the exercise in page 244 - textbook

## Cooking with Daniel from Nada Surf

I had the pleasure of spending a crisp, Spring day in Portsmouth, NH cooking and chatting with Daniel Lorca of the band Nada Surf as he prepared a gourmet, sit-down dinner for 28 pals.

When I first invited Nada Surf to be on the show, I was told that Daniel Lorca was the guy I wanted to talk to. Then Daniel emailed his response: "i'm way into it, but i don't want to talk about it, i wanna do it." After years of only having access to touring bands between their sound check and set, I've been doing a lot of *talking* about cooking with rockstars. To actually cook with a band was a dream come true.

### Six-hour Salad

Daniel prepared a salad of arugula, smoked tomatoes, tomato jam, and grilled avocado (it's as good as it sounds!). I jokingly called it "6-hour Salad" because that's how long he worked on it. The fresh tomatoes were slowly smoked over woodchips in the grill, and when they were softened, Daniel separated out the seeds which he reduced into a smoky jam. The tomatoes were cut into strips to put on the salads. As the day meandered, the avocados finally went on the grill after dark. I was on flashlight duty while Daniel checked for the perfect grill marks.

I wrote up a streamlined adaptation of his recipe that requires *much* less time and serves 6 people instead of *fivetimes* that amount.

### The Main Course

In addition to the smoky grilled salad, Daniel served tarragon cornish hens with a cognac cream sauce loaded with chanterelles and grapes, and wild rice with grilled ramps (wild garlicky leeks). Dinner was served close to midnight, but it was a party so nobody cared.

We left that night (technically, early the next morning) with full bellies, new cooking tips, and nearly 5 hours of footage. I'm considering renaming the show "Cooking with Nada Surf".


<!-- page 17 -->

# How style sheets work

1. Start with a document that has been marked up in HTML.
2. Write style rules for how you'd like certain elements to look.
3. **Attach the style rules to the document. When the browser displays the document, it follows your rules for rendering elements (unless the user has applied some mandatory styles, but we'll get to that later).**


<!-- page 18 -->

HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# Three Ways to Insert CSS

## External CSS:
- An external .css file
- The current page should refers to the external CSS file by the `<link>` element
`<link rel="stylesheet" href="mystyle.css">`

## Internal CSS:
- Defined inside the `<style>` element, inside the head section

## Inline CSS:
- Apply a unique style for a single element
`<h1 style="color:blue;text-align:center;">This is a heading</h1>`

```html
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
}
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
```


<!-- page 19 -->

# Three Ways to Insert CSS - Hands on

## Exercises & Homeworks / Lecture 4 / index.html


<!-- page 20 -->

# Further reading

## **Inheritance**
- Document structure
- Parents and children

## **Conflicting Styles: The Cascade**
- Priority, Rule order
- Specificity

Page 246


<!-- page 21 -->

# Test your knowledge

## Inheritance
1. If we add an <a> element inside a <h1> element, will the <a> element take the style of the <h1> element or not, why?
2. Ancestor, sibling là gì?

## Conflicting Styles: The Cascade
1. If the element <h1> takes some styles from the external css **my_style.css**, but also has some rules in the internal css HTML, and also some inline css, what is the priority?

Read more:
- https://www.w3schools.com/css/css_specificity.asp
- Page 246


<!-- page 22 -->

## 3.2. Formatting text

### Font properties (CSS 2.1)
- font-family
- font-size
- font-weight
- font-style

*More updates on CSS 3*

```css
body { font-family: Arial; }
var { font-family: Courier, monospace; }
p { font-family: "Duru Sans", Verdana, sans-serif; }
```

```css
p.normal {
    font-weight: normal;
}

p.thick {
    font-weight: bold;
}

p.thicker {
    font-weight: 900;
}
```

```css
p.normal {
    font-style: normal;
}

p.italic {
    font-style: italic;
}

p.oblique {
    font-style: oblique;
}
```


<!-- page 23 -->

# Further reading

Read the story in page 263-265 to see how many fonts can we use in designing web pages.

Inspect some websites you know, see their font-family settings. Which font do you prefer?


<!-- page 24 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# 3.2. Formatting text

## Exercise 4-2: Formatting a menu (page 268)

### **Black Goose Bistro • Summer Menu**
Baker's Corner, Seekonk, Massachusetts
Hours: Monday through Thursday: 11 to 9, Friday and Saturday; 11 to midnight

#### **Appetizers**
This season, we explore the spicy flavors of the southwest in our appetizer collection.

Black bean purses
Spicy black bean and a blend of mexican cheeses wrapped in sheets of phyllo and baked until golden. $3.95

Southwestern napoleons with lump crab — **new item!**
Layers of light lump crab meat, bean and corn salsa, and our handmade flour tortillas. $7.95

#### **Main courses**
Big, bold flavors are the name of the game this summer. Allow us to assist you with finding the perfect wine.

Jerk rotisserie chicken with fried plantains — **new item!**
Tender chicken slow-roasted on the rotisserie, flavored with spicy and fragrant jerk sauce and served with fried plantains and fresh mango. **Very spicy.** $12.95

Shrimp sate kebabs with peanut sauce
Skewers of shrimp marinated in lemongrass, garlic, and fish sauce then grilled to perfection. Served with spicy peanut sauce and jasmine rice. $12.95

Grilled skirt steak with mushroom fricasee
Flavorful skirt steak marinated in asian flavors grilled as you like it*. Served over a blend of sauteed wild mushrooms with a side of blue cheese mashed potatoes. $16.95

* We are required to warn you that undercooked food is a health risk.


<!-- page 25 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# More about fonts

**Font size:** Page 269
**Font Weight (Boldness)**
**Font Style (Italics)**
**Font Stretch (Condensed and Extended)**


<!-- page 26 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Changing text color

- Values: color value (name or numeric)
- Default: depends on the browser and user's preferences
- Applies to: all elements
- Inherits: yes

```css
h1 { color: gray; }
h1 { color: #666666; }
h1 { color: #666; }
h1 { color: rgb(102,102,102); }
```


<!-- page 27 -->

# Exercise 4-3. Using selector to format text

Add a few more style rules using descendant, ID, and class selectors combined with the font and color properties we've learned about so far

**Page 286**

## Black Goose Bistro • Summer Menu

Baker's Corner, Seekonk, Massachusetts
Hours: Monday through Thursday: 11 to 9, Friday and Saturday; 11 to midnight

### Appetizers

This season, we explore the spicy flavors of the southwest in our appetizer collection.

**Black bean purses**
Spicy black bean and a blend of mexican cheeses wrapped in sheets of phyllo and baked until golden. $3.95

**Southwestern napoleons with lump crab — new item!**
Layers of light lump crab meat, bean and corn salsa, and our handmade flour tortillas. $7.95

### Main courses

Big, bold flavors are the name of the game this summer. Allow us to assist you with finding the perfect wine.

**Jerk rotisserie chicken with fried plantains — new item!**
Tender chicken slow-roasted on the rotisserie, flavored with spicy and fragrant jerk sauce and served with fried plantains and fresh mango. **Very spicy.** $12.95

**Shrimp sate kebabs with peanut sauce**
Skewers of shrimp marinated in lemongrass, garlic, and fish sauce then grilled to perfection. Served with spicy peanut sauce and jasmine rice. $12.95

**Grilled skirt steak with mushroom fricasee**
Flavorful skirt steak marinated in asian flavors grilled as you like it*. Served over a blend of sauteed wild mushrooms with a side of blue cheese mashed potatoes. $16.95

* We are required to warn you that undercooked food is a health risk.


<!-- page 28 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Further reading

- ***Text line adjustments***
- ***Text decorations***
- ***Capitalization***
- ***Space out***
- ***Shadowing***
- ***List bullets***

Page 288


<!-- page 29 -->

BAV HỌC VIỆN NGÂN HÀNG BANKING ACADEMY OF VIETNAM 1961

### 3.3. Colors and background

Color values:
- Color names
- RGB color values

Foreground color

Background color


<!-- page 30 -->

# Color names

The most intuitive way to specify a color is to call it by name.

**color: silver;**

It has to be one of the color keywords predefined in the CSS Recommendation.

CSS3 adds support for the extended set of 140 (rather fanciful) color names.

| Color Name | Hex Code |
| :--- | :--- |
| black | #000000 |
| gray | #808080 |
| silver | #C0C0C0 |
| white | #FFFFFF |
| maroon | #800000 |
| red | #FF0000 |
| purple | #800080 |
| fuchsia | #FF00FF |
| green | #008000 |
| lime | #00FF00 |
| olive | #808000 |
| yellow | #FFFF00 |
| navy | #000080 |
| blue | #0000FF |
| teal | #008080 |
| aqua | #00FFFF |
| orange (CSS 2.1) | #FFA500 |


<!-- page 31 -->

# RGB color values

The most common way to specify a color is by its RGB value. It also gives you millions of colors to choose from.

**color: rgb(200, 178, 230);**
**color: #C8B2E6;**

- RGB: 255, 255, 255 white
    - R: 255 (100%)
    - G: 255 (100%)
    - B: 255 (100%)
- RGB: 128, 128, 128 gray
    - R: 128 (50%)
    - G: 128 (50%)
    - B: 128 (50%)
- RGB: 0, 0, 0 black
    - R: 0 (0%)
    - G: 0 (0%)
    - B: 0 (0%)
- RGB: 200, 178, 230 pleasant lavender
    - R: 200 (78%)
    - G: 178 (70%)
    - B: 230 (90%)


<!-- page 32 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Hands-on: use ColorPic to choose the correct color

Google for “Color picker” and install your favourite ones

- **RGB: 255, 255, 255 white**
    - R: 255 (100%)
    - G: 255 (100%)
    - B: 255 (100%)
- **RGB: 128, 128, 128 gray**
    - R: 128 (50%)
    - G: 128 (50%)
    - B: 128 (50%)
- **RGB: 0, 0, 0 black**
    - R: 0 (0%)
    - G: 0 (0%)
    - B: 0 (0%)
- **RGB: 200, 178, 230 pleasant lavender**
    - R: 200 (78%)
    - G: 178 (70%)
    - B: 230 (90%)


<!-- page 33 -->

# Background color

Use **background-color** to apply a background color to any element.

```css
blockquote {
  border: 4px dashed;
  color: green;
  background-color: #c6de89;
}
```

In the latitude of central New England, cabbages are not secure from injury from frost with less than a foot of earth thrown over the heads. In mild winters a covering of half that depth will be sufficient; but as we have no prophets to foretell our mild winters, a foot of earth is safer than six inches.


<!-- page 34 -->

# Exercise: Adding color to a document

## Page 325. Textbook

| Color | RGB / Hex |
| :--- | :--- |
| purple | R:153, G:51, B:153 <br> #993399 or #939 |
| muted purple | R:147, G:115, B:147 <br> #937393 |
| bright purple | R:199, G:0, B:242 <br> #C700F2 |
| vibrant purple | R:255, G:0, B:255 <br> #FF00FF |
| light green | R:210, G:220, B:157 <br> #D2DC9D |
| light brown | R:204, G:102, B:0 <br> #CC6600 or #C60 |

***

**Black Goose Bistro • Summer Menu**
Baker's Corner, Seekonk, Massachusetts
HOURS: MONDAY THROUGH THURSDAY 11 to 9, FRIDAY AND SATURDAY 11 to midnight

- Appetizers
- Main Courses
- Traditional Toasts
- Dessert Selection

### APPETIZERS
This season, we explore the spicy flavors of the southwest in our appetizer collection.

**Black bean purses**
Spicy black bean and a blend of mexican cheeses wrapped in sheets of phyllo and baked until golden. $3.95

**Southwestern napoleons with lump crab – new item!**
Layers of light lump crab meat, bean and corn salsa, and our handmade flour tortillas. $7.95

### MAIN COURSES
Big, bold flavors are the name of the game this summer. Allow us to assist you with finding the perfect wine.

**Jerk rotisserie chicken with fried plantains – new item!**
Tender chicken slow-roasted on the rotisserie, flavored with spicy and fragrant jerk sauce and served with fried plantains and fresh mango. Very spicy. $12.95

**Shrimp sate kebabs with peanut sauce**
Skewers of shrimp marinated in lemon...


<!-- page 35 -->

## 3.4. CSS hyperlinks

With CSS, links can be styled in many different ways.

Text Link, Text Link, Link Button, Link Button

Links can be styled with any CSS property (e.g. color, font-family, background, etc.).


<!-- page 36 -->

### 3.4. CSS hyperlinks

Links can be styled differently depending on what **state** they are in.

- a:link - a normal, unvisited link
- a:visited - a link the user has visited
- a:hover - a link when the user mouses over it
- a:active - a link the moment it is clicked

**Exercises & Homeworks / Lecture 4 / a_link.html**


<!-- page 37 -->

# Useful style sheets for links

The **text-decoration** property is mostly used to remove underlines from links:

The **background-color** property can be used to specify a background color for links:

## Button link
***Exercises & Homeworks / Lecture 4 / button_link.html***
