# CHƯƠNG 5. MỘT SỐ KỸ THUẬT XỬ LÝ WEB

**NỘI DUNG CHÍNH:**
- Gửi mail trong PHP, PHPMailer và SMTP.
- Captcha và mã hóa mật khẩu bằng `md5`.
- `.htaccess`, Rewrite URL, Redirect và bảo mật.
- Một số ký hiệu Regular Expression và ký hiệu riêng trong `.htaccess`.
- Mô hình MVC, Model, View, Controller và cấu trúc project MVC.
- PHP Framework, Laravel, cấu hình Laravel và vòng đời request.
- AJAX và PDO trong PHP.

## Mail Trong PHP

PHP có hàm `mail()` sẵn có để gửi email. Tuy nhiên, slide lưu ý hàm `mail()` có thể bị khóa vì lý do bảo mật. Nếu mã nguồn PHP gặp vấn đề khi dùng hàm này, nên chuyển sang **PHPMailer** để gửi mail ổn định hơn và không phụ thuộc vào hàm `mail()`.

## PHPMailer Và SMTP

### 1. Tính năng của PHPMailer

PHPMailer có các tính năng:

- Gửi mail thông qua giao thức SMTP.
- Có thể dùng email cá nhân hoặc email công ty để gửi, tăng độ uy tín.
- Gửi mail nhanh, ít lỗi mail bị chuyển vào spam.
- Có thể thêm `cc`, `bcc`, đính kèm file.
- Có thể tương tác hai chiều, khi khách hàng trả lời mail thì nhận được trong hộp thư.

### 2. SMTP

SMTP là viết tắt của **Simple Mail Transfer Protocol**, nghĩa là giao thức truyền tải thư tín đơn giản. SMTP thực hiện nhiệm vụ chính là gửi mail. Việc nhận mail hoặc truy xuất dữ liệu mail server do các giao thức như IMAP hoặc POP3 đảm nhiệm.

### 3. Import PHPMailer

Theo slide, có thể import thư viện bằng cách:

1. Download thư viện và đưa vào thư mục website.
2. Dùng `include` hoặc `require` để import thư viện.

```php
<?php
require 'PHPMailer.php';
?>
```

### 4. Cấu hình Gmail

Slide nêu thao tác cấu hình tài khoản Gmail cho phép gửi mail:

1. Vào quản lý tài khoản Gmail.
2. Chọn `Security`.
3. Bật `Less secure app access`.

## Captcha Và Mã Hóa Mật Khẩu

### 1. Tạo mã captcha

Slide đưa mã PHP tạo captcha bằng session, `md5()`, thư viện ảnh và xuất ảnh PNG.

```php
<?php
session_start();
$string = md5(time());
$string = substr($string, 0, 6);
$_SESSION['captcha'] = $string;

$img = imagecreate(150, 50);
$background = imagecolorallocate($img, 0, 0, 0);
$text_color = imagecolorallocate($img, 255, 255, 255);

imagestring($img, 4, 40, 15, $string, $text_color);
header("Content-type: image/png");
imagepng($img);
imagedestroy($img);
?>
```

**Giải thích:** Mã trên tạo chuỗi từ `md5(time())`, lấy 6 ký tự đầu, lưu vào `$_SESSION['captcha']`, tạo ảnh nền đen, chữ trắng và xuất ảnh PNG.

### 2. Hàm `md5()`

Hàm `md5()` trong PHP mã hóa một chuỗi ký tự thành chuỗi 32 ký tự theo hàm băm MD5. Mỗi ký tự mã hóa được biểu diễn ở hệ cơ số 16, kích thước chuỗi mã hóa trả về là 128 bit.

Cú pháp:

```php
md5(string $string, bool $binary = false): string
```

Trong đó:

- `$string`: chuỗi cần mã hóa.
- `$binary`: tùy chọn, mặc định `false`; nếu `true` thì trả về chuỗi nhị phân đã mã hóa.

**Ví dụ:**

```php
<?php
$str = "gochocit.com";
$str = md5($str);
// 82f994e3d08ae2fe4c7785e31b364454

$str = md5($str, false);
?>
```

## `.htaccess`

### 1. Giới thiệu

