### BÀI 6

#### BÀI GIẢNG 6: WEB LAYOUT & RESPONSIVE DESIGN

## TRANG 1

Thiết kế Web - Bài giảng 6: Web layout & Responsive design


## TRANG 2

Nội dung

5.1. Thành phần layout của website. 5.2. Flexbox. 5.3. Grid layout. 5.4. Responsive web design.


## TRANG 3

5.1. Thành phần layout của website

Wireframe diagram thể hiện cấu trúc của một webpage chỉ bằng outline cho từng loại content và widget.


## TRANG 4

5.1. Thành phần layout của website

Site diagram thể hiện cấu trúc tổng thể của site và cách các page riêng lẻ liên hệ với nhau.


## TRANG 5

5.1. Thành phần layout của website

Tổng quan:

- Header
- Navigation
- Main content
- Sidebar
- Footer


## TRANG 6

Header

Phần trên cùng của website, chứa:

- Logo
- Navigation menu (top menu)
- Banner
- Slogan

Đây là vùng ở đầu page, thường giữ ổn định và hiển thị khi visitor click qua lại trong site.


## TRANG 7

Navigation (hay Navigation Bar hoặc Main Menu)

Đây là các link ở đầu page giúp bạn tìm thứ mình cần. Navigation link thường nằm trong header hoặc ngay bên dưới header.


## TRANG 8

Navigation (hay Navigation Bar hoặc Main Menu)

Khi site được xem trên thiết bị di động, navigation thường biến thành icon có 3 dòng xếp chồng (gọi là "hamburger" vì giống góc nhìn ngang của một chiếc hamburger), do không gian trên mobile bị giới hạn.

Nhấn vào mobile navigation icon thường mở một vertical hoặc horizontal toggle menu.


## TRANG 9

Navigation (hay Navigation Bar hoặc Main Menu)

Trên các site phức tạp có rất nhiều page, đôi khi bạn sẽ thấy "mega menu", tức drop-down menu được kích hoạt khi hover lên một link trong main navigation. Drop-down mega menu sau đó hiển thị nhiều link được tổ chức theo category và sub-category, gần giống sitemap.


## TRANG 10

Main content

Website content là thông tin visitor tiếp nhận. Web copy hoặc body copy chỉ phần written text. Website content chỉ toàn bộ element dùng để truyền tải thông điệp: text, image, video, audio, v.v.


## TRANG 11

Sidebar (aside)

Sidebar là cột dọc hẹp nằm cạnh website content. Sidebar thường chứa advertisement, link tới content khác, call to action hoặc search box.

Hãy xem sidebar là phần phụ so với website content chính.


## TRANG 12

Footer

Footer thực hiện chức năng tương tự header: đó là vùng trên website ổn định từ page này sang page khác, nhưng footer nằm ở cuối page thay vì đầu page.

Bạn có thể đặt bất kỳ thứ gì trong footer. Tuy nhiên, footer thường có contact info, privacy policy, terms of use, sitemap, social media icon và link tới các page quan trọng khác trên site.


## TRANG 13

Các web component khác

Search box. Log in / Sign up. Feature image. Slider. Breadcrumb. CTA: button, pop-up, ribbon, slide-in, email opt-in box, thậm chí một text link đơn giản, đều là ví dụ về call to action. Call to action là một yêu cầu cụ thể và trực tiếp, đề nghị visitor thực hiện một hành động.


## TRANG 14

Các loại webpage

Homepage. Newsletter. Product/service page. Checkout page. Item page. Landing page. About page. Blog. Contact page. 404 error page (bắt buộc).


## TRANG 15

Ví dụ layout

https://vnexpress.net/ https://dantri.com.vn/ https://www.lazada.vn/

Hãy xác định layout component trong homepage, category page, item page,... của từng website.


## TRANG 16

Thảo luận

Tìm web layout đang là xu hướng trong năm nay.

- URL của sample layout
- Bạn thích điểm gì ở layout này
- Làm việc theo nhóm


## TRANG 17

5.2. Flexbox

- Flexbox cho phép kiểm soát tốt hơn việc sắp xếp item theo một axis.

- Grid dùng cho layout thật sự dựa trên lưới, giống cách các print designer đã dùng trong nhiều thập kỷ.

