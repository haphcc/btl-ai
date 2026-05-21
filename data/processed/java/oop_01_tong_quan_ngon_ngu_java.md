# Bài 1: Tổng quan ngôn ngữ Java

## Nội dung chính
- Lịch sử hình thành và phát triển của Java.
- Các đặc trưng chính của Java.
- Java như một ngôn ngữ lập trình, môi trường phát triển và môi trường thực thi.
- Các công nghệ Java: J2SE, J2EE, J2ME.
- Các dạng ứng dụng Java.
- Bộ công cụ JDK, máy ảo Java JVM và môi trường phát triển IDE.
- Cài đặt JDK và thiết lập môi trường làm việc.

## Tổng quan
Java là ngôn ngữ lập trình hướng đối tượng được thiết kế để có thể chạy trên nhiều nền tảng khác nhau. Điểm quan trọng của Java là chương trình nguồn được biên dịch thành `bytecode`, sau đó được thực thi thông qua máy ảo Java (Java Virtual Machine - JVM).

## Lịch sử phát triển của Java

### Bối cảnh ra đời
Cuối năm 1990, Sun Microsystems giao cho James Gosling và nhóm kỹ sư xây dựng phần mềm cho các thiết bị điện tử tiêu dùng như đầu video, lò nướng và thiết bị cầm tay. Khi đó, C++ có hạn chế là chương trình phải biên dịch lại cho từng hệ thống xử lý khác nhau.

Để giải quyết vấn đề này, nhóm phát triển tạo ra một ngôn ngữ mới dựa trên cú pháp C/C++, ban đầu có tên là Oak. Ngôn ngữ này hướng đến tính độc lập nền tảng, nghĩa là cùng một chương trình có thể chạy trên nhiều hệ thống khác nhau.

Năm 1993, Internet và World Wide Web phát triển mạnh. Sun chuyển hướng Oak thành môi trường lập trình cho Internet. Năm 1995, Oak được đổi tên thành Java.

### Ứng dụng của Java
Java ban đầu được dùng cho thiết bị điện tử thông minh và các trang web động thông qua `applet`. Sau đó Java được sử dụng rộng rãi trong:

- Cơ sở dữ liệu.
- Mạng máy tính và Internet.
- Trò chơi.
- Viễn thông.
- Ứng dụng doanh nghiệp.
- Ứng dụng desktop, web, mobile và nhúng.

## Các đặc trưng của Java

### Đơn giản
Java có cú pháp gần với C++ nhưng loại bỏ nhiều thành phần phức tạp:

- Không quản lý bộ nhớ thủ công theo kiểu C/C++.
- Không sử dụng con trỏ trực tiếp.
- Không hỗ trợ nạp chồng toán tử.
- Không dùng `include`, `struct`, `union` như C/C++.

### Khả chuyển
Trình biên dịch Java tạo ra `bytecode` độc lập với nền tảng. Nhờ đó, chương trình Java có thể chạy trên các hệ thống khác nhau nếu có JVM phù hợp.

### Hướng đối tượng
Java là ngôn ngữ lập trình hướng đối tượng. Chương trình Java được tổ chức trong các lớp. Ngay cả phương thức `main` cũng phải nằm trong một lớp.

Java không hỗ trợ đa kế thừa lớp như C++, nhưng sử dụng `interface` để đạt được khả năng mở rộng tương tự trong nhiều trường hợp.

### Phân tán
Java hỗ trợ xây dựng ứng dụng phân tán trên mạng. Các công nghệ như RMI, CORBA và JavaBean cho phép tái sử dụng lớp, gọi phương thức hoặc truy cập đối tượng từ xa.

### Đa luồng
Java cho phép tạo nhiều luồng thực thi. Các luồng có thể chạy song song và tương tác với nhau trong cùng một chương trình.

### Bảo mật
Java có nhiều lớp bảo mật:

- Cơ chế đóng gói của ngôn ngữ.
- Không cho truy cập trực tiếp vào bộ nhớ.
- Trình biên dịch kiểm tra mã nguồn.
- Trình thông dịch kiểm tra `bytecode`.
- Bộ nạp lớp kiểm tra lớp trước khi đưa vào môi trường thực thi.

### Biên dịch và thông dịch
Chương trình Java được biên dịch từ file `.java` thành file `.class` chứa `bytecode`. Khi chạy, JVM thông dịch hoặc thực thi `bytecode` trên nền tảng cụ thể.

```bash
javac Hello.java
java Hello
```

### Thu gom rác
Java có cơ chế thu gom rác (Garbage Collection). Cơ chế này theo dõi vùng nhớ đã cấp phát và tự động giải phóng vùng nhớ không còn được sử dụng.

## Java như một công nghệ

Java không chỉ là ngôn ngữ lập trình mà còn gồm:

- Ngôn ngữ lập trình Java.
- Môi trường phát triển.
- Môi trường thực thi và triển khai ứng dụng.

## Các công nghệ Java

| Công nghệ | Vai trò |
|---|---|
| J2SE | Xây dựng ứng dụng desktop, ứng dụng chuẩn và ứng dụng client-server |
| J2EE | Xây dựng ứng dụng doanh nghiệp, servlet, JSP, XML và hệ thống server |
| J2ME | Xây dựng ứng dụng cho thiết bị di động, PDA và hệ thống nhúng |

