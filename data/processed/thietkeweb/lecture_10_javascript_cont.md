### BÀI 10

#### BÀI GIẢNG 10: JAVASCRIPT (TIẾP)

Thiết kế Web - Bài giảng 10: JavaScript

Nội dung

6.5. Loop và conditional statement. 6.6. Function. 6.7. JavaScript object.

6.5. Loop và conditional statement

JavaScript for loop. JavaScript for in. JavaScript while loop. JavaScript if, else và else if. JavaScript break và continue.

JavaScript for loop

Loop có thể thực thi một block code nhiều lần.

Loop rất hữu ích khi bạn muốn chạy cùng một đoạn code lặp đi lặp lại, mỗi lần với một value khác nhau.

JavaScript for loop

Câu lệnh tổng quát:

- Expression 1 được thực thi một lần trước khi code block chạy.
- Expression 2 định nghĩa condition để thực thi code block.
- Expression 3 được thực thi mỗi lần sau khi code block đã chạy.

Thực hành

Tạo một array tên studentList, gồm 5 element là tên của 5 người bạn. Viết một for loop để alert cho các bạn rằng ngày mai là hạn nộp project assignment:

"Hey " + studentList[i] + ", today is " + today_value + ", deadline is coming!"

JavaScript if, else và else if

Conditional statement được dùng để thực hiện các action khác nhau dựa trên các condition khác nhau.

Trong JavaScript, chúng ta có các conditional statement sau:

- Dùng if để chỉ định block code được thực thi nếu condition là true.
- Dùng else để chỉ định block code được thực thi nếu cùng condition đó là false.
- Dùng else if để chỉ định condition mới cần kiểm tra nếu condition đầu tiên là false.
- Dùng switch để chỉ định nhiều block code thay thế.

JavaScript if, else và else if

Dùng if statement để chỉ định một block JavaScript code được thực thi nếu condition là true.

Ví dụ:

else statement

Dùng else statement để chỉ định một block code được thực thi nếu condition là false.

Ví dụ:

else if statement

Dùng else if statement để chỉ định một condition mới nếu condition đầu tiên là false.

Ví dụ:

Thực hành

Bài tập ở trang 606.

6.6. Function

JavaScript function. Function invocation. Function return.

JavaScript function

JavaScript function là một block code được thiết kế để thực hiện một task cụ thể.

JavaScript function được thực thi khi có "thứ gì đó" invoke nó (call nó).

Ví dụ:

Function invocation

Code bên trong function sẽ thực thi khi có "thứ gì đó" invoke (call) function:

- Khi một event xảy ra (khi user click một button)
- Khi nó được invoke (call) từ JavaScript code
- Tự động (self-invoked)

Function return

Khi JavaScript gặp return statement, function sẽ dừng thực thi.

Nếu function được invoke từ một statement, JavaScript sẽ "return" để thực thi code sau invoking statement.

Function thường tính toán một return value. Return value được "trả về" cho "caller".

Native function

JavaScript có hàng trăm predefined function, bao gồm:

alert(), confirm() và prompt(): các function này kích hoạt dialog box cấp browser.

Date(): trả về ngày và giờ hiện tại.

parseInt("123"): function này, cùng nhiều việc khác, nhận một string data type chứa number và chuyển nó thành number data type. String được truyền vào function như một argument.

... và nhiều built-in function khác.

Custom function

Để tạo custom function, chúng ta gõ keyword function, theo sau là name của function, opening và closing parentheses, rồi opening và closing curly brackets:

function name() { // Our function code goes here.

}

Tương tự variable và array, tên function có thể là bất kỳ tên nào bạn muốn, nhưng vẫn phải tuân thủ các rule cú pháp đặt tên. Nếu tạo một function chỉ alert một đoạn text, nó sẽ như sau:

