# CHƯƠNG 4. KẾT NỐI CSDL MYSQL VỚI PHP

**NỘI DUNG CHÍNH:**
- Hệ quản trị cơ sở dữ liệu MySQL và API cơ sở dữ liệu.
- Làm việc với PhpMyAdmin, tạo database, tạo bảng và sao lưu phục hồi CSDL.
- Các kiểu dữ liệu trong MySQL.
- Kết nối PHP với MySQL bằng MySQLi và thao tác SELECT, INSERT, UPDATE, DELETE.
- Prepared statement, LIMIT và OFFSET.
- Session, Cookie, xử lý giỏ hàng, cấu hình `php.ini`.
- Xử lý ngoại lệ và biến siêu toàn cục `$_SERVER`.

## Hệ Quản Trị CSDL MySQL

MySQL là hệ quản trị cơ sở dữ liệu quan hệ. Cơ sở dữ liệu quan hệ lưu trữ dữ liệu dưới dạng các bảng liên kết với nhau bởi trường khóa. MS Access, Oracle và MySQL là các hệ quản trị cơ sở dữ liệu quan hệ khác nhau.

Trong hệ điều hành Linux, MySQL được sử dụng phổ biến vì là phần mềm mã nguồn mở và dễ sử dụng.

## APIs Cơ Sở Dữ Liệu

API cơ sở dữ liệu cho phép người phát triển viết các ứng dụng có thể truy cập hoặc di chuyển giữa các sản phẩm cơ sở dữ liệu.

Một số API cơ sở dữ liệu phổ biến:

- Native-interface.
- Open Database Connectivity, ODBC.
- Java Database Connectivity, JDBC.
- Common Object Request Broker Architecture, CORBA.

PHP hỗ trợ MySQL để truy cập cơ sở dữ liệu. Một website kết nối đến CSDL để truy cập và lưu trữ thông tin.

Các bước kết nối CSDL:

1. Mở kết nối CSDL.
2. Làm việc với CSDL.
3. Đóng kết nối CSDL.

## Làm Việc Với PhpMyAdmin

Truy cập PhpMyAdmin tại:

```text
http://localhost/phpmyadmin/
```

### 1. Tạo cơ sở dữ liệu mới

Các bước:

1. Tại `Create database`, nhập tên CSDL cần tạo.
2. Tại `Collation`, chọn kiểu dữ liệu cho CSDL, ví dụ `utf8_general_ci`.
3. Nhấn `Create`.

### 2. Tạo bảng dữ liệu

Tại `Create table`:

- `Name`: nhập tên bảng.
- `Number of column`: nhập số trường cho bảng.
- Nhấn `GO`.

### 3. Tạo trường dữ liệu

Các thông tin khi tạo trường:

| Thuộc tính | Ý nghĩa |
|---|---|
| Name | Tên trường |
| Type | Kiểu dữ liệu |
| Length/values | Chiều dài hoặc giá trị |
| Default | Giá trị mặc định |
| Collation | Character set |
| Index | Chỉ mục, khóa |
| Comment | Chú thích |

### 4. Nhập và truy vấn dữ liệu

Để nhập dữ liệu:

1. Mở CSDL cần thao tác.
2. Mở bảng dữ liệu cần thao tác.
3. Dùng `Structure` để xem cấu trúc và chỉnh sửa bảng.
4. Dùng `Insert` để thêm dữ liệu vào bảng.

Để thực hiện truy vấn:

1. Chọn tab `SQL`.
2. Gõ mã lệnh vào cửa sổ.
3. Nhấn `GO`.

### 5. Sao lưu và phục hồi CSDL

Sao lưu CSDL:

1. Chọn tab `Export`.
2. Export CSDL thành file `.sql`.
3. Nhấn `GO`.

Phục hồi CSDL:

1. Mở CSDL cần phục hồi.
2. Chọn tab `Import`.
3. Chọn `Browse your computer` và chọn file `.sql`.
4. Chọn character set là `utf-8`.
5. Chọn `GO`.

## Các Kiểu Dữ Liệu Trong MySQL