File `.htaccess`, HyperText Access, là tệp cấu hình dùng bởi Web server Apache để cấu hình tùy chọn cho thư mục và file trên website. Nó cho phép quản trị website thiết lập quy tắc truy cập, cấu hình bảo mật, chuyển hướng, rewrite URL và nhiều tùy chọn khác.

`.htaccess` cho phép tùy chỉnh cấu hình ở cấp thư mục hoặc file cụ thể mà không cần can thiệp cấu hình toàn cục của Web server.

### 2. Ứng dụng phổ biến

- Điều hướng URL thân thiện, URL rewriting.
- Bảo mật thư mục.
- Chuyển hướng, redirect.
- Tùy chỉnh trang lỗi.
- Cấu hình cache, MIME types.

### 3. Cách tạo file `.htaccess`

1. Mở thư mục gốc website PHP, thường là `htdocs` hoặc `public_html`.
2. Tạo file tên chính xác `.htaccess`, không có tên file, chỉ có phần mở rộng.

Lưu ý:

- Một số hệ điều hành không cho tạo file bắt đầu bằng dấu chấm, cần bật hiển thị file ẩn.
- Trên Windows, dùng Notepad++ và `Save As` với tên `".htaccess"`.

### 4. Kích hoạt `.htaccess` trong Apache

Mở file cấu hình Apache, ví dụ trên XAMPP:

```text
C:\xampp\apache\conf\httpd.conf
```

Tìm dòng:

```apache
#LoadModule rewrite_module modules/mod_rewrite.so
```

Bỏ dấu `#` ở đầu. Tiếp theo tìm:

```apache
<Directory "C:/xampp/htdocs">
    AllowOverride None
</Directory>
```

Đổi thành:

```apache
<Directory "C:/xampp/htdocs">
    AllowOverride All
</Directory>
```

Sau đó khởi động lại Apache.

### 5. Kiểm tra `.htaccess`

Tạo file `.htaccess`:

```apache
# Bài test đầu tiên
Options -Indexes
```

`Options -Indexes` không cho phép hiển thị danh sách thư mục khi thư mục không có file `index.php`.

### 6. Một số lệnh cơ bản

File `.htaccess`:

- Có thể đặt ở thư mục gốc website hoặc thư mục con.
- Không viết theo ngôn ngữ lập trình mà dùng Regular Expression.
- Comment bằng dấu `#`.

```apache
RewriteEngine On
```

Bật chế độ rewrite.

```apache
ErrorDocument 404 http://www.example.com/404.html
```

Chuyển hướng khi gặp lỗi 404.

Một số lỗi:

- `404 - Not Found`.
- `401/403 - Unauthorized/Forbidden`.
- `400 - Bad Request`.
- `500 - Internal Server Error`.

## Rewrite URL

### 1. Cấu trúc RewriteRule

```apache
RewriteEngine On
RewriteRule [mẫu cần khớp] [đường dẫn thực tế] [tùy chọn]
```

Trong đó:

- `[mẫu cần khớp]`: đường dẫn muốn người dùng thấy.
- `[đường dẫn thực tế]`: file thực tế PHP sẽ xử lý.
- `[tùy chọn]`: ví dụ `L`, `R=301`.

### 2. Ví dụ URL thân thiện

Biến URL:

```text
http://localhost/myweb/tintuc
```

thành xử lý nội bộ:

```text
index.php?page=tintuc
```

```apache
RewriteEngine On
RewriteRule ^([a-zA-Z0-9_-]+)$ index.php?page=$1 [L]
```

**Giải thích:**

- `^` bắt đầu chuỗi và `$` kết thúc chuỗi.
- `[a-zA-Z0-9_-]+` chấp nhận chữ cái, số, gạch dưới, gạch ngang.
- `()` tạo capture group, dùng lại bằng `$1`.
- `index.php?page=$1` chuyển hướng nội bộ đến `index.php`.
- `[L]` dừng tại rule này nếu khớp.

### 3. Ví dụ route dạng controller/action

URL gốc:

```text
localhost/route_htaccess/home.php?trang=category&action=list
```

URL mong muốn:

```text
localhost/route_htaccess/category/list
```

Slide yêu cầu viết `.htaccess` thay thế đường dẫn.

### 4. Bài tập rewrite

Viết `.htaccess` rewrite:

```text
http://localhost/myweb/tintuc/123
```

thành:

```text
index.php?page=tintuc&id=123
```

File `.htaccess`:

```apache
RewriteEngine On
RewriteRule ^([a-zA-Z0-9_-]+)/([0-9]+)$ index.php?page=$1&id=$2 [L]
```

## Redirect

Redirect là chuyển hướng người dùng từ URL này sang URL khác tự động.

**Ví dụ:**

```text
http://example.com/old-page -> http://example.com/new-page
```

Cú pháp:

```apache
Redirect [mã trạng thái] [URL cũ] [URL mới]
```

Chuyển hướng vĩnh viễn:

```apache
Redirect 301 /old-page.html /new-page.html
```

### Chuyển HTTP sang HTTPS

Yêu cầu Web server có chứng chỉ SSL và HTTPS hoạt động.

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
```

**Giải thích:**

- `RewriteCond %{HTTPS} off`: nếu không phải HTTPS.
- `RewriteRule ^(.*)$`: bắt toàn bộ đường dẫn.
- `https://%{HTTP_HOST}/$1`: chuyển sang cùng host với HTTPS.
- `[R=301,L]`: chuyển vĩnh viễn và dừng xử lý rule.

## Bảo Mật Với `.htaccess`

### 1. Chặn truy cập thư mục

Tạo `.htaccess` trong thư mục cần chặn:

```apache
Deny from all
```

Khi người dùng truy cập trực tiếp vào thư mục, họ sẽ thấy `403 Forbidden`.

### 2. Chỉ cho phép một IP

```apache
Order Deny,Allow
Deny from all
Allow from 123.123.123.123
```

Người dùng không thuộc IP trên sẽ bị chặn.

## Ký Hiệu Regular Expression Trong `.htaccess`

| Ký hiệu | Ý nghĩa |
|---|---|
| `^` | Bắt đầu chuỗi |
| `$` | Kết thúc chuỗi |
| `.` | Đại diện một ký tự bất kỳ |
| `+` | 1 hoặc nhiều ký tự |
| `?` | 0 hoặc 1 ký tự |
| `*` | 0 hoặc nhiều ký tự |
| `()` | Gom nhóm biểu thức |
| `[^]` | Không thuộc danh sách |
| `|` | Hoặc |
| `\` | Escape ký tự đặc biệt |

**Ví dụ:**

```text
^[a-z]{10}$
^framgia$
^framgia[a-z]{2}
.{10,20}
[a-z]+
[a-z]*
[a-z]?
(a|b)
(framgia|viblo)
```

## Ký Hiệu Riêng Của `.htaccess`

| Ký hiệu | Ý nghĩa |
|---|---|
| `[F]` | Forbidden, trả lỗi 403 |
| `[L]` | Last rule, dừng rewrite |
| `[N]` | Next, tiếp tục rewrite đến rule kế tiếp |
| `[G]` | Gone, báo tài nguyên không còn tồn tại |
| `[P]` | Proxy |
| `[C]` | Chain |
| `[R]` | Redirect |
| `[NC]` | No-case, không phân biệt hoa thường |
| `[PT]` | Pass Through |
| `[OR]` | Toán tử điều kiện hoặc |
| `[NE]` | No Escape |
| `[NS]` | No Subrequest |
| `[QSA]` | Append Query String |
| `[S=x]` | Skip x rules tiếp theo |
| `[T=MIME-type]` | Khai báo MIME type |
| `-d` | Kiểm tra thư mục tồn tại |
| `-f` | Kiểm tra file tồn tại |
| `-s` | Kiểm tra file có giá trị khác 0 |

Một rule cơ bản:

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)$ index.php/$1 [L,QSA]
```

## Mô Hình MVC

MVC là mô hình thiết kế giúp tổ chức code thành các phần độc lập và tương tác theo cách nhất định. MVC gồm ba lớp:

- **Model:** quản lý dữ liệu, giao tiếp với CSDL, lưu trữ hoặc truy vấn dữ liệu.
- **View:** giao diện ứng dụng, biểu diễn dữ liệu thành dạng người dùng nhìn thấy.
- **Controller:** nhận request từ client, điều phối Model và View để tạo output phù hợp và trả kết quả cho người dùng.

