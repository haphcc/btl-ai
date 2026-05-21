# Chương 1: Giới thiệu về lập trình hướng đối tượng

## Nội dung chính
- Các khái niệm nền tảng về kỹ thuật lập trình và ngôn ngữ lập trình.
- Lập trình phi cấu trúc, lập trình có cấu trúc và các hạn chế của lập trình truyền thống.
- Khái niệm lập trình hướng đối tượng.
- Đối tượng, trạng thái, hành vi, thuộc tính, phương thức, lớp và lớp con.
- Lớp trừu tượng, truyền thông điệp, trừu tượng hóa, đóng gói, kế thừa và đa hình.

## Tổng quan
Chương này giới thiệu tư duy lập trình hướng đối tượng (Object-Oriented Programming - OOP). Nội dung bắt đầu từ sự phát triển của kỹ thuật lập trình, sau đó chỉ ra vì sao cần chuyển từ cách tổ chức chương trình theo thủ tục sang cách mô hình hóa hệ thống bằng các đối tượng có trạng thái và hành vi.

## 1.1. Các khái niệm về lập trình hướng đối tượng

### Kỹ thuật lập trình
Kỹ thuật lập trình là kỹ thuật thực thi một giải pháp phần mềm dựa trên cấu trúc dữ liệu, giải thuật, phương pháp luận và một hoặc nhiều ngôn ngữ lập trình phù hợp với yêu cầu đặc thù của ứng dụng.

Phương pháp luận trong lập trình bao gồm:

- Các mô thức lập trình.
- Ý tưởng và thuật toán để giải quyết vấn đề.
- Phong cách trình bày trong lập trình.
- Văn hóa lập trình.

### Ngôn ngữ lập trình
Ngôn ngữ lập trình là phương tiện để con người giao tiếp với máy tính. Một ngôn ngữ lập trình cần có:

- Mô thức hoặc nguyên tắc chung.
- Cú pháp để xác định mã nguồn hợp lệ.
- Ngữ nghĩa để xác định ý nghĩa của chương trình.

Ngôn ngữ máy biểu diễn chỉ thị bằng các chữ số nhị phân `0` và `1`. Ngôn ngữ lập trình bậc cao được chuẩn hóa để cả con người và máy tính có thể đọc, hiểu thông qua chương trình dịch.

### Trình dịch
Trình dịch (Compiler) là chương trình biên dịch toàn bộ chương trình nguồn thành mã máy trước khi thực hiện.

## 1.2. Lập trình phi cấu trúc

Lập trình phi cấu trúc còn được gọi là lập trình tuyến tính. Cách lập trình này phù hợp với bài toán nhỏ và đơn giản.

Đặc điểm:

- Chỉ gồm một chương trình chính.
- Chương trình là một dãy tuần tự các câu lệnh.
- Mã nguồn thường ngắn, ít hơn khoảng 100 dòng.

Nhược điểm:

- Không tái sử dụng được các đoạn mã.
- Không kiểm soát tốt phạm vi truy xuất dữ liệu.
- Dữ liệu thường là toàn cục.
- Dữ liệu có thể bị sửa đổi ở bất cứ vị trí nào trong chương trình.
- Không đáp ứng tốt việc triển khai phần mềm lớn.

## 1.3. Lập trình có cấu trúc

Lập trình có cấu trúc ra đời vào những năm 70. Chương trình được chia nhỏ thành các chương trình con:

- Thủ tục (Procedure).
- Hàm (Function).

Các chương trình con thường độc lập với nhau, có dữ liệu riêng và trao đổi thông tin qua tham số hoặc biến toàn cục. Cách tiếp cận này giúp chương trình rõ hơn so với lập trình tuyến tính, nhưng dữ liệu và xử lý vẫn tách rời nhau.

### Trừu tượng hóa trong lập trình có cấu trúc
Lập trình có cấu trúc bắt đầu xuất hiện khái niệm trừu tượng hóa: quan sát sự vật mà không quan tâm đến các chi tiết không quan trọng bên trong và không quan tâm việc thực hiện cụ thể như thế nào.

Các ngôn ngữ lập trình có cấu trúc được nêu trong slide gồm:

- C.
- Pascal.
- FoxPro.

## 1.4. Lập trình hướng đối tượng

Lập trình hướng đối tượng coi chương trình phần mềm là một tập hợp các đối tượng tương tác với nhau.

Phương pháp lập trình hướng đối tượng có các đặc điểm:

