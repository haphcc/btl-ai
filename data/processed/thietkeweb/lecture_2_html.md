### BÀI 2

#### BÀI GIẢNG 2: HTML

## HỌC VIỆN

## NGÂN HÀNG

Nội dung

2.1. Tạo một trang đơn giản. 2.2. Cú pháp HTML. 2.3. Marking up text. 2.4. Thêm link.

2.1. Tạo một trang đơn giản

Step 1: Bắt đầu với content. Step 2: Tạo cấu trúc cho document. Step 3: Xác định text element. Step 4: Thêm image. Step 5: Thay đổi cách text hiển thị bằng style sheet.

Ban đầu, chúng ta sẽ viết raw text content và xem browser xử lý nó như thế nào. Sau đó, bạn sẽ học cú pháp HTML element, các element dùng để thiết lập vùng chứa content và metadata, cách mô tả content bằng text element phù hợp, cách dùng attribute và empty element, rồi làm quen với việc định dạng content bằng Cascading Style Sheets (CSS).

## HTML

Mở text editor

Tạo document mới bằng:

- Notepad (Windows)

- TextEdit (MacOS)

Nhớ hiển thị phần mở rộng file.

Step 1: Bắt đầu với content

Exercise 2-1 (3 phút): Gõ nội dung homepage bên dưới vào document mới trong text editor. Hãy chép đúng như bạn thấy ở đây, giữ nguyên line break để thực hành theo bài.

Chọn "Save" hoặc "Save as" trong menu File, đặt tên file là: index.html.

Cái nhìn đầu tiên về content trong browser

Bạn sẽ thấy một trang giống như hình minh họa bên cạnh.

Quy ước đặt tên

Dùng suffix phù hợp cho file. HTML file phải kết thúc bằng .html hoặc .htm. Web graphics phải được đặt phần mở rộng theo đúng file format: .gif, .png, .jpg (.jpeg cũng được chấp nhận nhưng ít phổ biến hơn), hoặc .svg.

Không dùng dấu cách trong filename. Có thể dùng dấu gạch dưới hoặc dấu gạch ngang để tách từ trong filename, ví dụ robbins_bio.html hoặc robbinsbio.html.

Tránh ký tự đặc biệt như ?, %, #, /, :, ;,... Chỉ nên dùng chữ cái, số, dấu gạch dưới, dấu gạch ngang và dấu chấm. Cũng nên tránh ký tự quốc tế, chẳng hạn ký tự å trong tiếng Thụy Điển.

Quy ước đặt tên

Filename có thể phân biệt chữ hoa chữ thường, tùy cấu hình server. Dùng nhất quán chữ thường cho filename, dù không bắt buộc, là một cách giúp quản lý file dễ hơn.

Giữ tên file ngắn. Tên dài dễ bị gõ sai hơn, còn tên ngắn giúp giảm thêm vài byte kích thước file. Nếu thật sự cần đặt tên file dài gồm nhiều từ, bạn có thể tách từ bằng dấu gạch ngang, ví dụ a-long-document-title.html, để dễ đọc hơn.

Step 2: Tạo cấu trúc cho HTML document

Cấu tạo của một HTML element.

Mẹo nhỏ: slash và backslash.

Cấu trúc document cơ bản

- Document type declaration (còn gọi là DOCTYPE declaration) cho browser hiện đại biết nên dùng HTML specification nào để diễn giải document.

- Toàn bộ document nằm trong một html element. html element được gọi là root element vì nó chứa tất cả element trong document và không được nằm bên trong element nào khác.

Cấu trúc document cơ bản

- Meta element cung cấp document metadata, tức thông tin về document. Trong trường hợp này, nó chỉ định character encoding (một tập hợp chuẩn hóa gồm chữ cái, số và ký hiệu) được dùng trong document là Unicode phiên bản UTF-8. Các loại metadata khác do meta element cung cấp gồm author, keywords, publishing status và description có thể được search engine sử dụng.

Exercise 2-2 (5 phút): Thêm cấu trúc tối thiểu

Mở document index.html mới nếu nó chưa được mở.

1. Thêm DOCTYPE declaration.

2. Đặt toàn bộ document vào HTML root element bằng cách thêm start tag &lt;html&gt; sau DOCTYPE và end tag &lt;/html&gt; ở cuối toàn bộ text.

3. Tiếp theo, tạo document head chứa title cho page. Chèn tag &lt;head&gt; và &lt;/head&gt; trước content. Bên trong head element, thêm thông tin character encoding &lt;meta charset="utf-8"&gt; và title "Black Goose Bistro" được bao quanh bởi opening tag và closing tag &lt;title&gt;.

4. Cuối cùng, xác định body của document bằng cách bọc text content trong tag &lt;body&gt; và &lt;/body&gt;.

5. Lưu document trong thư mục hiện tại để ghi đè phiên bản cũ.

