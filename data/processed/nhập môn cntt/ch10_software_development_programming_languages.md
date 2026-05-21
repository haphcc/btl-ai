# Chapter 10: Building Systems & Applications: Software Development, Programming, & Languages

## Nội dung chính
- Phát triển hệ thống (Systems Development) và vòng đời dự án phần mềm.
- Các giai đoạn trong life cycle của dự án phần mềm.
- Lập trình như quy trình năm bước.
- Năm thế hệ ngôn ngữ lập trình.
- Các ngôn ngữ lập trình được dùng hiện nay.
- Lập trình hướng đối tượng (Object-Oriented Programming).
- Visual programming, markup languages và scripting languages.

## Tổng quan
Chương này giới thiệu cách xây dựng hệ thống và ứng dụng phần mềm. Nội dung bắt đầu từ phát triển hệ thống và vòng đời dự án, sau đó trình bày quy trình lập trình, các thế hệ ngôn ngữ lập trình và các kiểu ngôn ngữ quan trọng như hướng đối tượng, trực quan, đánh dấu và kịch bản.

## Unit 10A: Systems Development & Programming

### 10.1 Systems Development & the Life Cycle of a Software Project

**Khái niệm chính:**
- Systems development là quá trình phân tích, thiết kế, xây dựng, kiểm thử và triển khai hệ thống.
- Software project life cycle mô tả các giai đoạn từ ý tưởng đến vận hành.
- Kiểm thử từng phần và toàn hệ thống là bước quan trọng.

**Giải thích:**
Phần mềm không chỉ là viết code. Một dự án cần hiểu nhu cầu người dùng, xác định yêu cầu, thiết kế giải pháp, lập trình, kiểm thử, triển khai và bảo trì. Nếu bỏ qua giai đoạn phân tích hoặc kiểm thử, hệ thống có thể không đáp ứng nhu cầu hoặc có nhiều lỗi.

**Các giai đoạn thường gặp:**
1. Preliminary investigation: khảo sát ban đầu.
2. Systems analysis: phân tích hệ thống.
3. Systems design: thiết kế hệ thống.
4. Systems development: xây dựng hệ thống.
5. Systems implementation: triển khai hệ thống.
6. Systems maintenance: bảo trì hệ thống.

**Thuật ngữ cần nhớ:**
- `Systems development`: phát triển hệ thống.
- `Software life cycle`: vòng đời phần mềm.
- `Systems analysis`: phân tích hệ thống.
- `Systems design`: thiết kế hệ thống.
- `Implementation`: triển khai.
- `Maintenance`: bảo trì.

**Ví dụ / ứng dụng:**
- Xây dựng hệ thống quản lý thư viện cần khảo sát nghiệp vụ mượn trả, thiết kế cơ sở dữ liệu, lập trình giao diện, kiểm thử chức năng và đào tạo người dùng.

### Programming as a Five-Step Procedure

**Khái niệm chính:**
- Lập trình là quá trình giải quyết vấn đề bằng chương trình máy tính.
- Quy trình lập trình có thể chia thành năm bước.

**Giải thích:**
Người lập trình cần hiểu vấn đề trước khi viết code. Sau đó thiết kế thuật toán, viết mã, kiểm thử và bảo trì. Quy trình rõ ràng giúp giảm lỗi và làm chương trình dễ sửa.

**Quy trình năm bước:**
1. Clarify the problem: làm rõ vấn đề.
2. Design the solution: thiết kế giải pháp hoặc thuật toán.
3. Code the program: viết chương trình.
4. Test the program: kiểm thử chương trình.
5. Document and maintain the program: viết tài liệu và bảo trì.

**Thuật ngữ cần nhớ:**
- `Algorithm`: thuật toán, các bước giải quyết vấn đề.
- `Coding`: viết mã chương trình.
- `Testing`: kiểm thử.
- `Debugging`: tìm và sửa lỗi.
- `Documentation`: tài liệu mô tả chương trình.

**Ví dụ / ứng dụng:**
- Bài toán tính điểm trung bình cần xác định đầu vào là các điểm, công thức tính, viết mã, kiểm thử với dữ liệu mẫu và ghi chú cách dùng.