- Mô tả chính xác các đối tượng trong thế giới thực.
- Lấy đối tượng làm nền tảng xây dựng thuật toán.
- Thiết kế xoay quanh dữ liệu của hệ thống.
- Chương trình được chia thành các lớp đối tượng.
- Dữ liệu được đóng gói, che giấu và bảo vệ.
- Đối tượng làm việc với nhau thông qua thông báo.
- Chương trình được thiết kế theo cách từ dưới lên (bottom-up).

Theo nội dung slide, mỗi đối tượng trong chương trình có dữ liệu độc lập, chiếm bộ nhớ riêng và thuộc về một lớp đối tượng cụ thể. Các đối tượng thuộc cùng một lớp có các hành vi giống nhau.

## Đối tượng, trạng thái và hành vi

### Đối tượng trong thế giới thực
Đối tượng có thể là sinh viên, ô tô, xe máy, lớp học, tài khoản ngân hàng hoặc màu sắc. Mỗi đối tượng có:

- Thông tin hoặc trạng thái.
- Hoạt động hoặc hành vi.

**Ví dụ:** Một ô tô có số khung, số máy, hãng sản xuất, màu sắc, tốc độ, năm sản xuất. Các hành vi có thể là tăng ga, phanh, giảm tốc hoặc di chuyển đến một địa điểm.

### Đối tượng phần mềm
Đối tượng phần mềm (object) là một thực thể phần mềm bao bọc các thuộc tính và phương thức liên quan. Trạng thái được biểu diễn bằng thuộc tính (attribute) và quan hệ (relationship). Hành vi được biểu diễn bằng thao tác (operation) hoặc phương thức (method).

**Ví dụ:** Đối tượng quạt điện có thể có trạng thái và hành vi như sau:

| Trạng thái | Hành vi |
|---|---|
| Màu sắc: trắng | Bật quạt |
| Tốc độ: số 2 | Tắt quạt |
| Trạng thái: đang bật | Tăng tốc độ |
| Hướng quay: trái - phải | Giảm tốc độ, quay trái/phải |

## Thuộc tính và phương thức

Thuộc tính có thể gồm:

- Hằng, biến.
- Tham số nội tại.
- Thuộc tính có kiểu dữ liệu cổ điển hoặc kiểu do người dùng định nghĩa.

Phương thức là hàm nội tại của đối tượng, có kiểu trả về và còn được gọi là hàm thành viên.

## Lớp và lớp con

Lớp là tập hợp các đối tượng có cùng thuộc tính và hành vi. Lớp đóng vai trò như bản thiết kế hoặc bản mẫu mô tả cấu trúc dữ liệu gồm:

- Thành phần dữ liệu.
- Phương thức.

Lớp cũng được dùng như một kiểu dữ liệu do người dùng định nghĩa. Lớp con là lớp có thêm tính chất kế thừa đặc tính của lớp khác.

**Ví dụ:** Trong hệ thống nhân viên ngân hàng:

| Lớp | Thuộc tính/Hành vi |
|---|---|
| Nhân viên ngân hàng | Họ tên, mã nhân viên, chức vụ, ngày vào làm; chấm công, nhận lương, tuân thủ quy định |
| Giao dịch viên | Quầy giao dịch, mã quầy; mở tài khoản, nộp/rút tiền, in sao kê |
| Nhân viên tín dụng | Danh sách khách hàng phụ trách, hạn mức phê duyệt; tư vấn khoản vay, thẩm định hồ sơ, giải ngân |
| Nhân viên kiểm soát nội bộ | Phạm vi kiểm soát, báo cáo kiểm toán; kiểm tra chứng từ, phát hiện sai sót, đề xuất khắc phục |

## Lớp trừu tượng

Lớp trừu tượng là lớp không thể trở thành một lớp thực tế cụ thể. Nó được thiết kế để tạo ra lớp có đặc tính tổng quát. Bản thân lớp trừu tượng chưa có ý nghĩa đầy đủ để tạo đối tượng trực tiếp.

**Ví dụ:** Trong hệ thống quản lý phương tiện giao thông, lớp `PhuongTien` có thể quy định mọi phương tiện phải có hàm `diChuyen()`, nhưng không mô tả cách di chuyển cụ thể. Xe đạp, ô tô hoặc tàu thủy sẽ tự định nghĩa cách di chuyển riêng.

## Truyền thông điệp

Thông điệp là phương tiện để một đối tượng chuyển yêu cầu đến đối tượng khác. Một thông điệp gồm:

- Handle của đối tượng đích.
- Tên phương thức cần thực hiện.
- Các thông tin cần thiết khác, tức tham số.