### 1. Kiểu số

Slide nhắc đến các nhóm kiểu:

- Kiểu số nguyên.
- Kiểu dấu chấm động.
- Kiểu dấu chấm cố định.
- Kiểu bit.

Kiểu dấu chấm cố định như `DECIMAL` và `NUMERIC` dùng để bảo vệ độ chính xác, ví dụ dữ liệu tiền tệ.

**Ví dụ:** Trong SQL chuẩn, `DECIMAL(5,2)` có precision là 5 và scale là 2, nghĩa là lưu giá trị có 5 chữ số, trong đó có 2 chữ số thập phân. Phạm vi có thể là từ `-999.99` đến `999.99`.

```sql
DECIMAL(5,2)
```

Kiểu `BIT(N)` lưu trữ N giá trị bit, với N từ 1 đến 64. Có thể chỉ định giá trị bit bằng dạng:

```sql
b'111'
b'10000000'
```

### 2. Kiểu ngày giờ

Các kiểu dữ liệu ngày tháng và thời gian:

- `DATE`.
- `TIME`.
- `DATETIME`.
- `TIMESTAMP`.
- `YEAR`.

`TIME` hiển thị theo định dạng `HH:MM:SS` hoặc `HHH:MM:SS` cho giá trị giờ lớn. Giá trị của `TIME` có thể từ `-838:59:59` đến `838:59:59`.

`YEAR` dùng 1 byte để mô tả giá trị. Có thể khai báo `YEAR(2)` hoặc `YEAR(4)`. Với định dạng 4 số, MySQL hiển thị `YYYY`, phạm vi từ 1901 đến 2155 hoặc 0000.

### 3. Kiểu chuỗi

Các kiểu chuỗi:

- `CHAR`.
- `VARCHAR`.
- `BINARY`.
- `VARBINARY`.
- `BLOB`.
- `TEXT`.
- `ENUM`.
- `SET`.

`SET` là đối tượng chuỗi có không hoặc nhiều giá trị phân tách bằng dấu phẩy, tối đa 64 giá trị, chọn từ danh sách được đưa ra khi tạo bảng.

## Kết Nối PHP Với MySQL

Kết nối trong PHP là quá trình thiết lập kết nối giữa PHP với cơ sở dữ liệu như MySQL, PostgreSQL hoặc SQL Server. Quản lý kết nối hiệu quả giúp tối ưu hiệu suất và đảm bảo bảo mật khi thao tác CSDL.

Trong PHP có ba cách chính để kết nối MySQL:

- **MySQLi:** MySQL Improved Extension, chỉ dùng cho MySQL.
- **PDO:** PHP Data Objects, hỗ trợ nhiều CSDL khác nhau.
- **MySQL cũ:** deprecated, không nên dùng nữa.

### 1. Kết nối bằng MySQLi

Cú pháp:

```php
$con = new mysqli(host, username, password, dbname, port, socket);
```

Trong đó:

- `host`: tên server chứa CSDL, mặc định là `localhost`.
- `username`: tên người dùng.
- `password`: mật khẩu.
- `dbname`: tên cơ sở dữ liệu.
- `port`: cổng kết nối.
- `socket`: socket sử dụng.
- `$con`: biến lưu trữ kết nối.

**Ví dụ:**

```php
<?php
$con = new mysqli("localhost", "root", "", "database_name");

if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
}
?>
```

## Thực Hiện Truy Vấn CSDL

### 1. Truy vấn SELECT

Các bước:

1. Tạo đối tượng kết nối.
2. Xây dựng câu lệnh truy vấn.
3. Thực hiện truy vấn bằng phương thức `query()` hoặc hàm truy vấn.
4. Đọc dữ liệu bằng `fetch_assoc()` hoặc `mysqli_fetch_assoc()`.

```php
<?php
$con = new mysqli("localhost", "root", "", "database_name");
$sql = "SELECT * FROM table_name";
$result = $con->query($sql);

while ($row = $result->fetch_assoc()) {
    print_r($row);
}
?>
```

### 2. Truy vấn INSERT

Các bước:

1. Tạo đối tượng kết nối.
2. Xây dựng câu lệnh `INSERT`.
3. Thực hiện bằng `mysqli_query()` hoặc `$con->query()`.

```php
<?php
$sql = "INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2')";
$con->query($sql);
?>
```

### 3. Truy vấn UPDATE

```php
<?php
$sql = "UPDATE table_name SET column1='value1' WHERE id=1";
$con->query($sql);
?>
```

### 4. Truy vấn DELETE

```php
<?php
$sql = "DELETE FROM table_name WHERE id=1";
$con->query($sql);
?>
```

### 5. Đóng kết nối

Đóng kết nối theo hướng đối tượng:

```php
$con->close();
```

Slide ghi cách đóng bằng hàm là `mysqli_connect($con)`, nhưng ngữ cảnh là đóng kết nối nên cần kiểm tra lại khi đối chiếu với mã gốc trong slide.

## Tạo CSDL Và Bảng Bằng PHP

Các bước tạo CSDL hoặc bảng bằng PHP:

1. Tạo đối tượng kết nối.
2. Xây dựng câu lệnh truy vấn tạo CSDL hoặc tạo bảng.
3. Thực thi truy vấn với đối tượng kết nối.

```php
<?php
$con = new mysqli("localhost", "root", "");
$sql = "CREATE DATABASE database_name";
$con->query($sql);
?>
```

```sql
CREATE TABLE table_name (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);
```

## Prepared Statement

Prepared statement tạo ra một câu lệnh SQL truy vấn CSDL, trong đó một số giá trị chưa xác định được gọi là tham số. CSDL phân tích cú pháp, biên dịch, tối ưu hóa và lưu trữ câu lệnh nhưng chưa thực thi. Sau đó ứng dụng liên kết giá trị tham số và CSDL thực thi. Câu lệnh có thể được thực thi nhiều lần với các giá trị khác nhau.

```php
<?php
$stmt = $con->prepare("INSERT INTO table_name (name) VALUES (?)");
$stmt->bind_param("s", $name);
$stmt->execute();
?>
```

## LIMIT Và OFFSET

Truy vấn giới hạn dữ liệu dùng `LIMIT` và `OFFSET`.

```sql
SELECT * FROM Orders LIMIT 30;
```

Lấy 30 bản ghi đầu tiên.

```sql
SELECT * FROM Orders LIMIT 10 OFFSET 15;
```

Lấy 10 bản ghi từ bản ghi thứ 16.

## Session Và Cookie

Website lưu trữ thông tin người dùng trong CSDL để duy trì các lần truy xuất. Cookie cho phép website lưu trữ thông tin sử dụng. PHP hỗ trợ HTTP cookie.

### 1. Web page

Trang web sử dụng giao thức HTTP để gửi thông tin đến server. Slide mô tả HTTP là giao thức an toàn theo nghĩa lệnh hiện tại được hoàn thành không phụ thuộc vào các lệnh trước đó. Có hai loại trang web:

- Web tĩnh.
- Web động.

### 2. Cookie

Cookie là dữ liệu được website lưu trữ trên máy client trong một khoảng thời gian. PHP có thể tạo và trích xuất giá trị cookie.

Phân loại:

- **Persistent cookie:** tồn tại trong trình duyệt trong khoảng thời gian được chỉ định.
- **Non-persistent cookie:** bị xóa khi người dùng thoát trình duyệt.

Mục đích sử dụng cookie:

- Đếm số lần người dùng thăm website.
- Phân biệt người dùng mới và người dùng thường xuyên.
- Ghi nhận tần suất và ngày cuối cùng người dùng viếng thăm.
- Mở rộng thiết lập trang web cho người dùng.

#### Tạo cookie

Cú pháp:

```php
setcookie(name, value, expire, path, domain, secure, httponly);
```

Trong đó:

- `name`: tên cookie, bắt buộc.
- `value`: giá trị cookie.
- `expire`: thời điểm hết hạn.
- `path`: đường dẫn trên server.
- `domain`: tên miền của cookie.
- `secure`: cookie chỉ dùng qua HTTPS nếu là `true`.
- `httponly`: cookie chỉ truy cập qua HTTP nếu là `true`.

