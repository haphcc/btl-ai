# Chương 6: An ninh mạng

## Nội dung chính
- Các mức bảo vệ an toàn thông tin trên mạng.
- Quyền truy cập và kiểm soát thao tác trên tài nguyên.
- Mã hóa, bảo vệ vật lý và tường lửa.
- Các chiến lược bảo vệ mạng.
- Nguyên tắc least privilege, defence in depth và các nguyên tắc liên quan.

## Tổng quan
An ninh mạng nhằm bảo vệ tài nguyên, dữ liệu và dịch vụ mạng trước truy cập trái phép, phá hoại, mất mát hoặc gián đoạn. Chương này trình bày các lớp bảo vệ từ quyền truy cập, mã hóa, bảo vệ vật lý đến firewall và chiến lược phòng thủ.

## Quyền truy cập

### Kiểm soát quyền

**Khái niệm chính:**
- Quyền truy cập xác định người dùng được thao tác gì trên tài nguyên mạng.
- Quyền có thể áp dụng cho máy trạm, máy chủ, thư mục, chương trình và tập tin dữ liệu.
- Các thao tác thường gặp gồm đọc, thêm, sửa, xóa tập tin.

**Giải thích:**
Không phải mọi người dùng đều cần mọi quyền. Phân quyền đúng giúp hạn chế thiệt hại khi tài khoản bị lạm dụng hoặc người dùng thao tác sai.

## Mã hóa

### Encryption

**Khái niệm chính:**
- Mã hóa biến dữ liệu từ dạng đọc được sang dạng khó hiểu nếu không có khóa.
- Mã hóa bảo vệ dữ liệu khi lưu trữ và truyền trên mạng.
- Chính phủ, doanh nghiệp và cá nhân đều có thể sử dụng mã hóa để bảo vệ thông tin.

**Lưu ý:**
- Mã hóa không thay thế các biện pháp bảo mật khác; nó là một lớp trong hệ thống bảo vệ tổng thể.

## Bảo vệ vật lý

### Mục tiêu bảo vệ

**Khái niệm chính:**
- Bảo vệ phần cứng, dữ liệu và mạng.
- Phòng chống trộm cắp, phá hoại, hỏa hoạn và thiên tai.
- Tạo trở ngại đối với truy cập trái phép.
- Có hệ thống giám sát, thông báo và kế hoạch khôi phục sau sự cố.

**Giải thích:**
Nếu thiết bị bị lấy cắp hoặc phá hủy, các biện pháp bảo mật phần mềm có thể không đủ. Vì vậy an ninh mạng phải bao gồm cả bảo vệ môi trường vật lý.

## Tường lửa

### Firewall

**Khái niệm chính:**
- Firewall có thể là phần mềm hoặc thiết bị phần cứng.
- Chức năng là điều khiển truy cập tài nguyên mạng.
- Firewall ngăn xâm nhập trái phép và lọc luồng dữ liệu độc hại.
- Firewall bảo vệ máy trạm, máy chủ và mạng nội bộ.

**Mô hình / Quy trình / Cấu trúc:**
- Lưu lượng từ bên ngoài đi qua firewall.
- Firewall kiểm tra luật cho phép hoặc chặn.
- Lưu lượng hợp lệ được chuyển tiếp, lưu lượng không hợp lệ bị chặn hoặc ghi log.

## Chiến lược bảo vệ mạng

### Least Privilege

**Khái niệm chính:**
- Người dùng hoặc tiến trình chỉ được cấp quyền tối thiểu cần thiết để thực hiện công việc.
- Nguyên tắc này còn gắn với cách tiếp cận “cần-thì-biết”.

**Ví dụ / Minh họa:**
- Nhân viên chỉ cần xem báo cáo thì không nên có quyền xóa dữ liệu gốc.

### Defence in Depth

**Khái niệm chính:**
- Bảo vệ theo chiều sâu sử dụng nhiều lớp bảo vệ.
- Nếu một lớp bị vượt qua, các lớp khác vẫn tiếp tục bảo vệ hệ thống.

**Ví dụ / Minh họa:**
- Kết hợp phân quyền, mã hóa, firewall, giám sát, sao lưu và bảo vệ vật lý.

### Các nguyên tắc khác

**Mô hình / Quy trình / Cấu trúc:**
| Chiến lược | Ý nghĩa |
|---|---|
| Tính đơn giản | Hệ thống bảo mật càng đơn giản càng dễ kiểm soát lỗi. |
| Nút thắt | Tập trung kiểm soát tại các điểm ra/vào quan trọng. |
| Liên kết yếu nhất | Toàn hệ thống chỉ mạnh bằng điểm yếu nhất của nó. |
| Hỏng an toàn | Khi lỗi xảy ra, hệ thống chuyển về trạng thái an toàn. |
| Đa dạng bảo vệ | Dùng nhiều cơ chế/nhà cung cấp để giảm phụ thuộc vào một điểm yếu. |

## Tóm tắt chương
- An ninh mạng cần kết hợp quyền truy cập, mã hóa, bảo vệ vật lý và firewall.
- Phân quyền giúp giới hạn thao tác của người dùng trên tài nguyên.
- Mã hóa bảo vệ dữ liệu khi lưu trữ và truyền thông.
- Firewall kiểm soát lưu lượng và ngăn truy cập trái phép.
- Các chiến lược như least privilege và defence in depth giúp xây dựng hệ thống bảo vệ bền vững hơn.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Network security | An ninh mạng. |
| Access control | Kiểm soát quyền truy cập. |
| Encryption | Mã hóa dữ liệu. |
| Firewall | Tường lửa kiểm soát lưu lượng mạng. |
| Least privilege | Nguyên tắc cấp quyền tối thiểu cần thiết. |
| Defence in depth | Bảo vệ theo chiều sâu bằng nhiều lớp. |
| Fail-safe | Hỏng an toàn, chuyển về trạng thái an toàn khi lỗi. |
| Need-to-know | Chỉ cung cấp thông tin cho người thực sự cần biết. |

## Câu hỏi ôn tập
1. An ninh mạng nhằm bảo vệ những gì?
2. Quyền truy cập trên mạng có thể áp dụng cho những tài nguyên nào?
3. Mã hóa có vai trò gì trong bảo vệ dữ liệu?
4. Vì sao bảo vệ vật lý vẫn quan trọng trong an ninh mạng?
5. Firewall hoạt động với mục tiêu gì?
6. Nguyên tắc least privilege là gì?
7. Defence in depth khác gì với chỉ dùng một lớp bảo vệ?
8. Vì sao cần chú ý đến liên kết yếu nhất trong hệ thống bảo mật?