"Bạn có thể tạo cấu trúc page tổng thể bằng grid và dùng flexbox để xử lý header và navigation element."


## TRANG 18

Flexible box với CSS flexbox

Flexbox cho phép item co giãn bên trong container, tránh lãng phí không gian và overflow. Đây là lợi thế lớn khi làm layout phù hợp với nhiều viewport size.

Ưu điểm khác:

- Có thể làm cho tất cả item liền kề có cùng height
- Dễ căn giữa theo chiều ngang và chiều dọc
- Có thể thay đổi thứ tự hiển thị của item độc lập với source


## TRANG 19

Thiết lập flexbox container

&lt;div id="container"&gt;

&lt;div class="box box1"&gt;1&lt;/div&gt;

&lt;div class="box box2"&gt;2&lt;/div&gt;

&lt;div class="box box3"&gt;3&lt;/div&gt;

&lt;div class="box box4"&gt;4&lt;/div&gt;

&lt;div class="box box5"&gt;5&lt;/div&gt;

&lt;/div&gt;

#container {

display: flex;

}


## TRANG 20

Kiểm soát "flow" trong container

Chỉ định flow direction.


## TRANG 21

Kiểm soát "flow" trong container

Wrapping lên nhiều dòng.


## TRANG 22

Bài tập

Trang 427, giáo trình - Tạo navigation bar bằng Flexbox. Trang 434, giáo trình - A flexible online menu. Trang 445, giáo trình - Adjusting flex and order.


## TRANG 23

Bài tập

Đọc thêm:

- Controlling the Alignment of Flex Items in the Container, trang 428-433
- Expanding items (flex-grow), trang 437
- Changing the Order of Flex Items, trang 442


## TRANG 24

5.3. Grid layout

CSS Grid Layout Module cung cấp một hệ thống để bố trí element theo row và column (hãy nhớ Flexbox chỉ bố trí element trên một axis). Chrome 57+, Opera, Firefox 52+, Safari 10+ và iOS Safari 10+ đều bắt đầu hỗ trợ Grid standard không cần browser prefix từ tháng 3 năm 2017.


## TRANG 25

Cách Grid Layout hoạt động

1. Dùng property display để biến một element thành grid container. Children của element đó tự động trở thành grid item.

2. Thiết lập column và row cho grid. Bạn có thể thiết lập tường minh và/hoặc cung cấp chỉ dẫn về cách row và column được tạo tự động.

3. Gán từng grid item vào một area trên grid. Nếu bạn không gán tường minh, chúng sẽ chảy tuần tự vào các cell.


## TRANG 26

Thuật ngữ Grid

Bắt đầu từ markup, element được áp dụng property display: grid sẽ trở thành grid container. Tất cả direct child element của nó tự động trở thành grid item và được định vị trong grid.

Grid line; grid cell; grid area; grid track.


## TRANG 27

Khai báo Grid Display

Để biến một element thành grid container, đặt property display của nó là grid hoặc inline-grid.

Trong ví dụ đơn giản này, div #layout trở thành grid container, và mỗi child của nó (#one, #two, #three, #four, #five) trở thành grid item.


## TRANG 28

Thực hành

EXERCISE 16-4: Setting up a grid. Trang 461.

EXERCISE 16-5: Placing items on a grid. Trang 467.

EXERCISE 16-6: A grid layout for the bakery page. Trang 476.


## TRANG 29

5.4. Responsive web design

RWD là gì và vì sao cần RWD?

Responsive recipe. Breakpoint. Designing responsively.


## TRANG 30

RWD là gì và vì sao cần RWD?

Responsive web design giúp webpage hiển thị tốt trên mọi thiết bị.

Responsive web design chỉ dùng HTML và CSS. Webpage không nên bỏ bớt thông tin để vừa với thiết bị nhỏ hơn, mà nên thích nghi content để phù hợp với mọi thiết bị.

Responsive web design không phải là một program hay JavaScript.


## TRANG 31

RWD là gì và vì sao cần RWD?

