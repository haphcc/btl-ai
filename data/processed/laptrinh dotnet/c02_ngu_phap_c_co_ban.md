### BÀI 4

#### C02 NGỮ PHÁP C# CƠ BẢN

## TRANG 1

## Chương 2

Ngữ pháp C# cơ bản

## TRANG 2

## Nội dung

1. Cấu trúc chương trình C#

2. Kiểu dữ liệu

3. Các thành phần điều khiển

4. Mảng

## Chương 2. Các thành phần cơ bản

23/05/2026 2/47 trong C#

## TRANG 3

1. Cấu trúc chương trình C#

//Vùng bắt đầu khai báo sử dụng các không gian tên using System;

using System.Collections. Generic;

using System.Text;

//Khai báo không gian tên của ứng dụng namespace my Console Application { //Vùng bắt đầu khai báo tên các Class class Program { //Vùng khai báo các phương thức static void Main(string[] args) { //Vùng khai báo lệnh } } }

## Chương 2. Các thành phần cơ bản

23/05/2026 3/47 trong C#

## TRANG 4

2. Không gian tên (namespace)

▪Nhóm các tính năng có liên quan của C# vào một loại ▪Cho phép dễ dàng tái sử dụng mã nguồn ▪Trong thư viện.NET framework có nhiều không gian tên ▪Phải tham chiếu tới để sử dụng

## Chương 2. Các thành phần cơ bản

23/05/2026 4/47 trong C#

## TRANG 5

Các namespace cơ bản

## Chương 2. Các thành phần cơ bản

23/05/2026 5/47 trong C#

## TRANG 6

Không gian tên

▪Khai báo sử dụng:

●Using &lt;tên namespace&gt;;

▪Tạo không gian tên:

●namespace &lt;Tên namespace&gt; {

&lt;Định nghĩa lớp A&gt;

&lt;Định nghĩa lớp B&gt;

….

}

## Chương 2. Các thành phần cơ bản

23/05/2026 6/47 trong C#

## TRANG 7

2. Kiểu dữ liệu

▪Phân loại kiểu dữ liệu

●Theo phương thức định nghĩa:

▪Có sẵn (Build-in)

▪Người dùng tự định nghĩa (user-defined)

●Theo cách thức lưu trữ

▪Giá trị (Value)

▪Tham chiếu (Reference)

## Chương 2. Các thành phần cơ bản

23/05/2026 7/47 trong C#

## TRANG 8

Kiểu dữ liệu

▪Kiểu dữ liệu có sẵn ●C# hỗ trợ một số kiểu dữ liệu có sẵn, mỗi kiểu dữ liệu này tương ứng với một kiểu dữ liệu hỗ trợ bởi hệ thống xác nhận ngôn ngữ chung CLS (Common Language System) trong MS.NET

●Việc ánh xạ các kiểu dữ liệu nguyên thủy của C# đến các kiểu dữ liệu của.NET sẽ đảm bảo các đối tượng được tạo ra trong C# có thể được sử dụng đồng thời với các đối tượng được tạo ra bởi bất cứ ngôn ngữ khác được biên dịch bởi.NET như VB.NET

●Mỗi kiểu dữ liệu có kích thước xác định

## Chương 2. Các thành phần cơ bản

23/05/2026 8/47 trong C#

## TRANG 9

Kiểu dữ liệu

## Chương 2. Các thành phần cơ bản

23/05/2026 9/47 trong C#

## TRANG 10

Kiểu dữ liệu

▪Kiểu giá trị (value type)

●Dữ liệu được lưu trữ trên vùng nhớ ngăn xếp (stack)

●Ví dụ: int, long, float… ▪Kiểu tham chiếu (reference type)

●Địa chỉ lưu trữ trong ngăn xếp (stack)

●Dữ liệu thực sự được lưu trữ trong vùng nhớ Heap

●Ví dụ: class, delegate, interface, object, string, dynamic

## Chương 2. Các thành phần cơ bản

23/05/2026 10/47 trong C#

## TRANG 11

Chuyển đổi các kiểu dữ liệu

▪Chuyển đổi ngầm định (implicity)

●Trình biên dịch tự động thực hiện, đảm bảo không bị mất mát dữ liệu

●Ví dụ: short x=5;

int y=x;

▪Chuyển đổi tường minh (explicity)

●Sử dụng toán tử chuyển kiểu

●Sử dụng các tiện ích