function foo() { alert("Our function just ran!");

// This code won't run until we call the function 'foo()' }

Bài tập

Viết file [Ho_ten_sv].html có các thành phần tối thiểu và mã JavaScript thực hiện các yêu cầu sau:

Yêu cầu người dùng nhập vào một mật khẩu bằng prompt(). Viết hàm kiểm tra mật khẩu theo các tiêu chí sau:

- Ít nhất 8 ký tự.
- Chứa ít nhất một chữ cái viết hoa (A-Z).
- Chứa ít nhất một chữ cái viết thường (a-z).
- Chứa ít nhất một chữ số (0-9).
- Chứa ít nhất một ký tự đặc biệt (ví dụ: @, #, $, %...).

Nếu mật khẩu không hợp lệ, hiển thị thông báo lỗi tương ứng và yêu cầu nhập lại.

Nếu mật khẩu hợp lệ, hiển thị thông báo "Mật khẩu hợp lệ!" kèm theo độ mạnh của mật khẩu:

- Yếu: chỉ vừa đủ 8 ký tự.
- Trung bình: đáp ứng tất cả điều kiện nhưng dưới 12 ký tự.
- Mạnh: đáp ứng tất cả điều kiện và có từ 12 ký tự trở lên.

Thử nghiệm với các tình huống khác nhau trước khi nộp lại file [Ho_ten_sv].html.

6.7. JavaScript object

Real-life object, property và method. Object definition. Object property. Object method. Keyword this.

Real-life object, property và method

Trong đời thực, car là một object.

Car có property như weight và color, và method như start và stop.

Real-life object, property và method

Tất cả car có cùng property, nhưng property value khác nhau giữa các car.

Tất cả car có cùng method, nhưng method được thực hiện ở các thời điểm khác nhau.

Object definition

Object cũng là variable. Nhưng object có thể chứa nhiều value.

Đoạn code này gán nhiều value (Fiat, 500, white) cho một variable tên car.

Các value được viết dưới dạng cặp name:value (name và value ngăn cách bằng dấu hai chấm).

Object definition

Space và line break không quan trọng. Một object definition có thể trải trên nhiều dòng.

Object property

Các cặp name:value trong JavaScript object được gọi là property.

Truy cập object property

Bạn có thể truy cập object property theo hai cách.

Thực hành:

https://www.w3schools.com/js/tryit.asp?filename=tryjs_objects_properties_1

Object method

Method là action có thể được thực hiện trên object.

Method được lưu trong property dưới dạng function definition.

Keyword this

Trong JavaScript, keyword this tham chiếu tới một object.

Object nào được tham chiếu phụ thuộc vào cách this được invoke (sử dụng hoặc gọi).

this không phải là variable. Nó là keyword. Bạn không thể thay đổi value của this.

Keyword this

Trong function definition, this tham chiếu tới "owner" của function.

Trong ví dụ trên, this là person object "sở hữu" function fullName.

Nói cách khác, this.firstName nghĩa là property firstName của object this.

Truy cập object method

Bạn truy cập một object method bằng cú pháp sau.

Thực hành:

https://www.w3schools.com/js/tryit.asp?filename=tryjs_objects_method

Bài tập

Hãy viết một chương trình JavaScript để quản lý thông tin của một đội bóng. Để làm điều này, bạn cần thực hiện các bước sau:

1. Tạo một object có tên footballTeam để lưu thông tin về đội bóng. Object này cần có các property sau:

teamName: tên của đội bóng (string).

coachName: tên của huấn luyện viên (string).

players: một array chứa thông tin về các cầu thủ của đội bóng. Mỗi cầu thủ là một object với các property:

name: tên của cầu thủ (string).

age: tuổi của cầu thủ (number).

position: vị trí chơi bóng của cầu thủ (string).

isInjured: một boolean value cho biết cầu thủ có bị chấn thương hay không.

Bài tập

2. Tạo một method tên addPlayer trong object footballTeam để thêm một cầu thủ mới vào đội bóng. Method này nhận thông tin về cầu thủ và thêm cầu thủ đó vào array players.

3. Tạo một method tên listPlayers trong object footballTeam để in ra danh sách cầu thủ trong đội bóng. Method này duyệt qua array players và in thông tin về mỗi cầu thủ.

4. Tạo một method tên injuredPlayers trong object footballTeam để đếm và in số lượng cầu thủ bị chấn thương trong đội bóng.

5. Tạo một method tên teamInfo trong object footballTeam để in thông tin tổng quan về đội bóng, bao gồm tên đội bóng, tên huấn luyện viên và số lượng cầu thủ trong đội.

Checkpoint 1 cho bài thi cuối kỳ

Chọn một ý tưởng cho website của bạn. Startup company -> loại hình kinh doanh mới. Popular website -> tính năng mới. Không khuyến khích website đơn giản chỉ có 2-3 page. Khảo sát các website tương tự, liệt kê tất cả page của chúng. Ấn tượng của bạn là gì?

Khởi tạo một git repository.