Kể từ khi iPhone xuất hiện năm 2007, người dùng xem web trên điện thoại với mọi kích thước, tablet, "phablet", laptop cảm ứng, wearable, television, video game console, refrigerator,... Năm 2016, mức sử dụng mobile internet đã vượt desktop.

Đó là nơi RWD trở nên quan trọng.

Thực tế, với nhiều web designer, "responsive design" hiện nay đơn giản là "web design".


## TRANG 32

Ví dụ

Khi bạn dùng CSS và HTML để resize, hide, shrink, enlarge hoặc move content để nó hiển thị tốt trên mọi màn hình, đó được gọi là responsive web design.

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_col-s


## TRANG 33

Responsive recipe

Một giải pháp trước đây là dựa vào chức năng hiển thị web tích hợp trong điện thoại. Mặc định, mobile device hiển thị toàn bộ webpage được thu nhỏ để vừa với phần màn hình khả dụng. Người dùng có thể pinch để zoom vào chi tiết và scroll tới các phần khác nhau của page.

Cách khác là tạo một mobile site riêng cho màn hình nhỏ và người dùng "on the go". Vẫn còn nhiều công ty và dịch vụ dùng dedicated mobile site ("m-dot" site).

-> Còn xa so với "responsive design" mà chúng ta kỳ vọng.


## TRANG 34

Responsive recipe

Năm 2010, Ethan Marcotte đặt tên cho một giải pháp linh hoạt hơn trong bài viết "Responsive Web Design": https://alistapart.com/article/responsive-web-design/

- Flexible grid: thay vì giữ width cố định, responsive site dùng các phương pháp cho phép chúng co lại và chảy vào không gian browser khả dụng.

- Flexible image: image và embedded media khác cần có khả năng scale để vừa với containing element.

- CSS media query: media query cho phép cung cấp các bộ rule chỉ cho thiết bị thỏa mãn tiêu chí nhất định, chẳng hạn width và orientation.

- Viewport meta: làm width của webpage khớp với width của màn hình.


## TRANG 35

Thiết lập viewport

Để đưa website tiêu chuẩn lên màn hình nhỏ, mobile browser render page trên một canvas gọi là viewport, sau đó thu nhỏ viewport đó để vừa với width của màn hình (device width).


## TRANG 36

Viewport là gì?

Viewport là vùng nhìn thấy của người dùng trên webpage.

Viewport thay đổi theo thiết bị và sẽ nhỏ hơn trên điện thoại so với màn hình máy tính.

&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;

Mở các page này trên phone hoặc tablet:

https://www.w3schools.com/css/example_withoutviewport.htm

https://www.w3schools.com/css/example_withviewport.htm


## TRANG 37

Flexible grid (fluid layout)

Trong fluid layout, vùng page và grid của nó resize theo tỉ lệ để lấp đầy width khả dụng của screen hoặc window.

- đơn vị fr hoặc minmax() trong CSS Grid layout
- thiết lập property flex trong Flexbox
- percentage cho browser cũ

target / context = result. Target là kích thước của element bạn đang resize. Context là kích thước của containing element. Result là phần trăm bạn có thể dùng trong style rule.


## TRANG 38

Fluid layout lấp đầy viewport theo tỉ lệ.

Fixed layout giữ nguyên kích thước và có thể bị cắt hoặc để lại khoảng trống thừa.


## TRANG 39

Flexible grid (fluid layout)

Thực hành:

https://www.w3schools.com/css/tryresponsive_grid.htm

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_webpage

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_cols


## TRANG 40

Flexible image

Style rule cần dùng để làm image scale xuống vừa với kích thước container.


## TRANG 41

Flexible image

Nhưng hãy nhớ: chọn image size tốt nhất cho performance là một phần của quy trình responsive design.

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_image_mediaq


## TRANG 42

Media Query Magic

Media query áp dụng các style khác nhau dựa trên đặc điểm của browser: width, orientation dọc hoặc ngang, resolution, v.v. Chúng giúp gửi layout một cột cho màn hình nhỏ và layout nhiều cột cho màn hình lớn một cách linh hoạt.

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_mediaquery


## TRANG 43

Media Query Magic

Thực hành:

https://www.w3schools.com/css/tryit.asp?filename=tryresponsive_breakpoints


## TRANG 44

Bài tập

Trang 508.