## Chương 2. Các thành phần cơ bản

23/05/2026 11/47 trong C#

## TRANG 12

Chuyển đổi các kiểu dữ liệu

▪ Chuyển đổi tường minh (explicity)

● Sử dụng toán tử chuyển kiểu (Casting)

● Sử dụng các tiện ích

▪ Parse: phương thức chuyển đổi một chuỗi sang một kiểu dữ liệu khác

int a = Int32.Parse(“123”); // a sẽ mang giá trị số 123

float b = Float.Parse(“20.7”); //b sẽ mang giá trị 20.7

bool c = Boolean.Parse(“true”); //c sẽ mang giá trị true

## Chương 2. Các thành phần cơ bản

23/05/2026 12/47 trong C#

## TRANG 13

Chuyển đổi các kiểu dữ liệu

●Sử dụng các tiện ích

▪Try Parse(chuỗi cần chuyển, out biến chứa giá trị đã được chuyển đổi)

Try Parse trả về giá trị true (nếu chuyển thành công) hoặc false (nếu chuyển không thành công - mặc định)

Ví dụ:

int a;

Int32.TryParse(“123”, out a); //a mang giá trị 123

bool b;

Boolean.TryParse(“false”,out b); //b sẽ mang giá trị false

▪Convert: lớp tiện ích cung cấp nhiều phương thức chuyển đổi kiểu

Ví dụ:

double d = Convert.ToInt32(“123”); //d mang giá trị 123

## Chương 2. Các thành phần cơ bản

23/05/2026 13/47 trong C#

## TRANG 14

Biến và hằng (Variable & Constant)

▪Biến (Variable)

●Một vùng nhớ có định kiểu

●Có thể gán và thay đổi giá trị

●Các biến phải được khởi gán trước khi sử dụng

int tuoi; Cú pháp:

[loại] kiểu_dữ_liệu tên_biến; float diem;

- loại: public, private, protected, static

double tien;

- kiểu_dữ_liệu: int, long, float….

string ten;

- Tên biến: theo nguyên tắc đặt tên

var tuoi =30

## Chương 2. Các thành phần cơ bản

23/05/2026 14/47 trong C#

## TRANG 15

Biến và hằng (Variable & Constant) ▪Hằng (Constant)

●Là biến nhưng giá trị không thể thay đổi sau khi khởi gán

●Cú pháp: &lt;const &gt; &lt;kiểu&gt; &lt;tên hằng&gt; = &lt;giá trị&gt;;

●Ví dụ: const int a = 100;

●Hằng bắt buộc phải được gán giá trị lúc khai báo

●Không được gán trị của hằng bằng giá trị của biến

## Chương 2. Các thành phần cơ bản

23/05/2026 15/47 trong C#

## TRANG 16

Khai báo biến kiểu ngầm định

var bien1 = 3.14; // biến sẽ có kiểu double

var bien2 = 3; // biến sẽ có kiểu int

var bien3 = ”cần khởi tạo giá trị"; // string

var bien4 = (5 < 4); // bool

## Chương 2. Các thành phần cơ bản

23/05/2026 16/47 trong C#

## TRANG 17

Kiểu liệt kê

▪Là tập hợp các tên hằng có giá trị không thay đổi (thường được gọi là danh sách liệt kê).

▪Cú pháp:[thuộc tính] [bổ sung] enum &lt;tên liệt kê&gt; [:kiểu cơ sở] {danh sách các thành phần liệt kê} ▪Ví dụ:

## Chương 2. Các thành phần cơ bản

23/05/2026 17/47 trong C#

## TRANG 18

Kiểu liệt kê

## Chương 2. Các thành phần cơ bản

23/05/2026 18/47 trong C#

## TRANG 19

Kiểu chuỗi kí tự (string)

▪Khai báo ●Ví dụ: string st = “hello”;

▪Sử dụng ●Sử dụng các các toán tử: == (bằng),!= (khác), + (nối chuỗi) ●Ví dụ:

string s1 = "hello ";

string s2 = "world";

Console. Write Line(s1+ s2); //”hello world” Console. Write Line(s1 + s2 == "hello world"); //True

## Chương 2. Các thành phần cơ bản

23/05/2026 19/47 trong C#

## TRANG 20

Cách đặt tên

▪Luôn luôn sử dụng 2 cách đặt tên là Camel Case hoặc Pascal Case