### 1. Cấu trúc MVC trong slide

Thư mục `App` chứa:

- `Controllers`.
- `models`.
- `view`.

Các file và vai trò:

- `App.php`: xác định controller nào được gọi, action nào và tham số đi kèm.
- `.htaccess`: ghi đè đường dẫn trỏ về `index.php`.
- `Bootstrap.php` hoặc `routine.php`: file định tuyến.
- `routes.php`: thiết lập route mặc định là `home`.
- `Controller.php`: lớp cơ sở cho các controller, require model tương ứng và tạo đối tượng model.

### 2. Quy trình khi có request

1. Request được gửi đến ứng dụng.
2. `.htaccess` ghi đè mọi đường dẫn về `index.php`.
3. `index.php` gọi `bootstrap.php` để định tuyến.
4. Tạo đối tượng `App`.
5. `App.php` cắt URL để xác định controller, action và tham số.
6. Controller gọi model và view tương ứng.
7. View render dữ liệu trả về client.

## Framework PHP

Framework giúp phát triển website nhanh hơn bằng cách cung cấp nền tảng và các thành phần có sẵn.

Slide liệt kê 8 PHP framework:

1. Laravel.
2. CodeIgniter.
3. Symfony.
4. Zend.
5. Phalcon.
6. CakePHP.
7. Yii.
8. FuelPHP.

### 1. Laravel

Laravel giúp bắt đầu dự án web nhanh, có các chức năng như chứng thực người dùng và quản lý tác vụ. Laravel được xây dựng theo kiến trúc MVC.

### 2. CodeIgniter

CodeIgniter dễ học, tài liệu đầy đủ, hiệu năng tốt và phù hợp để tạo ứng dụng nhẹ chạy trên nhiều server.

Tính năng chính:

- Nền tảng nhẹ.
- Bắt đầu nhanh nhờ đơn giản và có tài liệu tốt.
- Tạo ứng dụng mở rộng cao nhờ MVC.

### 3. Symfony

Symfony linh hoạt, có hệ thống chức năng để chọn thành phần cần dùng hoặc dùng toàn bộ framework. Symfony có tích hợp kiểm thử hàm.

### 4. Zend

Zend là framework hướng đối tượng theo MVC, có thể sử dụng từng thành phần độc lập, tái sử dụng code và tích hợp thư viện bên thứ ba.

### 5. Phalcon

Phalcon có mã nguồn chính viết bằng C, hoạt động nhanh và ít tốn tài nguyên. Phalcon dùng kiến trúc MVC và cho phép thêm module, thư viện khi cần.

## Framework Laravel

### 1. Cài đặt Laravel

Bước 1: Download Composer:

```text
https://getcomposer.org/download/
```

Kiểm tra Composer:

```text
composer -v
```

Bước 2: Vào `htdocs`, mở PowerShell và chạy:

```text
composer create-project --prefer-dist laravel/laravel yourProject
```

Trong đó `yourProject` là tên dự án.

### 2. Chạy Laravel

Chạy qua thư mục `public`:

```text
PS C:\xampp\htdocs\Project_Laravel> cd public
PS C:\xampp\htdocs\Project_Laravel\public> php -S localhost:8080
```

Truy cập:

```text
localhost:8080
```

Hoặc dùng Artisan:

```text
PS C:\xampp\htdocs\Project_Laravel> php artisan serve
INFO  Server running on [http://127.0.0.1:8000]
```

Truy cập:

```text
localhost:8000
```

### 3. Cấu trúc Laravel

| Thành phần | Ý nghĩa |
|---|---|
| `.env` | Cấu hình môi trường, có thể ghi đè file config |
| `App` | Nơi viết app |
| `Console` | Code chạy trực tiếp trên console |
| `Exceptions` | File liên quan điều hướng lỗi |
| `Http/Controllers` | Chứa controller |
| `Http/Middleware` | Bộ lọc request |
| `Models` | Chứa class model |
| `Providers` | Khai báo service, trung tâm khởi tạo ứng dụng |
| `bootstrap` | Khởi động request |
| `config` | File cấu hình |
| `database/factories` | Định nghĩa dữ liệu mẫu |
| `database/migrations` | Tạo và chỉnh sửa dữ liệu |
| `database/seeds` | Tạo dữ liệu thêm vào CSDL |
| `public/index.php` | File chạy chính |
| `public/.htaccess` | Dùng với Apache |
| `resources/views` | Chứa view |
| `routes/web.php` | Route cho web |
| `routes/api.php` | Route cho API |
| `storage/logs` | Log lỗi |
| `vendor` | Core và thư viện |
| `artisan` | Hỗ trợ viết lệnh |

