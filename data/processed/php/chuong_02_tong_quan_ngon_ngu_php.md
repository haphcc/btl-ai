# CHƯƠNG 2. TỔNG QUAN NGÔN NGỮ PHP

**NỘI DUNG CHÍNH:**
- Giới thiệu và cài đặt PHP.
- Lịch sử phát triển PHP và PHP với doanh nghiệp.
- Bộ phát triển PHP và cơ chế hoạt động của mã lệnh PHP.
- Cú pháp cơ bản, biến, hằng, kiểu dữ liệu và toán tử trong PHP.
- Phương thức GET, POST và xử lý form.
- Câu lệnh điều khiển, vòng lặp và câu lệnh nhảy.
- Hàm trong PHP, include, header và mảng.

## Giới Thiệu Và Cài Đặt PHP

PHP được phát triển từ sản phẩm PHP/FI do Rasmus Lerdorf tạo ra năm 1995. Ban đầu PHP/FI là tập con đơn giản của các mã kịch bản Perl để theo dõi truy cập đến bản sơ yếu lý lịch trên mạng. PHP/FI là viết tắt của **Personal Home Page/Forms Interpreter**, gồm một số chức năng cơ bản như biến kiểu Perl, thông dịch tự động biến của form và cú pháp HTML nhúng.

### 1. Lịch sử phát triển

Năm 1997, PHP/FI 2.0 được viết lại bằng C và thu hút hàng nghìn người sử dụng. Khoảng 50.000 tên miền đã được ghi nhận có cài đặt PHP/FI 2.0, chiếm khoảng 1% số tên miền trên Internet thời điểm đó.

PHP 3.0 được Andi Gutmans và Zeev Suraski tạo ra năm 1997 sau khi viết lại hoàn toàn mã nguồn trước đó. PHP 3.0 là phiên bản đầu tiên có hình ảnh gần với PHP hiện nay. PHP 4 đưa số nhà phát triển PHP lên hàng trăm nghìn và hàng triệu website cài đặt PHP. PHP 5 chính thức ra mắt ngày 13 tháng 7 năm 2004, sau các bản beta và release candidate.

### 2. PHP với doanh nghiệp

PHP từng bị nhìn nhận là chưa sẵn sàng cho cấp doanh nghiệp. Zend đã thực hiện nhiều biện pháp để chuẩn hóa PHP và tạo sự tin cậy cho người dùng cao cấp.

Một số sản phẩm và framework được nhắc đến:

- **Zend Platform:** quản lý hệ thống ứng dụng PHP, nâng cao hiệu suất và tăng tốc ứng dụng PHP.
- **Zend Framework:** tập hợp các lớp và thư viện lập trình PHP 5, cung cấp giao diện lập trình chuẩn.
- **CodeIgniter, CakePHP, Symfony, Seagull:** framework hỗ trợ lập trình PHP cấp doanh nghiệp.

### 3. Bộ phát triển PHP

Cần cài đặt editor và server phù hợp:

- Editor: Sublime Text, Visual Studio Code, PHP Editor.
- Server để chạy PHP: Apache & MySQL, XAMPP, Laragon.

## Cơ Chế Hoạt Động Của Mã Lệnh PHP

Mã PHP được xử lý ở phía server. Trang `.php` có thể chứa HTML, CSS, JavaScript và PHP. Khi người dùng truy cập trang PHP qua trình duyệt, Web server chuyển mã PHP cho bộ thông dịch PHP xử lý, sau đó trả kết quả HTML về trình duyệt.

## Cú Pháp Cơ Bản Của PHP

Mã PHP được giới hạn bởi cặp ký hiệu:

```php
<?php
// mã PHP
?>
```

hoặc dạng rút gọn:

```php
<?
// mã PHP
?>
```

Các quy tắc cơ bản:

- Biến bắt đầu bằng dấu `$` và không cần khai báo trước kiểu dữ liệu.
- Mỗi câu lệnh kết thúc bằng dấu `;`.
- Chú thích nhiều dòng dùng `/* ... */`.
- Chú thích một dòng dùng `//` hoặc `#`.
- Cú pháp PHP tương tự các ngôn ngữ có cú pháp kiểu C, C++, Java, Perl.