●Camel Case: Chữ cái đầu tiên của từ đầu tiên viết thường, các từ còn lại viết hoa chữ đầu

●Pascal Case: Viết hoa chữ cái đầu tiên của tất cả các từ ▪Không đặt tên các biến khai báo cùng tên nhau mà chỉ khác nhau ở chữ hoa và chữ thường ▪Không sử dụng tên bắt đầu với ký tự số ▪Không sử dụng tên kết thúc với ký tự số

## Chương 2. Các thành phần cơ bản

23/05/2026 20/47 trong C#

## TRANG 21

Cách đặt tên

▪Luôn luôn đặt tên có ý nghĩa cụ thể ▪Tránh sử dụng từ viết tắt trừ khi quá dài ▪Tránh viết tắt những từ nhỏ hơn 5 ký tự ▪Tránh đặt tên các biến hoặc hàm trùng với hàm hoặc biến mặc định của Framework

Ví dụ: string int, public system;

▪Không thêm các tiền tố hoặc hậu tố không có nghĩa

▪Sử dụng các tiền tố biến boolean bằng “Is”, “Can”, “Has”

## Chương 2. Các thành phần cơ bản

23/05/2026 21/47 trong C#

## TRANG 22

Toán tử trong C#

▪Toán tử số học: +, -, *, /, %, ^, ++, -- ▪Toán tử quan hệ: ==,!=, >, >=, <, <= ▪Toán tử logic: &&, ||,!

▪Toán tử gán: =, +=, -=, /=, *=, %= ▪Toán tử 3 ngôi:

(biểu thức điều kiện)? (biểu thức 1): (biểu thức 2)

Ví dụ: a = a&gt;b?a-b:b-a;

## Chương 2. Các thành phần cơ bản

23/05/2026 22/47 trong C#

## TRANG 23

Toán tử trong C# ▪Độ ưu tiên của toán tử

Loại toán tử Toán tử Tính kết hợp

Một ngôi -, ++, -- phải sang trái

Hai ngôi ^ trái sang phải

*, /, %

+, -

= phải sang trái ▪Thứ tự ưu tiên giữa các kiểu toán tử Thứ tự Kiểu toán tử

1 Số học

2 So sánh (quan hệ)

3 logic

## Chương 2. Các thành phần cơ bản

23/05/2026 23/47 trong C#

| Loại toán tử | Toán tử | Tính kết hợp |
| --- | --- | --- |
| Một ngôi | -, ++, -- | phải sang trái |
| Hai ngôi | ^ | trái sang phải |
|  | *, /, % |  |
|  | +, - |  |
|  | = | phải sang trái |

| Thứ tự | Kiểu toán tử |
| --- | --- |
| 1 | Số học |
| 2 | So sánh (quan hệ) |
| 3 | logic |

## TRANG 24

3. Các cấu trúc điều khiển

▪Câu lệnh:

●Chương trình C# là một dãy các câu lệnh (statements)

●Mỗi câu lệnh kết thúc bởi dấu “;”

●Các câu lệnh được xử lý tuần tự theo chiều từ trên xuống dưới (trừ trường hợp các lệnh nhảy, rẽ nhánh, lặp…) ▪Lệnh nhảy không điều kiện

●Có lời gọi một phương thức

●Sử dụng các lệnh nhảy không điều kiện: goto, break, continue, return, throw

## Chương 2. Các thành phần cơ bản

23/05/2026 24/47 trong C#

## TRANG 25

Lệnh nhảy có điều kiện (rẽ nhánh)

▪Rẽ nhánh chỉ được thực hiện khi điều kiện rẽ nhánh là đúng (true) ▪Câu lệnh if…else (có thể lồng nhau) ▪Câu lệnh chọn: switch…case

## Chương 2. Các thành phần cơ bản

23/05/2026 25/47 trong C#

## TRANG 26

Câu lệnh if…else

▪Cú pháp:

if (biểu thức điều kiện) &lt;công việc 1&gt;;

[else &lt;công việc 2&gt;;] ▪Thực hiện

Nếu biểu thức điều kiện là True thì Công việc 1 được thực hiện, ngược lại công việc 2 được thực hiện.

▪Ví dụ:

Nhập một số, cho biết tính chẵn lẻ của số vừa nhập

## Chương 2. Các thành phần cơ bản

23/05/2026 26/47 trong C#

## TRANG 27

