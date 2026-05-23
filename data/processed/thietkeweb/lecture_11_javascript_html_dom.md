### BÀI 11

#### BÀI GIẢNG 11: JAVASCRIPT & HTML DOM

Thiết kế Web - Bài giảng 11: JavaScript & HTML DOM

Nội dung

7.1. Document Object Model (DOM). 7.2. Event handling. 7.3. Form validation. 7.4. AJAX.

7.1. Document Object Model (DOM)

HTML DOM. DOM method. DOM document. DOM element. DOM changing HTML. DOM changing CSS.

DOM

DOM là một chuẩn của W3C (World Wide Web Consortium).

"W3C Document Object Model (DOM) là một interface độc lập với platform và language, cho phép program và script truy cập, cập nhật động content, structure và style của một document."

## HTML DOM

HTML DOM là object model và programming interface tiêu chuẩn cho HTML. Nó định nghĩa:

- HTML element như object
- Property của tất cả HTML element
- Method để truy cập tất cả HTML element
- Event cho tất cả HTML element

Nói cách khác: HTML DOM là chuẩn cho cách lấy, thay đổi, thêm hoặc xóa HTML element.

## HTML DOM

Với HTML DOM, JavaScript có thể truy cập và thay đổi tất cả element của một HTML document.

## HTML DOM

Với object model, JavaScript có đủ khả năng để tạo dynamic HTML:

- JavaScript có thể thay đổi tất cả HTML element trong page
- JavaScript có thể thay đổi tất cả HTML attribute trong page
- JavaScript có thể thay đổi tất cả CSS style trong page
- JavaScript có thể xóa HTML element và attribute hiện có
- JavaScript có thể thêm HTML element và attribute mới
- JavaScript có thể phản hồi tất cả HTML event hiện có trong page
- JavaScript có thể tạo HTML event mới trong page

DOM method

HTML DOM method là các action bạn có thể thực hiện trên HTML element.

HTML DOM property là các value của HTML element mà bạn có thể set hoặc change.

Property là value bạn có thể get hoặc set (ví dụ thay đổi content của một HTML element).

Method là action bạn có thể thực hiện (ví dụ thêm hoặc xóa một HTML element).

DOM method - Ví dụ

Trong ví dụ trên, getElementById là một method, còn innerHTML là một property.

DOM document

DOM document

DOM document

DOM document

DOM element

Thực hành:

https://www.w3schools.com/js/js_htmldom_elements.asp

Bài tập:

https://github.com/sinhvtr/web_design_is19a/blob/main/JavaScript%20Exercises/Lecture%2011%20-%20JS%20%26%20DOM/Lecture11.html

1. Tìm tất cả phần tử div chứa đoạn text thể hiện giá sản phẩm. Có bao nhiêu phần tử như vậy?
2. In ra nội dung bên trong phần tử div cuối cùng tìm được.
3. Tìm tất cả phần tử ul trong trang web này, in ra số lượng phần tử tìm được.

DOM changing HTML

Changing HTML content: cách dễ nhất để sửa content của một HTML element là dùng property innerHTML.

document.getElementById(id).innerHTML = newHTML

Changing the value of an attribute:

document.getElementById(id).attribute = newValue

https://www.w3schools.com/js/tryit.asp?filename=tryjs_dom_image

https://www.w3schools.com/js/tryit.asp?filename=tryjs_dom_date

DOM changing HTML

Bài tập:

4. Tìm đến phần tử chứa dòng chữ Giỏ hàng, đổi dòng chữ này thành Cart.
5. Tìm đến phần tử chứa hình ảnh sản phẩm đầu tiên trên trang chủ, đổi hình ảnh thành một ảnh khác bất kỳ.

DOM changing CSS

Changing HTML style:

document.getElementById(id).style.property = newStyle

https://www.w3schools.com/js/tryit.asp?filename=tryjs_change_style

Using events: event được browser tạo ra khi "có điều gì đó xảy ra" với HTML element:

- Một element được click
- Page đã load
- Input field được thay đổi

https://www.w3schools.com/js/tryit.asp?filename=tryjs_dom_color2

DOM changing CSS

6. Chuyển tất cả giá sản phẩm thành chữ màu xanh blue, in đậm.
7. Tạo sự kiện khi di chuột vào ảnh logo thì width và height của ảnh được set thành 100.
8. Tạo sự kiện khi di chuột ra khỏi ảnh logo thì width và height của ảnh được set về 50 như cũ.

https://www.w3schools.com/js/tryit.asp?filename=tryjs_dom_animate_3

7.2. Event handling

Reacting to event. HTML event attribute. Assign event bằng HTML DOM.

Reacting to event

Khi user click chuột. Khi webpage đã load. Khi image đã load. Khi mouse di chuyển qua một element. Khi input field thay đổi. Khi HTML form được submit. Khi user nhấn một key.

https://www.w3schools.com/js/tryit.asp?filename=tryjs_event_onclick3

HTML event attribute

Để gán event cho HTML element, bạn có thể dùng event attribute.

https://www.w3schools.com/js/tryit.asp?filename=tryjs_events1

DOM event listener

Method addEventListener(), ví dụ:

addEventListener() gắn event handler vào một element mà không ghi đè event handler hiện có.

Syntax:

Bạn có thể dễ dàng remove event listener bằng method removeEventListener().

https://www.w3schools.com/js/tryit.asp?filename=tryjs_addeventlistener_add2

Bài tập

Exercises 11-12 / exercise_2.html. Sample: Exercises 11-12 / find_subjects_in_a_list.html

Đọc thêm

DOM Navigation: https://www.w3schools.com/js/js_htmldom_navigation.asp

DOM Nodes: https://www.w3schools.com/js/js_htmldom_nodes.asp

7.3. Form validation

Basic form validation. Data format validation.

Basic form validation

HTML form validation có thể được browser thực hiện tự động.

Nếu form field (fname) trống, required attribute sẽ ngăn form này được submit.

https://www.w3schools.com/js/js_validation.asp

Data format validation

HTML form validation có thể được thực hiện bằng JavaScript.

https://www.w3schools.com/js/tryit.asp?filename=tryjs_validation_js

Custom validation

Exercises 11-12 / exercise_1.html

7.4. AJAX

AJAX không phải là programming language.

AJAX là kỹ thuật để truy cập web server từ một webpage.

AJAX là viết tắt của Asynchronous JavaScript And XML.

https://www.w3schools.com/js/js_ajax_intro.asp
