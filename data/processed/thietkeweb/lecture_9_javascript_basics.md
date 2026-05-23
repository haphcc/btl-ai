### BÀI 9

#### BÀI GIẢNG 9: JAVASCRIPT CƠ BẢN

## TRANG 1

Thiết kế Web - Bài giảng 9: JavaScript


## TRANG 2

Nội dung

6.1. Giới thiệu JavaScript. 6.2. Cú pháp cơ bản. 6.3. Variable và data type. 6.4. Operator.


## TRANG 3

6.1. Giới thiệu JavaScript

JavaScript là gì?

- Một client-side scripting language -> chạy trên máy của người dùng, phụ thuộc vào khả năng và thiết lập của browser.
- Không liên quan đến Java.
- Được Brendan Eich tạo ra tại Netscape năm 1995, ban đầu có tên "LiveScript".
- Dynamic programming language: browser đọc code và diễn giải ngay khi chạy, không cần compiler.
- Loosely typed: chúng ta không cần khai báo kiểu của variable trong JS, chỉ cần gán value.


## TRANG 4

JS có thể làm gì?

Nếu "structural" layer của page là HTML markup và "presentational" layer được tạo bằng CSS, thì layer thứ ba, "behavioral" layer, được tạo bằng JavaScript.

- Truy cập tất cả element trên webpage bằng DOM.
- Phản hồi input của người dùng: thay đổi content của page, CSS style hoặc behavior của browser ngay khi chạy.


## TRANG 5

JS có thể làm gì - Ví dụ


## TRANG 6

Thêm JavaScript vào page

Trong HTML, JavaScript code được chèn giữa tag &lt;script&gt; và &lt;/script&gt;.

JavaScript trong &lt;head&gt;:

https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_head

JavaScript trong &lt;body&gt;:

https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_body

External JavaScript:

https://www.w3schools.com/js/tryit.asp?filename=tryjs_whereto_external

Để thêm nhiều script file vào một page, dùng nhiều script tag.


## TRANG 7

Thực hành

Tạo một HTML file đơn giản chứa một &lt;h1&gt; hiển thị: "This is my first JS example". Trong HTML file, tạo một &lt;button&gt; hiển thị: "Alert", và action khi click vào button sẽ gọi myFunction(). Với script được cung cấp bên dưới, hãy đặt nó vào webpage theo 3 cách để xem kết quả.


## TRANG 8

Mẹo hữu ích

Đặt script ở cuối element &lt;body&gt; giúp cải thiện tốc độ hiển thị, vì việc diễn giải script làm chậm quá trình display.

External script không được chứa tag &lt;script&gt;.

Đặt script trong external file có một số lợi ích:

- Tách HTML và code
- Làm HTML và JavaScript dễ đọc, dễ bảo trì hơn
- JavaScript file được cache có thể tăng tốc độ load page

External script có thể được tham chiếu bằng absolute path hoặc relative path.


## TRANG 9

6.2. Cú pháp cơ bản

JavaScript output. JavaScript statement. JavaScript syntax. JavaScript comment.


## TRANG 10

JavaScript output

Exercises & Homeworks / Lecture 9 / output.html

- Ghi vào một HTML element bằng innerHTML.
- Ghi vào HTML output bằng document.write().
- Ghi vào alert box bằng window.alert().
- Ghi vào browser console bằng console.log().

https://www.w3schools.com/js/js_output.asp

Trong tình huống nào nên áp dụng từng kiểu output?


## TRANG 11

Thực hành

Viết tên của bạn ra output bằng 4 cách khác nhau ở trên.

Mẹo hữu ích:

- Thay đổi property innerHTML của một HTML element là cách phổ biến để hiển thị data trong HTML.
- Dùng document.write() sau khi HTML document đã load sẽ xóa toàn bộ HTML hiện có -> method document.write() chỉ nên dùng để testing.
- Có thể bỏ qua keyword window -> alert("...").
- Dùng console.log() cho debugging.


## TRANG 12

JavaScript statement

Một script được tạo từ một chuỗi statement. Statement là command cho browser biết phải làm gì.

Dấu chấm phẩy ở cuối statement cho JavaScript biết command đã kết thúc, giống như dấu chấm kết thúc một câu.

Line break cũng có thể kết thúc command, nhưng best practice là kết thúc mỗi statement bằng dấu chấm phẩy.


## TRANG 13

JavaScript syntax

Cú pháp JavaScript định nghĩa hai loại value:

