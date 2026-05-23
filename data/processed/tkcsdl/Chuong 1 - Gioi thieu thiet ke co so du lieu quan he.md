# CHƯƠNG 1
# GIỚI THIỆU THIẾT KẾ CƠ SỞ DỮ LIỆU QUAN HỆ

# NỘI DUNG CHÍNH

- 1.1 Hệ thống thông tin
- 1.2 Chu trình phát triển các hệ thống thông tin
- 1.3 Vòng đời của cơ sở dữ liệu
- 1.4 Chiến lược thiết kế cơ sở dữ liệu
- 1.5 Hệ quản trị cơ sở dữ liệu
- 1.6 Hướng dẫn sinh viên thực hiện bài tập lớn

# 1.1. Hệ thống thông tin

- **Con người**
- **Dữ liệu**
- **Phương pháp & quy trình**
- **Phần cứng**
- **Phần mềm**

IS

## Gồm 5 thành phần cơ bản

- **Phần cứng** – Những thiết bị vật lý của hệ thống như máy tính, máy chủ, máy in, thiết bị mạng và các thiết bị khác
- **Phần mềm** – những chương trình, ứng dụng chạy trên các thiết bị phần cứng bao gồm hệ điều hành, hệ quản trị cơ sở dữ liệu, phần mềm ứng dụng
- **Dữ liệu** – Thông tin được xử lý, lưu trữ và truy xuất bởi hệ thống
- **Quy trình** - Các phương pháp và bước để nhập, xử lý, lưu trữ và truy xuất dữ liệu trong hệ thống.
- **Con người** - Các cá nhân sử dụng, quản lý và bảo trì hệ thống thông tin, bao gồm người dùng, quản trị viên và nhân viên IT

