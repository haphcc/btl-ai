### BÀI 12

#### BÀI GIẢNG 12: WEB DESIGN FRAMEWORKS

Thiết kế Web - Bài giảng 12: Web Design Frameworks

TS. Vũ Trọng Sinh. T: 097 567 4039. Khoa Công nghệ thông tin & Kinh tế số. E: sinhvt@hvnh.edu.vn. W: itde.hvnh.edu.vn

Nội dung

8.1. jQuery

8.2. Bootstrap

8.1. jQuery

jQuery intro. jQuery syntax. jQuery selector. jQuery event.

jQuery intro

- jQuery là một JavaScript library.
- jQuery là JavaScript library nhẹ, theo tinh thần "write less, do more".
- jQuery gom nhiều tác vụ phổ biến vốn cần nhiều dòng JavaScript code thành các method có thể gọi bằng một dòng code.
- jQuery cũng đơn giản hóa nhiều phần phức tạp của JavaScript, như AJAX call và DOM manipulation.

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide

Ấn tượng của bạn là gì?

Thêm jQuery vào webpage

Download jQuery library từ jQuery.com:

http://jquery.com/download/

Hoặc include jQuery từ CDN, ví dụ Google.

jQuery syntax

Cú pháp jQuery được thiết kế riêng để chọn HTML element và thực hiện action trên element đó.

Cú pháp cơ bản: $(selector).action()

- Dấu $ để định nghĩa/truy cập jQuery
- (selector) để "query" hoặc tìm HTML element
- jQuery action() được thực hiện trên element

jQuery syntax

Ví dụ:

$(this).hide() - ẩn element hiện tại.

$("p").hide() - ẩn tất cả element &lt;p&gt;.

$(".test").hide() - ẩn tất cả element có class="test".

$("#test").hide() - ẩn element có id="test".

Document Ready Event

Event này ngăn jQuery code chạy trước khi document load xong.

Một số action có thể fail nếu method chạy trước khi document load hoàn toàn:

- Cố ẩn một element chưa được tạo
- Cố lấy kích thước của một image chưa load

jQuery selector

jQuery selector cho phép bạn chọn và thao tác với HTML element.

jQuery selector được dùng để "find" hoặc select HTML element dựa trên name, id, class, type, attribute, value của attribute và nhiều tiêu chí khác. Nó dựa trên CSS selector hiện có, đồng thời có thêm một số custom selector riêng.

element selector

jQuery element selector chọn element dựa trên element name.

Bạn có thể chọn tất cả element &lt;p&gt; trên một page như sau:

$("p")

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_p

#id selector

jQuery #id selector dùng id attribute của HTML tag để tìm element cụ thể.

id nên là duy nhất trong một page, vì vậy bạn nên dùng #id selector khi muốn tìm một element duy nhất.

Để tìm element có id cụ thể, viết ký tự hash, theo sau là id của HTML element:

$("#test")

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_id

.class selector

jQuery .class selector tìm element có class cụ thể.

Để tìm element có class cụ thể, viết dấu chấm, theo sau là tên class:

$(".test")

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_class

jQuery event

Event biểu thị thời điểm chính xác khi một điều gì đó xảy ra.

Ví dụ: di chuột qua một element, chọn radio button, click vào một element.

jQuery event

Để gán click event cho tất cả paragraph trên một page, bạn có thể làm như sau.

Bước tiếp theo là định nghĩa điều gì xảy ra khi event được kích hoạt. Bạn phải truyền một function cho event.

Các jQuery event method thường dùng

Bài tập: Thiết kế một trang web gồm các phần sau:

Tiêu đề: đặt tiêu đề trang là "Bài tập jQuery Events."

Button: thêm một nút có văn bản "Click me!".

Ô văn bản: thêm một ô văn bản (input type="text") với id là "textInput".

Ảnh: thêm một ảnh bất kỳ với id là "mainImage".

Div: thêm một div với id là "resultDiv".

Các jQuery event method thường dùng

Yêu cầu tương tác:

Khi người dùng nhấn nút "Click me!", hiển thị thông báo cảnh báo bằng jQuery (dùng .click() hoặc .on("click")) với nội dung "Button Clicked!".