Cookie hết hạn sau 30 ngày:

```php
setcookie("user", "value", time() + 86400 * 30);
```

Hàm `setcookie()` phải thực hiện trước mã HTML. Giá trị cookie khi gửi được tự động mã hóa và khi truy xuất tự động giải mã. Nếu không muốn mã hóa, dùng `setrawcookie()`.

#### Truy xuất và xóa cookie

Truy xuất:

```php
$_COOKIE['name_cookie'];
```

Xóa cookie bằng cách thiết lập thời gian hết hạn trong quá khứ:

```php
<?php
setcookie("user", "", time() - 3600);
?>
```

#### Vấn đề của cookie

Cookie lưu thông tin trên client nên không bảo mật và không đáng tin cậy nếu người khác có quyền truy cập máy khách. Một số nhược điểm:

- Không chứa được lượng lớn thông tin.
- Số cookie trên domain và trên trình duyệt bị giới hạn.
- Nhiều cookie có thể làm chậm hệ thống.
- Người dùng có thể tắt cookie.
- Nhiều người dùng chung một hệ thống có thể ảnh hưởng thống kê truy cập.

### 3. Session

Session trong PHP là cơ chế lưu trữ dữ liệu tạm thời trên server trong suốt thời gian người dùng truy cập website. Mỗi người dùng có một Session ID duy nhất để phân biệt các phiên làm việc.

Đặc điểm:

- Lưu trữ trên server nên bảo mật hơn cookie.
- Tồn tại trong suốt phiên làm việc.
- Dùng Session ID duy nhất.
- Dùng để lưu trạng thái đăng nhập, giỏ hàng, quyền truy cập, thông tin form tạm thời.

Session khác cookie ở điểm:

- Cookie lưu thông tin trên máy khách.
- Session lưu thông tin trên Web server.

#### Vòng đời session

PHP làm việc với session theo ba giai đoạn:

1. Starting the session.
2. Registering the session variable.
3. Ending the session.

#### Bắt đầu session

```php
session_start();
```

`session_start()` phải đặt ở đầu mỗi trang web trước khi thực hiện mã lệnh khác. Nếu session tồn tại, nó kích hoạt biến session; nếu chưa tồn tại, nó tạo Session ID mới.

#### Khởi tạo biến session

Có ba cách được slide nhắc đến:

- `$_SESSION[]`.
- `$_HTTP_SESSION_VAR[]`.
- `session_register()`.

Cách dùng hiện đại:

```php
$_SESSION['username'] = 'admin';
```

#### Kết thúc session

Khi người dùng logout, PHP thực thi `session_destroy()`.

```php
session_destroy();
```

Hủy biến session:

```php
session_unset();
```

## Xử Lý Giỏ Hàng

Quy trình xử lý giỏ hàng trong slide:

1. Chi tiết sản phẩm.
2. Thêm sản phẩm vào giỏ hàng.
3. Xử lý thêm giỏ hàng.
4. Giỏ hàng.
5. Đặt hàng.
6. Xử lý đặt hàng.
7. Thanh toán.
8. Xử lý thanh toán.

Slide cũng nhắc đến lưu trữ giỏ hàng trong CSDL và liệt kê dữ liệu từ đơn hàng và chi tiết đơn hàng.

## Làm Việc Với `php.ini`

Một Web server có thể chứa nhiều file `php.ini`. Bộ thông dịch PHP làm việc theo cấu hình trong file `php.ini`. Có thể dùng hàm sau để tìm vị trí file cấu hình:

```php
phpinfo();
```

### 1. Cấu trúc `php.ini`

File `php.ini` gồm các chỉ thị dạng:

```text
directive=value
```

Trong đó:

- `directive`: tên thiết lập.
- `value`: giá trị gán cho thiết lập.

Các dòng bắt đầu bằng dấu `;` là dòng chú thích, dòng trống bị bỏ qua.

### 2. Một số thiết lập phổ biến