## Các dạng ứng dụng Java

### Ứng dụng console
Ứng dụng console chạy ở chế độ văn bản. Đây là dạng phù hợp cho người mới học vì giúp tập trung vào cú pháp, thuật toán và cấu trúc chương trình.

### Applet
Applet là chương trình Java nhúng trong trình duyệt. Dạng ứng dụng này từng được dùng để tạo nội dung web động, nhưng về sau ít phổ biến hơn do sự thay đổi của công nghệ trình duyệt.

### Ứng dụng GUI
Java hỗ trợ xây dựng giao diện người dùng bằng AWT và Swing. Swing cung cấp nhiều thành phần giao diện phong phú hơn AWT.

### Ứng dụng web và phân tán
Java có thể xây dựng ứng dụng web bằng Servlet, JSP và các công nghệ mạng như Socket, JavaBean, RMI, CORBA, EJB.

### Ứng dụng cơ sở dữ liệu
Java có thể kết nối với nhiều hệ quản trị cơ sở dữ liệu như Oracle, SQL Server, Microsoft Access và MySQL.

## JDK, JVM và IDE

### JDK
JDK (Java Development Kit) là bộ công cụ phát triển Java. JDK gồm:

- Thư viện lớp.
- Trình biên dịch.
- Công cụ gỡ lỗi.
- JRE để chạy chương trình.

Một số công cụ trong JDK:

| Công cụ | Chức năng |
|---|---|
| `javac` | Biên dịch file `.java` thành `.class` |
| `java` | Chạy chương trình Java |
| `appletviewer` | Chạy applet |
| `javadoc` | Tạo tài liệu từ chú thích mã nguồn |
| `jdb` | Gỡ lỗi chương trình |
| `javap` | Xem thông tin lớp đã biên dịch |
| `jar` | Đóng gói file Java |

### JVM
JVM (Java Virtual Machine) tạo môi trường thực thi cho chương trình Java. JVM nạp file `.class`, quản lý bộ nhớ và thực hiện thu gom rác.

JVM phụ thuộc vào nền tảng cụ thể, nhưng chương trình Java sau khi biên dịch thành `bytecode` có thể chạy trên các JVM khác nhau.

### IDE
IDE (Integrated Development Environment) là môi trường phát triển tích hợp, cung cấp công cụ soạn thảo, biên dịch, liên kết, chạy và gỡ lỗi chương trình.

Các IDE thường dùng cho Java:

- NetBeans.
- Eclipse.
- Visual Studio Code.

## Cài đặt môi trường Java

### Phần mềm cần có
- JDK 21.
- NetBeans, Eclipse hoặc Visual Studio Code.

### Trình tự cài đặt
1. Cài đặt JDK.
2. Thiết lập biến môi trường `PATH` và `CLASSPATH`.
3. Cài đặt IDE.
4. Tạo, biên dịch và chạy chương trình Java đầu tiên.

**Ví dụ:** Thiết lập đường dẫn đến thư mục `bin` của JDK.

```bash
set PATH=C:\Program Files\Java\jdk21\bin
```

**Giải thích:** Biến `PATH` giúp hệ điều hành tìm thấy các lệnh như `javac` và `java` khi biên dịch hoặc chạy chương trình từ dòng lệnh.

## Tóm tắt bài
- Java được phát triển từ nhu cầu tạo phần mềm có tính độc lập nền tảng.
- Chương trình Java được biên dịch thành `bytecode` và chạy trên JVM.
- Java có các đặc trưng: đơn giản, khả chuyển, hướng đối tượng, phân tán, đa luồng, bảo mật và có thu gom rác.
- JDK cung cấp công cụ phát triển, JVM cung cấp môi trường thực thi, IDE hỗ trợ lập trình thuận tiện hơn.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| `bytecode` | Mã trung gian được tạo ra sau khi biên dịch chương trình Java |
| JVM | Máy ảo Java dùng để chạy `bytecode` |
| JDK | Bộ công cụ phát triển Java |
| JRE | Môi trường chạy chương trình Java |
| IDE | Môi trường phát triển tích hợp |
| Garbage Collection | Cơ chế tự động giải phóng bộ nhớ không còn sử dụng |
| J2SE | Nền tảng Java cho ứng dụng chuẩn và desktop |
| J2EE | Nền tảng Java cho ứng dụng doanh nghiệp |
| J2ME | Nền tảng Java cho thiết bị di động và nhúng |

## Câu hỏi ôn tập
1. Vì sao Java được thiết kế để độc lập nền tảng?
2. `bytecode` là gì và có vai trò gì trong Java?
3. Trình bày vai trò của JVM trong quá trình chạy chương trình Java.
4. JDK gồm những công cụ nào?
5. Java khác C++ ở những điểm nào theo nội dung bài học?
6. Hãy nêu các dạng ứng dụng có thể xây dựng bằng Java.
7. Vì sao Java được xem là ngôn ngữ lập trình hướng đối tượng?