## Unit 10B: Programming Languages

### 10.2 Programming: Five Generations of Programming Languages

**Khái niệm chính:**
- Ngôn ngữ lập trình phát triển qua nhiều thế hệ.
- Thế hệ càng cao càng gần ngôn ngữ con người hơn và ít phụ thuộc phần cứng hơn.

**Giải thích:**
Máy tính chỉ hiểu mã máy, nhưng con người khó viết trực tiếp mã máy. Vì vậy, các ngôn ngữ lập trình được phát triển để giúp người lập trình diễn đạt giải pháp dễ hơn. Trình dịch hoặc trình thông dịch chuyển mã nguồn thành dạng máy có thể thực thi.

| Thế hệ | Mô tả |
|---|---|
| `First-generation language` | Ngôn ngữ máy, dùng mã nhị phân |
| `Second-generation language` | Assembly language, dùng ký hiệu gần máy |
| `Third-generation language` | Ngôn ngữ bậc cao như C, Java |
| `Fourth-generation language` | Ngôn ngữ gần mục tiêu ứng dụng, thường ít code hơn |
| `Fifth-generation language` | Hướng đến giải quyết vấn đề bằng mô tả logic hoặc ràng buộc |

**Thuật ngữ cần nhớ:**
- `Machine language`: ngôn ngữ máy.
- `Assembly language`: hợp ngữ.
- `High-level language`: ngôn ngữ bậc cao.
- `Compiler`: trình biên dịch.
- `Interpreter`: trình thông dịch.

**Ví dụ / ứng dụng:**
- C và Java là ví dụ ngôn ngữ bậc cao, dễ đọc hơn mã máy.

### 10.3 Programming Languages Used Today

**Khái niệm chính:**
- Có nhiều ngôn ngữ lập trình hiện đại, mỗi ngôn ngữ phù hợp mục đích khác nhau.
- Trình biên dịch dịch toàn bộ chương trình trước khi chạy; trình thông dịch dịch và chạy từng phần.

**Giải thích:**
Lựa chọn ngôn ngữ phụ thuộc vào loại ứng dụng, nền tảng, hiệu năng, thư viện và kỹ năng nhóm phát triển. Một số ngôn ngữ phù hợp hệ thống, một số phù hợp web, dữ liệu, ứng dụng doanh nghiệp hoặc giáo dục.

**Thuật ngữ cần nhớ:**
- `Source code`: mã nguồn do lập trình viên viết.
- `Object code`: mã đã được dịch.
- `Compiler`: dịch và lưu mã như một đơn vị để thực thi.
- `Interpreter`: dịch và thực thi từng lệnh hoặc từng phần.

**Ví dụ / ứng dụng:**
- Ngôn ngữ web có thể dùng cho giao diện, server hoặc xử lý dữ liệu tùy mục đích.

### 10.4 Programming Languages: Features & Uses

**Khái niệm chính:**
- Ngôn ngữ lập trình có cú pháp, kiểu dữ liệu, cấu trúc điều khiển và thư viện.
- Ngôn ngữ khác nhau hỗ trợ phong cách lập trình khác nhau.

**Giải thích:**
Một chương trình thường gồm biến, phép toán, điều kiện, vòng lặp, hàm và cấu trúc dữ liệu. Ngôn ngữ lập trình cung cấp cách viết các thành phần đó. Thư viện giúp dùng lại chức năng có sẵn thay vì viết từ đầu.

**Thuật ngữ cần nhớ:**
- `Syntax`: cú pháp.
- `Variable`: biến.
- `Data type`: kiểu dữ liệu.
- `Control structure`: cấu trúc điều khiển.
- `Library`: thư viện.

**Ví dụ / ứng dụng:**
- Một chương trình quản lý điểm cần biến lưu điểm, điều kiện kiểm tra đạt/trượt và hàm tính trung bình.

### 10.5 Object-Oriented Programming

**Khái niệm chính:**
- Lập trình hướng đối tượng (Object-Oriented Programming - OOP) tổ chức chương trình quanh đối tượng.
- Đối tượng có dữ liệu và hành vi.
- Các khái niệm quan trọng gồm class, object, inheritance, encapsulation và polymorphism.

