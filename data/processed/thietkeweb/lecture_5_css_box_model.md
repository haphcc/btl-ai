### BÀI 5

#### BÀI GIẢNG 5: CSS BOX MODEL

Thiết kế Web - Bài giảng 5: CSS box model

Nội dung

4.1. Box model. 4.2. Width và height. 4.3. Đơn vị đo khoảng cách. 4.4. Margin và padding. 4.5. Border. 4.6. Alignment. 4.7. Position attribute. 4.8. Overflow, float và display.

4.1. Box model

Cả block-level element và inline element đều tạo ra một hộp chữ nhật gọi là element box. Thực hành: Exercises & Homeworks / Lecture 5 / box_model.html

Chỉ định kích thước box

- Width
- Height
- Padding
- Border
- Margin

4.2. Width và height

Width và height của một box là giá trị số theo px, cm hoặc:

- auto: giá trị mặc định, do browser tính toán
- %: được tính theo phần trăm của outer box
- inherit: kế thừa từ parent/ancestor

Box-sizing: content-box | border-box

Thực hành

Sizing the content-box: giáo trình, trang 357. Sizing the border-box: giáo trình, trang 358. Exercises & Homeworks / Lecture 5 / sizing.html

Max-width và max-height

Max-width và max-height là giá trị chiều rộng và chiều cao tối đa. Với width thông thường, scrollbar sẽ xuất hiện trong browser nếu màn hình quá nhỏ. Với max-width, box sẽ được resize nếu màn hình không đủ lớn.

Thực hành

Exercises & Homeworks / Lecture 5 / max_width.html

4.3. Đơn vị đo khoảng cách

- Absolute distance
- Relative distance

4.3. Đơn vị đo khoảng cách

Absolute distance:

- cm: centimeters
- mm: millimeters
- in: inches (1in = 96px = 2.54cm)
- px: pixels (1px = 1/96 của 1in)
- pt: points (1pt = 1/72 của 1in)
- pc: picas (1pc = 12 pt)

Đọc thêm trong sách tham khảo: Responsive web design with HTML5 and CSS.

4.3. Đơn vị đo khoảng cách

Relative distance:

- em: tương đối với font size hiện tại
- rem: tương đối với font-size của root element
- ex: tương đối với x-height của font size hiện tại
- %: tương đối với parent element
- ch, vw, vh, vmin, vmax

Relative length unit co giãn tốt hơn giữa các môi trường render khác nhau.

Thực hành: relative distance

Exercises & Homeworks / Lecture 5 / relative_distance.html

4.4. Margin và padding

Margin được dùng để tạo khoảng cách xung quanh element, nằm bên ngoài bất kỳ border nào đã định nghĩa.

CSS có các property để chỉ định margin cho từng cạnh của element: margin-top, margin-right, margin-bottom, margin-left.

Giá trị margin

Tất cả margin property có thể nhận các giá trị sau:

- auto - browser tính margin
- length - chỉ định margin theo px, pt, cm, v.v.
- % - chỉ định margin theo phần trăm width của containing element
- inherit - margin được kế thừa từ parent element

Lưu ý: được phép dùng giá trị âm.

Exercises & Homeworks / Lecture 5 / margin.html

Margin - shorthand property

Nếu margin property có bốn giá trị:

margin: 25px 50px 75px 100px;

- top margin là 25px
- right margin là 50px
- bottom margin là 75px
- left margin là 100px

Câu hỏi: nếu margin có 3, 2 hoặc chỉ 1 giá trị thì sao?

Ví dụ: margin: 25px 50px;

Padding

Padding được dùng để tạo khoảng cách xung quanh content của element, nằm bên trong bất kỳ border nào đã định nghĩa.

Thực hành: Exercises & Homeworks / Lecture 5 / padding.html

Padding và element width

CSS property width chỉ định width của content area của element. Content area là phần nằm bên trong padding, border và margin của element.

Vì vậy, nếu một element có width đã chỉ định, padding được thêm vào element đó sẽ được cộng vào total width của element.

https://www.w3schools.com/css/tryit.asp?filename=trycss_padding_width

4.5. Border

Border đơn giản là một đường được vẽ quanh content area và padding tùy chọn của nó.

Border style:

- Value: none | solid | hidden | dotted | dashed | double | groove | ridge | inset | outset
- Default: none

Thực hành:

https://www.w3schools.com/css/tryit.asp?filename=trycss_border-style

Border style

Shorthand property border-style hoạt động theo hệ thống chiều kim đồng hồ (TRouBLe) đã mô tả trước đó cho padding.

border-style: solid dashed double dotted;

Border width (độ dày)

border-width

- Value: length | thin | medium | thick
- Default: medium

Border color

border-color

- Value: color name hoặc RGB/HSL value | transparent
- Default: giá trị của property color của element

CSS outline và border radius

Đọc thêm, trang 371.

Bài tập

Trang 364, 373 và 381.

Đọc thêm:

- Border image, trang 375
- Box drop shadow, trang 382

Test yourself, trang 384.

4.6. Alignment

Attribute align được dùng để điều chỉnh vị trí của element hoặc content bên trong element. Trong ví dụ bên dưới, tất cả element không được căn chỉnh; mặc định chúng sẽ nằm bên trái.

