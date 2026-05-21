# Chương 8: Bảng tính điện tử

## Nội dung chính
- Giới thiệu bảng tính điện tử và một số ứng dụng bảng tính.
- Sổ tính, trang tính, dòng, cột, ô và miền ô.
- Định dạng ô tính và miền ô tính.
- Các thao tác cơ bản trên trang tính.
- Địa chỉ ô: tương đối, tuyệt đối và hỗn hợp.
- Các hàm số và phân tích dữ liệu với Excel.
- Kỹ năng bảng tính cho nghề nghiệp.

## Tổng quan
Chương này giới thiệu bảng tính điện tử như công cụ xử lý dữ liệu dạng bảng. Nội dung tập trung vào Excel và các thao tác cơ bản: nhập dữ liệu, chọn vùng, định dạng, làm việc với địa chỉ ô và dùng bảng tính để phân tích dữ liệu.

## 1. Giới thiệu bảng tính điện tử

### Một số ứng dụng bảng tính

**Khái niệm chính:**
- Bảng tính điện tử là công cụ tạo, lưu trữ, tính toán và phân tích dữ liệu dạng bảng.
- Một số ứng dụng bảng tính: Microsoft 365 Excel, Microsoft Excel, OpenOffice Calc, Google Sheets.

**Giải thích:**
Bảng tính giúp tổ chức dữ liệu theo dòng và cột, thực hiện tính toán bằng công thức, định dạng dữ liệu và phân tích kết quả.

**Ví dụ / ứng dụng:**
- Lập bảng điểm.
- Quản lý chi tiêu.
- Tổng hợp dữ liệu khảo sát.

**Lưu ý:**
- Chọn công cụ bảng tính cần dựa vào nhu cầu làm việc cá nhân, cộng tác và khả năng tương thích.

## 2. Sổ tính và trang tính

### Cấu trúc trang tính Excel

**Khái niệm chính:**
- Sổ tính là tệp bảng tính.
- Trang tính là các sheet nằm trong sổ tính.
- Trang tính có dòng, cột, ô và miền ô.
- Một trang tính Excel có 1.048.576 dòng và 16.384 cột từ A đến XFD.

**Giải thích:**
Dữ liệu trong Excel được nhập vào ô. Mỗi ô được xác định bởi địa chỉ gồm tên cột và số dòng, ví dụ `A1`, `B5`.

**Ví dụ / ứng dụng:**
- Ô `A1` nằm ở cột A, dòng 1.
- Miền `A1:C5` gồm các ô từ A1 đến C5.

**Lưu ý:**
- Cần hiểu địa chỉ ô để viết công thức đúng.

## 3. Định dạng ô tính và miền ô tính

### Định dạng Number

**Khái niệm chính:**
- Thẻ Number trong Format Cells dùng để định dạng kiểu dữ liệu.

**Giải thích:**
Dữ liệu có thể là số, ngày tháng, tiền tệ, phần trăm hoặc văn bản. Định dạng đúng giúp hiển thị và tính toán chính xác.

**Ví dụ / ứng dụng:**
- Định dạng cột doanh thu là tiền tệ.
- Định dạng tỷ lệ là phần trăm.

**Lưu ý:**
- Định dạng hiển thị không phải lúc nào cũng thay đổi giá trị thực trong ô.

### Định dạng Alignment

**Khái niệm chính:**
- Alignment dùng để căn lề và bố trí nội dung trong ô.

**Giải thích:**
Căn trái, phải, giữa, xuống dòng trong ô giúp bảng dễ đọc hơn.

**Ví dụ / ứng dụng:**
- Dùng Wrap Text để dữ liệu dài tự xuống dòng trong ô.

**Lưu ý:**
- Cần điều chỉnh độ rộng cột và căn chỉnh để tránh dữ liệu bị che khuất.

### Định dạng Font

**Khái niệm chính:**
- Font dùng để thiết lập phông chữ, cỡ chữ, kiểu chữ, màu chữ và hiệu ứng chữ.

**Giải thích:**
Định dạng chữ giúp làm nổi bật tiêu đề, nhóm dữ liệu hoặc giá trị quan trọng.

**Ví dụ / ứng dụng:**
- In đậm hàng tiêu đề.
- Đổi màu chữ cho giá trị cần chú ý.

**Lưu ý:**
- Không nên lạm dụng nhiều màu và kiểu chữ làm bảng khó đọc.

### Định dạng Border và Fill

