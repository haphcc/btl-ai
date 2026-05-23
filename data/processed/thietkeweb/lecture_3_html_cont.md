### BÀI 3

#### BÀI GIẢNG 3: HTML (TIẾP)

Thiết kế Web - Bài giảng 3: HTML (tiếp)

Nội dung

2.5. Thêm image. 2.6. Table markup. 2.7. Form. 2.8. Embedded media.

2.5. Thêm image

- Image format
- img element
- Responsive image markup

Image format

Nhìn chung, image được tạo từ một lưới pixel màu (gọi là bitmap hoặc raster image) phải được lưu ở định dạng PNG, JPEG hoặc GIF để có thể đặt inline trong content.

Với vector image, chẳng hạn icon và illustration được tạo bằng drawing tool như Adobe Illustrator, chúng ta có định dạng SVG.

img element

img element nói với browser: "Đặt một image ở đây." Attribute src (source) cung cấp vị trí của image file (URL). Attribute alt cung cấp alternative text để hiển thị nếu image không khả dụng.

Cung cấp vị trí bằng src

Giá trị của src attribute là URL của image file.

Trong hầu hết trường hợp, image bạn dùng trên page sẽ nằm trên server của chính bạn, vì vậy bạn sẽ dùng relative URL để trỏ tới chúng.

Performance tip: tận dụng caching. Khi browser download một image, nó lưu file vào disk cache (vùng lưu tạm file trên ổ cứng). Nhờ vậy, nếu cần hiển thị lại page, browser có thể lấy bản sao image cục bộ mà không cần gửi server request mới.

Cung cấp kích thước bằng width và height

Attribute width và height chỉ định kích thước image theo số pixel.

Exercise 3-1 (10 phút): Thêm và linking image

Trong bài tập này, bạn sẽ thêm image vào page và dùng chúng làm link.

Giáo trình, trang 158.

Responsive image markup

Sau khi smartphone, tablet, "phablet" và các thiết bị khác xuất hiện, image lớn trông đẹp trên màn hình lớn lại trở nên quá nặng trên màn hình nhỏ:

- Làm chậm hiển thị page

- Tốn dữ liệu khi download

Ngược lại, image nhỏ download nhanh có thể bị mờ trên màn hình lớn, độ phân giải cao.

-> Cần một cách để toàn bộ webpage phản hồi và thích nghi với nhiều kích thước màn hình -> "Responsive".

Cách hoạt động

Tóm lại, responsive image hoạt động như sau: bạn cung cấp nhiều image được resize hoặc crop cho các kích thước màn hình khác nhau, và browser chọn image phù hợp nhất dựa trên thông tin nó biết về môi trường hiển thị hiện tại.

- Cung cấp image extra-large để hiển thị sắc nét trên màn hình độ phân giải cao

- Cung cấp một tập image với nhiều kích thước khác nhau cho các screen size khác nhau

- Cung cấp các phiên bản image có mức độ chi tiết khác nhau dựa trên kích thước và orientation của thiết bị (gọi là use case art direction)

- Cung cấp image format thay thế lưu cùng một image với file size nhỏ hơn nhiều

Bài tập về nhà

Làm bài tập ở trang 156: Adding responsive images. Kiểm thử kết quả trên nhiều thiết bị: mobile, tablet, laptop.

2.6. Table markup

Cách dùng table. Cấu trúc table. Spanning cell. Hoàn thiện table.

Cách dùng table

HTML table được tạo ra cho các trường hợp bạn cần thêm dữ liệu dạng bảng (data được sắp xếp thành row và column) vào webpage.

Table có thể dùng để tổ chức lịch trình, so sánh sản phẩm, thống kê hoặc các loại thông tin khác.

Cấu trúc table

Toàn bộ content của table nằm trong các cell được sắp xếp thành row. Cell chứa header information (title cho column, chẳng hạn "Calories") hoặc data, có thể là bất kỳ loại content nào.

Cấu trúc table

Việc xếp chồng các th và td element trong source là phổ biến để dễ tìm hơn.

Điều này không ảnh hưởng đến cách browser render chúng.

Spanning cell

Một đặc điểm cơ bản của cấu trúc table là cell spanning, tức kéo giãn một cell để bao phủ nhiều row hoặc column. Spanning cell cho phép tạo cấu trúc table phức tạp, nhưng cũng khiến markup khó theo dõi hơn một chút.

Bạn làm cho header cell hoặc data cell span bằng cách thêm attribute colspan hoặc rowspan.

Column span

Column span, được tạo bằng attribute colspan trong td hoặc th element, kéo giãn một cell sang phải để phủ qua các column tiếp theo.

Row span

Row span, được tạo bằng attribute rowspan, hoạt động giống column span nhưng làm cho cell kéo xuống qua nhiều row.

Hoàn thiện table

Exercise 3-2: The table challenge. Trang 174 - giáo trình.

2.7. Form

- Cách form hoạt động
- form element
- Variable và content
- Form control
- Tính năng accessibility của form

Cách form hoạt động

Một form hoạt động gồm hai phần.

- Phần thứ nhất là form bạn nhìn thấy trên page, được tạo bằng HTML markup.

Form gồm button, input field và drop-down menu (form control) dùng để thu thập thông tin từ người dùng.

- Thành phần còn lại của web form là application hoặc script trên server xử lý thông tin mà form thu thập và trả về response phù hợp. Đây là phần làm cho form hoạt động.

form element

form element là container cho toàn bộ content của form, bao gồm một số form control như text-entry field và button. Nó cũng có thể chứa block element (ví dụ h1, p và list).

Tuy nhiên, nó không được chứa một form element khác.

Attribute action

Attribute action cung cấp vị trí (URL) của application hoặc script sẽ được dùng để xử lý form:

&lt;form action="/mailinglist.php" method="POST"&gt;...&lt;/form&gt;

Variable và content

Attribute name cung cấp tên variable cho control.

&lt;textarea name="comment" rows="4" cols="45" placeholder="Leave us a comment."&gt;&lt;/textarea&gt;

Đặt tên variable: hãy đặt tên đơn giản, có tính mô tả và document chúng rõ ràng.

Form control

- Text-entry control
- File selection và upload control
- Specialized text-entry control
- Submit và reset button
- Hidden control
- Radio và checkbox button
- Date và time
- Pull-down và scrolling menu
- Numerical control
- Color picker control

Form control

Exercise 3-3: Starting the pizza order form. Trang 191 - giáo trình.

2.8. Embedded media

IFrame. Video và audio. Canvas.

IFrame

iframe (viết tắt của inline frame) element cho phép bạn embed một HTML document riêng hoặc web resource khác vào trong document -> window trong window.

Video và audio

&lt;video src="highlight_reel.mp4" width="640" height="480" poster="highlight_still.jpg" controls autoplay&gt; Your browser does not support HTML5 video. Get the &lt;a href="highlight_reel.mp4"&gt;MP4 video&lt;/a&gt;

&lt;/video&gt;

Browser không hỗ trợ video sẽ hiển thị bất kỳ content nào được cung cấp bên trong video element. Tin tốt là video và audio element được hỗ trợ tốt trong browser hiện đại.

Canvas

canvas element tạo một vùng trên webpage để vẽ bằng một tập JavaScript function dùng cho line, shape, fill, text, animation, v.v.

&lt;canvas width="600" height="400" id="my_first_canvas"&gt; Your browser does not support HTML5 canvas. Try using Chrome, Firefox, Safari or MS Edge.

&lt;/canvas&gt;

Exercise 3-4: Embed Google Maps vào page của bạn

https://developers.google.com/maps/documentation/javascript/adding-a-google-map