```text
max_execution_time = 30
memory_limit = 128M
error_reporting = E_ALL
```

Quản lý file:

```text
file_uploads = On
upload_max_filesize = 2M
post_max_size = 8M
```

Session:

```text
session.save_path = "/tmp"
session.gc_maxlifetime = 1440
```

Hiển thị lỗi:

```text
display_errors = On
log_errors = On
date.timezone = "Asia/Ho_Chi_Minh"
```

### 3. Lưu ý khi dùng `php.ini`

- Thay đổi trong `php.ini` ảnh hưởng toàn cục tới ứng dụng PHP trên máy chủ.
- Có thể ghi đè một số thiết lập bằng `.htaccess` hoặc `ini_set()`.
- Cần có quyền truy cập và chỉnh sửa file `php.ini`.

## Xử Lý Ngoại Lệ

PHP có Exception Model tương tự các ngôn ngữ lập trình khác. Exception giúp điều khiển tốt hơn khi xử lý lỗi.

Các từ khóa:

- `try`: chứa đoạn mã có thể gây ngoại lệ.
- `catch`: bắt và xử lý ngoại lệ.
- `throw`: ném ngoại lệ.
- `finally`: khối tùy chọn, luôn thực thi dù có ngoại lệ hay không.

```php
try {
    throw new Exception("Có lỗi xảy ra");
} catch (Exception $e) {
    echo $e->getMessage();
} finally {
    // luôn thực hiện
}
```

Đối tượng `Exception` có các phương thức:

| Phương thức | Ý nghĩa |
|---|---|
| `getMessage()` | Thông báo exception |
| `getCode()` | Mã exception |
| `getFile()` | Tên file nguồn gây lỗi |
| `getLine()` | Dòng gây lỗi |
| `getTrace()` | Mảng backtrace |
| `getTraceAsString()` | Chuỗi trace đã định dạng |

## `$_SERVER` Trong PHP

`$_SERVER` là mảng chứa thông tin về header, đường dẫn và vị trí tập lệnh. Máy chủ web tạo các mục trong mảng này. Không đảm bảo mọi Web server đều cung cấp thông tin giống nhau.

Một số thành phần:

| Thành phần | Mô tả |
|---|---|
| `$_SERVER['PHP_SELF']` | Tên file đang chạy |
| `$_SERVER['GATEWAY_INTERFACE']` | Phiên bản CGI của server |
| `$_SERVER['SERVER_NAME']` | Tên máy chủ |
| `$_SERVER['HTTP_ACCEPT']` | Header Accept của request hiện tại |
| `$_SERVER['HTTP_HOST']` | Host header của request |
| `$_SERVER['HTTP_REFERER']` | URL trang trước |
| `$_SERVER['HTTPS']` | Truy vấn qua HTTP an toàn |
| `$_SERVER['REMOTE_ADDR']` | Địa chỉ IP người dùng |
| `$_SERVER['REMOTE_HOST']` | Tên máy chủ phía người dùng |
| `$_SERVER['REMOTE_PORT']` | Cổng phía người dùng |
| `$_SERVER['SCRIPT_FILENAME']` | Đường dẫn tuyệt đối của script |
| `$_SERVER['SERVER_PORT']` | Cổng server, ví dụ 80 |
| `$_SERVER['SERVER_SIGNATURE']` | Thông tin phiên bản server |
| `$_SERVER['PATH_TRANSLATED']` | Đường dẫn hệ thống tập tin |
| `$_SERVER['SCRIPT_NAME']` | Đường dẫn script hiện tại |
| `$_SERVER['SCRIPT_URI']` | URI trang hiện tại |

## Bài Tập

Các bài tập trong slide:

- Tùy chỉnh cấu hình `php.ini`.
- Sử dụng `$_SERVER` để in tên máy chủ, IP người dùng, phương thức HTTP và đường dẫn file hiện tại.
- Xử lý ngoại lệ bằng `try`, `catch`, `throw`.
- Hiển thị lỗi theo môi trường development và production.
- Xây dựng hệ thống log lỗi với ngoại lệ.
