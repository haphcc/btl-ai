![Logo Học viện Ngân hàng](https://upload.wikimedia.org/wikipedia/vi/thumb/a/a5/Logo_Hoc_vien_Ngan_hang.svg/1200px-Logo_Hoc_vien_Ngan_hang.svg.png)

# CHƯƠNG 2
# KIỂU KIẾN TRÚC PHẦN MỀM

Hà Nội - 2026

# Nội dung trình bày

- Một số khái niệm
- Phân loại Kiểu Kiến trúc phần mềm
- Giới thiệu một số Kiểu kiến trúc phần mềm

# Kiểu Kiến trúc phần mềm

- Kiểu kiến trúc phần mềm được định nghĩa là một cách tổ chức và thiết kế các thành phần của một hệ thống phần mềm.
- Kiểu kiến trúc phần mềm bao gồm:
    - Cấu trúc tổ chức của hệ thống
    - Các quy tắc và chuẩn cho việc tương tác giữa các thành phần
    - Các quyết định về cách dữ liệu được lưu trữ, xử lý và truyền tải
- Kiểu kiến trúc phần mềm không chỉ là một khung cảnh về cấu trúc, mà còn đặt ra các nguyên tắc hướng dẫn việc xây dựng, triển khai, và duy trì hệ thống phần mềm.

# Kiểu Kiến trúc phần mềm

- Một số khía cạnh chính của Kiểu kiến trúc phần mềm:
    - **Cấu trúc Tổ chức**: Quyết định cách hệ thống được tổ chức thành các thành phần khác nhau và cách chúng tương tác với nhau. Các kiến trúc thường được biểu diễn dưới dạng biểu đồ hoặc mô hình.
    - **Quyết định Kiến trúc**: Bao gồm các quyết định lớn về nền tảng công nghệ, ngôn ngữ lập trình, kiểu cơ sở dữ liệu, và các quy tắc tổ chức chung.
    - **Mô hình Dữ liệu**: Định nghĩa cách dữ liệu được tổ chức, lưu trữ và truy cập. Bao gồm cả cấu trúc cơ sở dữ liệu và cách dữ liệu di chuyển qua hệ thống.

# Kiểu Kiến trúc phần mềm

- Một số khía cạnh chính của Kiểu kiến trúc phần mềm:
    - **Giao diện Người dùng**: Đặc tả cách người dùng tương tác với hệ thống. Bao gồm cả giao diện người dùng và các thành phần liên quan.
    - **Bảo trì và Mở rộng**: Định nghĩa cách hệ thống có thể được bảo trì và mở rộng trong tương lai. Bao gồm cả khả năng thêm mới các tính năng và thay đổi mà không ảnh hưởng đến toàn bộ hệ thống.
    - **Hiệu suất và Độ tin cậy**: Bao gồm các quyết định về hiệu suất hệ thống và khả năng đảm bảo tính tin cậy và ổn định.

Kiến trúc phần mềm đóng vai trò quan trọng trong việc đảm bảo sự hiểu rõ và quản lý chặt chẽ của một dự án phần mềm, giúp tăng tính linh hoạt, tái sử dụng mã nguồn và giảm rủi ro trong quá trình phát triển và duy trì hệ thống.

# Phân loại Kiểu Kiến trúc phần mềm (1)

- Phân loại Kiểu kiến trúc phần mềm:
    - Hệ thống luồng dữ liệu (DataFlow Systems):
        - Tuần tự hàng loạt (Batch sequential); đường ống (Pipes) và bộ lọc (Filters);...
    - Hệ thống Gọi và Trả về (Call & Return Systems):
        - Chương trình chính (Main program) và Chương trình con (Subroutine); hệ thống hướng đối tượng (OO systems);...
    - Các thành phần độc lập (Independent components):
        - Quy trình giao tiếp (Communicating process); Hệ thống sự kiện (Event systems)

## Nội dung trình bày
- Một số khái niệm
- Phân loại Kiểu Kiến trúc phần mềm
- Giới thiệu một số Kiểu kiến trúc phần mềm

# Hệ thống Luồng dữ liệu (DataFolow Systems)

## Kiểu kiến trúc tuần tự hàng loạt

# Kiểu kiến trúc tuần tự hàng loạt

- Kiểu kiến trúc tuần tự hàng loạt:
    - Đây là một kiểu kiến trúc trong lập trình và xử lý dữ liệu, trong đó các công việc hoặc nhiệm vụ được thực hiện theo từng lô (batch) một. Thay vì thực hiện công việc một cách đồng thời hoặc liên tục, kiến trúc này tập trung vào việc chia công việc thành các nhóm và thực hiện chúng tuần tự.
    - Đây là một trong những kiểu lâu đời nhất trong thiết kế hệ thống máy tính. Nó xuất hiện trong những ngày đầu của quá trình xử lý dữ liệu khi những hạn chế của thiết bị máy tính đòi hỏi các vấn đề lớn phải được chia thành các thành phần có thể tách rời và có thể giao tiếp bằng cách truyền băng từ.

---

### Sơ đồ minh họa quy trình (Data flow & Data transformation)

* **Data transformation (Biến đổi dữ liệu):** Gồm các bước `validate`, `sort`, `Update`, `Report`.
* **Luồng dữ liệu (Data flow):**
  `tape` $\rightarrow$ `validate` $\rightarrow$ `tape` $\rightarrow$ `sort` $\rightarrow$ `tape` $\rightarrow$ `Update` $\rightarrow$ `tape` $\rightarrow$ `Report` $\rightarrow$ `report`
  *(Trong đó, bước `Update` có liên kết tương tác với một `tape` khác ở phía dưới)*