Khi người dùng gõ vào ô văn bản và sau đó nhấn Enter, hiển thị giá trị đã nhập trong div có id "resultDiv" (dùng .keypress() và .val()).

Khi người dùng di chuyển con trỏ chuột qua ảnh, thay đổi attribute src của ảnh để đổi hình ảnh (dùng .mouseenter() và .attr()).

Gợi ý: tạo một HTML file mới và bổ sung JavaScript code sử dụng jQuery library. Sau đó dùng các event như .click(), .keypress() và .mouseenter() để thực hiện các chức năng tương ứng.

jQuery effect

Hide and Show. Fade. Slide. Animate. Chaining.

Hide and Show

Với jQuery, bạn có thể ẩn và hiện HTML element bằng method hide() và show():

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_slow

Syntax:

$(selector).hide(speed, callback);

$(selector).show(speed, callback);

Toggle

Bạn cũng có thể chuyển đổi giữa ẩn và hiện một element bằng method toggle().

Syntax:

$(selector).toggle(speed, callback);

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_toggle

Fade

Với jQuery, bạn có thể làm một element fade in và fade out.

jQuery có các fade method sau:

- fadeIn(): https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_fadein
- fadeOut(): https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_fadeout
- fadeToggle(): https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_fadetoggle
- fadeTo(): https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_fadeto

Slide

Với jQuery, bạn có thể tạo sliding effect trên element.

jQuery có các slide method sau:

- slideDown()
- slideUp()
- slideToggle()

Animation

Method jQuery animate() được dùng để tạo custom animation.

Syntax:

$(selector).animate({params}, speed, callback);

- Required parameter params định nghĩa các CSS property sẽ được animate.
- Optional parameter speed chỉ định duration của effect. Nó có thể nhận value "slow", "fast" hoặc milliseconds.
- Optional parameter callback là function được thực thi sau khi animation hoàn tất.

Animation

Method jQuery animate() được dùng để tạo custom animation.

Syntax:

$(selector).animate({params}, speed, callback);

Required parameter params định nghĩa các CSS property sẽ được animate. Optional parameter speed chỉ định duration của effect và có thể nhận value "slow", "fast" hoặc milliseconds. Optional parameter callback là function được thực thi sau khi animation hoàn tất.

https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_animation1_multicss

Chaining

Chaining cho phép chạy nhiều jQuery method trên cùng một element trong một statement duy nhất.

Để chain một action, chỉ cần nối action đó vào action trước.

Dùng jQuery trong project

1. Xác định requirement.
2. Tìm jQuery plugin: https://plugins.jquery.com/ hoặc https://www.jqueryscript.net/
3. Download source code (thường là file .zip) hoặc link tới plugin qua CDN.
4. Include CSS cần thiết.
5. Initialize plugin.
6. Customize option (tùy chọn).
7. Run và test site.

Ví dụ: triển khai Slick Carousel

Step 1: hiểu mục đích của plugin.

Slick Carousel là một jQuery plugin phổ biến để tạo carousel responsive, hỗ trợ swipe.

Ví dụ: triển khai Slick Carousel

Step 2: include jQuery và Slick Carousel.

jQuery:

&lt;script src="https://code.jquery.com/jquery-3.6.0.min.js"&gt;&lt;/script&gt;

Slick Carousel:

&lt;link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/&gt;

&lt;script src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"&gt;&lt;/script&gt;

Ví dụ: triển khai Slick Carousel

Step 3: tạo HTML structure.

Ví dụ: triển khai Slick Carousel

Step 4: initialize plugin trong JavaScript.

Ví dụ: triển khai Slick Carousel

Step 5: customize option.

Code bên trên bao gồm các option như autoplay, autoplaySpeed, dots và arrows.

Bạn có thể điều chỉnh các option này dựa trên nhu cầu thiết kế.

Bài tập: triển khai jQuery UI Datepicker

Đây là một ví dụ khác, dùng plugin "jQuery UI Datepicker", cho phép user chọn ngày dễ dàng bằng calendar interface thân thiện. Plugin này thường được dùng trong form cần date input.