### 1. Tạo và chạy trang PHP

Trang PHP:

- Được tạo bằng editor.
- Có phần mở rộng `.php`.
- Có thể chứa HTML, CSS, JavaScript, PHP và một số mã hỗ trợ khác.
- Được duyệt trên local hoặc Internet bằng trình duyệt web.

### 2. Lệnh in ra màn hình

Các lệnh thường dùng:

```php
echo "Nội dung cần in";
print_r($bien);
var_dump($bien);
```

Ý nghĩa:

- `echo`: in chuỗi ký tự hoặc nội dung biến ra màn hình.
- `print_r($bien)`: in thông tin kiểu dữ liệu, kích thước và nội dung biến.
- `var_dump($bien)`: in kiểu dữ liệu, kích thước và nội dung biến.

Khác biệt giữa `print` và `echo`:

- `print` là một hàm, khi thực thi trả về 1 nếu thành công, 0 nếu không thành công; có thể gán kết quả cho biến.
- `echo` không trả về kết quả.
- `echo` có thể dùng với nhiều tham số, `print` chỉ dùng với một tham số.

## Kiểu Dữ Liệu, Biến Và Hằng

### 1. Kiểu dữ liệu

PHP có các kiểu dữ liệu vô hướng:

- `integer`: số nguyên, chiếm 4 byte, giá trị khoảng từ -2 tỷ đến +2 tỷ.
- `float` hoặc `double`: số thực, phạm vi khoảng $(-10^{-308}, +10^{308})$.
- `string`: ký tự, chuỗi ký tự và con số.
- `boolean`: đúng hoặc sai.

Các kiểu dữ liệu khác:

- `array`: mảng.
- `object`: đối tượng.
- `resource`: tài nguyên.
- `null`: dữ liệu rỗng.

### 2. Khai báo và khởi tạo biến

Cú pháp:

```php
$variable_name = value;
```

Trong đó:

- `$variable_name`: tên biến.
- `value`: giá trị biến lưu trữ.

Biến được gán giá trị kiểu gì thì biến có kiểu dữ liệu đó.

**Ví dụ:**

```php
$name = "PHP";
$age = 18;
```

Gán bằng tham chiếu:

```php
$new_varname = &$old_varname;
```

### 3. Biến NULL

`NULL` là kiểu đặc biệt chỉ có một giá trị `NULL`.

```php
$my_var = NULL;
$my_var = null;
```

Một biến được gán `NULL` trả về `false` trong biểu thức Boolean và trả về `false` khi kiểm tra bằng `isset()`.

### 4. Hàm làm việc với biến

| Hàm | Ý nghĩa |
|---|---|
| `isset($varname)` | Trả về `true` nếu biến đã được thiết lập |
| `empty($varname)` | Trả về `true` nếu biến là 0, chuỗi rỗng hoặc chưa thiết lập |
| `gettype($varname)` | Trả về kiểu dữ liệu của biến |
| `settype($varname, "data type")` | Ép kiểu cho biến |
| `unset($varname)` | Giải phóng bộ nhớ đã cấp phát cho biến |
| `is_int()`, `is_array()`, `is_float()`, `is_numeric()`, `is_string()` | Kiểm tra kiểu dữ liệu tương ứng |

### 5. Cú pháp Document

Cú pháp Document bắt đầu với `<<<END` và kết thúc bằng `END;`. Cú pháp này hữu ích với chuỗi dài và giúp tránh nhiều vấn đề về dấu nháy.

```php
$text = <<<END
Nội dung chuỗi dài.
END;
```

### 6. Hằng

Hằng là một định danh chứa giá trị không thay đổi trong suốt quá trình thực thi chương trình. Hằng được khai báo bằng hàm `define()` và có thể truy cập ở bất kỳ đâu trong kịch bản.

Cú pháp:

```php
define(string_name, mixed_value);
```

