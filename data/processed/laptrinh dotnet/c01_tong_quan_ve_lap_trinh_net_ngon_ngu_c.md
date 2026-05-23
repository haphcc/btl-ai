### BÀI 3

#### C01 TONG QUAN VE LAP TRINH .NET & NGON NGU C#

## TRANG 1

## Chương 1

Tổng quan về lập trình .NET và ngôn ngữC#

## TRANG 2

## Nội dung

1. Tổng quan về .NET

2. Giới thiệu về Microsoft Visual Studio

3. Ngôn ngữC#

4. Các bước xây dựng chương trình C#

5. Hướng dẫn debug chương trình

## TRANG 3

1. Tổng quan về .NET

▪.NET là gì ●NET là nền tảng phát triển phần mềm do Microsoft phát triển nhằm hỗ trợ

▪Xây dựng

▪Chạy

▪Quản lý

●Các loại ứng dụng:

▪Console

▪Desktop

▪Web

▪Mobile

▪Cloud

## TRANG 4

1. Tổng quan về .NET

▪Sự phát triển của.NET ●Trước đây:

▪.NET Framework (chỉ Windows) ●Hiện nay:

▪.NET (Unified Platform)

▪Cross-platform: Windows - Linux - mac OS ●Phiên bản phổ biến:

## ▪.NET 6 (LTS)

## ▪.NET 7

## ▪.NET 8 (LTS)

## TRANG 5

1. Tổng quan.NET

▪.NET có 2 thành phần chính:

●Bộ thực thi ngôn ngữchung (Common Language Runtime - CLR)

●Thư viện lớp (Base Class Library - BCL)

Common Language Base Class

## .NET

Runtime - Library - BCL CLR

## Chương 1. Tổng quan về lập trình hướng đối tượng

23/05/2026 5/46 và ngôn ngữC#

## TRANG 6

1. Tổng quan.NET

▪Mô hình biên dịch và thực thi trong.NET

## TRANG 7

2. Tổng quản về MS visual studio

▪2.1. Microsoft Visual Studio là gì?

●Microsoft Visual Studio là môi trường phát triển tích hợp (IDE) do Microsoft phát triển

●Được sử dụng để:

▪Viết mã nguồn

▪Biên dịch

▪Chạy chương trình

## TRANG 8

▪2.2. Vai trò của Visual Studio trong lập trình C#

●Trong quá trình phát triển ứng dụng C#, Visual Studio giúp:

▪Quản lý project và solution

▪Hỗ trợ viết code thông minh (Intelli Sense)

▪Phát hiện lỗi cú pháp sớm

▪Debug chương trình

▪Tích hợp công cụ quản lý thư viện (.NET SDK, Nu Get)

## TRANG 9

▪2.3. Các phiên bản Visual Studio

●Hiện nay Visual Studio có 3 phiên bản chính:

▪Community (miễn phí - dùng cho học tập)

▪Professional

▪Enterprise

## TRANG 10

▪2.4 Visual Studio và Visual Studio Code (phân biệt)

## TRANG 11

▪2.5. Giao diện chính của Visual Studio

●Các thành phần cơ bản:

▪Editor: soạn thảo mã nguồn

▪Solution Explorer: quản lý project, file

▪Properties Window: thuộc tính

▪Output / Error List: thông báo lỗi

▪Toolbar: build, run, debug

## TRANG 12

3. Ngôn ngữC#

▪C# được phát triển bởi nhóm tác giả điều hành bởi Anders Hejlsberg ▪C# được dẫn xuất từC vàC++ nhưng nó được tạo từ nền tảng tốt hơn ▪C# là ngôn ngữ hướng đối tượng (Object Oriented Language) ●Hỗ trợ định nghĩa và làm việc với lớp (class)

●Hỗ trợ đầy đủ các đặc trưng của lập trình hướng đối tượng: đóng gói (encapsulation), kế thừa (inheritance) và đa hình (polymorphism) ▪C# cung cấp những đặc tính hướng thành phần (component oriented): thuộc tính, sự kiện

## Chương 1. Tổng quan về lập trình hướng đối tượng

23/05/2026 12/46 và ngôn ngữC#

## TRANG 13

1 G a 7 @ { | Ak w T | | " "

Open recent Get started

Get code from an online repository like Git Hub 4 This week or Azure Dev Ops TF] Consoleappt. sin 22-Aug-21 1037 PM SỀ Ä)_ Open a project or solution (C\Users\huett\source\repos\Console Appt Opena local Visual Studio project or sin file

4 This month FT Win Formsapprsin 06-Aug-21 10:12 PM % Open a local folder CAUser Ahuett\source\repos\Win Forms App1 Navigate and edit code within any folder

bế Create a new project Cho ose a project template with code scaffolding to get started

Continue without code >

HE Type here to search otl @wuebneodsgma= wh oe 8PF Ra ini AO Ö6 E2 Ae) NG,uuạy9⁄17 PM, BÊ, |

