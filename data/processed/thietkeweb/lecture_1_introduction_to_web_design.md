### BÀI 1

#### BÀI GIẢNG 1: GIỚI THIỆU VỀ THIẾT KẾ WEB

## TRANG 1

Thiết kế Web - Bài giảng 1: Giới thiệu về thiết kế web


## TRANG 2

Khởi động

Hãy kể tên tất cả thuật ngữ bạn biết về Web Development. Ví dụ: Website, webpage, HTML, Google Chrome,...


## TRANG 3

Nội dung

1.1. Các khái niệm cơ bản về thiết kế web. 1.2. Quy trình phát triển web. 1.3. Các công việc liên quan. 1.4. Ngôn ngữ thiết kế web. 1.5. Công cụ thiết kế web.


## TRANG 4

1.1. Các khái niệm cơ bản về thiết kế web

- Internet và web
- Cung cấp thông tin của bạn
- Browser
- Địa chỉ webpage (URL)
- Cấu trúc của một webpage
- Ghép tất cả lại với nhau


## TRANG 5

Internet và web

Internet là một mạng lưới quốc tế gồm các máy tính được kết nối với nhau. Không công ty nào sở hữu Internet; đây là một nỗ lực hợp tác được quản lý bởi hệ thống các tiêu chuẩn và quy tắc.

Có nhiều cách để truyền thông tin giữa các máy tính, bao gồm email (POP3/IMAP/SMTP), file transfer (FTP), secure shell (SSH),... Đây là các protocol.

Web, ban đầu được gọi là World Wide Web, là một trong những cách thông tin được chia sẻ qua Internet. Web đặc biệt ở chỗ nó cho phép các document liên kết với nhau bằng hypertext link, từ đó tạo thành một "web" thông tin khổng lồ được kết nối.

Web sử dụng protocol gọi là HTTP (Hyper Text Transfer Protocol).

Web là một phần con của Internet. Nó chỉ là một trong nhiều cách truyền thông tin qua các máy tính nối mạng.


## TRANG 6

Cung cấp thông tin của bạn

Server là phần mềm (không phải bản thân máy tính) cho phép máy tính giao tiếp với các máy tính khác; tuy nhiên, trong thực tế người ta cũng thường dùng từ "server" để chỉ máy tính đó.

Vai trò của server software là chờ yêu cầu thông tin, sau đó truy xuất và gửi thông tin đó trở lại nhanh nhất có thể.

Thuật ngữ: HTTP, Apache, IIS, IP Address, DNS -> Bạn biết thuật ngữ nào?


## TRANG 7

Browser

Phần mềm thực hiện việc gửi request được gọi là client.

Người dùng sử dụng desktop browser, mobile browser và các assistive technologies khác (chẳng hạn screen reader) như các client để truy cập document trên web. Server trả về document để browser (trong ngữ cảnh kỹ thuật còn gọi là user agent) hiển thị.


## TRANG 8

Thảo luận

Bạn biết những browser nào? Bạn thích browser nào hơn?

Vì sao?

Hãy thử truy cập một số website bằng browser trên cả máy tính và thiết bị di động. Có điểm gì khác nhau?

Ví dụ: https://dantri.com.vn/, https://www.youtube.com/, ... Gợi ý: bật responsive view trong inspect tool để xem nhiều kích thước màn hình.


## TRANG 9

Server-side và Client-side

Các thuật ngữ này cho biết máy nào đang thực hiện xử lý.

- Client-side application chạy trên máy của người dùng (còn gọi là frontend)
- Server-side application và function sử dụng năng lực xử lý của máy chủ server (backend)


## TRANG 10

Thuật ngữ

Lược sử Internet. Intranet và Extranet. Open source. Trang 23.


## TRANG 11

Địa chỉ webpage (URL)

Mỗi page và resource trên web đều có một địa chỉ riêng gọi là URL, viết tắt của Uniform Resource Locator.

Các phần của URL: một URL đầy đủ thường gồm ba thành phần: protocol, site name và absolute path tới document hoặc resource.


## TRANG 12

Thảo luận

Mở https://dantri.com.vn/ và duyệt một số trang bên trong để quan sát các thành phần của URL. Tương tự, mở https://vnexpress.net/ và duyệt một số trang.


## TRANG 13

Thuật ngữ

URL rút gọn/simplified URL

- Bỏ qua protocol (http và https)

- Trỏ tới file mặc định: khi server nhận request tới một tên thư mục thay vì một file cụ thể, nó sẽ tìm trong thư mục đó một document mặc định, thường có tên là index.html

- Shortened URL


## TRANG 14

Cấu trúc của một webpage

HTML document. Hình ảnh. Style. Behavior.


## TRANG 15

Thực hành: Xem source của một webpage (5 phút)

Safari: Develop -> Show -> Page Source. Chrome: View -> Developer -> View Source. Firefox: Tools -> Web Developer -> Page Source. Hoặc chỉ cần nhấn phím F12.