### 4. Vòng đời request Laravel

1. Request đến `public/index.php`.
2. Bootstrap chạy `app.php`.
3. Kernel tiền xử lý.
4. ServiceProviders khởi động.
5. Request đi qua `routes/web.php`.
6. Middleware lọc theo điều kiện xác thực.
7. Controller và action xử lý.
8. View trả kết quả về client.

### 5. Cấu hình Laravel

Laravel cần hai thư mục có quyền ghi:

- `bootstrap/cache`.
- `storage`.

Laravel cần `APP_KEY` để mã hóa cookie, session cookie và dữ liệu mã hóa khác. Nếu không có `APP_KEY`, ứng dụng không chạy đúng.

Tạo key:

```text
php artisan key:generate
```

Thiết lập timezone trong `config/app.php` tại khóa `timezone`.

Thiết lập môi trường:

- `APP_DEBUG=true`: hiển thị lỗi cụ thể khi phát triển.
- `APP_DEBUG=false`: hiển thị lỗi chung, chi tiết nằm trong `storage/logs`.
- `APP_ENV=local` hoặc `APP_ENV=production`.

Kiểm tra môi trường:

```text
php artisan env
```

Thiết lập CSDL trong `.env`, sau đó chạy migrations:

```text
php artisan migrate
```

## AJAX

AJAX được dùng để gửi dữ liệu đến server mà không cần tải lại trang, cập nhật một phần trang web hoặc kiểm tra dữ liệu đầu vào mà không gửi request toàn trang.

Các thành phần:

- HTML hoặc XHTML và CSS hiển thị dữ liệu.
- DOM thông qua JavaScript để hiển thị động và tương tác.
- `XMLHttpRequest` để trao đổi dữ liệu không đồng bộ với Web server.
- Dữ liệu truyền có thể là XML, HTML, plain text, JSON hoặc định dạng khác.

### 1. Ưu điểm AJAX

- Chỉ yêu cầu nội dung cần cập nhật, giảm băng thông và thời gian tải trang.
- Giảm kết nối đến server vì script và stylesheet chỉ cần yêu cầu một lần.
- Tăng tính tương tác của website.
- Dùng công nghệ sẵn có, dễ học và sử dụng.
- Được hỗ trợ trong các trình duyệt phổ biến.

### 2. Nhược điểm AJAX

- Khó bookmark trạng thái vì nhiều thao tác chạy ngầm.
- Nội dung động có thể khó hiển thị trên công cụ tìm kiếm.
- Nút back của trình duyệt có thể không hoạt động theo trạng thái AJAX.
- Nếu trình duyệt tắt JavaScript hoặc không hỗ trợ `XMLHttpRequest`, AJAX không chạy.
- Thiếu chuẩn cơ bản có thể gây khó trong kiểm thử.
- Có thể mở thêm hướng tấn công nếu không kiểm thử đầy đủ.

### 3. Các bước sử dụng AJAX

1. Xác định mục tiêu sử dụng AJAX.
2. Tạo đối tượng `XMLHttpRequest`.
3. Dùng `open()` xác định phương thức và URL.
4. Dùng `onreadystatechange` xác định hàm xử lý phản hồi.
5. Dùng `send()` gửi yêu cầu và dữ liệu.
6. Xử lý phản hồi từ server.
7. Hiển thị hoặc xử lý phản hồi trên trang.

## PDO Trong PHP

Slide cuối chương nhắc đến:

- Giới thiệu PDO trong PHP.
- Kết nối MySQL bằng PDO.
- Lợi ích khi sử dụng PDO.
- Prepared Statement với PDO.
- Thêm dữ liệu.
- Sửa dữ liệu.
- Xóa dữ liệu.

PDO là hướng kết nối CSDL được giới thiệu trong chương như một kỹ thuật làm việc với cơ sở dữ liệu bên cạnh MySQLi.