Ví dụ câu lệnh if...else

using System;

using System.Collections. Generic;

using System.Text;

namespace If Else { class Program { static void Main(string[] args) { int n;

Console. Write("nhap so n:");

n = Convert.ToInt32(Console. Read Line());

if ((n % 2) == 0) Console. Write Line(n + " la so chan");

else Console. Write Line(n + " la so le");

Console. Read Line();

} } }

## Chương 2. Các thành phần cơ bản

23/05/2026 27/47 trong C#

## TRANG 28

Câu lệnh switch case

▪Cú pháp switch (biểu thức) { case giá_trị_1: {Các lệnh 1; break; } ...

case giá_trị_n: {Các lệnh n; break; } [default: Các lệnh n+1;] } ▪Thực hiện Biểu thức có giá trị 1, lệnh 1 thực hiện...

Mặc định, lệnh n+1 được thực hiện

## Chương 2. Các thành phần cơ bản

23/05/2026 28/47 trong C#

## TRANG 29

Ví dụ câu lệnh switch case ▪Nhập vào số nguyên, viết ra dạng chữ của số đó class Program { static void Main(string[] args) { int n;

Console. Write("nhap so n (0&lt;n&lt;4):");

n = Convert.ToInt32(Console. Read Line());

switch (n) { case 1: { Console. Write Line(n + ": mot"); break; } case 2: { Console. Write Line(n + ": hai"); break; } case 3: { Console. Write Line(n + ": ba"); break; } default:

{ Console. Write Line(n + " Khong biet do c"); break; } } Console. Read Line();

} }

## Chương 2. Các thành phần cơ bản

23/05/2026 29/47 trong C#

## TRANG 30

Câu lệnh lặp

▪Câu lệnh lặp for ▪Câu lệnh lặp while ▪Câu lệnh lặp do...while ▪Câu lệnh lặp foreach...in

## Chương 2. Các thành phần cơ bản

23/05/2026 30/47 trong C#

## TRANG 31

Câu lệnh lặp for

▪Cú pháp

for ([Khởi tạo]; [Biểu thức điều kiện]; [Bước lặp])

&lt;Câu lệnh&gt;;

▪Thực hiện B1. Thực hiện Khởi tạo

B2. Kiểm tra điều kiện

- Nếu đúng thực hiện Câu lệnh rồi Bước lặp và quay lại

B2.

- Nếu sai chuyển sang câu lệnh sau for

## Chương 2. Các thành phần cơ bản

23/05/2026 31/47 trong C#

## TRANG 32

Ví dụ câu lệnh for

▪Ví dụ: In ra màn hình 10 số nguyên dương đầu tiên using System;

using System.Collections. Generic;

using System. Linq;

using System.Text;

namespace for Statement { class Program { static void Main(string[] args) { Console. Write Line("10 so nguyen duong dau tien");

for (int i = 1; i <= 10; i++) Console. Write("{0} ", i);

Console. Read Line();

} } }

## Chương 2. Các thành phần cơ bản

23/05/2026 32/47 trong C#

## TRANG 33

Câu lệnh lặp while

▪Cú pháp while (biểu thức điều kiện) &lt;Công việc&gt;;

▪Ví dụ:

class Program { static void Main(string[] args) { Console. Write Line("10 so nguyen duong dau tien");

int i = 1;

while (i <= 10) { Console. Write("{0} ", i);

i++;

} Console. Read Line();

} }

## Chương 2. Các thành phần cơ bản

23/05/2026 33/47 trong C#

## TRANG 34

Câu lệnh lặp do...while

▪Cú pháp do &lt;công việc&gt; while &lt;biểu thức điều kiện&gt;;

▪Ví dụ:

class Program { static void Main(string[] args) { Console. Write Line("10 so nguyen duong dau tien");

int i = 1;

do { Console. Write("{0} ", i);

i++;

} while (i <= 10);

Console. Read Line();

} }

## Chương 2. Các thành phần cơ bản

23/05/2026 34/47 trong C#

## TRANG 35

Câu lệnh lặp foreach...in

▪Cho phép tạo vòng lặp thông qua một tập hợp hay một mảng ▪Cú pháp foreach(&lt;kiểu tập hợp&gt; &lt;tên truy cập thành phần&gt; in &lt;tên tập hợp&gt;) { &lt;Khối lệnh&gt;;

} ▪Thực hiện Số lần lặp Khối lệnh tương ứng bằng số lượng phần tử trong tập hợp

