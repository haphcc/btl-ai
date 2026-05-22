# C5_Sao luu du lieu va phuc hoi thong tin



<!-- page 1 -->

# HỌC VIỆN NGÂN HÀNG
## KHOA CÔNG NGHỆ THÔNG TIN & KINH TẾ SỐ

# **CHƯƠNG V**
# **SAO LƯU DỮ LIỆU VÀ PHỤC HỒI THÔNG TIN**


<!-- page 2 -->

# Nội dung

## 5.1 Một số khái niệm
## 5.2 Sao lưu dự phòng dữ liệu
## 5.3 Phục hồi dữ liệu sau sự cố
## 5.4 Các xu hướng công nghệ trong đảm bảo ATTT


<!-- page 3 -->

# 5.1. Một số khái niệm

- **Sao lưu dữ liệu (Data Backup):** Là quá trình tạo ra bản sao của dữ liệu gốc và lưu trữ tại các vị trí khác nhau nhằm phòng ngừa mất mát dữ liệu do sự cố (lỗi phần cứng, tấn công mạng, lỗi con người,...)

- **Phục hồi dữ liệu (Data Recovery):** Là quá trình khôi phục lại dữ liệu từ các bản sao lưu khi xảy ra sự cố.

- **Khôi phục thảm họa (Disaster Recovery – DR):** Là tập hợp các chính sách, công cụ và quy trình nhằm khôi phục hệ thống CNTT sau các sự cố nghiêm trọng (cháy nổ, tấn công ransomware, thiên tai,...).

3


<!-- page 4 -->

# 5.1. Một số khái niệm

- **Chỉ số RPO (Recovery Point Objective):** Xác định mức độ dữ liệu có thể chấp nhận mất mát (tính theo thời gian).

- **Chỉ số RTO (Recovery Time Objective):** Xác định thời gian tối đa cho phép để phục hồi hệ thống sau sự cố.


<!-- page 5 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.1 Mục tiêu

- **Đảm bảo khả năng phục hồi dữ liệu khi xảy ra sự cố**
- **Giảm thiểu gián đoạn hoạt động**
- **Tuân thủ các quy định pháp lý và tiêu chuẩn bảo mật**


<!-- page 6 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- **Sao lưu toàn bộ (Full Backup)**: Sao chép toàn bộ dữ liệu tại một thời điểm
    - **Ưu điểm**: dễ phục hồi
    - **Nhược điểm**: tốn tài nguyên và thời gian


<!-- page 7 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- **Sao lưu gia tăng (Incremental Backup)**: Chỉ sao lưu phần dữ liệu thay đổi kể từ lần sao lưu gần nhất
    - **Ưu điểm**: Tiết kiệm dung lượng
    - **Nhược điểm**: Phục hồi phức tạp


<!-- page 8 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.2 Các phương pháp sao lưu

- **Sao lưu vi sai (Diffirential Backup):** Sao lưu phần dữ liệu thay đổi kể từ lần sao lưu toàn bộ gần nhất

    - **Ưu điểm:** Phục hồi đơn giản

    - **Nhược điểm:** Tốn thời gian và dung lượng sao lưu gia tăng


<!-- page 9 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.3 Mô hình và chiến lược sao lưu

- **Quy tắc 3 - 2 - 1:**

- 3 bản sao lưu dữ liệu
- 2 loại phương tiện lưu trữ khác nhau
- 1 bản lưu ngoài site (offsite)


<!-- page 10 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.3 Mô hình và chiến lược sao lưu

- **Sao lưu tại chỗ (on-site backup)**
- **Sao lưu ngoài site (Off-site backup)**
- **Sao lưu đám mây (Cloud backup)**


<!-- page 11 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

- **Hệ thống NAS, SAN**

| SAN vs NAS |
| :--- |
| **STORAGE AREA NETWORK (SAN)** | **NETWORK ATTACHED STORAGE (NAS)** |
| (Hình ảnh minh họa kết nối từ máy tính đến thiết bị lưu trữ) | (Hình ảnh minh họa kết nối từ máy tính đến thiết bị lưu trữ) |
| **STORAGE DEVICES** | **STORAGE DEVICE** |


<!-- page 12 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

- **Lưu trữ đám mây (AWS S3, Azure Backup, Google Cloud Storage)**

- **AWS S3**: Độ bền cực cao, hệ sinh thái lớn

- **Azure**: Tích hợp sâu với hệ sinh thái Microsoft

- **GCS**: Cung cấp các lớp lưu trữ với tốc độ truy cập nhanh


<!-- page 13 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.4 Công nghệ và công cụ hỗ trợ

