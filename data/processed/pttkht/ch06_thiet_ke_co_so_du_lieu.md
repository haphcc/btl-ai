# Chương 6: Thiết kế cơ sở dữ liệu

## Nội dung chính
- Mô hình dữ liệu và các loại mô hình dữ liệu.
- Mô hình dữ liệu quan hệ.
- Các dạng chuẩn và chuẩn hóa quan hệ.
- Chuẩn hóa biểu đồ lớp.
- Thiết kế cơ sở dữ liệu vật lý.

## Tổng quan
Chương này trình bày thiết kế cơ sở dữ liệu trong phát triển hệ thống thông tin. Nội dung bắt đầu từ khái niệm mô hình dữ liệu, chuyển sang mô hình quan hệ, chuẩn hóa và cuối cùng là thiết kế vật lý để triển khai trên hệ quản trị cơ sở dữ liệu.

## Mô hình dữ liệu

### Khái niệm mô hình dữ liệu

**Khái niệm chính:**
- Mô hình dữ liệu là cách biểu diễn cấu trúc dữ liệu cho một cơ sở dữ liệu.
- Cấu trúc dữ liệu gồm đối tượng dữ liệu, mối liên hệ giữa dữ liệu, ngữ nghĩa dữ liệu và ràng buộc dữ liệu.
- Mô hình dữ liệu tập trung vào mô tả và tổ chức dữ liệu, không tập trung vào thao tác xử lý.

**Giải thích:**
Mô hình dữ liệu giúp nhóm phát triển và người dùng hiểu dữ liệu nào cần quản lý, các dữ liệu liên hệ với nhau ra sao và có những ràng buộc nghiệp vụ nào.

### Các loại mô hình dữ liệu

**Khái niệm chính:**
- Mô hình dữ liệu quan niệm.
- Mô hình dữ liệu logic.
- Mô hình dữ liệu vật lý.

**Quy trình / Mô hình / Ký hiệu:**
| Loại mô hình | Ý nghĩa |
|---|---|
| Quan niệm | Mô tả dữ liệu ở mức nghiệp vụ, độc lập với công nghệ. |
| Logic | Mô tả dữ liệu gần với cách biểu diễn của hệ quản trị cơ sở dữ liệu. |
| Vật lý | Mô tả cách lưu trữ và triển khai dữ liệu trên công nghệ cụ thể. |

## Mô hình dữ liệu quan hệ

### Quan hệ là bảng

**Khái niệm chính:**
- Trong mô hình quan hệ, dữ liệu được tổ chức thành các bảng.
- Bảng gồm cột và dòng.
- Mỗi dòng biểu diễn một bản ghi; mỗi cột biểu diễn một thuộc tính.

**Giải thích:**
Mô hình quan hệ phổ biến vì dễ hiểu, dễ triển khai và phù hợp với nhiều hệ quản trị cơ sở dữ liệu. Khi thiết kế, cần xác định bảng, khóa, thuộc tính và quan hệ giữa các bảng.

## Các dạng chuẩn và chuẩn hóa quan hệ

### Mục đích chuẩn hóa

**Khái niệm chính:**
- Chuẩn hóa nhằm tạo quan hệ có cấu trúc tốt.
- Mục tiêu là giảm dư thừa dữ liệu và hạn chế bất thường khi thêm, sửa, xóa dữ liệu.

**Giải thích:**
Quan hệ có cấu trúc kém dễ gây lặp dữ liệu, mâu thuẫn dữ liệu và khó bảo trì. Chuẩn hóa giúp thiết kế cơ sở dữ liệu ổn định hơn.

### Các dạng chuẩn

**Quy trình / Mô hình / Ký hiệu:**
| Dạng chuẩn | Ý nghĩa khái quát |
|---|---|
| 1NF | Dữ liệu trong mỗi ô nên là giá trị nguyên tử. |
| 2NF | Loại bỏ phụ thuộc bộ phận vào khóa ghép. |
| 3NF | Loại bỏ phụ thuộc bắc cầu không cần thiết. |

**Lưu ý:**
- Nội dung chuẩn hóa trong slide gắn với mục tiêu xây dựng quan hệ có cấu trúc tốt.

## Chuẩn hóa biểu đồ lớp

### Từ lớp sang dữ liệu

**Khái niệm chính:**
- Biểu đồ lớp có thể được chuyển đổi thành thiết kế dữ liệu.
- Các lớp, thuộc tính và quan hệ cung cấp đầu vào cho thiết kế bảng.

**Giải thích:**
Khi chuyển mô hình hướng đối tượng sang cơ sở dữ liệu quan hệ, cần xem xét cách biểu diễn lớp, quan hệ kế thừa, quan hệ liên kết và cơ số bằng bảng, khóa chính và khóa ngoại.

## Thiết kế cơ sở dữ liệu vật lý

### Nội dung thiết kế vật lý

**Khái niệm chính:**
- Chọn công nghệ lưu trữ và quản lý dữ liệu.
- Chuyển mô hình logic thành thiết kế vật lý.
- Xác định cấu trúc lưu trữ, chỉ mục và các yếu tố hiệu năng.

**Giải thích:**
Thiết kế vật lý phụ thuộc vào hệ quản trị cơ sở dữ liệu và môi trường triển khai. Giai đoạn này xem xét giới hạn công nghệ, thời gian đáp ứng và yêu cầu xử lý.

## Tóm tắt chương
- Mô hình dữ liệu biểu diễn đối tượng dữ liệu, quan hệ, ngữ nghĩa và ràng buộc.
- Có ba mức mô hình dữ liệu: quan niệm, logic và vật lý.
- Mô hình quan hệ biểu diễn dữ liệu bằng bảng.
- Chuẩn hóa giúp giảm dư thừa và tạo quan hệ có cấu trúc tốt.
- Thiết kế vật lý chuyển mô hình logic sang triển khai cụ thể.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Mô hình dữ liệu | Cách biểu diễn cấu trúc dữ liệu cho cơ sở dữ liệu. |
| Mô hình quan niệm | Mô hình dữ liệu ở mức nghiệp vụ, độc lập công nghệ. |
| Mô hình logic | Mô hình dữ liệu gần với cách biểu diễn trong DBMS. |
| Mô hình vật lý | Thiết kế lưu trữ dữ liệu trên công nghệ cụ thể. |
| Mô hình quan hệ | Mô hình tổ chức dữ liệu thành các bảng. |
| Chuẩn hóa | Quá trình cải thiện cấu trúc quan hệ để giảm dư thừa và bất thường dữ liệu. |
| Database design | Thiết kế cơ sở dữ liệu cho hệ thống thông tin. |

## Câu hỏi ôn tập
1. Mô hình dữ liệu là gì?
2. Mô hình dữ liệu gồm những cấu trúc dữ liệu nào?
3. Phân biệt mô hình quan niệm, logic và vật lý.
4. Mô hình dữ liệu quan hệ biểu diễn dữ liệu như thế nào?
5. Vì sao cần chuẩn hóa quan hệ?
6. Nêu ý nghĩa của quan hệ có cấu trúc tốt.
7. Chuẩn hóa biểu đồ lớp liên quan gì đến thiết kế cơ sở dữ liệu?
8. Thiết kế cơ sở dữ liệu vật lý gồm những nội dung nào?