Chuẩn bị 10 phút, làm việc theo nhóm.

8.2. Bootstrap

Bootstrap

Bootstrap 4 là phiên bản mới hơn của Bootstrap, với component mới, stylesheet nhanh hơn và responsive tốt hơn. Tuy nhiên, Internet Explorer 9 trở xuống không được hỗ trợ.

Bootstrap 5 là phiên bản mới nhất trong tài liệu này, với thay đổi lớn và mượt hơn. Tuy nhiên, Internet Explorer 11 trở xuống không được hỗ trợ, và jQuery được thay bằng vanilla JavaScript.

W3.CSS

Tailwind CSS

Bootstrap 4 - Quick start

Thử ví dụ này:

https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_default&stacked=h

Bạn nghĩ gì về source code?

Bootstrap là gì?

- Bootstrap là front-end framework miễn phí giúp web development nhanh và dễ hơn.
- Bootstrap bao gồm design template dựa trên HTML và CSS cho typography, form, button, table, navigation, modal, image carousel và nhiều thành phần khác, cùng các JavaScript plugin tùy chọn.
- Bootstrap cũng giúp bạn dễ tạo responsive design.

Bootstrap version

Bootstrap 5 (phát hành năm 2021) là phiên bản mới nhất trong tài liệu này; nó hỗ trợ các bản phát hành ổn định mới nhất của mọi browser và platform lớn. Tuy nhiên, Internet Explorer 11 trở xuống không được hỗ trợ.

Khác biệt chính giữa Bootstrap 5 và Bootstrap 3 & 4 là Bootstrap 5 đã chuyển sang JavaScript thay vì jQuery.

Vì sao dùng Bootstrap?

- Dễ dùng: chỉ cần kiến thức cơ bản về HTML và CSS là có thể bắt đầu dùng Bootstrap.
- Responsive feature: responsive CSS của Bootstrap thích nghi với phone, tablet và desktop.
- Mobile-first approach: trong Bootstrap, mobile-first style là một phần của core framework.
- Browser compatibility: Bootstrap 4 tương thích với các browser hiện đại (Chrome, Firefox, Internet Explorer 10+, Edge, Safari và Opera).

Cách dùng Bootstrap trong website

- Include Bootstrap 4 từ CDN
- Bạn vừa thử cách này ở ví dụ đầu tiên
- Download Bootstrap 4 từ getbootstrap.com
- Dùng offline version của Bootstrap
- https://getbootstrap.com/

Tạo webpage đầu tiên với Bootstrap 4

Exercise 1: Thêm responsive image gallery

Cải thiện webpage bằng cách thêm responsive image gallery bên dưới content hiện có.

- Dùng Bootstrap grid system để hiển thị 6 image.
- Sắp xếp image thành hai row, mỗi row ba image trên màn hình medium và lớn hơn.
- Trên màn hình nhỏ, image nên xếp dọc (mỗi row một image).

Exercise 2: Thêm contact form

Thêm contact form bên dưới Jumbotron. Form gồm:

- Text input cho "Name"
- Email input cho "Email"
- Textarea cho "Message"
- Submit button được style bằng Bootstrap

Đảm bảo form được căn giữa và responsive bằng container.

Exercise 3: Thêm pricing table

Bên dưới Jumbotron, thêm pricing table với ba column đại diện cho các pricing plan khác nhau (ví dụ Basic, Standard, Premium).

- Dùng Bootstrap grid system để tạo column.
- Mỗi column gồm một card có title (plan name), description, price và button.
- Style các card bằng Bootstrap card component.

Bài tập

Từ danh sách Bootstrap template, chọn một template để phân tích. Ví dụ: https://startbootstrap.com/themes

- Tạo một Google Docs document trống, đặt tên "Group# - Homepage".
- Truy cập homepage của template đã chọn, chụp toàn bộ interface thành một image và paste vào document.
- Với từng component, chụp image, tìm Bootstrap class phù hợp và ghi vào document.

Ví dụ: https://startbootstrap.com/previews/agency

Project checkpoint

Từ các website tham khảo của bạn, chọn một website để phân tích.

Ghi lại tất cả component có thể được style bằng Bootstrap.