## TRANG 14

c===›

---mn Ừờ Ừe-

- Cort; - n x

p J Search for templates (Alt+S) - Clear all

Recent project templates ad > Windows * Console k

Bx Console Application c Console Application A project for creating a command-line application that can run on.NET Core on » Windows, Linux and mac OS (i Windows Forms App c# =4 Linux mac OS Windows Console fea | Console App (NET Framework) A project for creating a command-line application

{ C# Windows Console `

Not finding what you're looking for?

Install more tools and features

rr

## TRANG 15

con - o x R ¡ ~~ Configure your new project

Console Application c# Linux mac OS Windows Console [=~]--------- Location

Solution name @)

(J Place solution and project in the same directory

## TRANG 16

▪Bạn chọn. net framework và tiến hành viết code

## TRANG 17

4. Cấu trúc chương trình C#

//Vùng bắt đầu khai báo sử dụng các không gian tên using System;

using System.Collections. Generic;

using System.Text;

//Khai báo không gian tên của ứng dụng namespace my Console Application { //Vùng bắt đầu khai báo tên các Class class Program { //Vùng khai báo các phương thức static void Main(string[] args) { //Vùng khai báo lệnh } } }

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 17/47

## TRANG 18

Một số khái niệm trong C#

▪C# là ngôn ngữ phân biệt chữ hoa/thường ▪Chú thích ●Chú thích trên một dòng // ●Chú thích trên nhiều dòng /*…… */ ●Trình biên dịch bỏ qua chú thích ▪Từ khoá (keyword) ●Có các chức năng đặc biệt không thể thay đổi trong ngôn ngữ ●Không được dùng làm tên biến, tên lớp hay bất kỳ thứ gì khác ●Tất cả các từ khoá đều được viết thường Ví dụ: class

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 18/47

## TRANG 19

Danh sách các từ khoá trong C#

abstract object byte private event this fixed uint new bool override char struct false try foreach as operator case protected explicit throw float ulong null break params checked switch finally typeof goto base out catch public extern true for unchecked

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 19/47

## TRANG 20

Console nhập xuất

▪Đọc ký tự văn bản từ cửa sổ console ●Console. Read() ●Console. Read Line() ▪Xuất chuỗi kí tự ●Console. Write() ●Console. Write Line() Ví dụ:

Console. Write Line("Bill total:\t{0,8:c}", bill Total); Console. Write Line("Tip total/ra te:\t{0,8:c} ({1:p1})", tip, tip Ra te);

Kết quả in ra màn hình

Bill total: $52.23

Tip total/ra te: $9.40 (18.0 %)

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 20/47

## TRANG 21

Console nhập xuất

▪Xuất chuỗi kí tự ●Định dạng số:

Console. Write Line(“chuỗi định dạng”, số) ●Trong đó:

▪Chuỗi định dạng: {số thứ tự, số lượng khoảng trống: kí tự định dạng}

▪Ví dụ: {0,8:C} viết kiểu tiền tệ, dành 8 vị trí ●Một số kí tự định dạng ▪C: Currency

▪D: Decimal

▪E: Scientific

▪F: Fixed point

▪G: General (mặc định)

▪P: Percent

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 21/47

## TRANG 22

class Program

{

static void Main(string[] args)

{

Console. Write Line("tên của bạn là gì? ");

string ten = Console. Read Line();

Console. Write Line("Bạn số ngở đâu");

string vitri = Console. Read Line();

Console. Write Line("Xin chào bạn {0}, đến từ {1}", ten, vitri);

Console. Read();

}

}

## TRANG 23

2. Không gian tên (namespace)

▪Nhóm các tính năng có liên quan của C# vào một loại ▪Cho phép dễ dàng tái sử dụng mã nguồn ▪Trong thư viện.NET có nhiều không gian tên ▪Phải tham chiếu tới để sử dụng

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 23/47

## TRANG 24

Các namespace cơ bản

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 24/47

## TRANG 25

Không gian tên

▪Khai báo sử dụng:

●Using &lt;tên namespace&gt;;

▪Tạo không gian tên:

●namespace &lt;Tên namespace&gt; {

&lt;Định nghĩa lớp A&gt;

&lt;Định nghĩa lớp B&gt;

….

}

23/05/2026 Chương 2. Các thành phần cơ bản trong C# 25/47