**Khái niệm chính:**
- Border tạo khung viền cho ô hoặc miền ô.
- Fill tô màu nền cho ô hoặc miền ô.

**Giải thích:**
Khung viền giúp phân tách vùng dữ liệu. Màu nền giúp nhấn mạnh tiêu đề hoặc nhóm thông tin.

**Ví dụ / ứng dụng:**
- Kẻ khung ngoài và khung trong cho bảng.
- Tô màu nền hàng tiêu đề.

**Lưu ý:**
- Định dạng cần phục vụ đọc dữ liệu, không chỉ trang trí.

## 4. Các thao tác cơ bản

### Chọn ô, miền ô, cột, dòng và trang tính

**Khái niệm chính:**
- Chọn dòng hoặc cột bằng cách nhấn vào số hiệu dòng hoặc tên cột.
- Chọn miền ô liền kề bằng cách kéo từ ô đầu đến ô cuối.
- Chọn các ô không liền kề bằng cách giữ Ctrl và nhấn từng ô.
- Chọn toàn trang tính bằng ô giao giữa tiêu đề dòng và cột.

**Giải thích:**
Chọn đúng vùng dữ liệu là bước cần thiết trước khi định dạng, sao chép hoặc tính toán.

**Ví dụ / ứng dụng:**
- Chọn cả cột điểm để định dạng số.
- Chọn nhiều ô không liền kề để tô màu.

**Lưu ý:**
- Kiểm tra vùng chọn trước khi thao tác để tránh ảnh hưởng dữ liệu ngoài ý muốn.

### Di chuyển con trỏ trong trang tính

**Khái niệm chính:**
- Phím mũi tên di chuyển từng ô.
- Page Up và Page Down di chuyển theo trang màn hình.
- Home về cột đầu tiên của dòng hiện tại.
- Ctrl kết hợp phím mũi tên để di chuyển nhanh đến biên vùng dữ liệu.

**Giải thích:**
Các phím điều hướng giúp làm việc nhanh hơn với trang tính lớn.

**Ví dụ / ứng dụng:**
- Dùng Ctrl + mũi tên để đến cuối vùng dữ liệu.

**Lưu ý:**
- Một số phím tắt có thể khác nhau tùy phiên bản Excel.

### Nhập và sửa dữ liệu

**Khái niệm chính:**
- Nhấn vào ô để nhập dữ liệu.
- Nhấn F2 để sửa trực tiếp nội dung ô.
- Dữ liệu dài có thể tràn sang ô bên cạnh hoặc xuống dòng nếu bật Wrap Text.

**Giải thích:**
Excel cho phép nhập văn bản, số, ngày tháng và công thức. Khi dữ liệu dài, cần điều chỉnh hiển thị để không bị khó đọc.

**Ví dụ / ứng dụng:**
- Nhập tên sinh viên, mã lớp, điểm số.
- Dùng Wrap Text cho ô mô tả dài.

**Lưu ý:**
- Công thức trong Excel thường bắt đầu bằng dấu `=`.

### Nhập nhanh dữ liệu

**Khái niệm chính:**
- Ctrl + Enter nhập cùng một nội dung vào nhiều ô đã chọn.
- Fill Handle giúp điền nhanh dãy số hoặc ngày tháng theo quy luật.

**Giải thích:**
Nhập nhanh giúp giảm thao tác lặp lại khi tạo bảng dữ liệu.

**Ví dụ / ứng dụng:**
- Nhập cùng một nhãn cho nhiều ô.
- Kéo Fill Handle để tạo dãy ngày tăng dần.

**Lưu ý:**
- Cần kiểm tra quy luật Excel tự nhận khi dùng Fill Handle.

## 5. Làm việc với đối tượng đồ họa

### Đối tượng đồ họa trong trang tính

**Khái niệm chính:**
- Picture: hình ảnh từ tệp.
- Screenshot: chụp màn hình chương trình đang mở.
- ClipArt: hình vẽ đơn giản.
- Shape: hình học đơn giản.
- SmartArt: công cụ biểu diễn quy trình hoặc sơ đồ.

**Giải thích:**
Đối tượng đồ họa giúp minh họa dữ liệu, quy trình hoặc ý tưởng trong trang tính.

**Ví dụ / ứng dụng:**
- Chèn SmartArt để mô tả quy trình xử lý dữ liệu.
- Chèn ảnh minh họa vào bảng báo cáo.

**Lưu ý:**
- Đồ họa không nên che khuất dữ liệu quan trọng.

## 6. Địa chỉ ô tính

