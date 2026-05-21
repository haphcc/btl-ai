# Chương 8: Kiểm thử hệ thống

## Nội dung chính
- Khái niệm và mục tiêu kiểm thử.
- Các loại lỗi trong kiểm thử.
- Những tài liệu cần thiết trước khi kiểm thử.
- Tiến trình kiểm thử.
- Nguyên tắc, cấp độ và chiến lược kiểm thử phần mềm.

## Tổng quan
Chương này trình bày kiểm thử hệ thống trong giai đoạn triển khai và vận hành. Kiểm thử nhằm phát hiện lỗi càng sớm càng tốt, bảo đảm hệ thống vận hành như mong đợi và phù hợp với thiết kế.

## Khái niệm kiểm thử

### Định nghĩa

**Khái niệm chính:**
- Theo IEEE, kiểm thử phần mềm là quá trình khảo sát một thành phần hoặc hệ thống dưới điều kiện xác định để quan sát và đánh giá một khía cạnh của hệ thống.
- Theo `The Art of Software Testing`, kiểm thử là quá trình thực thi chương trình với mục đích tìm lỗi.

**Giải thích:**
Kiểm thử không chỉ nhằm chứng minh phần mềm chạy được, mà quan trọng hơn là tìm ra lỗi, sai lệch và rủi ro trước khi hệ thống được sử dụng chính thức.

### Mục tiêu kiểm thử

**Khái niệm chính:**
- Phát hiện càng nhiều lỗi càng sớm càng tốt, đặc biệt là lỗi nghiêm trọng.
- Kiểm thử hợp lệ để bảo đảm hệ thống hoạt động như mong đợi.
- Kiểm thử khiếm khuyết để tìm lỗi và hành vi sai.

## Các loại lỗi trong kiểm thử

### Ba kiểu lỗi

**Khái niệm chính:**
- Chức năng chương trình chạy lỗi hoặc cho kết quả không đúng.
- Chương trình không làm điều cần phải làm.
- Chương trình làm điều không cần làm.

**Giải thích:**
Một hệ thống có thể sai không chỉ vì bị lỗi khi chạy. Nó cũng có thể sai vì thiếu chức năng bắt buộc hoặc thực hiện thêm hành vi ngoài yêu cầu.

## Tài liệu cần thiết

### Tài liệu đầu vào cho kiểm thử

**Khái niệm chính:**
- Tài liệu yêu cầu người dùng.
- Tài liệu đặc tả.
- Tài liệu thiết kế.

**Giải thích:**
Các tài liệu này là cơ sở để xác định hệ thống cần kiểm thử gì, kết quả đúng là gì và cách đánh giá kết quả kiểm thử.

## Tiến trình kiểm thử

### Các bước thực hiện

**Quy trình / Mô hình / Ký hiệu:**
1. Lập kế hoạch kiểm thử (`Test Plan`).
2. Chuẩn bị môi trường kiểm thử như phần cứng, phần mềm và ngôn ngữ.
3. Thiết kế test case.
4. Thực hiện kiểm thử.
5. Theo dõi và xử lý lỗi.
6. Thống kê, báo cáo kết quả kiểm thử.

**Lưu ý:**
- Test case cần mô tả điều kiện kiểm thử, dữ liệu kiểm thử, bước thực hiện và kết quả mong đợi.

## Các nguyên tắc kiểm thử

### Nguyên tắc chung

**Khái niệm chính:**
- Kiểm thử cần được lập kế hoạch.
- Kiểm thử phải dựa trên yêu cầu và thiết kế.
- Lỗi cần được ghi nhận, theo dõi và xử lý.
- Kiểm thử nên được thực hiện ở nhiều mức khác nhau.

**Giải thích:**
Kiểm thử hiệu quả đòi hỏi quy trình rõ ràng. Nếu chỉ kiểm thử tự phát, nhóm phát triển khó biết đã kiểm thử đủ hay chưa và khó truy vết lỗi.

## Cấp độ và chiến lược kiểm thử

### Cấp độ kiểm thử

**Khái niệm chính:**
- Kiểm thử có thể được thực hiện bởi đội ngũ dự án.
- Một số kiểm thử có thể do cơ quan hoặc bên ngoài thực hiện để chấp nhận ứng dụng.

**Quy trình / Mô hình / Ký hiệu:**
| Cấp độ | Mục đích |
|---|---|
| Kiểm thử thành phần | Kiểm tra từng phần của hệ thống. |
| Kiểm thử tích hợp | Kiểm tra sự phối hợp giữa các phần. |
| Kiểm thử hệ thống | Kiểm tra toàn bộ hệ thống. |
| Kiểm thử chấp nhận | Xác nhận hệ thống đáp ứng nhu cầu người dùng. |

## Tóm tắt chương
- Kiểm thử là quá trình đánh giá hệ thống để tìm lỗi và xác nhận mức đáp ứng yêu cầu.
- Mục tiêu kiểm thử là phát hiện lỗi sớm, đặc biệt lỗi nghiêm trọng.
- Kiểm thử cần tài liệu yêu cầu, đặc tả và thiết kế.
- Tiến trình kiểm thử gồm lập kế hoạch, chuẩn bị môi trường, thiết kế test case, thực hiện, xử lý lỗi và báo cáo.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Testing | Kiểm thử phần mềm hoặc hệ thống. |
| Test Plan | Kế hoạch kiểm thử. |
| Test case | Trường hợp kiểm thử gồm dữ liệu, bước thực hiện và kết quả mong đợi. |
| Kiểm thử hợp lệ | Kiểm thử để xác nhận hệ thống vận hành như mong đợi. |
| Kiểm thử khiếm khuyết | Kiểm thử nhằm phát hiện lỗi. |
| Kiểm thử chấp nhận | Kiểm thử để xác nhận hệ thống được người dùng chấp nhận. |

## Câu hỏi ôn tập
1. Kiểm thử phần mềm là gì theo IEEE?
2. Vì sao kiểm thử được xem là quá trình tìm lỗi?
3. Mục tiêu của kiểm thử là gì?
4. Nêu ba loại lỗi có thể tồn tại trong ứng dụng phần mềm.
5. Trước khi kiểm thử cần chuẩn bị những tài liệu nào?
6. Trình bày tiến trình kiểm thử.
7. Test case thường cần những thông tin gì?
8. Phân biệt kiểm thử hệ thống và kiểm thử chấp nhận.