Quá trình xử lý thông điệp:

1. Gửi thông báo và tham số cho đối tượng.
2. Kiểm tra tính hợp lệ của thông báo.
3. Gọi hàm tương ứng với phương thức.

**Ví dụ:** Khách hàng rút tiền tại ATM. Thông điệp gửi đến máy ATM gồm yêu cầu `rutTien()`, số tiền cần rút và mã PIN. ATM kiểm tra mã PIN, kiểm tra số dư, sau đó nếu hợp lệ thì nhả tiền và in biên lai.

## Một số cơ chế trong lập trình hướng đối tượng

### Trừu tượng hóa
Trừu tượng hóa là khả năng bỏ qua các thành phần không quan trọng và chỉ tập trung vào đặc điểm cần thiết.

Có hai loại trừu tượng hóa:

- Trừu tượng hóa dữ liệu: che giấu chi tiết cách dữ liệu được lưu trữ.
- Trừu tượng hóa chức năng: che giấu cách một hành động được thực hiện.

**Ví dụ:** Khi dùng ứng dụng ngân hàng và thấy số dư, người dùng không cần biết dữ liệu được lưu trong SQL, dạng nhị phân hay trên nhiều máy chủ dự phòng.

### Đóng gói
Đóng gói là cơ chế ràng buộc dữ liệu và các thao tác trên dữ liệu thành một thể thống nhất.

Đóng gói gồm:

- Bao gói: người dùng giao tiếp với hệ thống qua giao diện.
- Che giấu: ngăn chặn thao tác không được phép từ bên ngoài.

Ưu điểm:

- Quản lý sự thay đổi.
- Bảo vệ dữ liệu.

**Ví dụ:** Với ATM, người dùng chỉ nhập thẻ, mã PIN và số tiền. Các quy trình xác thực, kiểm tra số dư, kết nối ngân hàng được đóng gói bên trong.

### Kế thừa
Kế thừa là khả năng xây dựng lớp mới thừa hưởng thuộc tính của lớp đã có. Lớp nhận được có thể bổ sung thành phần mới hoặc định nghĩa lại thành phần của lớp cha.

Các loại kế thừa:

- Đơn kế thừa.
- Đa kế thừa.

### Đa hình
Đa hình là khả năng đưa một phương thức có cùng tên vào các lớp con nhưng thực hiện theo các cách khác nhau.

Đa hình được thực hiện bởi:

- Định nghĩa lại.
- Nạp chồng.

Cơ chế đa hình dựa trên:

- Kết gán sớm.
- Kết gán muộn.

## Tóm tắt chương
- Lập trình hướng đối tượng mô hình hóa chương trình thành các đối tượng tương tác với nhau.
- Đối tượng có trạng thái và hành vi; lớp là bản mẫu của các đối tượng cùng kiểu.
- Lập trình phi cấu trúc và lập trình có cấu trúc có nhiều hạn chế khi hệ thống lớn và cần bảo trì.
- Các cơ chế quan trọng của OOP gồm trừu tượng hóa, đóng gói, kế thừa và đa hình.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Object | Đối tượng, thực thể phần mềm có thuộc tính và phương thức |
| Class | Lớp, bản thiết kế cho các đối tượng cùng kiểu |
| Attribute | Thuộc tính biểu diễn trạng thái của đối tượng |
| Method | Phương thức biểu diễn hành vi của đối tượng |
| Abstract class | Lớp trừu tượng, không tạo đối tượng trực tiếp |
| Encapsulation | Đóng gói dữ liệu và thao tác |
| Inheritance | Kế thừa đặc điểm từ lớp đã có |
| Polymorphism | Đa hình, cùng tên phương thức nhưng hành vi khác nhau |
| Message | Thông điệp gửi yêu cầu từ đối tượng này đến đối tượng khác |

## Câu hỏi ôn tập
1. Kỹ thuật lập trình là gì?
2. Lập trình phi cấu trúc có những hạn chế nào?
3. Vì sao lập trình có cấu trúc vẫn chưa giải quyết triệt để vấn đề dữ liệu và xử lý?
4. Đối tượng phần mềm gồm những thành phần nào?
5. Phân biệt trạng thái và hành vi của đối tượng.
6. Lớp và lớp con có quan hệ như thế nào?
7. Trừu tượng hóa dữ liệu và trừu tượng hóa chức năng khác nhau ra sao?
8. Đóng gói giúp bảo vệ dữ liệu như thế nào?
9. Kế thừa và đa hình có vai trò gì trong OOP?