Căn giữa element

Để căn giữa theo chiều ngang một block element (như &lt;div&gt;), dùng margin: auto;

Thiết lập width của element sẽ ngăn nó kéo giãn ra tới các cạnh của container.

Element sau đó chiếm width đã chỉ định, và phần không gian còn lại được chia đều cho hai margin.

Thực hành:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_container

Căn giữa text

Để chỉ căn giữa text bên trong một element, dùng:

text-align: center;

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_text

Căn giữa image

Để căn giữa một image, đặt left margin và right margin là auto và biến nó thành block element:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_image

Căn trái và căn phải

Một cách căn chỉnh element là dùng:

position: absolute;

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_pos

Một cách khác là dùng property float:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_float

Căn giữa theo chiều dọc

Có nhiều cách căn giữa một element theo chiều dọc trong CSS. Một giải pháp đơn giản là dùng top và bottom padding:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_padding

Để căn giữa cả theo chiều dọc và chiều ngang, dùng padding và:

text-align: center;

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_padding2

Một mẹo khác là dùng property line-height với giá trị bằng property height:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_line-height

Căn giữa theo chiều dọc

Nếu padding và line-height không phù hợp, một giải pháp khác là dùng positioning và property transform:

https://www.w3schools.com/css/tryit.asp?filename=trycss_align_transform

Bạn cũng có thể dùng flexbox để căn giữa. Lưu ý flexbox không được hỗ trợ trong IE10 và các phiên bản cũ hơn:

https://www.w3schools.com/css/tryit.asp?filename=trycss3_align_flex

4.7. Position attribute

Property position chỉ định loại phương pháp định vị được dùng cho một element (static, relative, fixed, absolute hoặc sticky).

Element sau đó được định vị bằng các property top, bottom, left và right. Tuy nhiên, các property này không hoạt động nếu chưa thiết lập property position. Chúng cũng hoạt động khác nhau tùy theo giá trị position.

position: static;

HTML element mặc định được định vị static.

Element có position static không bị ảnh hưởng bởi các property top, bottom, left và right.

Element có position: static; không được định vị theo cách đặc biệt; nó luôn được định vị theo normal flow của page:

https://www.w3schools.com/css/tryit.asp?filename=trycss_position_static

position: relative;

Element có position: relative; được định vị tương đối so với vị trí bình thường của nó.

Thiết lập các property top, right, bottom và left cho relatively-positioned element sẽ khiến nó được điều chỉnh lệch khỏi vị trí bình thường. Content khác sẽ không được điều chỉnh để lấp khoảng trống do element để lại.

https://www.w3schools.com/css/tryit.asp?filename=trycss_position_relative

position: fixed;

Element có position: fixed; được định vị tương đối với viewport, nghĩa là nó luôn ở cùng một vị trí dù page được scroll. Các property top, right, bottom và left được dùng để định vị element.

Fixed element không để lại khoảng trống trên page tại vị trí mà nó đáng lẽ xuất hiện.

https://www.w3schools.com/css/tryit.asp?filename=trycss_position_fixed

position: absolute;

Element có position: absolute; được định vị tương đối với positioned ancestor gần nhất (thay vì tương đối với viewport như fixed).

Tuy nhiên, nếu absolute positioned element không có positioned ancestor, nó dùng document body và di chuyển cùng page scrolling.

Lưu ý: absolute positioned element bị loại khỏi normal flow và có thể overlap element khác.

https://www.w3schools.com/css/tryit.asp?filename=trycss_position_absolute

Định vị text trong image

https://www.w3schools.com/css/tryit.asp?filename=trycss_image_text_top_left

4.8. Overflow, float và display

CSS property overflow kiểm soát điều gì xảy ra với content quá lớn để vừa trong một vùng.

Property overflow có các giá trị sau:

- visible - mặc định. Overflow không bị cắt; content render bên ngoài box của element
- hidden - overflow bị cắt và phần content còn lại sẽ không nhìn thấy
- scroll - overflow bị cắt và scrollbar được thêm để xem phần content còn lại
- auto - tương tự scroll, nhưng chỉ thêm scrollbar khi cần

https://www.w3schools.com/css/tryit.asp?filename=trycss_overflow_intro

4.8. Overflow, float và display

CSS property float chỉ định element sẽ float như thế nào.

CSS property clear chỉ định element nào có thể float bên cạnh cleared element và ở phía nào.

Property float có thể nhận một trong các giá trị sau:

- left - element float sang trái container
- right - element float sang phải container
- none - element không float (hiển thị đúng nơi nó xuất hiện trong text). Đây là mặc định
- inherit - element kế thừa giá trị float từ parent

https://www.w3schools.com/css/tryit.asp?filename=trycss_layout_float3

4.8. Overflow, float và display

Property display là CSS property quan trọng nhất để kiểm soát layout.

Mỗi HTML element có một giá trị display mặc định tùy theo loại element. Giá trị display mặc định của hầu hết element là block hoặc inline.

https://www.w3schools.com/css/css_display_visibility.asp

Trang 414, 416.

Test yourself, trang 417.