![Sơ đồ quy trình: Data -> Application code -> Information -> Decisions](https://i.imgur.com/5y1yY1O.png)

- Tất cả các ứng dụng (Application) gồm hai thành phần: **dữ liệu** và **mã lệnh**.
- **Dữ liệu** và **mã lệnh** được kết hợp cùng nhau để biểu diễn các chức năng và hoạt động của tổ chức, tạo ra **thông tin** hỗ trợ quá trình ra **quyết định**.

**Hiệu quả của một hệ thống thông tin phụ thuộc vào ba yếu tố**

- Thiết kế và triển khai cơ sở dữ liệu
- Thiết kế và triển khai ứng dụng
- Quy trình quản lý

# 1.2. Chu trình phát triển HTTT

- **Lập kế hoạch**
    - Xác định phạm vi
    - Xác định tính khả thi của dự án

- **Phân tích**
    - Tìm hiểu yêu cầu người dùng
    - Đánh giá hệ thống cũ
    - Thiết kế mức logic

- **Thiết kế chi tiết**
    - Cụ thể hóa từng thành phần

- **Cài đặt**
    - Lập trình
    - Kiểm thử
    - Hiệu chỉnh

- **Bảo trì và vận hành**

**LẬP KẾ HOẠCH:**

- **Cần trả lời các câu hỏi**
    - Nên tiếp tục/chỉnh sửa/thay thế hệ thống thông tin hiện tại?
- **Nếu cần thay thế hệ thống cũ bằng hệ thống mới thì cần xác định phạm vi**
    - Kỳ vọng về khả năng của hệ thống mới về cả phần cứng và phần mềm?
    - Chi phí xây dựng hệ thống?
    - Chi phí vận hành hệ thống?

Ví dụ

# Hãy đề xuất các câu hỏi để xác định kế hoạch xây dựng hệ thống thông tin cho trường hợp sau:

Chị A đang có một cửa hàng, chị đang dùng một phần mềm quản lý bán hàng: giúp chị quản lý hàng tồn, doanh thu, nhập/xuất của cửa hàng. Chị A đang muốn thành lập một chuỗi cửa hàng vào năm tới, hãy xây dựng một hệ thống giúp chị A kiểm tra tình trạng kinh doanh của tất cả các cơ sở trong chuỗi cửa hàng tại bất kỳ thời điểm.

## PHÂN TÍCH:
- **Cần trả lời các câu hỏi**
    - Yêu cầu của người dùng là gì?
    - Những yêu cầu này có phù hợp?
- **Mục tiêu**
    - Tạo ra được một bản thiết kế logic
        - Xác định được các yêu cầu người dùng
        - Xác định được các biểu mẫu liên quan
        - Xác định được các chức năng cần xây dựng, input, output tương ứng
        - Xác định dữ liệu cần lưu trữ
        - Xác định được mô hình dữ liệu mức khái niệm: thực thể, mối quan hệ giữa các thực thể

- **THIẾT KẾ CHI TIẾT**: Thiết kế CSDL, thiết kế giao diện, menu, báo cáo, các thiết bị có thể được sử dụng để hệ thống được khai thác hiệu quả (vd: máy in, máy scan, loa,...)

**CÀI ĐẶT:**

- **Chuẩn bị cơ sở hạ tầng:** Các thiết bị phần cứng, hệ điều hành, hệ quản trị cơ sở dữ liệu, các phần mềm hỗ trợ lập trình, cơ sở dữ liệu đã thiết kế cũng được thực thi.
- **Xây dựng các tính năng của hệ thống**
    - Lập trình viên: xây dựng tính năng
    - Tester: Kiểm thử tính đúng (giao diện, dữ liệu, quy trình), kiểm thử hiệu năng

## BẢO TRÌ VÀ VẬN HÀNH

Khi hệ thống hoạt động, người dùng sẽ bắt đầu đưa ra những yêu cầu. Những yêu cầu này tạo ra hoạt động bảo trì hệ thống, chúng có thể được phân loại thành ba loại:

- Bảo trì sửa chữa để giải quyết lỗi hệ thống.
- Bảo trì tự động theo sự thay đổi của môi trường nghiệp vụ triển khai.
- Bảo trì hoàn thiện để tăng cường khả năng của hệ thống.

# 1.3. Vòng đời phát triển CSDL

- **Khởi tạo**
    - Tìm hiểu công ty
    - Xác định bài toán và các ràng buộc
    - Xác định mục tiêu

- **Thiết kế**
    - Thiết kế mức khái niệm
    - Lựa chọn hệ quản trị CSDL
    - Thiết kế logic
    - Thiết kế vật lý

- **Thực thi**
    - Cài đặt hệ quản trị CSDL
    - Tạo CSDL
    - Chuyển đổi/tạo dữ liệu

- **Kiểm thử & đánh giá**
    - Kiểm thử CSDL
    - Tối ưu hóa CSDL
    - Đánh giá CSDL và ứng dụng

- **Vận hành**
    - Chạy CSDL thật

- **Bảo trì**
    - Thực hiện các thay đổi
    - Nâng cấp CSDL

## KHỞI TẠO

- **Tìm hiểu công ty**: Cơ cấu tổ chức, nhiệm vụ mỗi thành viên, mong muốn của tổ chức
- **Xác định bài toán và các ràng buộc**: Hệ thống có các chức năng gì, chức năng này được tham gia bởi ai, thứ tự thực hiện, ràng buộc nghiệp vụ
- **Xác định mục tiêu**: Mục tiêu của hệ thống là gì, thông tin cần lưu trữ là gì, dữ liệu của hệ thống có được chia sẻ cho các hệ thống hay người dùng bên ngoài hay không
- **Xác định phạm vi**: Phạm vi công việc, thời gian, chi phí

## THIẾT KẾ:

- **Thiết kế mức khái niệm**: Xác định các thực thể, mối quan hệ giữa các thực thể trong hệ thống (ERM)
- **Lựa chọn hệ quản trị CSDL**

- **Thiết kế logic:**
    - Ánh xạ thiết kế mức khái niệm sang logic (bảng, ràng buộc).
    - Chuẩn hóa cơ sở dữ liệu.
    - Kiểm tra tính logic của các ràng buộc.
    - Kiểm tra sự đáp ứng của CSDL với yêu cầu của người dùng.

- **Thiết kế vật lý:**
    - Định nghĩa cách tổ chức dữ liệu: bảng, cột, chỉ mục – index, view
    - Định nghĩa các biện pháp bảo mật: người dùng, nhóm người dùng, quyền truy cập.
    - Định nghĩa các biện pháp đo lường hiệu năng.

**THỰC THI:**

- **Cài đặt hệ quản trị CSDL**
- **Tạo CSDL**
- **Chuyển đổi/tạo dữ liệu**: Tạo dữ liệu cho hệ thống: Danh mục địa bàn hành chính, danh mục sản phẩm, danh mục người dùng,...

- **KIỂM THỬ, ĐÁNH GIÁ:**
    - Quyền truy cập
    - Tính đúng đắn của dữ liệu đã được thực thi
- **Tối ưu hóa CSDL:** Kiểm tra các yếu tố ảnh hưởng tới tốc độ CSDL
- **Đánh giá CSDL và ứng dụng**
    - Thiết kế phương án backup cơ sở dữ liệu, thực hiện test sao lưu, phục hồi
    - Transaction log backup

# 1.4. Chiến lược thiết kế CSDL

[Sơ đồ: Mô hình khái niệm -> Thực thể -> Thuộc tính]

- **Top-down** bắt đầu bằng cách xác định các tập dữ liệu và sau đó xác định các thành phần dữ liệu cho từng tập hợp đó. Quá trình này liên quan đến việc xác định các loại thực thể khác nhau và định nghĩa các thuộc tính của từng thực thể.
- **Bottom-up** trước tiên xác định các thành phần dữ liệu và sau đó nhóm chúng lại với nhau trong tập dữ liệu. Trong nói cách khác, trước tiên nó xác định các thuộc tính, sau đó nhóm chúng lại để tạo thành các thực thể.

# Bài tập: Lựa chọn chiến lược thiết kế

- **Ví dụ 1**: Trường đại học A cần lưu trữ thông tin của sinh viên, khoa, môn học, lớp và điểm kết thúc học phần của sinh viên, thông tin về sinh viên bao gồm ...
- **Ví dụ 2**: Trường Đại học A muốn lưu trữ thông tin học tập của sinh viên để dễ dàng tra cứu thông tin. Các báo cáo sau cần lập vào cuối kỳ

| Lớp: | | Giáo viên: | |
| :--- | :--- | :--- | :--- |
| **Môn:** | thiết kế cơ sở dữ liệu | **Thời gian học:** | |
| **STT** | **Mã SV** | **Họ Tên** | **Điểm** |
| 1 | 24A4001 | Nguyễn văn A | 9 |
| 2 | 24A4002 | Nguyễn Thị B | 8 |
| .. | ... | ... | ... |

# 1.5. Hệ quản trị CSDL

- **Hệ quản trị CSDL (database management system – DBMS) là tập hợp các phần mềm giúp tạo CSDL và cung cấp cơ chế lưu trữ, truy cập theo các mô hình CSDL.**
- **Ví dụ:**
    - SQL Server, MS Access, Oracle là hệ quản trị CSDL điển hình cho mô hình quan hệ.
    - IMS của IBM là hệ quản trị CSDL cho mô hình phân cấp
    - IDMS là hệ quản trị CSDL cho mô hình mạng
    - ...

**Lợi ích mà DBMS mang lại:**

- Quản trị CSDL
- Cung cấp giao diện làm việc để che dấu các đặc tính phức tạp về mặt cấu trúc tổ chức dữ liệu vật lý
- Hỗ trợ ngôn ngữ giao tiếp CSDL
- Có cơ chế bảo mật an toàn

## Tại sao DBMS lại phổ biến?

- Dễ dàng định nghĩa, duy trì và thao tác dữ liệu lưu trữ
- Trích xuất dữ liệu dễ dàng
- Dữ liệu được chuẩn hóa và bảo vệ tốt
- Nhiều nhà cung cấp phần mềm
- Dễ dàng chuyển đổi giữa nhà cung cấp và nhà triển khai
- Là sản phẩm trưởng thành và ổn định

**Các chức năng chính của một DBMS:**

- Data dictionary management
- Data storage management
- Data transformation and presentation
- Security management
- Multiuser access control.
- Backup and recovery management
- Data integrity management
- Database access languages and application programming interfaces
- Database communication interfaces.

**Lựa chọn DBMS trong quá trình thiết kế:**

- **Phụ thuộc vào mục tiêu của hệ thống**
    - Phục vụ hoạt động giao dịch
    - Phục vụ hoạt động báo cáo
- **Phụ thuộc vào lượng dữ liệu lưu trữ**
- **Phụ thuộc yêu cầu tốc độ của hệ thống**
- **Lựa chọn DBMS theo mô hình dữ liệu nào cần phải thiết kế cơ sở dữ liệu theo mô hình đó**
- **Môn học này hướng dẫn thiết kế theo mô hình CSDL quan hệ**

# 1.6. Hướng dẫn thực hiện BTL

**Tham khảo các hệ thống sau**

1. Hệ thống thương mại điện tử: Shoppee, Lazada, tiki, fptshop,
2. Hệ thống booking: Vé máy bay, khách sạn, tour du lịch, grap,..
3. Hệ thống đăng tin giao vặt: batdongsan.com.vn; meeyland, homedy, chotot, zaloshop,
4. Hệ thống quản lý giao dịch trên mobile banking, hoặc một nghiệp vụ nào đó tại ngân hàng
5. Hệ thống vì mục đích cộng đồng: quản lý quỹ từ thiện, xây dựng kho dữ liệu tiếng nói,...
6. Hệ thống mạng xã hội: Facebook, Twitter,..
7. Hệ thống chating: FB message,
8. Hệ thống quản lý nội dung: Dân trí.com
9. Hệ thống quản lý tổ chức: Nhân sự, lương, kế toán, sinh viên, thư viện, cửa hàng, siêu thị
10. ...

# 1.6. Hướng dẫn thực hiện BTL

- **Tạo nhóm 4 - 5 thành viên**
- **Hạn đăng ký: (buổi học thứ 2)**
- **Thông tin đăng ký: Thông tin thành viên, tên đề tài, 1 bài viết nhỏ trả lời các câu hỏi (Tối thiểu 250 từ)**
    - Hệ thống lựa chọn để thiết kế cơ sở dữ liệu được tạo ra nhằm mục đích gì?
    - Hệ thống này được sử dụng bởi ai, họ phụ trách làm công việc gì?
    - Hệ thống quản lý những dữ liệu nào?