Exercise 2-2 (5 phút): Thêm cấu trúc tối thiểu

Step 3: Xác định text element

Khi markup content, nhiệm vụ của bạn là chọn HTML element mô tả content một cách có ý nghĩa nhất. Ví dụ: &lt;h1&gt;, &lt;p&gt;, &lt;b&gt;.

Ngoài việc thêm ý nghĩa cho content, markup còn tạo cấu trúc cho document -> DOM (Document Object Model).

Exercise 2-3 (5 phút): Định nghĩa text element

1. Mở document index.html trong text editor nếu nó chưa được mở.

2. Dòng text đầu tiên, "Black Goose Bistro", là heading chính của page, vì vậy chúng ta markup nó bằng Heading Level 1 (h1). Đặt opening tag &lt;h1&gt; ở đầu dòng và closing tag &lt;/h1&gt; sau dòng đó như sau:

&lt;h1&gt;Black Goose Bistro&lt;/h1&gt;

3. Page của chúng ta cũng có ba subhead. Markup chúng bằng Heading Level 2 (h2) theo cách tương tự. Tôi làm mẫu phần đầu tiên; bạn làm tương tự với "Catering" và "Location and Hours."

&lt;h2&gt;The Restaurant&lt;/h2&gt;

Exercise 2-3 (5 phút): Định nghĩa text element

4. Mỗi h2 element được theo sau bởi một đoạn text ngắn, vì vậy hãy markup chúng bằng paragraph (p) element theo cách tương tự. Đây là phần đầu tiên; bạn làm các phần còn lại:

&lt;p&gt;The Black Goose Bistro offers casual lunch and dinner fare in a relaxed atmosphere. The menu changes regularly to highlight the freshest local ingredients.&lt;/p&gt;

5. Trong phần Catering, tôi muốn nhấn mạnh rằng khách chỉ cần để việc nấu nướng cho chúng ta. Để nhấn mạnh text, markup nó bằng emphasis element (em) như sau:

&lt;p&gt;You have fun. &lt;em&gt;We'll handle the cooking.&lt;/em&gt; Black Goose Catering can handle events from snacks for a meetup to elegant corporate fundraisers.&lt;/p&gt;

Exercise 2-3 (5 phút): Định nghĩa text element

Kết quả sẽ như sau.

Block và Inline Element

Theo mặc định, heading và paragraph hiển thị dưới dạng block element. Browser xử lý block element như các hộp chữ nhật nhỏ được xếp chồng trên page.

Mỗi block element bắt đầu trên một dòng mới.

Inline element không bắt đầu dòng mới; chúng đi theo luồng nội dung. Ví dụ: tag &lt;em&gt;.

Default Style

Browser xác định h1 trông như thế nào bằng cách nào?

Nó dùng style sheet. Tất cả browser đều có style sheet tích hợp riêng mô tả cách render mặc định của các element.

Cách render mặc định tương đối giống nhau giữa các browser (ví dụ h1 luôn lớn và đậm), nhưng vẫn có một số khác biệt (blockquote element cho trích dẫn dài có thể được thụt lề hoặc không).

Làm thế nào để tùy chỉnh visual của các element này theo ý chúng ta?

Step 4: Thêm image

Image element (img) là một empty element. Nó yêu cầu browser lấy image file từ server và chèn vào page.

Attribute

Một tag &lt;img&gt; tự nó chưa hữu ích vì nó không cho biết image nào sẽ được sử dụng. Đây là lúc attribute xuất hiện.

Attribute là chỉ dẫn dùng để làm rõ hoặc chỉnh sửa một element.

Với img element, attribute src (viết tắt của "source") là bắt buộc và chỉ định vị trí (URL) của image file.

Attribute

Cú pháp của attribute như sau:

&lt;element attributename="value"&gt;Content&lt;/element&gt;

&lt;element attribute1="value" attribute2="value"&gt;

Exercise 2-4 (5 phút): Thêm image

1. Lấy một bản sao image file tên blackgoose.png trên ổ cứng của bạn.

2. Chèn nó vào đầu first-level heading bằng cách gõ img element và các attribute như sau:

&lt;h1&gt;&lt;img src="blackgoose.png" alt="logo"&gt;Black Goose Bistro&lt;/h1&gt;

3. Thêm line break (br) sau img element để đưa headline text xuống dòng mới.

&lt;h1&gt;&lt;img src="blackgoose.png" alt="logo"&gt;&lt;br&gt;Black Goose Bistro&lt;/h1&gt;

Exercise 2-4 (5 phút): Thêm image

Lưu index.html rồi mở hoặc refresh nó trong browser window.

Step 5: Thay đổi giao diện bằng style sheet

Thay đổi appearance của text element và background của page bằng một số rule style sheet đơn giản.