Trong đó:

- `string_name`: tên hằng.
- `mixed_value`: giá trị số hoặc chuỗi.

**Ví dụ:**

```php
define("SITE_NAME", "PHP & MySQL");
```

## Toán Tử Trong PHP

PHP hỗ trợ nhiều nhóm toán tử:

- Toán tử số học.
- Toán tử gán.
- Toán tử so sánh.
- Toán tử logic.
- Toán tử tăng, giảm.
- Toán tử chuỗi.
- Toán tử điều kiện.
- Một số toán tử mới trong PHP 7.

### 1. Toán tử tăng, giảm

```php
$a = 1;
$a++;

$b = 1;
++$b;

$a--;
--$b;
```

### 2. Toán tử chuỗi

Toán tử chuỗi xử lý dữ liệu chuỗi. Nếu toán hạng không phải chuỗi, PHP chuyển đổi sang chuỗi trước khi thực hiện toán tử.

### 3. Toán tử điều kiện

Cú pháp:

```php
(biểu_thức_logic) ? (giá_trị_nếu_đúng) : (giá_trị_nếu_sai);
```

### 4. Toán tử PHP 7

Chia nguyên dùng hàm:

```php
intdiv($m, $n);
```

Toán tử spaceship:

```php
$x <=> $y;
```

Kết quả:

- `-1` nếu `$x < $y`.
- `0` nếu `$x = $y`.
- `1` nếu `$x > $y`.

Toán tử null coalescing:

```php
$result = $value ?? $default;
```

Toán tử `??` trả về chính giá trị nếu nó không `null`, ngược lại trả về giá trị khác.

Toán tử `use` được dùng để nhập class, interface hoặc trait từ namespace khác. Trong PHP, `use` cũng có thể đưa biến từ phạm vi bên ngoài vào hàm ẩn danh.

## Phương Thức GET Và POST

### 1. Các bước xử lý thông tin trên form HTML

1. Người dùng nhập thông tin vào HTML form và gửi đến Web server.
2. Web server gửi thông tin đến kịch bản PHP.
3. PHP xử lý thông tin.
4. PHP gửi đầu ra trở lại trình duyệt web.

### 2. Thẻ form HTML

Thẻ `<form>` dùng để tạo HTML form:

```html
<form action="url_xu_ly.php" method="GET">
    <!-- các điều khiển nhập liệu -->
</form>
```

Thuộc tính:

- `action`: URI nơi dữ liệu được gửi sau khi submit.
- `method`: giao thức gửi dữ liệu, gồm `GET` hoặc `POST`.

### 3. Phương thức GET

GET gửi thông tin người dùng bằng cách thêm dữ liệu vào cuối URL sau dấu `?`. Dữ liệu là chuỗi các cặp tên/giá trị, phân cách bằng dấu `&`.

Cấu trúc một biến:

```text
Name=value
```

Cấu trúc nhiều biến:

```text
Name1=value1&Name2=value2&Name3=value3
```

**Ví dụ:**

```text
Name=john&age=18
```

URL:

```text
http://www.information.com/text.php?Name=john&age=18
```

Nhận dữ liệu GET:

```php
$varname = $_GET["variable"];
```

Hạn chế của GET:

- Dữ liệu trên form bị giới hạn theo ASCII.
- Khối lượng dữ liệu chuyển giao bị giới hạn.
- Chiều dài chuỗi yêu cầu thường bị hạn chế, slide nêu 255 ký tự.

### 4. Phương thức POST

POST gửi thông tin người dùng qua nội dung HTTP request. POST có thể truyền nhiều thông tin hơn GET và thường dùng cho thao tác dữ liệu như thêm, sửa.

Nhận dữ liệu POST:

```php
$varname = $_POST["variable"];
```

Slide lưu ý rằng dữ liệu POST không được mã hóa mặc định, vì vậy vẫn cần quan tâm đến bảo mật.

### 5. So sánh GET và POST