### Địa chỉ tương đối

**Khái niệm chính:**
- Địa chỉ tương đối có dạng `cột dòng`, ví dụ `A2`, `F25`.
- Địa chỉ này thay đổi khi sao chép công thức đến vị trí mới.

**Giải thích:**
Địa chỉ tương đối phù hợp khi công thức cần tự điều chỉnh theo vị trí.

**Ví dụ / ứng dụng:**
- Sao chép công thức từ hàng này sang hàng khác để tính cùng loại dữ liệu.

**Lưu ý:**
- Nếu không muốn địa chỉ thay đổi, không dùng địa chỉ tương đối.

### Địa chỉ tuyệt đối

**Khái niệm chính:**
- Địa chỉ tuyệt đối có dạng `$cột$dòng`, ví dụ `$L$1`.
- Địa chỉ này giữ nguyên khi sao chép công thức.

**Giải thích:**
Địa chỉ tuyệt đối dùng khi công thức luôn tham chiếu đến một ô cố định.

**Ví dụ / ứng dụng:**
- Ô chứa tỷ giá, lãi suất hoặc hệ số cố định.

**Lưu ý:**
- Dấu `$` khóa cột và dòng.

### Địa chỉ hỗn hợp

**Khái niệm chính:**
- Địa chỉ hỗn hợp có dạng `$A2` hoặc `B$1`.
- Cột hoặc dòng có dấu `$` sẽ được giữ nguyên khi sao chép công thức.

**Giải thích:**
Địa chỉ hỗn hợp dùng khi chỉ muốn cố định cột hoặc dòng.

**Ví dụ / ứng dụng:**
- Bảng tính có nhiều dòng và nhiều cột cần tham chiếu theo một chiều cố định.

**Lưu ý:**
- Hiểu đúng dấu `$` giúp tránh sai công thức khi sao chép.

## 7. Hàm số và phân tích dữ liệu với Excel

### Vai trò của hàm trong bảng tính

**Khái niệm chính:**
- Hàm giúp tính toán và phân tích dữ liệu tự động.
- Excel hỗ trợ nhiều nhóm hàm phục vụ học tập và nghề nghiệp.

**Giải thích:**
Hàm giúp xử lý dữ liệu nhanh hơn thao tác thủ công, đặc biệt với bảng dữ liệu lớn.

**Ví dụ / ứng dụng:**
- Tính tổng, trung bình, giá trị lớn nhất, nhỏ nhất.
- Phân tích danh sách, lọc dữ liệu, tạo báo cáo.

**Lưu ý:**
- Cần kiểm tra vùng dữ liệu đầu vào của hàm để tránh kết quả sai.

## Tóm tắt chương
- Bảng tính điện tử giúp tổ chức, tính toán và phân tích dữ liệu dạng bảng.
- Excel dùng sổ tính, trang tính, dòng, cột, ô và miền ô.
- Định dạng Number, Alignment, Font, Border và Fill giúp bảng dễ đọc.
- Địa chỉ ô có ba dạng: tương đối, tuyệt đối và hỗn hợp.
- Kỹ năng bảng tính là kỹ năng quan trọng trong học tập và nghề nghiệp.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Bảng tính điện tử | Công cụ xử lý dữ liệu dạng bảng. |
| Sổ tính | Tệp bảng tính gồm một hoặc nhiều trang tính. |
| Trang tính | Sheet chứa các ô được tổ chức theo dòng và cột. |
| Ô | Đơn vị nhập dữ liệu trong bảng tính. |
| Miền ô | Vùng gồm nhiều ô. |
| Fill Handle | Công cụ kéo để nhập nhanh dữ liệu theo quy luật. |
| Địa chỉ tương đối | Địa chỉ thay đổi khi sao chép công thức. |
| Địa chỉ tuyệt đối | Địa chỉ cố định khi sao chép công thức. |
| Địa chỉ hỗn hợp | Địa chỉ cố định cột hoặc dòng. |

## Câu hỏi ôn tập
1. Bảng tính điện tử dùng để làm gì?
2. Kể tên một số ứng dụng bảng tính.
3. Sổ tính và trang tính khác nhau như thế nào?
4. Địa chỉ ô là gì?
5. Nêu các nhóm định dạng trong Format Cells.
6. Fill Handle dùng để làm gì?
7. Phân biệt địa chỉ tương đối, tuyệt đối và hỗn hợp.
8. Vì sao kỹ năng bảng tính quan trọng trong nghề nghiệp?