**Giải thích:**
OOP giúp mô hình hóa chương trình theo các đối tượng gần với thế giới thực. Class là khuôn mẫu, object là thể hiện cụ thể. Inheritance giúp lớp mới kế thừa đặc điểm lớp cũ. Encapsulation che giấu chi tiết bên trong. Polymorphism cho phép cùng một giao diện có nhiều cách thực hiện.

**Thuật ngữ cần nhớ:**
- `Class`: lớp, khuôn mẫu tạo đối tượng.
- `Object`: đối tượng, thể hiện của lớp.
- `Inheritance`: kế thừa.
- `Encapsulation`: đóng gói.
- `Polymorphism`: đa hình.

**Ví dụ / ứng dụng:**
- Trong hệ thống trường học, `Student` có thể là class; mỗi sinh viên cụ thể là object.

### 10.6 Markup & Scripting Languages

**Khái niệm chính:**
- Markup languages dùng để đánh dấu cấu trúc và ý nghĩa nội dung.
- Scripting languages thường dùng để viết các đoạn lệnh tự động hóa hoặc xử lý web.
- Visual programming cho phép lập trình bằng thao tác trực quan thay vì chỉ viết mã văn bản.

**Giải thích:**
Markup language như HTML không phải ngôn ngữ lập trình theo nghĩa truyền thống mà dùng để mô tả cấu trúc tài liệu. Scripting language thường linh hoạt, dễ viết và hay dùng trong web, tự động hóa hoặc xử lý tác vụ nhanh.

| Loại ngôn ngữ | Vai trò |
|---|---|
| `Markup language` | Đánh dấu cấu trúc nội dung |
| `Scripting language` | Viết kịch bản tự động hóa hoặc xử lý web |
| `Visual programming` | Lập trình bằng thành phần trực quan |

**Thuật ngữ cần nhớ:**
- `HTML`: ngôn ngữ đánh dấu siêu văn bản.
- `XML`: ngôn ngữ đánh dấu mở rộng.
- `Script`: đoạn lệnh kịch bản.
- `Visual programming`: lập trình trực quan.

**Ví dụ / ứng dụng:**
- HTML dùng để cấu trúc trang web.
- JavaScript thường dùng để tạo tương tác trên web.

## Tóm tắt chương
- Phát triển hệ thống gồm phân tích, thiết kế, xây dựng, triển khai và bảo trì.
- Lập trình nên đi theo quy trình rõ ràng: hiểu vấn đề, thiết kế, viết mã, kiểm thử, tài liệu và bảo trì.
- Ngôn ngữ lập trình phát triển qua năm thế hệ từ ngôn ngữ máy đến ngôn ngữ cấp cao hơn.
- Compiler và interpreter là hai cách dịch mã chương trình.
- OOP tổ chức phần mềm theo class và object.
- Markup languages mô tả cấu trúc tài liệu; scripting languages hỗ trợ tự động hóa và web.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Systems Development | Phát triển hệ thống |
| Software Life Cycle | Vòng đời dự án phần mềm |
| Systems Analysis | Phân tích hệ thống |
| Systems Design | Thiết kế hệ thống |
| Algorithm | Thuật toán |
| Debugging | Tìm và sửa lỗi |
| Machine Language | Ngôn ngữ máy |
| Assembly Language | Hợp ngữ |
| High-Level Language | Ngôn ngữ bậc cao |
| Compiler | Trình biên dịch |
| Interpreter | Trình thông dịch |
| Object-Oriented Programming | Lập trình hướng đối tượng |
| Markup Language | Ngôn ngữ đánh dấu |
| Scripting Language | Ngôn ngữ kịch bản |

## Câu hỏi ôn tập
1. Systems development là gì?
2. Vòng đời dự án phần mềm gồm những giai đoạn nào?
3. Vì sao cần phân tích hệ thống trước khi viết code?
4. Quy trình lập trình năm bước gồm những bước nào?
5. Compiler khác interpreter như thế nào?
6. Năm thế hệ ngôn ngữ lập trình khác nhau ra sao?
7. Object-oriented programming là gì?
8. Class và object khác nhau thế nào?
9. Markup language khác scripting language như thế nào?