| GET | POST |
|---|---|
| Dữ liệu form dạng cặp name/value được thêm vào URL | Dữ liệu gửi qua nội dung HTTP request |
| Có thể được đánh dấu URL | Không đánh dấu theo URL |
| Ít bảo mật vì dữ liệu hiển thị trên URL | Bảo mật hơn vì dữ liệu nằm trong thân request |
| Khối lượng dữ liệu giới hạn | Không giới hạn theo cách của GET |
| Dùng chủ yếu cho tìm kiếm, sắp xếp, phân trang | Dùng chủ yếu cho thêm, sửa dữ liệu |

### 6. Trường ẩn

Hidden field được nhúng trong HTML form để gửi biến từ form này sang form khác mà không yêu cầu người dùng nhập lại.

```html
<input type="hidden" name="hidden1" value="php message">
```

## Câu Lệnh Và Cấu Trúc Điều Khiển

Câu lệnh là phần tử nhỏ nhất trong ngôn ngữ lập trình. Câu lệnh có thể là câu lệnh đơn hoặc nhóm câu lệnh trong cặp `{}` và thường kết thúc bằng `;`.

Kịch bản PHP có thể gồm:

- Câu lệnh gán.
- Lời gọi hàm.
- Câu lệnh điều kiện.
- Câu lệnh trống.

### 1. Rẽ nhánh if-else

```php
if ($condition) {
    // câu lệnh khi đúng
} else {
    // câu lệnh khi sai
}
```

`else if` dùng khi có nhiều nhánh điều kiện.

### 2. Switch-case

```php
switch ($expression) {
    case $value1:
        // câu lệnh 1
        break;
    case $value2:
        // câu lệnh 2
        break;
    default:
        // câu lệnh mặc định
}
```

### 3. Vòng lặp

Vòng lặp thực thi một khối lệnh cần lặp lại. Khi điều kiện đúng, thân vòng lặp được thực hiện; khi điều kiện sai, vòng lặp kết thúc.

Vòng lặp `while` kiểm tra điều kiện trước:

```php
while ($condition) {
    // thân vòng lặp
}
```

Vòng lặp `do-while` kiểm tra điều kiện ở cuối và thực thi thân vòng lặp ít nhất một lần:

```php
do {
    // thân vòng lặp
} while ($condition);
```

Vòng lặp `for` dùng khi biết trước số lần lặp:

```php
for ($expr1; $expr2; $expr3) {
    // thân vòng lặp
}
```

Trong đó:

- `expr1`: biểu thức khởi tạo, thường khởi tạo biến đếm.
- `expr2`: biểu thức kiểm tra điều kiện.
- `expr3`: biểu thức thay đổi biến đếm.

Vòng lặp `foreach` dùng với mảng hoặc tập hợp đối tượng:

```php
foreach ($array as $value) {
    // xử lý $value
}
```

### 4. Câu lệnh nhảy

- `break`: dừng vòng lặp hoặc câu lệnh điều kiện, chuyển điều khiển đến sau vòng lặp hoặc sau lệnh điều kiện.
- `continue`: bỏ qua phần còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo.
- `exit`: kết thúc chương trình.

## Hàm Trong PHP

Hàm là tên của một đoạn chương trình dùng để thực thi nhiệm vụ cụ thể. Hàm giúp chia chương trình thành các chức năng, tái sử dụng mã lệnh và dễ chỉnh sửa chương trình.

### 1. Hàm có sẵn

Các nhóm hàm có sẵn trong PHP được nhắc đến:

- Hàm toán học.
- Hàm xử lý chuỗi.
- Hàm ngày và giờ.
- Hàm xử lý lỗi.

Hàm `time()` trả về số giây đã trôi qua từ nửa đêm ngày 1/1/1970. Hàm `getdate()` nhận một timestamp và trả về mảng liên hợp chứa thông tin ngày.

Hàm `die()` dừng hệ thống, không dịch tiếp nội dung PHP và trả về thông báo bên trong nó:

```php
die("Thông báo lỗi");
```

### 2. Hàm do người dùng tự định nghĩa

Cú pháp:

```php
function function_name($arg1, $arg2)
{
    // statement list
    return $expr;
}
```

`return` trả về giá trị cho hàm và dừng thực thi hàm.

### 3. Truyền tham số cho hàm

PHP hỗ trợ ba cách truyền tham số:

- Truyền tham trị.
- Truyền tham chiếu.
- Truyền giá trị mặc định.

Truyền tham chiếu dùng ký hiệu `&`:

```php
function changeValue(&$value)
{
    // thay đổi trực tiếp biến truyền vào
}
```

Giá trị mặc định:

```php
function hello($name = "PHP")
{
    return $name;
}
```

### 4. Hàm lồng nhau và đệ quy

Một hàm có thể gọi hàm khác. Thực thi một hàm bên trong một hàm khác gọi là hàm lồng nhau. Một hàm gọi đến chính nó được gọi là hàm đệ quy.

### 5. Biến trong hàm

Các loại biến được nhắc đến:

- Biến toàn cục.
- Biến cục bộ.
- Biến tĩnh.

## PHP Include Và Header

### 1. Include

Cú pháp:

```php
include('filename');
require('filename');
require_once('filename');
```

Slide ghi `Require_one`, nhưng trong PHP thường dùng `require_once`.

### 2. Hàm header

Hàm `header()` gửi một tiêu đề HTTP thô tới client. Hàm này phải được gọi trước khi bất kỳ đầu ra thực nào được gửi.

Cú pháp:

```php
header(string $string, bool $replace = true, int $http_response_code = 0);
```

Trong đó:

- `string`: chuỗi header được gửi.
- `replace`: có thay thế header trước đó hay không, mặc định là `true`.
- `http_response_code`: mã phản hồi HTTP.

## Mảng Trong PHP

Mảng là một biến có thể lưu trữ danh sách các biến được tham chiếu bởi một tên duy nhất. Mảng lưu trữ tập hợp các giá trị cùng kiểu dữ liệu.

Phân loại:

- Mảng một chiều.
- Mảng nhiều chiều.
- Mảng chỉ số.
- Mảng liên kết, associative array.

### 1. Khởi tạo mảng

Dùng hàm `array()`:

```php
$array_name = array([key1 =>] value1, [key2 =>] value2);
```

Trong đó:

- `$array_name`: tên mảng.
- `key`: chỉ số mảng, nếu không có thì mặc định là số từ 0.
- `value`: giá trị phần tử.

Định nghĩa một phần tử mảng:

```php
$array_name[$key] = "element_value";
```

### 2. Mảng associative

Mảng associative là mảng có chỉ số kiểu chuỗi.

```php
$cities = array(
    "ab" => "Hà Nội",
    "ac" => "Thái Bình",
    "aa" => "Thanh Hóa"
);
```

### 3. Trộn mảng

Hàm `array_merge()` dùng để gộp hai hoặc nhiều mảng:

```php
$merged_array_name = array_merge($first_array, $second_array);
```

### 4. Mảng nhiều chiều

Mảng nhiều chiều là mảng lưu trữ bên trong một mảng khác. Mỗi phần tử có thể là một mảng.

```php
$array_name = array(
    key1 => array(key => value),
    key2 => array(key => value)
);
```

### 5. Một số hàm liên quan đến mảng

Các nhóm hàm được nhắc đến:

- Hàm cơ bản.
- Hàm tìm kiếm và sắp xếp.
- Hàm tạo mảng và xử lý.

## Bài Tập

Các bài tập trong slide gồm:

- Viết hàm tính giai thừa dạng đệ quy và không đệ quy.
- Viết hàm kiểm tra số nguyên tố.
- Viết hàm đảo ngược chuỗi.
- Kiểm tra các ký tự trong chuỗi là chữ thường.
- Kiểm tra chuỗi ngày tháng nhập vào.
- Tính số ngày giữa hai chuỗi ngày tháng.
- Chuẩn hóa chuỗi văn bản.
- Khai báo, xử lý, trộn, sắp xếp và tìm kiếm trong mảng.