- Fixed value (literal): number hoặc string
- Variable value

JavaScript identifier/name (variable, keyword và function) phải bắt đầu bằng:

- Chữ cái (A-Z hoặc a-z)
- Dấu dollar ($)
- Hoặc dấu gạch dưới (_)

JavaScript identifier phân biệt chữ hoa chữ thường: variable tên myVariable, myvariable và MYVariable là 3 object khác nhau.


## TRANG 14

JavaScript comment

Single-line comment bắt đầu bằng //.

Multi-line comment bắt đầu bằng /* và kết thúc bằng */.

Khi nào dùng JavaScript comment:

1. Giải thích code
2. Ngăn execution (debugging)


## TRANG 15

6.3. Variable và data type

JavaScript variable. Khi nào dùng var, let hoặc const? Data type. Array.


## TRANG 16

JavaScript variable

JavaScript variable có thể được khai báo theo 4 cách:

- Tự động
- Dùng var
- Dùng let
- Dùng const


## TRANG 17

Khi nào dùng var, let hoặc const?

1. Luôn khai báo variable.
2. Luôn dùng const nếu value không nên thay đổi.
3. Luôn dùng const nếu type không nên thay đổi (Array và Object).
4. Chỉ dùng let nếu không thể dùng const.
5. Chỉ dùng var nếu bắt buộc hỗ trợ browser cũ.
6. Không thể khai báo lại variable đã khai báo bằng let hoặc const, nhưng var thì có thể.


## TRANG 18

Data type

JavaScript có thể xử lý nhiều loại data, nhưng hiện tại chỉ cần nghĩ tới number và string.

String được viết trong dấu nháy kép hoặc nháy đơn.

Number được viết không có dấu nháy.

Nếu đặt một number trong dấu nháy, nó sẽ được xử lý như text string.


## TRANG 19

Array

Array là một variable đặc biệt có thể giữ nhiều hơn một value.

Nếu bạn có một list item (ví dụ list tên xe), lưu từng xe vào các variable riêng lẻ sẽ rất bất tiện.

Nếu muốn loop qua các xe và tìm một xe cụ thể thì sao? Nếu không phải 3 xe mà là 300 xe thì sao?

Giải pháp là array.


## TRANG 20

Array

Array có thể giữ nhiều value dưới một name duy nhất, và bạn có thể truy cập value bằng index number.

Lưu ý: [0] là element đầu tiên. [1] là element thứ hai.

Changing an Array Element.


## TRANG 21

Thực hành

Mở file index.html trong thư mục Lecture 9 - Materials. Chạy code trong browser để xem kết quả. Chỉnh sửa đoạn code sau:

const pi = "3.14";

let x = pi + 1;

... document.getElementById("demo").innerHTML = x + "&lt;br&gt;" + person + "&lt;br&gt;" + answer;

Giải thích kết quả.


## TRANG 22

6.4. Operator

Các loại JavaScript operator. JavaScript arithmetic. JavaScript assignment.


## TRANG 23

Các loại JavaScript operator

- Arithmetic operator
- Assignment operator
- Comparison operator (tự đọc)
- String operator (tự đọc)
- Logical operator
- Bitwise operator
- Ternary operator
- Type operator


## TRANG 24

JavaScript arithmetic

Arithmetic operator thực hiện phép tính số học trên number (literal hoặc variable).

https://www.w3schools.com/js/js_arithmetic.asp


## TRANG 25

JavaScript assignment

Assignment operator gán value cho JavaScript variable.

https://www.w3schools.com/js/js_assignment.asp


## TRANG 26

Thực hành (do ChatGPT đưa ra)

Viết một đoạn mã JavaScript để thực hiện các bước sau:

1. Khai báo một biến có tên là tuoiHienTai và gán giá trị bất kỳ là tuổi hiện tại của bạn.
2. Khai báo một biến có tên là soNamTang và gán giá trị bất kỳ là số năm bạn muốn tính sau đó.
3. Sử dụng biến tuoiHienTai và soNamTang để tính tuổi của bạn sau soNamTang năm và lưu kết quả vào một biến có tên là tuoiSauSoNamTang.
4. Sử dụng toán tử tăng dần (++) để tăng giá trị của biến tuoiHienTai lên 1 đơn vị.
5. Sử dụng console.log() để in ra màn hình thông tin sau soNamTang năm và tuổi hiện tại sau khi tăng thêm 1 năm.


## TRANG 27

Giáo trình, trang 619.