## Chương 2. Các thành phần cơ bản

23/05/2026 35/47 trong C#

## TRANG 36

Ví dụ câu lệnh lặp foreach…in

▪Tính tổng các phần tử trong mảng

## Chương 2. Các thành phần cơ bản

23/05/2026 36/47 trong C#

## TRANG 37

4. Mảng trong C#

▪Mảng là tập hữu hạn các phần tử có cùng kiểu dữ liệu ▪Khai báo &lt;kiểu dữ liệu&gt;[] &lt;tên mảng&gt; int[] so;

float[] diem;

string[] tenlop;

▪Cấp phát bộ nhớ cho mảng (dùng new)

[kiểu dữ liệu][] [tên mảng] = new [kiểu dữ liệu][tổng số phần tử] int [] so = new int[10];

float[] diem = new float[3];

## Chương 2. Các thành phần cơ bản

23/05/2026 37/47 trong C#

## TRANG 38

Mảng trong C#

▪Giá trị mặc định: mỗi thành phần sẽ chứa giá trị mặc định của kiểu dữ liệu

Ví dụ: int [] so = new int[5]; tạo một mảng gồm 5 số nguyên, mỗi thành phần giá trị mặc định là 0 ▪Khởi tạo thành phần của mảng ●Đặt các giá trị khởi tạo trong cặp dấu { } ●Ví dụ:

int[] my Int Array1 = new int[5]{2,4,6,8,10};

int[] my Int Array2 = {2,4,6,8,10};

## Chương 2. Các thành phần cơ bản

23/05/2026 38/47 trong C#

## TRANG 39

Mảng trong C#

▪Truy cập các thành phần trong mảng

●Dùng toán tử chỉ số []: &lt;tên mảng&gt;[chỉ số]

●Chỉ số phần tử đầu tiên là 0

●Ví dụ:

## Chương 2. Các thành phần cơ bản

23/05/2026 39/47 trong C#

## TRANG 40

Mảng trong C# ▪Ví dụ: Nhập mảng a gồm N phần tử, in mảng vừa nhập ra màn hình class Program { static void Main(string[] args) { int n, i;

int[] a;

Console. Write Line("Nhap so luong phan tu: ");

n = Convert.ToInt32(Console. Read Line());

a = new int[n];

for (i = 0; i < n; i++) { Console. Write Line("Nhap phan tu thu {0}: ", i);

a[i] = convert. Toint32(Console. Read Line());

} Console. Write Line("Mang vua nhap la: ");

for (i = 0; i < n; i++) { Console. Write("{0} ", a[i]);

} Console. Read Line();

} }

## Chương 2. Các thành phần cơ bản

23/05/2026 40/47 trong C#

## TRANG 41

Mảng trong C# ▪Ngôn ngữC# cung cấp cú pháp chuẩn cho việc khai báo những đối tượng Array

## Chương 2. Các thành phần cơ bản trong C#23/05/2026 41/47

## TRANG 42

Mảng trong C#

## Chương 2. Các thành phần cơ bản

23/05/2026 42/47 trong C#

## TRANG 43

## Bài tập về nhà

▪Bài 1. Viết chương trình nhập 2 số thực a và b.

Tính tổng, hiệu, tích, thương của 2 số đó.

▪Bài 2. Viết chương trình giải và biện luận phương trình bậc nhất ax + b = 0 ▪Bài 3. Viết chương trình nhập vào 3 số a, b, c.

Kiểm tra xem 3 số đó có thoả mãn 3 cạnh của tam giác? Nếu thoả mãn tính chu vi và diện tích của tam giác đó.

## Chương 2. Các thành phần cơ bản

23/05/2026 43/47 trong C#

## TRANG 44

## Bài tập về nhà

▪Bài 4. Viết chương trình nhập vào từ bàn phím dãy gồm N số nguyên. Sắp xếp dãy theo chiều tăng dần và in kết quả ra màn hình.

▪Bài 5. Viết chương trình sinh ra một số ngẫu nhiên có giá trị nằm trong khoảng [0,20], sau đó cho phép người dùng đoán giá trị ngẫu nhiên đó 7 lần, nếu sau 7 lần vẫn chưa đoán được sẽ thông báo người dùng bị thua cuộc

## Chương 2. Các thành phần cơ bản

23/05/2026 44/47 trong C#
