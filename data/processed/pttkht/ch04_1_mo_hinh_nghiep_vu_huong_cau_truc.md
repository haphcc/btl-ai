# Chương 4.1: Mô hình nghiệp vụ hướng cấu trúc

## Nội dung chính
- Phân tích hệ thống theo phương pháp hướng cấu trúc.
- Mục tiêu của mô hình nghiệp vụ hướng cấu trúc.
- Biểu đồ luồng dữ liệu DFD.
- Các thành phần cơ bản của DFD.
- Biểu đồ ngữ cảnh, phân rã tiến trình và quy tắc xây dựng DFD.

## Tổng quan
Chương này trình bày cách mô hình hóa nghiệp vụ theo hướng cấu trúc. Nội dung trọng tâm là biểu đồ luồng dữ liệu DFD, một công cụ mô tả hệ thống thông qua tiến trình xử lý, luồng dữ liệu, kho dữ liệu và tác nhân ngoài.

## Phân tích hệ thống hướng cấu trúc

### Khái niệm

**Khái niệm chính:**
- Hướng cấu trúc tập trung vào chức năng xử lý và luồng dữ liệu của hệ thống.
- Hệ thống được phân rã từ mức tổng quát đến mức chi tiết.
- Kết quả mô hình hóa giúp người phân tích hiểu hệ thống hiện tại và đề xuất hệ thống mới.

**Giải thích:**
Thay vì bắt đầu bằng lớp và đối tượng, phương pháp hướng cấu trúc đặt câu hỏi: hệ thống nhận dữ liệu gì, xử lý như thế nào, lưu ở đâu và tạo ra kết quả gì. Cách nhìn này phù hợp khi phân tích quy trình nghiệp vụ và luồng thông tin trong tổ chức.

## Biểu đồ luồng dữ liệu DFD

### Khái niệm DFD

**Khái niệm chính:**
- DFD là viết tắt của `Data Flow Diagram`.
- DFD mô tả luồng dữ liệu đi qua các tiến trình xử lý trong hệ thống.
- DFD cho thấy dữ liệu được nhận từ đâu, được xử lý thế nào, được lưu ở đâu và được gửi cho ai.

**Giải thích:**
DFD không tập trung vào cách cài đặt kỹ thuật mà tập trung vào logic nghiệp vụ. Vì vậy DFD phù hợp trong giai đoạn phân tích để trao đổi với người dùng và nhóm phát triển.

### Thành phần của DFD

**Quy trình / Mô hình / Ký hiệu:**
| Thành phần | Ý nghĩa |
|---|---|
| Tác nhân ngoài | Người, bộ phận hoặc hệ thống bên ngoài có trao đổi dữ liệu với hệ thống đang xét. |
| Tiến trình xử lý | Hoạt động biến đổi dữ liệu đầu vào thành dữ liệu đầu ra. |
| Luồng dữ liệu | Dữ liệu di chuyển giữa tác nhân, tiến trình và kho dữ liệu. |
| Kho dữ liệu | Nơi lưu trữ dữ liệu cần dùng trong hệ thống. |

**Lưu ý:**
- Tên tiến trình nên là động từ hoặc cụm động từ thể hiện hành động xử lý.
- Tên luồng dữ liệu và kho dữ liệu nên là danh từ hoặc cụm danh từ.

## Biểu đồ ngữ cảnh

### Mức tổng quát

**Khái niệm chính:**
- Biểu đồ ngữ cảnh mô tả toàn bộ hệ thống như một tiến trình duy nhất.
- Biểu đồ thể hiện các tác nhân ngoài và các luồng dữ liệu trao đổi với hệ thống.

**Giải thích:**
Biểu đồ ngữ cảnh giúp xác định ranh giới hệ thống. Đây là bước quan trọng để tránh nhầm lẫn giữa phần hệ thống cần xây dựng và môi trường bên ngoài.

## Phân rã tiến trình

### Từ tổng quát đến chi tiết

**Khái niệm chính:**
- Tiến trình mức cao được phân rã thành các tiến trình mức thấp hơn.
- Mỗi mức phân rã làm rõ hơn các xử lý bên trong hệ thống.
- Các luồng dữ liệu giữa các mức cần giữ tính nhất quán.

**Giải thích:**
Phân rã giúp mô hình không quá phức tạp trên một biểu đồ duy nhất. Người đọc có thể bắt đầu từ biểu đồ ngữ cảnh, sau đó đi dần vào các DFD chi tiết.

## Quy tắc xây dựng DFD

### Nguyên tắc trình bày

**Quy trình / Mô hình / Ký hiệu:**
- Mỗi tiến trình phải có ít nhất một luồng dữ liệu vào và một luồng dữ liệu ra.
- Không vẽ luồng dữ liệu trực tiếp giữa hai kho dữ liệu.
- Không vẽ luồng dữ liệu trực tiếp giữa hai tác nhân ngoài trong phạm vi hệ thống.
- Kho dữ liệu thường phải được đọc hoặc ghi bởi một tiến trình.
- Các mức DFD phải cân bằng về luồng dữ liệu vào/ra.

**Lưu ý:**
- File `.ppt` cũ của chương này chứa nhiều đối tượng ảnh, nên phần ví dụ chi tiết trong slide không trích xuất được đầy đủ. Nội dung trên tập trung vào các khái niệm và ký hiệu cốt lõi đọc được từ tiêu đề chương và chủ đề DFD.

## Tóm tắt chương
- Mô hình nghiệp vụ hướng cấu trúc tập trung vào chức năng và luồng dữ liệu.
- DFD mô tả dữ liệu đi qua tác nhân ngoài, tiến trình, kho dữ liệu và luồng dữ liệu.
- Biểu đồ ngữ cảnh xác định ranh giới hệ thống ở mức tổng quát.
- Phân rã tiến trình giúp mô tả hệ thống từ mức cao đến mức chi tiết.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Hướng cấu trúc | Phương pháp phân tích tập trung vào chức năng xử lý và luồng dữ liệu. |
| DFD | Biểu đồ luồng dữ liệu, mô tả dữ liệu đi qua các tiến trình của hệ thống. |
| Tác nhân ngoài | Đối tượng bên ngoài trao đổi dữ liệu với hệ thống. |
| Tiến trình xử lý | Hoạt động biến đổi dữ liệu đầu vào thành dữ liệu đầu ra. |
| Luồng dữ liệu | Dòng di chuyển dữ liệu giữa các thành phần của DFD. |
| Kho dữ liệu | Nơi lưu trữ dữ liệu trong hệ thống. |
| Biểu đồ ngữ cảnh | DFD mức cao nhất mô tả toàn bộ hệ thống như một tiến trình. |

## Câu hỏi ôn tập
1. Phân tích hệ thống hướng cấu trúc tập trung vào điều gì?
2. DFD là gì và dùng để làm gì?
3. Nêu các thành phần cơ bản của DFD.
4. Tác nhân ngoài khác gì với tiến trình xử lý?
5. Biểu đồ ngữ cảnh có vai trò gì?
6. Vì sao cần phân rã tiến trình trong DFD?
7. Nêu một số quy tắc khi xây dựng DFD.
8. Vì sao cần giữ cân bằng dữ liệu giữa các mức DFD?
