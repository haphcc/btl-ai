### BÀI 4

#### BÀI GIẢNG 4: CSS

## TRANG 1

Thiết kế Web - Bài giảng 4: CSS


## TRANG 2

Nội dung

3.1. Giới thiệu CSS. 3.2. Formatting text. 3.3. Color và background. 3.4. CSS hyperlink. 3.5. CSS table. 3.6. CSS form.


## TRANG 3

3.1. Giới thiệu CSS

CSS là viết tắt của Cascading Style Sheets. CSS mô tả cách HTML element được hiển thị trên màn hình, trên giấy hoặc trong các media khác. CSS giúp tiết kiệm nhiều công sức vì có thể kiểm soát layout của nhiều webpage cùng lúc.


## TRANG 4

Cách style sheet hoạt động

1. Bắt đầu với một document đã được markup bằng HTML.

2. Viết style rule cho cách bạn muốn một số element hiển thị.

3. Gắn style rule vào document. Khi browser hiển thị document, nó tuân theo các rule của bạn để render element (trừ khi người dùng áp dụng một số style bắt buộc; phần này sẽ nói sau).


## TRANG 5

Markup document

Mở file cooking.html trong course materials (LWD5e_materials/ch11) để xem document hiển thị mặc định như thế nào.


## TRANG 6

Viết style rule

Style sheet được tạo từ một hoặc nhiều chỉ dẫn style (gọi là style rule) mô tả cách một element hoặc nhóm element sẽ được hiển thị.

Mỗi rule chọn một element và khai báo nó sẽ trông như thế nào.

h1 { color: green; } p { font-size: large; font-family: sans-serif; }


## TRANG 7

Viết style rule

Selector xác định element hoặc các element bị ảnh hưởng, còn declaration cung cấp chỉ dẫn render. Declaration gồm property (chẳng hạn color) và value của nó (green), được ngăn cách bằng dấu hai chấm và một khoảng trắng.


## TRANG 8

Kiểm tra kiến thức

Xác định các phần khác nhau của style rule sau:

blockquote { line-height: 1.5; }

Đâu là:

- Selector: _________

- Declaration: _________

- Property: _________

- Value: _________


## TRANG 9

Selector

- Simple selector (chọn element dựa trên name, id, class)
- Combinator selector (chọn element dựa trên quan hệ cụ thể giữa chúng)
- Pseudo-class selector (chọn element dựa trên một state nhất định)
- Pseudo-element selector (chọn và style một phần của element)
- Attribute selector (chọn element dựa trên attribute hoặc attribute value)

https://www.w3schools.com/css/css_selectors.asp


## TRANG 10

Simple selector

- Element selector chọn HTML element dựa trên element name.

- id selector dùng id attribute của một HTML element để chọn một element cụ thể.

- id của một element là duy nhất trong một page, vì vậy id selector được dùng để chọn một element duy nhất.

- class selector chọn HTML element có class attribute cụ thể.

- universal selector (*) chọn tất cả HTML element trên page.

- grouping selector chọn tất cả HTML element có cùng style definition.


## TRANG 11

Element selector

Ở đây, tất cả element &lt;p&gt; trên page sẽ được căn giữa và có màu chữ đỏ.


## TRANG 12

id selector

CSS rule dưới đây sẽ được áp dụng cho HTML element có id="para1".


## TRANG 13

class selector

Trong ví dụ này, element &lt;p&gt; sẽ được style theo class="center" và class="large".


## TRANG 14

universal selector

CSS rule dưới đây sẽ ảnh hưởng tới mọi HTML element trên page.


## TRANG 15

group selector

Trong ví dụ này, chúng ta đã nhóm các selector.


## TRANG 16

Exercise 4-1

Làm bài tập ở trang 244 - giáo trình.


## TRANG 17

Cách style sheet hoạt động

1. Bắt đầu với một document đã được markup bằng HTML.

2. Viết style rule cho cách bạn muốn một số element hiển thị.

3. Gắn style rule vào document. Khi browser hiển thị document, nó tuân theo các rule của bạn để render element.


## TRANG 18

Ba cách chèn CSS

External CSS:

- Một file external .css

- Page hiện tại tham chiếu tới external CSS file bằng element &lt;link&gt;

&lt;link rel="stylesheet" href="mystyle.css"&gt;

Internal CSS:

- Được định nghĩa bên trong element &lt;style&gt;, trong phần head

Inline CSS:

- Áp dụng một style duy nhất cho một element đơn lẻ

