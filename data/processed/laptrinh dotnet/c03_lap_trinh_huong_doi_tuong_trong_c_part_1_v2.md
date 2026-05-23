### BÀI 5

#### C03 LAP TRINH HUONG DO I TUONG TRONG C# PART 1 V2

## HỌC VIỆN NGÂN HÀNG

## KHOA CÔNG NGHỆ THÔNG TIN VÀ KINH TẾ SỐ

## Chương 3

## LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG

## TRONG C#

## Nội dung chương 3

1 Lớp và đối tượng

2 Kế thừa và đa hình

3 Mảng

4 Danh sách

5 Sử dụng Generic

6 Xử lý ngoại lệ

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 2/33

3.1. Lớp và đối tượng

1 Định nghĩa lớp, đối tượng

2 Phương thức khởi tạo, hủy đối tượng

3 Truy ền tham số

4 Biểu thức Lamda

23/05/2026

3.1.1 Định nghĩa lớp và đối

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 4/33

Định nghĩa lớp và đối tượng

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 5/33

3.1.1 Định nghĩa lớp, đối tượng

 Người ta gộp tất cả các đối tượng cùng chung thuộc tính, phương thức thành 1 lớp.

 Một lớp là một kiểu mẫu chung cho các đối tượng thuộc cùng một loại.

 Lớp là một kiểu dữ liệu để tạo ra các đối tượng.

 Cú pháp:

[phạm vi truy cập] [thuộc tính] class &lt;tên lớp&gt; { //Khai báo các thuộc tính //Khai báo các phương thức } [phạm vi truy cập]: khả năng truy nhập thành phần dữ liệu (public, private, internal, protected, internal protected) [thuộc tính]: có thểl à static

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 6/33

Đối tượng (Object)

Đối tượng” là gì?

◼ là một người, địa điểm, sự kiện, sựv ật … Ví dụ: Đối tượng trong thếgi ới thực: Khách hàng sử dụng thẻATM ◼ Thông tin cá nhân: tên, tuổi, số tài khoản, lượng tiền đang có trong tài khoản… ◼ Hoạt động: Đăng ký làm thẻ, huỷth ẻ, rút tiền, nạp tiền…

23/05/2026 Chương 1. Tổng quan về lập trình hướng đối tượng và 7/46 ngôn ngữC#

Đối tượng trong thế giới thực

Một đối tượng trong thếgi ới thực là một thực thểc ụth ểm à thông thường chúng ta có thểs ờ, nhìn thấy hay cảm nhận được

Trạng thái Hành động Đối tượng có:

Con chó Tên Sủa trạng thái (state) Màu Vẩy tai và hành động Giống Chạy (behavior) ăn Xe đạp Bánh xe Tăng tốc Bàn đạp Giảm tốc Dây xích Chuyển bánh răng

23/05/2026 Chương 1. Tổng quan về lập trình hướng đối tượng và 8/46 ngôn ngữC#

|  | Trạng thái | Hành động |
| --- | --- | --- |
| Con chó | Tên
Màu
Giống | Sủa
Vẩy tai
Chạy
ăn |
| Xe đạp | Bánh xe
Bàn đạp
Dây xích | Tăng tốc
Giảm tốc
Chuyển bánh răng |

Đối tượng phần mềm

Các đối tượng phần mềm có thểđược dùng đểbi ểu diễn các đối tượng trong thếgi ới thực Cũng có trạng thái và hành động ◼ Trạng thái: thuộc tính (attribute, property) ◼ Hành động: Phương thức (method) Đối tượng (object) là một thực thể phần mềm bao bọc thuộc tính và các phương thức liên quan Có trạng thái và hành động Thuộc tính ◼ Trạng thái: Thuộc tính (attribute, property) ◼ Hành động: Phương thức (method) ◼ Thuộc tính được xác định bởi các giá trị gọi là thuộc tính thể hiện Các đối tượng giao tiếp với nhau bằng các thông điệp

Phương thức 23/05/2026 Chương 1. Tổng quan về lập trình hướng đối tượng và 9/46 ngôn ngữC#

Quản lý thư viện

Sinh viên mượn sách ◼ class Sinh viên{ string Ho Ten SV string Ma SV void Nhap() void Nhap (string masv, string tensinhvien) Muon (Sach q1) } class Sach{ string Ma Sach string Ten Sach string Nam Xuat Ban void Nhap (string ma, string ten, int namxuatban) } 23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 10/33

Phạm vi truy nhập

public Có thể được truy xuất bởi bất cứ phương thức của lớp nào khác

private Chỉ có thể truy xuất bởi các phương thức của chính lớp đó

protected Có thể được truy xuất bởi các phương thức của chính lớp đó và các lớp dẫn xuất (derived) từ nó

internal Có thể được truy xuất bởi các phương thức của các lớp trong cùng khối kết hợp (assembly)

internal Có thể được truy xuất bởi các phương thức của protected lớp đó, lớp dẫn xuất từ lớp đó và các lớp trong cùng khối kết hợp (assembly) với nó

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 11/33

| public | Có thể được truy xuất bởi bất cứ phương thức
của lớp nào khác |
| --- | --- |
| private | Chỉ có thể truy xuất bởi các phương thức của
chính lớp đó |
| protected | Có thể được truy xuất bởi các phương thức của
chính lớp đó và các lớp dẫn xuất (derived) từ nó |
| internal | Có thể được truy xuất bởi các phương thức của
các lớp trong cùng khối kết hợp (assembly) |
| internal
protected | Có thể được truy xuất bởi các phương thức của
lớp đó, lớp dẫn xuất từ lớp đó và các lớp trong
cùng khối kết hợp (assembly) với nó |

Ví dụ - Lớp hình chữ nhật

class HCN { private float Dai, Rong;

public float Chu Vi() { return (Dai + Rong)*2;

} public float Dien Tich() { return Dai* Rong;

} public void Nhap() { Console. Write Line("Nhap chieu dai: ");

Dai = float. Parse(Console. Read Line());

Console. Write Line("Nhap chieu rong: ");

Rong = float. Parse(Console. Read Line());

} public void Xuat(){ // Tựvi ết }

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 12/33

Chú ý

Các thành phần dữ liệu xem như biến toàn cục đối với các phương thức của lớp (các phương thức của lớp có quyền truy cập đến các thành phần này mà không cần khai báo lại) Mặc định, mức độtruy cập là private Các lớp thuộc cùng một project có thể xem là cùng một khối kết hợp (assembly)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 13/33

Khai báo đối tượng

Cú pháp: Sử dụng từkho á new &lt;tên lớp&gt; &lt;tên đối tượng&gt;;

&lt;tên đối tượng&gt; = new &lt;tên lớp&gt;([các giá trịkh ởi tạo nếu có]);

Hoặc:

&lt;tên lớp&gt; &lt;tên đối tượng&gt; = new &lt;tên lớp&gt;([các giá trịkh ởi tạo nếu có]);

Chú ý ◼ Sau khi khai báo biến đối tượng thì biến đó chỉl à một con trỏ ◼ Sau khi cấp phát bằng từkho á new thì biến trỏ tới một đối tượng thực sự

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 14/33

Truy cập thuộc tính/phương thức

Truy cập thuộc tính ◼ &lt;tên đối tượng&gt;.&lt;tên thuộc tính&gt; Truy cập phương thức ◼ &lt;tên đối tượng&gt;.&lt;tên phương thức&gt;([danh sách đối số nếu có]) Ví dụ:

◼ Tạo đối tượng hình chữnh ật h internal class Program { static void Main(string[] args) {

## HCN h;

h = new HCN();

h. Nhap();

h. Xuat();

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 15/33

## Bài tập 1

Hãy tạo lớp Sinh Vien:

◼ Thuộc tính private: ma SV, ten SV ◼ Phương thức public: Nhap(), Xuat() ◼ Từh àm Main của lớp Program hãy tạo một đối tượng Sinh Vien, thực hiện nhập/xuất thông tin của sinh viên đó

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 16/33

Thuộc tính/phương thức tĩnh static

 Thuộc tính static là thuộc tính thuộc về lớp (class) chứ không thuộc về riêng một đối tượng (instance). Tất cả các đối tượng của lớp đều chia sẻ cùng một bản sao của thuộc tính này.

class Sinh Vien { public static String Ten Truong = “Học viện Ngân hàng”;

} Phương thức static là một phương thức được gọi mà không cần tạo ra một đối tượng của lớp. Nó chỉcó thểtruy cập các thành viên static trong lớp class Sinh Vien { public static void Say Hello() { Console. Write Line("Hello, world!, I am from “ + Ten Truong);

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 17/33

Phương thức khởi tạo, huỷ đối tượng

Khởi tạo đối tượng → Gọi phương thức tạo lập (constructor) ◼ Được gọi đến 1 cách tựđộng khi đối tượng của lớp được tạo ra. Dùng đểkh ởi tạo giá trịđầu cho các thành phần dữ liệu của đối tượng thuộc lớp.

◼ Phương thức tạo lập mặc định: được CLR cung cấp nếu người lập trình không định nghĩa ◼ Phương thức tạo lập do người lập trình định nghĩa ◼ Trước khi phương thức tạo lập được chạy, đối tượng chưa thực sựt ồn tại trong bộnh ớ, sau khi tạo lập hoàn thành, bộ nhớl ưu trữmột thểhiện của lớp.

◼ Khi ta không định nghĩa một phương thức tạo lập nào cho lớp, trình biên dịch sẽt ựđộng tạo một phương thức tạo lập mặc định cho lớp đó và khởi tạo các biến bằng các giá trị mặc định.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 18/33

3.1.2 Phương thức khởi tạo, huỷ đối tượng

Có 2 loại phương thức khởi tạo:

Phương thức khởi tạo không tham số:

✓Là phương thức khởi tạo không có bất kỳ tham số truy ền vào nào.

✓Thường dùng để khởi tạo các giá trị mặc định cho các thuộc tính bên trong class khi khởi tạo đối tượng.

Phương thức khởi tạo có tham số:

✓Là phương thức khởi tạo có tham số truy ền vào. Và khi khởi tạo đối tượng để phương thức này được gọi ta cần truy ền đầy đủ các tham số.

✓Thường dùng để khởi tạo các giá trị cho các thuộc thuộc tính bên trong class khi khởi tạo đối tượng (các giá trị này do người khởi tạo đối tượng truy ền vào).

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 19/33

Phương thức khởi tạo mặc định

Khi tạo đối tượng của lớp mà không khai báo phương thức khởi tạo (constructor), C# sẽ tự động cung cấp một phương thức khởi tạo mặc định (default constructor).

Phương thức khởi tạo mặc định này không có tham số và sẽ tự động khởi tạo các thuộc tính của đối tượng với các giá trị mặc định.

Kiểu dữ liệu Giá trị mặc định

Numeric (int, long,…) 0

bool false

char ‘\0’ (null)

reference null

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 20/33

| Kiểu dữ liệu | Giá trị mặc định |
| --- | --- |
| Numeric (int, long,…) | 0 |
| bool | false |
| char | ‘\0’ (null) |
| reference | null |

Xây dựng phương thức khởi tạo

Phương thức khởi tạo có tên trùng với tên lớp, không có kiểu trảvề, phạm vi truy cập thường là public Có thểcó nhiều phương thức khởi tạo trong cùng lớp Phương thức khởi tạo có thểcó tham số ho ặc không ◼ Ví dụ:

public class_name() public class_name(danh sách tham số)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 21/33

Ví dụ - Phương thức khởi tạo

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 22/33

3.1.2. Phương thức huỷ (destructor)

 Phương thức hủy (destructor) được sử dụng để dọn dẹp tài nguyên hoặc thực hiện các công việc cần thiết khi đối tượng bị hủy và bị xóa khỏi bộ nhớ. Phương thức hủy cũng có cùng tên với tên lớp tuy nhiên phía trước có dấu “~”.

❑ Đặc điểm của phương thức hủy như sau:

✓ Phương thức hủy không cho phép kế thừa và không cho phép nạp chồng ✓ Phương thức hủy không được gọi tường minh ✓ Phương thức hủy không có phạm vi truy cập và không có tham số truy ền vào  Cú pháp: ~&lt;tên lớp&gt;()

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 23/33

3.1.2. Phương thức huỷ (destructor)

 C# có cơ chết ựđộng thu gom rác (garbage collector) →người lập trình không phải huỷđ ối tượng một cách tường minh  Bộ thu gom rác tựđộng gọi phương thức huỷ

public class HCN { // Thuộc tính public double Dai;

public double Rong;

// Phương thức hủy

## ~HCN()

{ Console. Write Line("Phương thức hủy được gọi. Đối tượng HCN đã bị hủy.");

} } //// class Program { static void Main() { // Tạo đối tượng Hinh Chu Nhat HCN hcn1 = new HCN ();

} 23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 24/33

Từ khoá this

 Từkho á this trỏđ ến thểhiện hiện tại (current instance) của đối tượng Trước khi tìm hiểu từkh óa this là gì, giảsửch úng ta cho tham số của hàm xây dựng cùng tên với dữ liệu thành viên của lớp

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 25/33

Từ khoá this

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 26/33

3.1.3. Truy ền tham số

Trong lập trình C#, có hai loại truy ền tham số vào hàm:

• Truy ền tham trị: một bản sao của biến sẽ được tạo ra, sao chép giá trị của biến, truy ền biến đã được sao chép này vào hàm, dù có thực hiện bao nhiêu phép tính toán cũng không ảnh hưởng đến biến gốc • Truy ền tham chiếu: truy ền ngay địa chỉ của biến được lưu trên bộ nhớ vào hàm (hay hiểu cách khác là truy ền chính biến đó vào hàm) khi thực hiện tính toán thì giá trị biến này thay đổi theo. ref vàout là hai từkh óa dùng để truy ền tham chiếu vào hàm.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 27/33

3.1.3 Truy ền tham số

Ví dụtruy ền tham trị:

//Phương thức đổi chỗ 2 số, truy ền tham trị static void Swap1(int a, int b) { int temp;

temp=a;

a=b;

b=temp;

} →int x=10; int y = 20; Swap1 (x,y) →giá trị của x vày =?

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 28/33

Truy ền tham chiếu

C# hỗtr ợtruy ền tham chiếu, sử dụng các từ khoá:

◼ ref: truy ền tham chiếu, biến được tham chiếu phải được khởi tạo trước khi truy ền ◼ out: truy ền tham chiếu, biến được tham chiếu không cần khởi gán trước khi truy ền. Trong phương thức phải có lệnh gán giá trịcho các biến tham chiếu này.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 29/33

Ví dụ - truy ền tham chiếu, từ khoá ref

//Phương thức đổi chỗ 2 số, truy ền tham chiếu, từ khoá ref static void Swap2(ref int a, ref int b) { int temp;

temp = a;

a = b;

b = temp;

Console. Write Line("Trong phuong thuc: a={0}, b={1},",a,b);

} static void Main(string[] args) { int n,m;

n = 30; m = 40;

Console. Write Line("Truoc khi goi swap2: n = {0}, m={1},", n, m);

Swap2(ref n, ref m);

Console. Write Line("Sau khi goi swap2: n = {0}, m = {1},", n, m);

Console. Read Line();

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 30/33

Ví dụ - truy ền tham chiếu, từ khoá out

//Phương thức thay đổi giá trị, sử dụng truy ền tham chiếu, từ khoá out static void Change(out int a, out int b) { a = 100;

b = 200;

Console. Write Line("Trong phuong thuc: a={0},b={1},", a, b);

} static void Main(string[] args) { int n,m;

Change (out n, out m);

Console. Write Line("Sau khi goi Change: n={0}, m={1},",n, m);

Console. Read Line();

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 31/33

3.1.4 Biểu thức lamda

Biểu thức lambda trong C# là một cách ngắn gọn để định nghĩa một hàm vô danh (không có tên) ngay trong mã mà không cần phải khai báo một phương thức riêng biệt.

Lambda rất hữu ích khi cần một hàm đơn giản, đặc biệt khi làm việc với các API như LINQ hoặc các phương thức yêu cầu hành động như sắp xếp hoặc lọc dữ liệu.

Cấu trúc cơ bản của biểu thức lambda:

✓Sử dụng toán tử=&gt; (các_tham_số) =&gt; biểu_th ức;

✓Một cấu trúc lệnh sau toán tử=&gt;

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 32/33

3.1.4 Biểu thức lamda

Các loại biểu thức lambda:

 Biểu thức lambda với một tham số: Nếu chỉ có một tham số, có thể bỏ qua dấu ngoặc đơn.

var square = x =&gt; x * x;

Console. Write Line(square(5)); // Output: 25  Biểu thức lambda với nhiều tham số: Khi có nhiều tham số, cần dùng dấu ngoặc đơn.

var sum = (x, y) =&gt; x + y;

Console. Write Line(sum(5, 3)); // Output: 8  Biểu thức lambda với khối lệnh: Nếu biểu thức lambda có nhiều dòng mã, ta cần dùng dấu ngoặc nhọn {}.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 33/33

3.1.4 Biểu thức lamda

Biểu thức lambda rất thường được dùng trong LINQ thay cho cú pháp truy vấn SQL để truy vấn dữ liệu.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 34/33

3.1.4 Biểu thức lamda

Sắp xếp một danh sách số theo thứt ựt ăng dần

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 35/33

3.1.4 Biểu thức lamda

Tính tổng các số trong danh sách

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 36/33

3.1.4 Biểu thức lamda

Tìm các số chia hết cho 3 và 5

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 37/33

3.1.4 Biểu thức lamda

Ví dụsử dụng LINQ đểl ọc dữ liệu:

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 38/33

3.2. Kế thừa và đa hình

1 Kếth ừa

2 Đa hình

3 Lớp trừu tượng và giao diện

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 39/33

3.2.1 Kế thừa

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 40/33

3.2.1. Kếth ừa

Kếth ừa ◼ Là cơ chếcho phép định nghĩa một lớp mới (lớp dẫn xuất - drived class) dựa trên một lớp có sẵn (lớp cơ sở- base class) ◼ Lớp dẫn xuất kếth ừa hầu hết các thành phần của lớp cơ sở(biến thành viên, phương thức), ngoại trừ  Các thành phần private  Phương thức tạo lập  Phương thức huỷ  Các thành phần tĩnh (static) ◼ Lớp dẫn xuất chỉcó thểkếth ừa trực tiếp từmột lớp cơ sở

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 41/28

3.2.1 Kếth ừa

Cú pháp định nghĩa:

class &lt;Tên lớp dẫn xuất&gt;: &lt;Tên lớp cơ sở&gt; { // Thân lớp dẫn xuất } Ví dụ:

◼Khai báo lớp Nguoi gồm Các thuộc tính: Ho Ten, Ngay Sinh, Que Quan Phương thức: Xuat ◼Khai báo lớp Sinh Vien kếth ừa từl ớp Nguoi Bổ sung thêm thuộc tính Ma SV

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 42/28

Ví dụ - Kế thừa

class Nguoi { public string Ho Ten;

public Date Time Ngay Sinh;

public string Que Quan;

public void Xuat() { Console. Write Line("Ho va ten: " +Ho Ten);

Console. Write Line("Ngay sinh: {0}/{1}/{2}", Ngay Sinh. Day,Ngay Sinh. Month,Ngay Sinh. Year);

Console. Write Line("Que quan: " +Que Quan);

}

} class Sinh Vien:Nguoi { public string Ma SV;

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 43/28

Ví dụ - Kế thừa

class Program { static void Main(string[] args) { Nguoi P1 = new Nguoi();

P1. Ho Ten = "Nguyen Van A";

P1. Ngay Sinh = Convert.To Date Time("3/9/1994");

P1. Que Quan = "Ha Noi";

Console. Write Line("Thong tin cua nguoi: ");

P1. Xuat();

Sinh Vien sv1 = new Sinh Vien();

sv1. Ho Ten = "Nguyen Van B";

sv1. Ngay Sinh = Convert.To Date Time("30/9/1994");

sv1. Que Quan = "Thai Binh";

sv1. Ma SV = "15A4040011";

Console. Write Line("\n Thong tin cua sinh vien: ");

sv1. Xuat();

Console. Write Line("Ma sinh vien: " + sv1. Ma SV);

Console. Read Line();

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 44/28

Gọi phương thức tạo lập

Phương thức tạo lập trong lớp dẫn xuất ◼ Nếu lớp cơ sởkh ông có phương thức tạo lập hoặc có phương thức tạo lập không có tham số thì phương thức tạo lập ởl ớp dẫn xuất được định nghĩa như cách thông thường ◼ Nếu lớp cơ sởph ương thức tạo lập có tham số thì phương thức tạo lập của lớp dẫn xuất cũng phải có tham số ◼ Cú pháp:

&lt;Tên lớp dẫn xuất&gt;(Tham số lớp dẫn xuất):

base(tham số lớp cơ sở) ◼ Truy xuất đến các thành phần của lớp cơ sở:

base. Tên Thành Phần

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 45/28

Ví dụ - Phương thức tạo lập

Xây dựng phương thức tạo lập cho lớp Nguoi và lớp Sinh Vien class Nguoi { public string Ho Ten;

public Date Time Ngay Sinh;

public string Que Quan;

public void Xuat() { Console. Write Line("Ho va ten: " +Ho Ten);

Console. Write Line("Ngay sinh: {0}/{1}/{2}", Ngay Sinh. Day,Ngay Sinh. Month,Ngay Sinh. Year);

Console. Write Line("Que quan: " +Que Quan);

} public Nguoi(string ht, Date Time dt, string qq) { this. Ho Ten = ht;

this. Ngay Sinh = dt;

this. Que Quan = qq;

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 46/28

Ví dụ - Phương thức tạo lập

class Sinh Vien:Nguoi { public string Ma SV;

public Sinh Vien(string ht, Date Time dt, string qq, string ma):

base(ht, dt, qq) { this. Ma SV=ma;

} } class Program { static void Main(string[] args) { Nguoi P1 = new Nguoi("Nguyen Van A", Convert.To Date Time("3/8/1994"),"Ha Noi");

Console. Write Line("Thong tin cua nguoi: ");

P1. Xuat();

Sinh Vien sv1 = new Sinh Vien("Nguyen Thi B",Convert.To Date Time("12/9/1994"),"Ha Tay","15A4040012");

Console. Write Line("\n Thong tin cua sinh vien: ");

sv1. Xuat();

Console. Write Line("Ma sinh vien: " +sv1. Ma SV);

Console. Read Line();

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 47/28

Ghi đè phương thức của lớp cha

Ghi đè phương thức lớp cha: Dùng từkho á override ◼ Ví dụ:

public override void Xuat() { //Nội dung phương thức } Che phương thức lớp cha: Dùng từkho á new ◼ Ví dụ:

public new Xuat() { //Nội dung phương thức }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 48/28

Cấm kế thừa lớp

Dùng từkho á sealed Ví dụ:

using System;

public sealed class My Class { public My Class(){} }

public class My New Class:My Class //Định nghĩa lỗi { }

class Test { public static void Main() { } }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 49/28

3.2.2 Đa hình (polymorphism)

Tính đa hình là hiện tượng các đối tượng thuộc các lớp khác nhau có thể hiểu cùng 1 thông điệp theo các cách khác nhau.

Để thể hiện được tính đa hình:

▪ Các lớp phải có quan hệ kế thừa với cùng 1 lớp cha nào đó.

▪ Phương thức đa hình phải được ghi đè (override) ở các lớp con Đa hình gồm có 2 loại:

◼ Đa hình khi chạy: override - ghi đè ◼ Đa hình khi biên dịch: overload - nạp chồng

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 50/28

3.2.2 Đa hình - Ghi đè

Các bước thực hiện ◼ Bước 1:

Đánh dấu phương thức ảo (virtual) trong lớp cơ sở Ví dụ:

public virtual void Draw() { //Nội dung phương thức } ◼ Bước 2:

Đánh dấu phương thức ghi đè (override) trong lớp dẫn xuất public override void Draw() { //Nội dung phương thức }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 51/28

3.2.2 Đa hình - Ghi đè

Ví dụ:

◼Khai báo lớp Nguoi gồm Các thuộc tính: Ho Ten, Ngay Sinh, Que Quan Phương thức: Xuat (virtual) ◼Khai báo lớp Sinh Vien kếth ừa từl ớp Nguoi Bổ sung thêm thuộc tính Ma SV Phương thức: Xuat (override)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 52/28

Ví dụ - Đa hình

class Nguoi { public string Ho Ten;

public Date Time Ngay Sinh;

public string Que Quan;

public Nguoi(string ht, Date Time dt, string qq) { this. Ho Ten = ht;

this. Ngay Sinh = dt;

this. Que Quan = qq;

} public virtual void Xuat() //Khai báo phương thức ảo { Console. Write Line("Ho va ten: " + Ho Ten);

Console. Write Line("Ngay sinh: {0}/{1}/{2}", Ngay Sinh. Day, Ngay Sinh. Month, Ngay Sinh. Year);

Console. Write Line("Que quan: " + Que Quan);

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 53/28

Ví dụ - Đa hình

class Sinh Vien: Nguoi { public string Ma SV;

public Sinh Vien(string ht, Date Time dt, string qq, string ma): base(ht, dt, qq) { this. Ma SV = ma;

} public override void Xuat() //Ghi đè phương thức { Console. Write Line("Ma sinh vien: " + Ma SV);

base. Xuat(); //Kế thừa lại phương thức } }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 54/28

Ví dụ - Đa hình

class Program { static void Main(string[] args) { Nguoi P1 = new Nguoi("Nguyen Van A", Convert.To Date Time("3/8/1994"), "Ha Noi");

Console. Write Line("Thong tin cua nguoi: ");

P1. Xuat(); //Phương thức Xuat của lớp Nguoi Sinh Vien sv1 = new Sinh Vien("Nguyen Thi B", Convert.To Date Time("12/9/1994"), "Ha Tay", "15A4040012");

Console. Write Line("\n Thong tin cua sinh vien: ");

sv1. Xuat(); //Phương thức Xuat của lớp Sinh Vien Console. Read Line();

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 55/28

Vấn đề cấp phát vùng nhớ cho đối tượng

Hãy cho biết 2 câu lệnh sau, câu nào lỗi

1) SinhVien x = new Nguoi();

2) Nguoi a = new SinhVien();

→Vấn đềs âu xa nằm ở đâu?

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 56/28

3.2.2 Đa hình

Ví dụ:

◼Khai báo lớp Nguoi gồm Các thuộc tính: Ho Ten, Ngay Sinh, Que Quan Phương thức: Xuat (virtual) ◼Khai báo lớp Sinh Vien kếth ừa từl ớp Nguoi Bổ sung thêm thuộc tính Ma SV Phương thức: Xuat (override)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 57/28

Ví dụ - Đa hình

class Nguoi { public string Ho Ten;

public Date Time Ngay Sinh;

public string Que Quan;

public Nguoi(string ht, Date Time dt, string qq) { this. Ho Ten = ht;

this. Ngay Sinh = dt;

this. Que Quan = qq;

} public virtual void Xuat() //Khai báo phương thức ảo { Console. Write Line("Ho va ten: " + Ho Ten);

Console. Write Line("Ngay sinh: {0}/{1}/{2}", Ngay Sinh. Day, Ngay Sinh. Month, Ngay Sinh. Year);

Console. Write Line("Que quan: " + Que Quan);

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 58/28

Ví dụ - Đa hình

class Sinh Vien: Nguoi { public string Ma SV;

public Sinh Vien(string ht, Date Time dt, string qq, string ma): base(ht, dt, qq) { this. Ma SV = ma;

} public override void Xuat() //Ghi đè phương thức { Console. Write Line("Ma sinh vien: " + Ma SV);

base. Xuat(); //Kế thừa lại phương thức } }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 59/28

Ví dụ - Đa hình

class Program { static void Main(string[] args) { Nguoi P1 = new Nguoi("Nguyen Van A", Convert.To Date Time("3/8/1994"), "Ha Noi");

Console. Write Line("Thong tin cua nguoi: ");

P1. Xuat(); //Phương thức Xuat của lớp Nguoi Sinh Vien sv1 = new Sinh Vien("Nguyen Thi B", Convert.To Date Time("12/9/1994"), "Ha Tay", "15A4040012");

Console. Write Line("\n Thong tin cua sinh vien: ");

sv1. Xuat(); //Phương thức Xuat của lớp Sinh Vien Console. Read Line();

} }

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 60/28

Ví dụ - Đa hình

Nêu sựkh ác nhau giữa kếth ừa và đa hình?

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 61/28

Nạp chồng phương thức (Method Overloading)

Các phương thức trực thuộc lớp có thể trùng tên nhau nhưng phải khác nhau ở kiểu giá trị trả về, danh sách kiểu các tham số, cách xây dựng các phương thức như vậy người ta gọi là phương thức nạp chồng:

Đểph ân biệt được các hàm với nhau, căn cứ vào một trong hai yếu tố:

◼ Khác tên ◼ Khác tham số ho ặc kiểu dữ liệu của tham số Ví dụ:

void my Method(int p1);

void my Method(int p1, int p2);

void my Method(double p1, double s1);

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 62/33

Nạp chồng phương thức (Method Overloading)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 63/33

Nạp chồng phương thức (Method Overloading)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 64/33

Ví dụtổng quát

Xây dựng lớp Phan So class Phan So public void In Phan So() { { int Tu, Mau;

//nạp chồng các phương thức khởi tạo Console. Write Line("{0}/{1} ", public Phan So() Tu, Mau);

{ } Tu = 0; Public static Phan So Mau = 1; Cong(Phan So PS1, Phan So PS2) } { public Phan So(int x) int TS = Tu * PS2. Mau + { Mau * PS2. Tu;

Tu = x; int MS = Mau * PS2. Mau;

Mau = 1; //Gọi phương thức tạo 2 tham số } Phan So Ket Qua = new public Phan So(int t, int m) Phan So(TS, MS);

{ return Ket Qua;

Tu = t; } Mau = m;

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 65/33

Ví dụtổng quát

static void Main(string[] args) { Phan So p1 = new Phan So();

Console. Write("Phan so p1 = ");

p1. In Phan So();

Phan So p2 = new Phan So(5);

Console. Write("Phan so p2 = ");

p2. In Phan So();

int ts, ms;

Console. Write("Nhap tu so: ");

ts = int. Parse(Console. Read Line());

Console. Write("Nhap mau so: ");

ms = int. Parse(Console. Read Line());

Phan So p3 = new Phan So(ts, ms);

Console. Write("Phan so p3 = ");

p3. In Phan So();

//p1=p2+p3 p1 = Phan So. Cong(p2,p3);

Console. Write("Phan so p1 = p2 + p3 = ");

p1. In Phan So();

Console. Read Line();

}

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 66/33

3.2.3. Đóng gói dữ liệu với thuộc tính (property)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 67/38

3.2.3. Đóng gói dữ liệu với thuộc tính (property)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 68/28

3.2.3. Đóng gói dữ liệu với thuộc tính (property)

 Thuộc tính (property) là đặc tính mới trong C#.

 Thuộc tính là các phương thức lấy giá trị(get) và gán giá trị (set).

 Cho phép truy cập đến các thành phần dữ liệu của đối tượng ở mức độđ ọc hoặc ghi hoặc cả2 và che giấu cài đặt thực sựb ên trong lớp.

Các thuộc tính ◼ Chỉđ ọc (read only): chỉcó phương thức get (chỉđ ọc giá trị của thuộc tính) ◼ Chỉghi (write only): chỉcó phương thức set (chỉghi giá trị cho thuộc tính) ◼ Vừa đọc vừa ghi (read/write): có cả2 phương thức get và set. Được phép đọc và ghi giá trị

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 69/38

Thuộc tính (property)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 70/28

Thuộc tính (property)

int

23/05/2026 71/28

Thuộc tính (property)

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 72/28

Thuộc tính (property)

Cú pháp public &lt;Kiểu trảvề&gt; &lt;Tên thuộc tính&gt; { //Phương thức lấy giá trị get { //các lệnh return &lt;Biểu thức&gt;;

} set { //các lệnh &lt;Biến thành viên&gt; = value;

} } Chú ý ◼ value: từkho á chỉgi á trịd ùng đểg án

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 73/38

Ví dụ - Thuộc tính

Khai báo lớp Student //Thuộc tính Diem Toan (read/write) class Student public float Diem Toan { { get { return _Diem Toan; } //Tên các property không có dấu _, tên set // các thành phần dữ liệu có dấu _ { private string _Ten; _Diem Toan = value;

float _Diem Toan, _Diem Tin, _Diem TB; _Diem TB = (_Diem Toan + //Hàm tạo _Diem Tin) / 2;

public Student() } { } _Ten = ""; //Thuộc tính Diem Tin (read/write) _Diem Toan = 0; public float Diem Tin _Diem Tin = 0; { _Diem TB = 0; get { return _Diem Tin; } } set //Thuộc tính Ten (read/write) { _Diem Tin = value;

public string Ten _Diem TB = (_Diem Toan + { _Diem Tin) / 2;

get { return _Ten; } } set { _Ten = value; } } 23/05/2026 } Chương 3. Lập trình hướng đối tượng trong C# 74/38

Ví dụ - Thuộc tính (tiếp)

//Thuoc tinh Diem Trung Binh- (read only) public float Diem Trung Binh { get { return _Diem TB; } }

static void Main(string[] args) { Student s1 = new Student();

Console. Write("Nhap ho ten: ");

s1. Ten = Console. Read Line();

Console. Write("Nhap diem Toan: ");

s1. Diem Toan = float. Parse(Console. Read Line());

Console. Write("Nhap diem Tin: ");

s1. Diem Tin = float. Parse(Console. Read Line());

Console. Write Line("Ten: {0}, diem Toan: {1}, diem Tin: {2}, diem Trung binh: {3}", s1. Ten, s1. Diem Toan, s1. Diem Tin, s1. Diem Trung Binh);

Console. Read Line();

} 23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 75/38

3.2.4. Lớp trừu tượng và giao diện

 Lớp trừu tượng ◼ Là những lớp không hoàn thiện ◼ Thiết lập như là lớp cơ sởcho những lớp dẫn xuất  Phương thức trừu tượng ◼ Là phương thức không hoàn thiện (chỉcó nguyên mẫu, không có

## phần mô tảcài đặt chi tiết)

◼ Không có sựth ực thi  Cú pháp abstract class &lt;tên lớp&gt; abstract void &lt;tên phương thức&gt;();

(có dấu chấm phẩy; sau tên phương thức)

- Khi kếthừa 1 lớp trừu tượng, bắt buộc phải override tất cả các

phương thức trừu tượng.

- Không thểtạo ra các đối tượng từabstract class.

- 1 abstract class bắt buộc phải có tối thiểu 1 phương thức

abstract 23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 76/28

Lớp trừu tượng

VD: Chúng ta có một lớp Animal gồm 2 phương thức:

Eat() { //thức ăn “Động vật ăn cỏ”} Animal Sound() {//Tiếng kêu “Quạqu ạ” } Và chúng ta có 3 lớp: Cow, Cat, Bird kếth ừa từl ớp Animal, tuy nhiên 3 loài này thì:

◼ Không cùng ăn một loại thức ăn ◼ Và tiếng kêu cũng không giống nhau Do đó mà các phương thức Eat(), Animal Sound() cần phải khác nhau cho từng loại động vật trong khi chúng cũng được kếth ừa từmột lớp duy nhất là Animal.

Đểgi ải quyết vấn đền ày, chúng ta cần đến abstract class, tức là lớp abstract Animal sẽkhai báo ra khuôn mẫu là Eat() và Animal Sound(), rồi ứng với mỗi lớp con kếth ừa Cow,Bird, Cat sẽ định nghĩa lại cho phù hợp với chất riêng của nó.23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 77/30

Lớp trừu tượng

Ví dụ ◼ Xây dựng lớp Hinh Hoc gồm phương thức: Tính chu vi, diện tích là phương thức trừu tượng.

◼ Xây dựng lớp Tam Giac, Hinh Chu Nhat kếth ừa từ lớp Hinh Hoc, xây dựng phương thức tính chu vi, diện tích

//Lớp trừu tượng abstract public class Hinh Hoc { abstract public void Nhap();

abstract public double Chu Vi();

abstract public double Dien Tich();

}

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 78/28

Ví dụ lớp trừu tượng

//Lớp Tam Giac public class Tam Giac:Hinh Hoc { private double a, b, c;

public override void Nhap() { Console. Write("Nhap canh a: ");

a=Convert.To Double(Console. Read Line());

Console. Write("Nhap canh b: ");

b=Convert.To Double(Console. Read Line());

Console. Write("Nhap canh c: ");

c=Convert.To Double(Console. Read Line());

} public override double Chu Vi() { return a + b + c;

} public override double Dien Tich() { double p = (a + b + c) / 2;

return Math. Sqrt(p * (p - a) * (p - b) * (p - c));

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 79/28

Ví dụ lớp trừu tượng

//Lớp hình chữnh ật public class Hinh Chu Nhat: Hinh Hoc { private double a, b;

public override void Nhap() { Console. Write("Nhap chieu dai: ");

a = Convert.To Double(Console. Read Line());

Console. Write("Nhap chieu rong: ");

b = Convert.To Double(Console. Read Line());

} public override double Chu Vi() { return (a + b) * 2;

} public override double Dien Tich() { return a * b;

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 80/28

Ví dụ lớp trừu tượng

class Program { static void Main(string[] args) { // Hinh Hoc H1= new Hinh Hoc(); =&gt; báo lỗi Tam Giac TG1 = new Tam Giac(); (hoặc Hinh Hoc TG1=new Tam Giac();) TG1. Nhap();

Console. Write Line("Thong tin ve tam giac: ");

Console. Write Line("Chu vi la: {0}", TG1. Chu Vi());

Console. Write Line("Dien tich la: {0,8:f2}", TG1. Dien Tich());

Hinh Chu Nhat HCN1 = new Hinh Chu Nhat();

HCN1. Nhap();

Console. Write Line("Thong tin ve hinh chu nhat: ");

## H1 = HCN1;

Console. Write Line("Chu vi la: {0}", H1. Chu Vi());

Console. Write Line("Dien tich la: {0,8:f2}", H1. Dien Tich());

Console. Read Line();

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 81/28

Giao diện (interface)

Giao diện ◼ Là một dạng của lớp trừu tượng ◼ Sử dụng với mục đích hỗtr ợtính đa hình (đa kế thừa) ◼ Chỉcó nguyên mẫu của phương thức, thuộc tính (Lớp kếth ừa từgiao diện phải có cài đặt cụ thể) ◼ Lớp kếth ừa giao diện được gọi là lớp thực thi (implement) giao diện

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 82/28

Giao diện (interface)

 Giả sử có 2 lớp

- Động vật trên cạn

- Động vật dưới nước

 Tiếp theo mình tạo 1 lớp Ếch. Vì ếch là loài lưỡng cư nên nó phải được thừa hưởng thuộc tính và phương thức của cả 2 lớp Động vật trên cạn và Động vật dưới nước. Nhưng C# không hỗ trợ đa kế thừa, vì vậy Interface ra đời như một giải pháp thay thế.

 Interface được hiểu như là 1 khuôn mẫu chung mà mọi lớp thực thi nó đều phải tuân theo. Bên trong Interface là 1 tập hợp các thành

## phần chỉ có khai báo mà không có phần định nghĩa.

- Chỉ chứa khai báo không chứa phần định nghĩa.

- Việc ghi đè 1 thành phần trong interface cũng không cần từ

khoá override.

- Không thể khai báo phạm vi truy cập cho các thành phần bên

trong interface. Các thành phần này sẽ mặc định là public.

- Giải quyết được đa kếthừa.

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 83/30

Giao diện (interface)

Cú pháp interface &lt;Tên giao diện&gt;[:Giao diện cơ sở] {

## Nội dung

} [Giao diện cơ sở]: interface khác mà nó kếth ừa Tên giao diện bắt đầu bằng chữI Chú ý ◼ Các thành phần trong giao diện mặc định đều là public ◼ Mỗi lớp có thểkếth ừa một lớp khác đồng thời kế thừa nhiều giao diện

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 84/28

Giao diện (interface)

Ví dụ: Lớp ếch kế thừa 2 interface là động vật trên cạn và động vật dưới nước.

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 85/30

Ví dụ Giao diện

Xây dựng giao diện Inguoi gồm các phương thức Nhập, Xuất, thuộc tính Tuoi //Giao diện Inguoi public interface INguoi { void Nhap();

void Xuat();

int Tuoi { get;

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 86/28

Ví dụ Giao diện

//Lớp Sinh Vien thực thi giao diện INguoi public class Sinh Vien: INguoi { private string Ho Ten;

private int Nam Sinh;

public void Nhap() { Console. Write("Nhap ho ten: ");

Ho Ten = Console. Read Line();

Console. Write("Nhap nam sinh: ");

Nam Sinh = Convert.To Int16(Console. Read Line());

} public int Tuoi { get { return System. Date Time. Today. Year - Nam Sinh;

} } public void Xuat() { Console. Write Line("Ho ten: " + Ho Ten);

Console. Write Line("Tuoi: " + Tuoi);

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 87/28

Ví dụ Giao diện

class Program { static void Main(string[] args) { Sinh Vien SV1 = new Sinh Vien();

SV1. Nhap();

SV1. Xuat();

Console. Read Line();

} }

23/05/2026 Chương 3 - Lập trình hướng đối tượng trong C# 88/28

## Bài tập về nhà

Bài 1. Xây dựng chương trình làm việc với phân số ◼ Xây dựng lớp Phan So gồm:

class Phan So{ private int Tu So; //Tửsố private int Mau So; //Mẫu số } ◼ Xây dựng các phương thức trong lớp Phan So  Hàm tạo (khởi tạo tửsố= 0, mẫu số= 1)  Hàm tạo 2 tham số tử, mẫu  Nhập phân số  In phân số  Rút gọn phân số  Tính tổng/hiệu/tích/thương 2 phân số 23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 89/33

Bài 2. Xây dựng chương trình làm việc với các điểm trong không gian 2 chiều ◼ Khai báo lớp Điểm gồm:

class Diem{ private double x; //Hoành độ private double y; //Tung độ } ◼ Xây dựng các phương thức  Hàm tạo không tham số: khởi tạo điểm toạđộ(0,0)  Hàm tạo 2 tham số x, y: khởi tạo điểm có toạđộ(x,y)  Nhập toạđộ  In toạđộđi ểm ra màn hình  Tính khoảng cách giữa 2 điểm

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 90/33

Bài 3. Chương trình làm việc với mảng 1 chiều ◼ Xây dựng lớp Mang1Chieu gồm class Mang1Chieu{ private int n; //Số phần tửcủa mảng int[] a; //Mảng 1 chiều } ◼ Xây dựng các phương thức trong lớp Mang1Chieu Hàm tạo Mang1Chieu(int n) đểkh ởi tạo mảng gồm n phần tử Nhập mảng In mảng ra màn hình Sắp xếp mảng public void sapxep(int thutu) //thutu = 0: tăng dần, thutu=1: giảm dần Tìm kiếm public int timkiem(int m) //Trảvề-1 nếu không thấy, trảvềv ịtr í nếu tìm thầy 23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 91/33

Bài 4. Xây dựng lớp Nhan Vien ◼ Các thành phần dữ liệu  Họt ên, Năm sinh, Địa chỉ, Lương cơ bản, Hệ số, Phụ cấp, Tổng tiền ◼ Các phương thức  Hàm tạo không tham số  Nhập nhân viên  Tính lương: Tổng tiền = Lương cơ bản x Hệ số+ Phụ cấp  In nhân viên ra màn hình

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 92/33

Bài 5. Chương trình quản lý Sinh viên ◼ Xây dựng lớp Sinh Vien  Các thành phần dữ liệu:

◼ Mã sinh viên, Họt ên, Năm sinh, Quê quán, Điểm lập trình, Điểm CSDL, Điểm TB (trong đó: Điểm TB=Điểm Lập trình + Điểm CSDL)/2  Các hàm tạo ◼ Hàm tạo không tham số ◼ Hàm tạo có 5 tham số(Họt ên, năm sinh, quê quán, Điểm lập trình, Điểm CSDL)  Các phương thức ◼ Nhập thông tin sinh viên ◼ In thông tin sinh viên ra màn hình

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 93/33

## Bài 6

Xây dựng lớp Nhan Vien ◼ Thuộc tính: Ho Ten, Ngay Sinh ◼ Phương thức: Nhap, Xuat Xây dựng 2 lớp Nhan Vien Cong Nhat, Nhan Vien Chinh Thuc kếth ừa lớp Nhan Vien ◼ Nhan Vien Cong Nhat  Thuộc tính: So Ngay Cong  Phương thức: Tinh Luong trảvềSo Ngay Cong*200.000  Ghi đè phương thức Nhap, Xuat ◼ Nhan Vien Chinh Thuc  Thuộc tính: He So Luong  Phương thức: Tinh Luong trảvềHe So Luong*2.000.000  Ghi đè phương thức Nhap, Xuat

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 94/33

Trong lớp program:

Viết chương trình cho phép người dùng được phép lựa chọn nhập loại nhân viên bất kỳt ừb àn phím: chọn 1 được nhập nhân viên công nhật, chọn 2 được nhập nhân viên chính thức

- Hiển thịthông tin nhân viên vừa nhập.

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 95/33

## Bài tập trắc nghiệm

https://www. tutorialsteacher. com/online- test/csharp-test

23/05/2026 Chương 3. Lập trình hướng đối tượng trong C# 96/33