-> Cascading Style Sheets (CSS)

Exercise 2-5 (3 phút): Thêm style sheet

Style element được đặt bên trong document head.

Bắt đầu bằng cách thêm style element vào document như minh họa.

Exercise 2-5 (3 phút): Thêm style sheet

Copy style code từ sample file vào index.html của bạn.

Lưu file và xem kết quả trong browser.

2.2. Cú pháp HTML

Tất cả HTML document phải bắt đầu bằng document type declaration: <!DOCTYPE html&gt;.

HTML document bắt đầu bằng &lt;html&gt; và kết thúc bằng &lt;/html&gt;.

Phần hiển thị của HTML document nằm giữa &lt;body&gt; và &lt;/body&gt;.

HTML element

HTML element là toàn bộ phần từ start tag đến end tag:

&lt;tagname&gt;Content goes here...&lt;/tagname&gt;

HTML element có thể lồng nhau (nghĩa là element có thể chứa element khác).

HTML element không có content được gọi là empty element.

HTML tag không phân biệt chữ hoa chữ thường: &lt;P&gt; có cùng ý nghĩa với &lt;p&gt;.

HTML attribute

Tất cả HTML element đều có thể có attribute.

Attribute cung cấp thông tin bổ sung về element.

Attribute luôn được khai báo trong start tag.

Attribute thường đi theo cặp name/value như sau:

name="value"

2.3. Marking up text

Paragraph. Heading. Thematic break. List. Các element khác.

Paragraph element

Paragraph là element cơ bản nhất của một text document. Đánh dấu một paragraph bằng p element bằng cách chèn opening tag &lt;p&gt; ở đầu paragraph và closing tag &lt;/p&gt; sau paragraph đó.

Paragraph có thể chứa text, image và các inline element khác, nhưng không được chứa heading, list, sectioning element hoặc các element thường hiển thị mặc định như block.

Heading

Khi bạn thêm heading vào content, browser sử dụng chúng để tạo document outline cho page.

Các assistive reading device như screen reader dùng document outline để giúp người dùng quét nhanh và điều hướng qua page.

Search engine xem xét heading level như một phần trong algorithm của chúng.

Thematic break

Nếu muốn thể hiện rằng một chủ đề đã kết thúc và một chủ đề khác bắt đầu, bạn có thể chèn "paragraph-level thematic break" bằng hr element.

hr element thêm một đường phân tách logic giữa các section của page hoặc giữa các paragraph mà không đưa vào heading level mới.

List

Unordered list: tập hợp item không theo thứ tự cụ thể.

Ordered list: list trong đó thứ tự item là quan trọng.

Description list (hiếm dùng): list gồm các cặp name và value, bao gồm nhưng không giới hạn ở term và definition.

List

Unordered list với style mặc định.

List

Unordered list với style sheet phù hợp.

List

Ordered list với style mặc định.

Các content element khác

Long quotation. Preformatted text. Figure.

-> Tự đọc.

Exercise 2-6: Marking up a recipe (15 phút)

Tìm raw text của một công thức nấu ăn. Bạn tự quyết định element nào là semantic match tốt nhất cho từng phần content.

Bạn sẽ dùng paragraph, heading, list và ít nhất một special content element.

Trang 81.

2.4. Thêm link

href attribute. Link tới page trên web. Link trong chính site của bạn. Mở trong browser window mới. Mail link.

href attribute

Absolute URL:

href="http://www.oreilly.com/book1/recipes/index.html"

Relative URL:

href="recipes/index.html"

Link tới page trên web (external link)

Hầu hết thời gian, bạn sẽ muốn tạo link tới một page trên web:

&lt;li&gt;&lt;a href="http://www.foodnetwork.com"&gt;The Food Network&lt;/a&gt;&lt;/li&gt;

Link trong chính site của bạn

Một phần lớn việc linking là giữa các page trong chính site của bạn: từ homepage tới section page, từ section page tới content page, v.v. Trong các trường hợp này, bạn có thể dùng relative URL.

Link trong chính site của bạn

Link trong cùng một directory. Link tới directory thấp hơn. Link tới directory cao hơn. Link bằng site root relative pathname. Link tới một điểm cụ thể trong page.

Mở trong browser window mới

Thiết lập target="_blank" luôn khiến browser mở một window mới.

Ví dụ:

&lt;a href="http://www.oreilly.com" target="_blank"&gt;O'Reilly&lt;/a&gt;

Mail link

Một sample mailto link được minh họa như sau:

&lt;a href="mailto:alklecker@example.com"&gt;Contact Al Klecker&lt;/a&gt;

Bài tập về nhà

Exercise 5-3 (trang 110). Test yourself (trang 128): toàn bộ 11 câu hỏi.

Nộp lên LMS, 1 điểm đóng góp cho 2 bài nộp đầu tiên (TA review).