### Phần mềm sao lưu chuyên dụng

- **Veeam**: nổi bật với sao lưu ảo hóa
- **Acronis**: Tích hợp bảo mật AI
- **Bacula**: mạnh về khả năng mở rộng

13


<!-- page 14 -->

# 5.2. Sao lưu dự phòng dữ liệu

## 5.2.5 Các rủi ro trong sao lưu

- **Sao lưu không đầy đủ hoặc không kiểm tra định kỳ**
- **Dữ liệu Backup bị mã hóa bởi ransomware**
- **Lỗi cấu hình hoặc lỗi con người**


<!-- page 15 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.1 Các loại sự cố phổ biến

- **Lỗi phần cứng (ổ cứng, máy chủ)**
- **Tấn công mạng (ransomware, DDoS)**
- **Lỗi phần mềm**
- **Sai sót do con người**
- **Thiên tai**


<!-- page 16 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.2 Quy trình phục hồi dữ liệu

1. **Phát hiện sự cố**

2. **Đánh giá mức độ thiệt hại**

3. **Xác định nguồn Backup phù hợp**

4. **Thực hiện phục hồi**

5. **Kiểm tra tính toàn vẹn dữ liệu**

6. **Đưa hệ thống trở lại hoạt động**


<!-- page 17 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.3 Các mô hình phục hồi

- **Cold Site:**

- **Warm Site:**

- **Hot Site:**


<!-- page 18 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

### Kiểm tra định kỳ khả năng khôi phục

- **Xác thực khả năng phục hồi:** Đảm bảo dữ liệu sao lưu có thể sử dụng được và kế hoạch DR (Disaster Recovery) thực sự hoạt động trong tình huống khẩn cấp
- **Đo lường thời gian:** Đánh giá mục tiêu thời gian khôi phục RTO và mục tiêu điểm khôi phục (RPO) có đạt yêu cầu không
- **Phát hiện lỗ hổng:** Nhận diện các điểm yếu trong quy trình khôi phục hiện tại để cải thiện kịp thời


<!-- page 19 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

### Mô phỏng kịch bản tấn công

- **Các kịch bản tấn công phổ biến**
    - Tấn công mạng & Hạ tầng
    - Tấn công ứng dụng Web
    - Tấn công lừa đảo (Phishing)
    - Tấn công Ransomware
    - Tấn công có chủ đích

19


<!-- page 20 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

### Mô phỏng kịch bản tấn công

- **Quy trình xây dựng kịch bản diễn tập:**

1. Xác định phạm vi
2. Thiết kế kịch bản: Dựa trên các mối đe dọa thực tế
3. Thực hiện mô phỏng: Chạy kịch bản trong môi trường an toàn
4. Phân tích & Báo cáo: Đánh giá khả năng phòng thủ và đưa ra khuyến nghị và vá lỗi

20


<!-- page 21 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm tra phục hồi

### Đánh giá thời gian RTO/RPO thực tế

- **Mức độ quan trọng của dữ liệu (RPO):**

- Tài chính/Ngân hàng: RPO rất thấp, gần bằng 0 để tránh tổn thất
- Y tế/Logistics: RPO khoảng 1-4 giờ để đảm bảo dữ liệu cập nhật
- Giáo dục/Ứng dụng nhỏ: RPO có thể là 4-24 giờ


<!-- page 22 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.4 Kiểm thử phục hồi

- **Đánh giá thời gian RTO/RPO thực tế**

    - **Thời gian cho phép dừng hệ thống (RTO):** Tổng thời gian khôi phục, bao gồm phát hiện sự cố, khôi phục dữ liệu và kiểm tra hệ thống
    - Chi phí thực thi
    - Kiểm tra và đánh giá lại: Cần thường xuyên kiểm tra, so sánh dữ liệu thực tế với mục tiêu đã đề ra để điều chỉnh chiến lược backup


<!-- page 23 -->

# 5.3. Phục hồi dữ liệu sau sự cố

## 5.3.5 Những thách thức

- **Thời gian downtime dài**
- **Dữ liệu không đồng nhất**
- **Thiếu quy trình chuẩn hóa**

23


<!-- page 24 -->

# 5.4. Các xu hướng công nghệ trong ATTT

## 5.4.1 Sao lưu thông minh

## 5.4.2 Bảo vệ chống ransomware

## 5.4.3 Điện toán đám mây và đa đám mây

## 5.4.4 Tự động hóa và Orchestration

## 5.4.5 Zero Trust trong sao lưu
......


<!-- page 25 -->

# Thank You !