&lt;h1 style="color:blue;text-align:center;"&gt;This is a heading&lt;/h1&gt;


## TRANG 19

Ba cách chèn CSS - Thực hành

Exercises & Homeworks / Lecture 4 / index.html


## TRANG 20

Đọc thêm

Inheritance

- Document structure

- Parent và child

Conflicting style: Cascade

- Priority, rule order

- Specificity

Trang 246.


## TRANG 21

Kiểm tra kiến thức

Inheritance

1. Nếu thêm một element &lt;a&gt; bên trong element &lt;h1&gt;, element &lt;a&gt; có nhận style của element &lt;h1&gt; hay không? Vì sao?

2. Ancestor, sibling là gì?

Conflicting style: Cascade

1. Nếu element &lt;h1&gt; nhận một số style từ external CSS my_style.css, đồng thời có rule trong internal CSS của HTML và cũng có inline CSS, thứ tự ưu tiên là gì?

Đọc thêm:

- https://www.w3schools.com/css/css_specificity.asp

- Trang 246


## TRANG 22

3.2. Formatting text

Font property (CSS 2.1): font-family, font-size, font-weight, font-style. Các cập nhật khác trong CSS 3.


## TRANG 23

Đọc thêm

Đọc câu chuyện ở trang 263-265 để xem chúng ta có thể dùng bao nhiêu font khi thiết kế webpage.

Inspect một số website bạn biết, xem thiết lập font-family của chúng. Bạn thích font nào hơn?


## TRANG 24

3.2. Formatting text

- Exercise 4-2: Formatting a menu (trang 268)


## TRANG 25

Thêm về font

Font size: trang 269. Font Weight (Boldness). Font Style (Italics). Font Stretch (Condensed và Extended).


## TRANG 26

Thay đổi text color

- Value: color value (name hoặc numeric)
- Default: phụ thuộc vào browser và preference của người dùng
- Applies to: tất cả element
- Inherits: yes


## TRANG 27

Exercise 4-3: Dùng selector để format text

Thêm một vài style rule nữa bằng descendant, ID và class selector kết hợp với các font và color property đã học đến thời điểm này. Trang 286.


## TRANG 28

Đọc thêm

Text line adjustment. Text decoration. Capitalization. Space out. Shadowing. List bullet. Trang 288.


## TRANG 29

3.3. Color và background

Color value:

- Color name

- RGB color value

Foreground color. Background color.


## TRANG 30

Color name

Cách trực quan nhất để chỉ định một color là gọi nó bằng tên.

color: silver;

Tên đó phải là một trong các color keyword được định nghĩa sẵn trong CSS Recommendation.

CSS cũng hỗ trợ tập mở rộng gồm 140 color name.


## TRANG 31

RGB color value

Cách phổ biến nhất để chỉ định một color là dùng RGB value. Cách này cũng cho bạn hàng triệu màu để lựa chọn.

color: rgb(200, 178, 230);

color: #C8B2E6;


## TRANG 32

Thực hành: dùng Color Picker để chọn đúng color

Google "Color picker" và cài công cụ bạn thích.


## TRANG 33

Background color

Dùng background-color để áp dụng background color cho bất kỳ element nào.


## TRANG 34

Exercise: Thêm color vào document

Trang 325 - giáo trình.


## TRANG 35

3.4. CSS hyperlink

Với CSS, link có thể được style theo nhiều cách khác nhau.

Link có thể được style bằng bất kỳ CSS property nào (ví dụ color, font-family, background, v.v.).


## TRANG 36

3.4. CSS hyperlink

Link có thể được style khác nhau tùy vào state của nó.

- a:link - link bình thường, chưa được truy cập
- a:visited - link người dùng đã truy cập
- a:hover - link khi người dùng di chuột qua
- a:active - link tại thời điểm được click

Exercises & Homeworks / Lecture 4 / a_link.html


## TRANG 37

Style sheet hữu ích cho link

Property text-decoration thường được dùng để bỏ gạch chân khỏi link.

Property background-color có thể dùng để chỉ định background color cho link.

Button link. Exercises & Homeworks / Lecture 4 / button_link.html


## TRANG 38

Đọc thêm

3.5. CSS table: https://www.w3schools.com/css/css_table.asp

3.6. CSS form: https://www.w3schools.com/css/css_form.asp


## TRANG 39

Bài tập về nhà

Trang 334 - giáo trình: Working with colors, background images and positioning.
