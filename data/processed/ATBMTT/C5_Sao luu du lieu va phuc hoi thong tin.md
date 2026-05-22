# C5_Sao luu du lieu va phuc hoi thong tin

# Chương V

## Sao Lưu Dữ Liệu Và Phục Hồi Thông Tin

## Học ViệN Ngân HàNg

## Khoa Công Nghệ Thông Tin & Kinh Tế Số

Nội dung

Một số khái niệm

## 5.1

Sao lưu dự phòng dữ liệu

## 5.2

Phục hồi dữ liệu sau sự cố

## 5.3

## 5.4

Các xu hướng công nghệ trong đảm bảo ATTT

## 5.1. Một số khái niệm

- Sao lưu dữ liệu (Data Backup): Là quá trình tạo ra

bản sao của dữliệu gốc và lưu trữtại các vịtrí khác

nhau nhằm phòng ngừa mất mát dữliệu do sựcố

(lỗi phần cứng, tấn công mạng, lỗi con người,...)

- Phục hồi dữ liệu (Data Recovery): Là quá trình khôi

phục lại dữliệu từcác bản sao lưu khi xảy ra sựcố.

- Khôi phục thảm họa (Disaster Recovery – DR): Là

tập hợp các chính sách, công cụ và quy trình nhằm

khôi phục hệ thống CNTT sau các sự cố nghiêm

trọng (cháy nổ, tấn công ransomware, thiên tai,...).

## 5.1. Một số khái niệm

- Chỉ số RPO (Recovery Point Objective): Xác định

mức độ dữ liệu có thể chấp nhận mất mát (tính theo

thời gian).

- Chỉ số RTO (Recovery Time Objective): Xác định

thời gian tối đa cho phép để phục hồi hệ thống sau

sự cố.

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.1 Mục tiêu

- Đảm bảo khả năng phục hồi dữ liệu khi xảy ra

sự cố

- Giảm thiểu gián đoạn hoạt động

- Tuân thủ các quy định pháp lý và tiêu chuẩn

bảo mật

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- Sao lưu toàn bộ (Full Backup): Sao chép toàn

bộ dữ liệu tại một thời điểm

- Ưu điểm: dễ phục hồi

- Nhược điểm: tốn tài nguyên và thời gian

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- Sao lưu gia tăng (Incremental Backup): Chỉ sao

lưu phần dữ liệu thay đổi kể từ lần sao lưu gần

nhất

- Ưu điểm: Tiết kiệm dung lượng

- Nhược điểm: Phục hồi phức tạp

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- Sao lưu vi sai (Diffirential Backup): Sao lưu

phần dữ liệu thay đổi kể từ lần sao lưu toàn bộ

gần nhất

- Ưu điểm: Phục hồi đơn giản

- Nhược điểm: Tốn thời gian và dung lượng

sao lưu gia tăng

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.3 Mô hình và chiến lược sao lưu

- Quy tắc 3 - 2 – 1:

- 3 bản sao lưu dữ liệu

- 2 loại phương tiện lưu trữ khác nhau

- 1 bản lưu ngoài site (offsite

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.3 Mô hình và chiến lược sao lưu

- Sao lưu tại chỗ (on-site backup)

- Sao lưu ngoài site (Off-site backup)

- Sao lưu đám mây (Cloud backup

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

- Hệ thống NAS, SAN

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

- Lưu trữ đám mây (AWS S3, Azure Backup,

Google Cloud Storage)

- AWS S3: Độ bền cực cao, hệ sinh thái lớn

- Azure: Tích hợp sâu với hệ sinh thái Microsoft

- GCS: Cung cấp các lớp lưu trữ với tốc độ truy

cập nhanh

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

- Phần mềm sao lưu chuyên dụng

- Veeam: nổi bật với sao lưu ảo hóa

- Acronis: Tích hợp bảo mật AI

- Bacula: mạnh về khải năng mở rộng

## 5.2. Sao lưu dự phòng dữ liệu

## 5.2.5 Các rủi ro trong sao lưu

- Sao lưu không đầy đủ hoặc không kiểm tra

định kỳ

- Dữ liệu Backup bị mã hóa bởi ransomware

- Lỗi cấu hình hoặc lỗi con người

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.1 Các loại sự cố phổ biến

- Lỗi phần cứng (ổ cứng, máy chủ)

- Tấn công mạng (ransomware, DDoS)

- Lỗi phần mềm

- Sai sót do con người

- Thiên tai

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.2 Quy trình phục hồi dữ liệu

## 1. Phát hiện sự cố

## 2. Đánh giá mức độ thiệt hại

## 3. Xác định nguồn Backup phù hợp

## 4. Thực hiện phục hồi

## 5. Kiểm tra tính toàn vẹn dữ liệu

## 6. Đưa hệ thống trở lại hoạt động

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.3 Các mô hình phục hồi

- Cold Site:

- Warm Site

- Hot Site:

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- Kiểm tra định kỳ khả năng khôi phục

- Xác thực khả năng phục hồi: Đảm bảo dữliệu

sao lưu có thểsửdụng được và kếhoạch DR

(Disaster Recovery) thực sựhoạt động trong tình

huống khẩn cấp

- Đo lường thời gian: Đánh giá mục tiêu thời gian

khôi phục RTO và mục tiêu điểm khôi phục (RPO)

có đạt yêu cầu không

- Phát hiện lỗ hổng: Nhận diện các điểm yếu trong

quy trình khôi phục hiện tại để cải thiện kịp thời

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- Mô phỏng kịch bản tấn công

- Các kịch bản tấn công phổ biến

• Tấn công mạng & Hạ tầng

• Tấn công ứng dụng Web

• Tấn công lừa đảo (Phishing)

• Tấn công Ransomware

• Tấn công có chủ đích

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- Mô phỏng kịch bản tấn công

- Quy trình xây dựng kịch bản diễn tập:

## 1. Xác định phạm vi

## 2. Thiết kê kịch bản: Dựa trên các mối đe dọa

thực tế

## 3. Thực hiện mô phỏng: Chạy kịch bản trong

môi trường an toàn

## 4. Phân tích & Báo cáo: Đánh giá khả năng

phòng thủ và đưa ra khuyến nghị và vá lỗi

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- Đánh giá thời gian RTO/RPO thực tế

- Mức độ quan trọng của dữ liệu (RPO):

• Tài chính/Ngân hàng: RPO rất thấp, gần bằng

## 0 để tránh tổn thất

• Y tế/Logistics: RPO khoảng 1-4 giờ để đảm

bảo dữ liệu cập nhật

• Giáo dục/Ứng dụng nhỏ: RPO có thể là 4-24

giờ

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- Đánh giá thời gian RTO/RPO thực tế

- Thời gian cho phép dừng hệ thống (RTO):

Tổng thời gian khôi phục, bao gồm phát hiện sự

cố, khôi phục dữliệu và kiểm tra hệthống

- Chi phí thực thi

- Kiểm tra và đánh giá lại: Cần thường xuyên kiểm

tra, so sánh dữliệu thực tếvới mục tiêu đã đềra

đểđiều chỉnh chiến lược backup

## 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.5 Những thách thức

- Thời gian downtime dài

- Dữ liệu không đồng nhất

- Thiếu quy trình chuẩn hóa

## 5.4. Các xu hướng công nghệ trong ATTT

## 5.4.1 Sao lưu thông minh

## 5.4.2 Bảo vệ chống ransomware

## 5.4.3 Điện toán đám mây và đa đám mây

## 5.4.4 Tự động hóa và Orchestration

## 5.4.5 Zero Trust trong sao lưu

……

Thank You !

www.themegallery.com