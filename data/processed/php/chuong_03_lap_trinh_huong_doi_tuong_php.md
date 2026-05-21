# CHƯƠNG 3. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG PHP

**NỘI DUNG CHÍNH:**
- Giới thiệu lập trình hướng đối tượng trong PHP.
- Lớp, đối tượng, thuộc tính và phương thức.
- `$this`, `new` và toán tử `->`.
- Kế thừa, ghi đè, hàm tạo và hàm hủy.
- Phạm vi truy cập `public`, `private`, `protected`.
- Interface, abstract class, static và final.
- Ứng dụng xây dựng lớp xử lý truy xuất cơ sở dữ liệu.

## Giới Thiệu OOP Trong PHP

Lập trình hướng đối tượng, **Object-Oriented Programming - OOP**, là mô hình lập trình dựa trên khái niệm đối tượng. Trong PHP, OOP giúp tổ chức mã nguồn tốt hơn, tái sử dụng code dễ dàng hơn và cải thiện khả năng bảo trì hệ thống.

PHP có mô hình đối tượng hoàn chỉnh, bao gồm các tính năng như khả năng hiển thị, lớp và phương thức trừu tượng, phương thức, giao diện và nhân bản.

Các khái niệm cơ bản:

- Đối tượng, object.
- Lớp, class.
- Trừu tượng hóa, abstract.
- Đóng gói, encapsulation.
- Đa hình, polymorphism.
- Kế thừa, inherit.

## Lớp Và Đối Tượng

### 1. Lớp

Lớp là khuôn mẫu để tạo ra đối tượng. Slide đưa ra cú pháp tổng quát:

```php
class class_name
{
    function function_name($var1, $var2)
    {
        // nội dung phương thức
    }
}
```

### 2. Đối tượng và thể hiện của lớp

Đối tượng là thể hiện cụ thể của một lớp. Khai báo đối tượng dùng từ khóa `new`.

```php
$ten_doi_tuong = new TenLop();
```

Truy cập thành phần của lớp thông qua đối tượng bằng toán tử `->`:

```php
$ten_doi_tuong->ten_thanh_phan;
```

Con trỏ `$this` dùng bên trong lớp để truy cập thành phần của chính đối tượng hiện tại:

```php
$this->thanh_phan;
```

## Thuộc Tính Và Phương Thức

Thuộc tính và phương thức của lớp tồn tại trong các không gian tên riêng biệt. Vì vậy, một lớp có thể có một thuộc tính và một phương thức cùng tên. Việc truy cập thuộc tính hay gọi phương thức phụ thuộc vào ngữ cảnh sử dụng.

### 1. Thuộc tính

Các biến thành viên của lớp được gọi là thuộc tính. Thuộc tính có thể được định nghĩa bằng các từ khóa visibility, `static`, `readonly`, sau đó là khai báo kiểu và khai báo biến.

Khai báo thuộc tính có thể bao gồm giá trị khởi tạo, nhưng giá trị khởi tạo phải là giá trị hằng.

Truy cập thuộc tính thường dùng toán tử `->`. Thuộc tính tĩnh truy cập bằng `::` với từ khóa `self`.

```php
class Product
{
    public string $name = "PHP";
    public static int $count = 0;
}

$p = new Product();
echo $p->name;

echo Product::$count;
```

### 2. Phương thức

Phương thức là hàm được khai báo trong lớp. Phương thức xử lý hành vi của đối tượng.

```php
class Product
{
    public function showName()
    {
        return $this->name;
    }
}
```

### 3. Hàm ẩn danh trong thuộc tính

Slide có nhắc đến việc lưu hàm ẩn danh trong thuộc tính của lớp. Đây là cách gán một hàm không tên vào thuộc tính để gọi khi cần.

```php
$object->handler = function () {
    // xử lý
};
```

## Lớp ReadOnly Và Chỉ Thị `::class`

### 1. Lớp ReadOnly

Từ PHP 8, lớp có thể được đánh dấu là lớp chỉ đọc. Điều này thiết lập tất cả thuộc tính được khai báo trong lớp ở dạng chỉ đọc và ngăn việc tạo thuộc tính động. Với lớp readonly, không thể khai báo thuộc tính tĩnh trong nó.

### 2. Chỉ thị `::class`

Chỉ thị `::class` trả về tên lớp và namespace chứa nó theo dạng:

```text
Ns\ClassName
```

Chỉ thị này cũng có thể dùng để trả về tên lớp của đối tượng.

## Kế Thừa

Một lớp có thể kế thừa hằng số, phương thức và thuộc tính của lớp khác bằng từ khóa `extends`.

```php
class ChildClass extends ParentClass
{
    // nội dung lớp con
}
```

Các lưu ý:

- PHP không hỗ trợ kế thừa nhiều lớp; một lớp chỉ kế thừa từ một lớp cơ sở.
- Hằng số, phương thức và thuộc tính kế thừa có thể được ghi đè bằng cách khai báo lại cùng tên trong lớp con.
- Nếu lớp cha định nghĩa phương thức hoặc hằng số là `final`, lớp con không được ghi đè.

### Sự tương thích khi ghi đè phương thức

Slide lưu ý rằng phương thức con loại bỏ một tham số hoặc bắt buộc một tham số tùy chọn là không tương thích với phương thức gốc. Khi ghi đè, cần giữ tương thích chữ ký phương thức.

## Hàm Tạo Và Hàm Hủy

### 1. Hàm tạo

Hàm tạo dùng để khởi tạo các thành phần của lớp khi khai báo đối tượng. Trong PHP, hàm tạo dùng phương thức `__construct()`.

```php
class User
{
    public function __construct()
    {
        // khởi tạo
    }
}
```

Cú pháp theo slide:

```php
function __construct([args]): void
{
    // nội dung hàm tạo
}
```

Hàm tạo được gọi khi khai báo và khởi tạo đối tượng của lớp.

Hàm tạo có thể có tham số:

```php
class User
{
    public function __construct($name)
    {
        $this->name = $name;
    }
}
```

### 2. Hàm hủy

PHP có khái niệm hàm hủy tương tự các ngôn ngữ hướng đối tượng khác như C++. Phương thức hủy được gọi khi không còn tham chiếu đến đối tượng hoặc trong trình tự tắt máy.

```php
__destruct(): void
```

Ví dụ dạng cú pháp:

```php
class User
{
    public function __destruct()
    {
        // giải phóng tài nguyên
    }
}
```

## Phạm Vi Truy Cập

PHP có ba phạm vi truy cập:

- `private`.
- `public`.
- `protected`.

Mặc định là `public`.

Ý nghĩa:

- `public`: có thể truy cập từ bên ngoài lớp.
- `private`: chỉ truy cập trong chính lớp khai báo.
- `protected`: truy cập trong lớp khai báo và lớp kế thừa.

```php
class User
{
    public $name;
    private $password;
    protected $role;
}
```

## Interface

PHP cho phép định nghĩa interface với các thành viên kiểu `public`. Các lớp có thể thực thi interface bằng từ khóa `implements`.

```php
interface Logger
{
    public function write($message);
}

class FileLogger implements Logger
{
    public function write($message)
    {
        // ghi log
    }
}
```

Interface giúp quy định các phương thức mà lớp triển khai phải định nghĩa.

## Lớp Trừu Tượng

Lớp trừu tượng là lớp không thể được khởi tạo, chỉ được kế thừa. Trong PHP, khai báo lớp trừu tượng bằng từ khóa `abstract`.

```php
abstract class BaseController
{
    abstract public function index();
}
```

Khi kế thừa từ lớp trừu tượng, tất cả phương thức được đánh dấu `abstract` trong lớp cha phải được định nghĩa bởi lớp con. Các phương thức này phải được định nghĩa với cùng tính nhìn thấy.

```php
class HomeController extends BaseController
{
    public function index()
    {
        // xử lý trang chủ
    }
}
```

## Static

Khai báo thành viên hoặc phương thức là `static` cho phép truy cập chúng mà không cần khởi tạo lớp.

Một thành viên `static` không thể truy cập bằng đối tượng đã khởi tạo như thuộc tính thường. Phương thức `static` có thể được gọi qua tên lớp.

```php
class Counter
{
    public static $count = 0;

    public static function increase()
    {
        self::$count++;
    }
}

Counter::increase();
echo Counter::$count;
```

## Final

PHP 5 giới thiệu từ khóa `final`. Từ khóa này ngăn lớp con ghi đè phương thức khi đặt trước định nghĩa phương thức. Nếu chính lớp được khai báo là `final`, lớp đó không thể được kế thừa.

```php
class ParentClass
{
    final public function run()
    {
        // không được ghi đè
    }
}
```

```php
final class FinalClass
{
    // không thể kế thừa lớp này
}
```

## Ứng Dụng Xây Dựng Lớp Xử Lý Truy Xuất CSDL

Slide kết thúc bằng hướng ứng dụng OOP để xây dựng các lớp xử lý truy xuất cơ sở dữ liệu. Cấu trúc được nêu gồm:

- Lớp kết nối CSDL.
- Lớp truy xuất dữ liệu.
- Ứng dụng.

Cách tổ chức này giúp tách phần kết nối, phần thao tác dữ liệu và phần sử dụng trong ứng dụng, phù hợp với tinh thần tổ chức mã nguồn của OOP.