Inspect hình ảnh, menu, title,... mà bạn nhìn thấy trên trang.


## TRANG 16

Ghép tất cả lại với nhau

https://www.youtube.com/watch?v=0cU4sIP-OuE


## TRANG 17

Thuật ngữ

Static site và dynamic site.

HTTP Status Codes.

Tự đọc, trang 32.


## TRANG 18

Quiz (5 phút)

1. HTML ______ a. Phần mềm chờ request và trả về document

2. W3C ______ b. Vị trí của một web document hoặc resource

3. Server______ c. Markup language dùng để mô tả web content

4. CSS ______ d. Ánh xạ domain name với địa chỉ IP dạng số

5. HTTP ______ e. Protocol dùng cho file transfer

6. IP ______ f. Protocol dùng để truyền web document trên Internet

7. URL ______ g. Ngôn ngữ dùng để chỉ dẫn web content hiển thị như thế nào

8. IIS______ h. Web-server software do Microsoft cung cấp

9. DNS ______ i. Internet Protocol

10. FTP ______ j. Tổ chức giám sát các công nghệ web


## TRANG 19

1.2. Quy trình phát triển web

1. Thu thập yêu cầu

2. Lập kế hoạch

3. Thiết kế

4. Tạo nội dung

5. Programming

6. Testing

7. Triển khai & bảo trì


## TRANG 20

Thu thập yêu cầu

Phỏng vấn khách hàng, phân tích tài liệu để hiểu yêu cầu:

- Mục đích của website

- Đối tượng người dùng mục tiêu

- Các tính năng chính của website

- Công nghệ, theme

- Ngân sách


## TRANG 21

Lập kế hoạch

Lập kế hoạch chi tiết bao gồm mục đích, ngân sách, timeline và resource. Xây dựng sitemap / wireframe.


## TRANG 22

Thiết kế

Bao gồm cả UI & UX.


## TRANG 23

Tạo nội dung

Content is king. Nội dung có thể là trang About Us, trang mô tả sản phẩm, tiêu đề menu. Thông thường, khách hàng sẽ cung cấp content.


## TRANG 24

Programming

Viết source code để website hoạt động.


## TRANG 25

Testing

Xác minh rằng tất cả phần visual và functional của website hoạt động bình thường.

- Functional test

- Availability test

- GUI test

- Compatibility test

- Performance test

- Security test


## TRANG 26

Triển khai & bảo trì

Đưa source code và các file cần thiết lên web server để website chạy trên Internet. Theo dõi performance của website. Xử lý lỗi.


## TRANG 27

1.3. Các công việc liên quan

Content creator. Backend developer. UI/UX designer. SEO. Visual designer. Product manager. Frontend developer. Multimedia producer.


## TRANG 28

1.3. Các công việc liên quan

Sự khác nhau giữa các job title sau là gì?

UI/UX designer

Visual designer

Frontend developer

Thảo luận.


## TRANG 29

1.4. Ngôn ngữ thiết kế web

## HTML, CSS, JAVASCRIPT

Còn PHP, JSP, ASP.Net thì sao?


## TRANG 30

## HTML

HTML là viết tắt của Hyper Text Markup Language. HTML là markup language tiêu chuẩn để tạo webpage. HTML mô tả cấu trúc của một webpage.


## TRANG 31

CSS

CSS là ngôn ngữ chúng ta dùng để tạo style cho webpage.

CSS là viết tắt của Cascading Style Sheets. CSS mô tả cách các HTML element được hiển thị trên màn hình, trên giấy hoặc trong các media khác.


## TRANG 32

JavaScript

JavaScript là programming language phổ biến nhất thế giới.

JavaScript là programming language của Web.


## TRANG 33

1.5. Công cụ thiết kế web

Dùng cho thiết kế user interface:

- Adobe

- Adobe Dreamweaver

- Adobe Photoshop

- Adobe Illustrator

- Figma


## TRANG 34

1.5. Công cụ thiết kế web

Dùng cho coding:

- VS Code

- Sublime Text

- JetBrains

- Codepen.io

- jsFiddle.net


## TRANG 35

1.5. Công cụ thiết kế web

Dùng cho debugging:

- View page source (Ctrl + U)

- Developer tools trên browser (F12)

- Responsive view


## TRANG 36

1.5. Công cụ thiết kế web

Website builder (no-code):

- Google Sites

- MS Power Pages

- https://bubble.io/

- https://www.shopify.com/website/builder

- https://www.wix.com/

Hãy tìm một nền tảng website builder miễn phí và thử xây dựng website yêu thích của bạn.


## TRANG 37

Thực hành & bài tập về nhà

Cài đặt coding tool yêu thích của bạn. Tìm và tham gia các cộng đồng Front-end & web development (Facebook, Reddit, Discord, Slack,...). Kể tên ít nhất 10 vai trò khác nhau trong web design.
