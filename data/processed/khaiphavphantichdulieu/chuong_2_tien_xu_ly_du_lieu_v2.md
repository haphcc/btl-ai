### BÀI 2

#### CHUONG 2 TIEN XU LY DU LIEU V2

## TRANG 1

## CHƯƠNG 2 - TIỀN XỬ LÝ DỮ LIỆU

## THS. LÊ THỊ HỒNG NHUNG T: 0987867486

Khoa Công nghệ thông tin & kinh tế số E: NHUNGLTH@hvnh. edu. vn W: itde. hvnh. edu. vn

## TRANG 2

## Nội dung

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

2.2. Tóm tắt mô tả về dữ liệu

2.3. Làm sạch dữ liệu

2.4. Tích hợp dữ liệu

2.5. Biến đổi dữ liệu

2.6. Thu giảm dữ liệu

2.7. Rời rạc hóa dữ liệu

2.8. Tạo cây phân cấp ý niệm

2.9. Tóm tắt

Tiền xử lý dữ liệu 2

## TRANG 3

Tài liệu tham khảo

[1] J. Han and M. Kamber, Data Mining, “Concepts and Techniques”,

Morgan Kaufmann, 3rd Edition, 2019

[2] Ian H. witten, Eibe Frank, and Marker Hall, “Data Mining - Practical

Machine Learning Tools and Techniques”, Morgan Kaufmann, 2016

[3] Daniel T. Larose, Discovering Knowledge in Data - An introduction

to Data Mining, John Wiley & Sons, 2005

[4] Max Bramer, “Principles of Data Mining”, Springer, 2007

[5] Ho Tu Bao, “Introduction to Knowledge Discovery and Data

Minning”, National Center of Natural Science a Technology, 2010

Tiền xử lý dữ liệu 3

## TRANG 4

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

Giai đoạn tiền xử lý dữ liệu

Quá trình xử lý dữ liệu thô/gốc (ra w/original data) nhằm cải thiện chất lượng dữ liệu (quality of the data) và do đó, cải thiện chất lượng của kết quả khai phá.

Dữ liệu thô/gốc

Có cấu trúc, bán cấu trúc, phi cấu trúc

Được đưa vào từ các nguồn dữ liệu trong các hệ thống xử lý tập tin (file processing systems) và/hay các hệ thống cơ sở dữ liệu (database systems)

Chất lượng dữ liệu (data quality): tính chính xác, tính hiện hành, tính toàn vẹn, tính nhất quán

Tiền xử lý dữ liệu 4

## TRANG 5

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

Chất lượng dữ liệu (data quality)

• Tính chính xác (accuracy): giá trị được ghi nhận đúng với giá trị thực.

• Tính hiện hành (currency/timeliness): giá trị được ghi nhận không bị lỗi thời.

• Tính toàn vẹn (completeness): tất cả các giá trị dành cho một biến/thuộc tính đều được ghi nhận.

• Tính nhất quán (consistency): tất cả giá trị dữ liệu đều được biểu diễn như nhau trong tất cả các trường hợp.

Tiền xử lý dữ liệu 5

## TRANG 6

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

Đánh giá/ Biểu diễn thông tin Khám phá dữ liệu Lực cho n mẫu Dữ liệu được khám phá

Chọn lọc/Biến đổi dữ liệu Kho dữ liệu

Làm sạch dữ liệu Tích hợp dữ liệu

Nguồn dữ liệu

Tiền xử lý dữ liệu 6

## TRANG 7

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

Tiền xử lý dữ liệu 7

## TRANG 8

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

❖Các kỹ thuật tiền xử lý dữ liệu

Làm sạch dữ liệu (data cleaning/cleansing): loại bỏ nhiễu (remove noise), hiệu chỉnh những phần dữ liệu không nhất quán (correct data inconsistencies)

Tích hợp dữ liệu (data integration): trộn dữ liệu (merge data) từ nhiều nguồn khác nhau vào một kho dữ liệu

Biến đổi dữ liệu (data transformation): chuẩn hoá dữ liệu (data normalization)

Thu giảm dữ liệu (data reduction): thu giảm kích thước dữ liệu (nghĩa là giảm số phần tử) bằng kết hợp dữ liệu (data aggregation), loại bỏ các đặc điểm dư thừa (redundant features) (nghĩa là giảm số chiều/thuộc tính dữ liệu), gom cụm dữ liệu

Tiền xử lý dữ liệu 8

## TRANG 9

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

❖Các kỹ thuật tiền xử lý dữ liệu

Làm sạch dữ liệu (data cleaning/cleansing)

➢Tóm tắt hoá dữ liệu: nhận diện đặc điểm chung của dữ liệu và sự hiện diện của nhiễu hoặc các phần tử kì dị (outliers)

➢Xử lý dữ liệu bị thiếu (missing data)

➢Xử lý dữ liệu bị nhiễu (noisy data)

Tích hợp dữ liệu (data integration)

➢Tích hợp lược đồ (schema integration) và so trùng đối tượng (object matching)

➢Vấn đề dư thừa (redundancy)

➢Phát hiện và xử lý mâu thuẫn giá trị dữ liệu (detection and resolution of data value conflicts)

Tiền xử lý dữ liệu 9

## TRANG 10

2.1. Tổng quan về giai đoạn tiền xử lý dữ liệu

❖Các kỹ thuật tiền xử lý dữ liệu

Biến đổi dữ liệu (data transformation)

Làm mịn dữ liệu (smoothing)

Kết hợp dữ liệu (aggregation)

Tổng quát hóa dữ liệu (generalization)

Chuẩn hóa dữ liệu (normalization)

Xây dựng thuộc tích (attribute/feature construction)

Thu giảm dữ liệu (data reduction)

Kết hợp khối dữ liệu (data cube aggregation)

Chọn tập con các thuộc tính (attribute subset selection)

Thu giảm chiều (dimensionality reduction)

Thu giảm lượng (numerosity reduction)

Tạo phân cấp ý niệm (concept hierarchy generation) và rời rạc hóa (discretization)

Tiền xử lý dữ liệu 10

## TRANG 11

2.2. Tóm tắt mô tả về dữ liệu

Xác định các thuộc tính (properties) tiêu biểu của dữ liệu về xu hướng chính (central

tendency) và sự phân tán (dispersion) của dữ liệu

• Các độ đo về xu hướng chính: mean, median, mode, midrange

• Các độ đo về sự phân tán: quartiles, interquartile ra nge (IQR), variance

Làm nổi bật các giá trị dữ liệu nên được xem như nhiễu (noise) hoặc phần tử biên

(outliers), cung cấp cái nhìn tổng quan về dữ liệu

Tiền xử lý dữ liệu 11

## TRANG 12

2.2. Tóm tắt mô tả về dữ liệu

Dữ liệu mẫu về đơn giá của các mặt hàng đã được bán

Tiền xử lý dữ liệu 12

## TRANG 13

2.2. Tóm tắt mô tả về dữ liệu

Các độ đo về xu hướng chính của dữ liệu

Mean: giá trị trung bình

Weighted arithmetic mean

x if N odd  N / 2  Median Median = (x N / 2 + x N / 2 +1) / 2 if N even 

Mode: giá trị xuất hiện thường xuyên nhất trong tập dữ liệu

Midrange: giá trị trung bình của các giá trị lớn nhất và nhỏ nhất trong tập dữ liệu

Tiền xử lý dữ liệu 13

## TRANG 14

2.2. Tóm tắt mô tả về dữ liệu

Các độ đo về xu hướng chính của dữ liệu

Mean = Σ(count[i]*price[i])/Σ(count[i])

Weighted arithmetic mean

Median

Mode = price[i] nếu count[i] lớn nhất

Midrange = (Σ(count[i]*price[i]) + Σ(count[j]*price[j]))/(Σ(count[i]) + Σ(count[j])) nếu price[i] lớn nhất và price[j] nhỏ nhất

Tiền xử lý dữ liệu 14

## TRANG 15

2.2. Tóm tắt mô tả về dữ liệu

Các độ đo về sự phân tán của dữ liệu

Quartiles

The first quartile (Q1): the 25th percentile

The second quartile (Q2): the 50th percentile (median)

The third quartile (Q3): the 75th percentile

Interquartile Ra nge (IQR) = Q3 - Q1

Outliers (the most extreme observations): giá trị nằm cách trên Q3 hay dưới Q1 một khoảng 1.5x IQR

Variance

Tiền xử lý dữ liệu 15

## TRANG 16

2. Hiểu dữ liệu

Tóm tắt mô tả dữ liệu bởi độ tập trung và độ phân tán Độ phân tán:

❖ Quartiles: Tứ phân vị The first quartile (Q1): the 25th percentile The second quartile (Q2): the 50th percentile (median) The third quartile (Q3): the 75th percentile

❖ Interquartile Ra nge (IQR) = Q3 - Q1 Outliers: giá trị nằm cách trên Q3 hay dưới Q1 một khoảng 1.5x IQR

❖ Variance

## TRANG 17

2.2. Tóm tắt mô tả về dữ liệu

## Q1 Q2 Q3

## Tóm tắt mô tả về sự phân bố dữ liệu gồm năm trị số quan trọng: median, Q1, Q3, trị

lớn nhất, và trị nhỏ nhất (theo thứ tự: Minimum, Q1, Median, Q3, Maximum).

Tiền xử lý dữ liệu 17

## TRANG 18

2.3. Làm sạch dữ liệu

Xử lý dữ liệu bị thiếu (missing data)

Nhận diện phần tử biên (outliers) và giảm thiểu nhiễu (noisy data)

Xử lý dữ liệu không nhất quán (inconsistent data)

Tiền xử lý dữ liệu 18

## TRANG 19

2.3. Làm sạch dữ liệu

Xử lý dữ liệu bị thiếu (missing data)

Định nghĩa của dữ liệu bị thiếu

Dữ liệu không có sẵn khi cần được sử dụng

Nguyên nhân gây ra dữ liệu bị thiếu

Khách quan (không tồn tại lúc được nhập liệu, sự cố, …)

Chủ quan (tác nhân con người)

Giải pháp cho dữ liệu bị thiếu

Bỏ qua

Xử lý thủ công (không tự động, bán tự động)

Dùng giá trị thay thế (tự động): hằng số toàn cục, trị phổ biến nhất, trung bình toàn cục, trung bình cục bộ, trị dự đoán, …

Ngăn chặn dữ liệu bị thiếu: thiết kế tốt CSDL và các thủ tục nhập liệu (các ràng buộc dữ liệu)

Tiền xử lý dữ liệu 19

## TRANG 20

2.3. Làm sạch dữ liệu

❖Nhận diện phần tử biên (outliers) và giảm thiểu nhiễu (noisy data)

Định nghĩa

Outliers: những dữ liệu (đối tượng) không tuân theo đặc tính/hành vi chung của tập dữ liệu (đối tượng).

Noisy data: outliers bị loại bỏ (rejected/discarded outliers) như là những trường hợp ngoại lệ (exceptions).

Nguyên nhân

Khách quan (công cụ thu thập dữ liệu, lỗi trên đường truy ền, giới hạn công nghệ, …)

Chủ quan (tác nhân con người)

Tiền xử lý dữ liệu 20

## TRANG 21

2.3. Làm sạch dữ liệu

Nhận diện phần tử biên (outliers) và giảm thiểu nhiễu (noisy data)

Giải pháp nhận diện phần tử biên

Dựa trên phân bố thống kê (statistical distribution-based)

Dựa trên khoảng cách (distance-based)

Dựa trên mật độ (density-based)

Dựa trên độ lệch (deviation-based)

Giải pháp giảm thiểu nhiễu

Binning

Hồi quy (regression)

Phân tích cụm (cluster analysis)

Tiền xử lý dữ liệu 21

## TRANG 22

2.3. Làm sạch dữ liệu

Giải pháp giảm thiểu nhiễu

Binning (by bin means, bin median, bin boundaries)

• Dữ liệu có thứ tự

• Phân bố dữ liệu vào các bins (buckets)

• Bin boundaries: trị min và trị max

Tiền xử lý dữ liệu 22

## TRANG 23

2.3. Làm sạch dữ liệu

Nhận diện phần tử biên (outliers) và giảm thiểu nhiễu (noisy data)

Giải pháp giảm thiểu nhiễu

Hồi quy (regression)

y Y1

Y1’ y = ax + b

X1 x

Tiền xử lý dữ liệu 23

## TRANG 24

2.3. Làm sạch dữ liệu

❖Nhận diện phần tử biên (outliers) và giảm thiểu nhiễu (noisy data)

Giải pháp giảm thiểu nhiễu

▪Phân tích cụm (cluster analysis)

Tiền xử lý dữ liệu 24

## TRANG 25

2.3. Làm sạch dữ liệu

Xử lý dữ liệu không nhất quán

➢Định nghĩa của dữ liệu không nhất quán

❖Dữ liệu được ghi nhận khác nhau cho cùng một đối tượng/thực thể → discrepancies from inconsistent data representations

▪ 2015/12/25 và 25/12/2015

❖Dữ liệu được ghi nhận không phản ánh đúng ngữ nghĩa cho các đối tượng/thực thể

▪ Ràng buộc khóa ngoại

➢Nguyên nhân

• Sự không nhất quán trong các quiư ớc đặt tên hay mã dữ liệu

• Định dạng không nhất quán của các vùng nhập liệu

• Thiết bị ghi nhận dữ liệu, …

Tiền xử lý dữ liệu 25

## TRANG 26

2.3. Làm sạch dữ liệu

• Xử lý dữ liệu không nhất quán (inconsistent data)

• Giải pháp

• Tận dụng siêu dữ liệu, ràng buộc dữ liệu, sự kiểm tra của nhà phân tích dữ

liệu cho việc nhận diện

• Điều chỉnh dữ liệu không nhất quán bằng tay

• Các giải pháp biến đổi/chuẩn hóa dữ liệu tự động

Tiền xử lý dữ liệu 26

## TRANG 27

2.4. Tích hợp dữ liệu

Tích hợp dữ liệu: quá trình trộn dữ liệu từ các nguồn khác nhau vào một kho dữ liệu sẵn sàng cho quá trình khai phá dữ liệu

➢Vấn đề nhận dạng thực thể (entity identification problem)

➢Tích hợp lược đồ (schema integration)

➢So trùng đối tượng (object matching)

➢Vấn đề dư thừa (redundancy)

➢Vấn đề mâu thuẫn giá trị dữ liệu (data value conflicts) →Liên quan đến cấu trúc và tính không thuần nhất (heterogeneity) về ngữ nghĩa (semantics) của dữ liệu →Hỗ trợ việc giảm và tránh dư thừa và không nhất quan về dữ liệu → cải thiện tính chính xác và tốc độ quá trình khai phá dữ liệu

Tiền xử lý dữ liệu 27

## TRANG 28

2.4. Tích hợp dữ liệu

Vấn đề nhận dạng thực thể

Các thực thể (object/entity/attribute) đến từ nhiều nguồn dữ liệu.

Hai hay nhiều thực thể khác nhau diễn tả cùng một thực thể thực.

Ví dụ ở mức lược đồ (schema): customer_id trong nguồn S1 và cust_number trong nguồn S2.

Ví dụ ở mức thể hiện (instance): “R & D” trong nguồn S1 và “Research & Development” trong nguồn S2. “Male” và “Female” trong nguồn S1 và “Nam” và “Nữ” trong nguồn S2.

→ Vai trò của siêu dữ liệu (metadata)

Tiền xử lý dữ liệu 28

## TRANG 29

2.4. Tích hợp dữ liệu

❖Vấn đề dư thừa

Hiện tượng: giá trị của một thuộc tính có thể được dẫn ra/tính từ một/nhiều thuộc tính khác, vấn đề trùng lắp dữ liệu (duplication).

Nguyên nhân: tổ chức dữ liệu kém, không nhất quán trong việc đặt tên chiều/thuộc tính.

Phát hiện dư thừa: phân tích tương quan (correlation analysis)

Dựa trên dữ liệu hiện có, kiểm tra khả năng dẫn ra một thuộc tính B từ thuộc tính A.

Đối với các thuộc tính số (numerical attributes), đánh giá tương quan giữa hai thuộc tính với các hệ số tương quan (correlation coefficient, aka Pearson’s product moment coefficient).

Đối với các thuộc tính rời rạc (categorical/discrete attributes), đánh giá tương quan giữa hai thuộc tính với phép kiểm thử chi-square (2).

Tiền xử lý dữ liệu 29

## TRANG 30

2.4. Tích hợp dữ liệu

Phân tích tương quan giữa hai thuộc tính số A và B r A,B  [-1, 1] r A,B > 0: A và B tương quan thuận với nhau, trị số của A tăng khi trị số của B tăng, r A,B càng lớn thì mức độ tương quan càng cao, A hoặc B có thể được loại bỏ vì dư thừa.

r A,B = 0: A và B không tương quan với nhau (độc lập).

r A,B < 0: A và B tương quan nghịch với nhau, A và B loại trừ lẫn nhau.

Tiền xử lý dữ liệu 30

## TRANG 31

2.4. Tích hợp dữ liệu

Phân tích tương quan giữa hai thuộc tính số A và B

A

A

B B

A A A

## B B B

Tiền xử lý dữ liệu 31

## TRANG 32

2.4. Tích hợp dữ liệu

Phân tích tương quan giữa hai thuộc tính rời rạc A và B

A cóc giá trị phân biệt, a1, a2, …, ac.

B có r giá trị phân biệt, b1, b2, …, br.

oij: số lượng đối tượng (tuples) có trị thuộc tính A là ai và trị thuộc tính B là bj.

count(A=ai): số lượng đối tượng có trị thuộc tính A là ai.

count(B=bj): số lượng đối tượng có trị thuộc tính B là bj.

Tiền xử lý dữ liệu 32

## TRANG 33

2.4. Tích hợp dữ liệu

Phân tích tương quan giữa hai thuộc tính rời rạc A và B

Phép kiểm thống kê chi-square kiểm tra giả thuyết liệu A và B có độc lập với nhau dựa trên một mức quan trọng (significance level) với độ tự do (degree of freedom). Nếu giả thuyết bị loại bỏ thì A và B có sự liên hệ với nhau dựa trên thống kê.

- Độ tự do (degree of freedom): (r-1)*(c-1)

- Tra bảng phân bố chi-square để xác định giá trị 2.

- Nếu giá trị tính toán được lớn hơn hay bằng trị tra bảng được thì hai thuộc tính

A và B độc lập nhau (giả thuyết đúng).

Tiền xử lý dữ liệu 33

## TRANG 34

2.4. Tích hợp dữ liệu

Giới tính Giới tính (nữ) Tổng (nam) Sở thích (Fiction) 250 200 450

Sở thích 50 1000 1050 (Non Fiction) Tổng 300 1200 1500

0.5 0.10 0.05 0.02 0.01 0.001

1 0.455 2.706 3.841 5.412 6.635 10.827

2 1.386 4.605 5.991 7.824 9.210 13.815

3 2.366 6.251 7.815 9.837 11.345 16.268

4 3.357 7.779 9.488 11.668 13.277 18.465

5 4.351 9.236 11.070 13.388 15.086 20.51

Tiền xử lý dữ liệu 34

|  | Giới tính
(nam) | Giới tính (nữ) | Tổng |
| --- | --- | --- | --- |
| Sở thích (Fiction) | 250 | 200 | 450 |
| Sở thích
(NonFiction) | 50 | 1000 | 1050 |
| Tổng | 300 | 1200 | 1500 |

|  | 0.5 | 0.10 | 0.05 | 0.02 | 0.01 | 0.001 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.455 | 2.706 | 3.841 | 5.412 | 6.635 | 10.827 |
| 2 | 1.386 | 4.605 | 5.991 | 7.824 | 9.210 | 13.815 |
| 3 | 2.366 | 6.251 | 7.815 | 9.837 | 11.345 | 16.268 |
| 4 | 3.357 | 7.779 | 9.488 | 11.668 | 13.277 | 18.465 |
| 5 | 4.351 | 9.236 | 11.070 | 13.388 | 15.086 | 20.51 |

## TRANG 35

2.4. Tích hợp dữ liệu

## 300𝑥450

e11 = = 90 e12 = 360 1500 e21 = 210 e22 = 840 b1 = 300, b2 = 1200, a1 = 450, a2 = 1050 (250 −90)2 (50 −210)2 (200 −360)2 (1000 −840)2

## Χ = 507.93 = + + + = 507.93 > 10.827

90 210 360 840 (r-1)x(c-1) = (2-1)x(2-1) độ tự do và với độ chính xác 0.001 =&gt; Phủ định giả thiết Giới tính và sở thích đọc Fiction là độc lập với nhau.

Tiền xử lý dữ liệu 35

## TRANG 36

2.5. Biến đổi dữ liệu

Biến đổi dữ liệu: quá trình biến đổi hay kết hợp dữ liệu vào những dạng thích hợp cho quá trình khai phá dữ liệu

Làm trơn dữ liệu (smoothing)

Kết hợp dữ liệu (aggregation)

Tổng quát hoá (generalization)

Chuẩn hoá (normalization)

Xây dựng thuộc tính/đặc tính (attribute/feature construction)

Tiền xử lý dữ liệu 36

## TRANG 37

2.5. Biến đổi dữ liệu

Làm trơn dữ liệu (smoothing)

Các phương pháp binning (bin means, bin medians, bin boundaries)

Hồi quy

Các kỹ thuật gom cụm (phân tích phần tử biên)

Các phương pháp rời rạc hóa dữ liệu (các phân cấp ý niệm)

→ Loại bỏ/giảm thiểu nhiễu khỏi dữ liệu.

Tiền xử lý dữ liệu 37

## TRANG 38

2.5. Biến đổi dữ liệu

Kết hợp dữ liệu (aggregation)

Các tác vụ kết hợp/tóm tắt dữ liệu

Chuyển dữ liệu ở mức chi tiết này sang dữ liệu ở mức kém chi tiết hơn

Hỗ trợ việc phân tích dữ liệu ở nhiều độ mịn thời gian khác nhau

→ Thu giảm dữ liệu (data reduction)

Tiền xử lý dữ liệu 38

## TRANG 39

2.5. Biến đổi dữ liệu

Tổng quát hóa (generalization)

Chuyển đổi dữ liệu cấp thấp/nguyên tố/thô sang các khái niệm ở mức cao hơn thông qua các phân cấp ý niệm

→ Thu giảm dữ liệu (data reduction)

Tiền xử lý dữ liệu 39

## TRANG 40

2.5. Biến đổi dữ liệu

Chuẩn hóa (normalization)

min-max normalization

z-score normalization

Normalization by decimal scaling

→Các giá trị thuộc tính được chuyển đổi vào một miền trị nhất định được định nghĩa trước.

Tiền xử lý dữ liệu 40

## TRANG 41

2.5. Biến đổi dữ liệu

Chuẩn hóa (normalization)

min-max normalization

• Giá trị cũ: v [min A, max A]

• Giá trị mới: v’  [new_min A, new_max A]

→Ví dụ: chuẩn hóa điểm số từ 0-4.0 sang 0-10.0.

→Đặc điểm của phép chuẩn hóa min-max?

Tiền xử lý dữ liệu 41

## TRANG 42

2.5. Biến đổi dữ liệu

Chuẩn hóa (normalization)

z-score normalization

Giá trị cũ: v tương ứng với mean Ā và standard deviation б A

Giá trị mới: v’

→ Đặc điểm của chuẩn hóa z-score?

Tiền xử lý dữ liệu 42

## TRANG 43

2.5. Biến đổi dữ liệu

Chuẩn hóa (normalization)

Normalization by decimal scaling

Giá trị cũ: v

Giá trị mới: v’ với j là số nguyên nhỏ nhất sao cho Max(|v’|) < 1

Tiền xử lý dữ liệu 43

## TRANG 44

2.5. Biến đổi dữ liệu

Xây dựng thuộc tính/đặc tính (attribute/feature construction)

Các thuộc tính mới được xây dựng và thêm vào từ tập các thuộc tính sẵn có.

Hỗ trợ kiểm tra tính chính xác và giúp hiểu cấu trúc của dữ liệu nhiều chiều.

Hỗ trợ phát hiện thông tin thiếu sót về các mối quan hệ giữa các thuộc tính dữ liệu.

→ Các thuộc tính dẫn xuất

Tiền xử lý dữ liệu 44

## TRANG 45

2.6. Thu giảm dữ liệu

Tập dữ liệu được biến đổi đảm bảo các toàn vẹn, nhưng nhỏ/ít hơn nhiều về số lượng so với ban đầu.

Các chiến lược thu giảm

Kết hợp khối dữ liệu (data cube aggregation)

Chọn một số thuộc tính (attribute subset selection)

Thu giảm chiều (dimensionality reduction)

Thu giảm lượng (numerosity reduction)

Rời rạc hóa (discretization)

Tạo phân cấp ý niệm (concept hierarchy generation) → Thu giảm dữ liệu: lossless và lossy

Tiền xử lý dữ liệu 45

## TRANG 46

2.6. Thu giảm dữ liệu

Kết hợp khối dữ liệu (data cube aggregation)

Dạng dữ liệu: additive, semi- additive (numerical) Sum() Kết hợp dữ liệu bằng các hàm nhóm: average, min, max, sum, count, …

→Dữ liệu ở các mức trừu tượng khác nhau.

→Mức trừu tượng càng cao giúp thu giảm lượng dữ liệu càng cube: Sale nhiều.

Tiền xử lý dữ liệu 46

## TRANG 47

2.6. Thu giảm dữ liệu

❖Chọn một số thuộc tính (attribute subset selection)

Giảm kích thước tập dữ liệu bằng việc loại bỏ những thuộc tính/chiều/đặc trưng (attribute/dimension/feature) dư thừa/không thích hợp (redundant/irrelevant)

## Mục tiêu: tập ít các thuộc tính nhất vẫn đảm bảo phân bố xác suất (probability

distribution) của các lớp dữ liệu đạt được gần với phân bố xác suất ban đầu với tất cả các thuộc tính

→ Bài toán tối ưu hóa: vận dụng heuristics

Tiền xử lý dữ liệu 47

## TRANG 48

2.6. Thu giảm dữ liệu

Chọn một số thuộc tính (attribute subset selection)

Tiền xử lý dữ liệu 48

## TRANG 49

2.6. Thu giảm dữ liệu

Thu giảm chiều (dimensionality reduction)

Biến đổi wavelet (wavelet transforms)

Phân tích nhân tố chính (principal component analysis)

→ đặc điểm và ứng dụng?

Tiền xử lý dữ liệu 49

## TRANG 50

2.6. Thu giảm dữ liệu

Thu giảm lượng (numerosity reduction)

Các kỹ thuật giảm lượng dữ liệu bằng các dạng biểu diễn dữ liệu thay thế.

Các phương pháp có thông số (parametric): mô hình ư ớc lượng dữ liệu → các thông số được lưu trữ thay cho dữ liệu thật

Hồi quy

Các phương pháp phi thông số (nonparametric): lưu trữ các biểu diễn thu giảm của dữ liệu

Histogram, Clustering, Sampling

Tiền xử lý dữ liệu 50

## TRANG 51

2.7. Rời rạc hóa dữ liệu

❖Giảm số lượng giá trị của một thuộc tính liên tục (continuous attribute) bằng các chia miền trị thuộc tính thành các khoảng (intervals)

❖Các nhãn (labels) được gán cho các khoảng (intervals) này và được dùng thay giá trị thực của thuộc tính

❖Các trị thuộc tính có thể được phân hoạch theo một phân cấp (hierarchical) hayở nhiều mức phân giải khác nhau (multiresolution)

Tiền xử lý dữ liệu 51

## TRANG 52

2.7. Rời rạc hóa dữ liệu

❖Rời rạc hóa dữ liệu cho các thuộc tính số (numeric attributes)

Các phân cấp ý niệm được dùng để thu giảm dữ liệu bằng việc thu thập và thay thế các ý niệm cấp thấp bởi các ý niệm cấp cao.

Các phân cấp ý niệm được xây dựng tự động dựa trên việc phân tích phân bố dữ liệu.

Chi tiết của thuộc tính sẽ bị mất.

Dữ liệu đạt được có ý nghĩa và dễ được diễn dịch hơn, đòi hỏi ít không gian lưu trữ hơn.

Tiền xử lý dữ liệu 52

## TRANG 53

2.7. Rời rạc hóa dữ liệu

Các phương pháp rời rạc hóa dữ liệu cho các thuộc tính số

Binning

Histogram analysis

Interval merging by 2 analysis

Cluster analysis

Entropy-based discretization

Discretization by “natural/intuitive partitioning”

Tiền xử lý dữ liệu 53

## TRANG 54

2.8. Tạo cây phân cấp ý niệm

Dữ liệu phân loại (categorical data)

Dữ liệu rời rạc (discrete data)

Miền trị thuộc tính phân loại (categorical attribute)

Số giá trị phân biệt hữu hạn

Không có thứ tự giữa các giá trị

→ Tạo phân cấp ý niệm cho dữ liệu rời rạc

Tiền xử lý dữ liệu 54

## TRANG 55

2.8. Tạo cây phân cấp ý niệm

Các phương pháp tạo phân cấp ý niệm cho dữ liệu rời rạc (categorical/discrete data)

Đặc tả thứ tự riêng phần (partial ordering)/thứ tự toàn phần (total ordering) của các thuộc tính tường minh ở mức lược đồ bởi người sử dụng hoặc chuyên gia

Đặc tả một phần phân cấp bằng cách nhóm dữ liệu tường minh

Tiền xử lý dữ liệu 55

## TRANG 56

2.8. Tạo cây phân cấp ý niệm

Các phương pháp tạo phân cấp ý niệm cho dữ liệu rời rạc (categorical/discrete data)

Đặc tả một tập các thuộc tính, nhưng không bao gồm thứ tự riêng phần của chúng

Đặc tả chỉ một tập riêng phần các thuộc tính (partial set of attributes)

Tạo phân cấp ý niệm bằng cách dùng các kết nối ngữ nghĩa được chỉ định trước

Tiền xử lý dữ liệu 56

## TRANG 57

2.9. Tóm tắt

❖Dữ liệu thực tế: không đầy đủ (incomplete/missing), nhiễu (noisy), không nhất quán (inconsistent)

❖Quá trình tiền xử lý dữ liệu

➢làm sạch dữ liệu: xử lý dữ liệu bị thiếu, làm trơn dữ liệu nhiễu, nhận dạng các phần tử biên, hiệu chỉnh dữ liệu không nhất quán

➢tích hợp dữ liệu: vấn đề nhận dạng thực thể, vấn đề dư thừa, vấn đề mâu thuẫn giá trị dữ liệu

➢biến đổi dữ liệu: làm trơn dữ liệu, kết hợp dữ liệu, tổng quát hóa, chuẩn hóa, xây dựng thuộc tính/đặc tính

➢thu giảm dữ liệu: kết hợp khối dữ liệu, chọn một số thuộc tính, thu giảm chiều, rời rạc hóa và tạo phân cấp ý niệm

Tiền xử lý dữ liệu 57

## TRANG 58

2.9. Tóm tắt

❖Rời rạc hóa dữ liệu

Thu giảm số trị của một thuộc tính liên tục (continuous attribute) bằng cách chia miền trị thành các khoảng (interval) có dán nhãn. Các nhãn này được dùng thay cho các giá trị thực.

Tiến hành theo hai cách: trên xuống (top do wn) và dưới lên (bottom up), có giám sát (supervised) và không có giám sát (unsupervised).

Tạo phân hoạch phân cấp/đa phân giải (multiresolution) trên các trị thuộc tính → phân cấp ý niệm cho thuộc tính số (numerical attribute)

❖Tạo cây phân cấp ý niệm

Hỗ trợ khai phá dữ liệu ở nhiều mức trừu trượng Cho thuộc tính số (numerical attributes): binning, histogram analysis, entropy-based discretization, 2-merging, cluster analysis, discretization by intuitive partitioning

Cho thuộc tính phân loại/rời rạc (categorical/discrete attributes): chỉ định tường minh bởi người sử dụng hay chuyên gia, nhóm dữ liệu tường minh, dựa trên số lượng trị phân biệt (khác nhau) của mỗi thuộc tính

Tiền xử lý dữ liệu 58

## TRANG 59

Cho dữ liệu về một thuộc tính A của một tập 12 đối tượng như sau: 4, 6, 5, 9, 8, 1, 3, 2, 7, 10, 12, 11. Kết quả nào sau đây là hợp lý nhất khi thực hiện làm trơn dữ liệu (giảm thiểu nhiễu) với 3 bin có cùng số lượng đối tượng và sử dụng bin boundaries?

a. bin 1: 4, 4, 9, 9; bin 2: 8, 8, 2, 2; bin 3: 7, 7, 11, 11 b. bin 1: 1, 1, 4, 4; bin 2: 5, 5, 8, 8; bin 3: 9, 9, 12, 12 c. bin 1: 4, 4, 9, 9; bin 2: 1, 1, 8, 8; bin 3: 7, 7, 12, 12 d. bin 1: 4, 6, 6, 9; bin 2: 8, 3, 3, 2; bin 3: 7, 10, 10, 11 e. Ý kiến khác.

5/23/2026 59

## TRANG 60

Cho dữ liệu về một thuộc tính A của một tập 20 đối tượng như sau: 4, 9, 6, 4, 5, 9, 15, 8, 1, 1, 3, 13, 2, 7, 10, 9, 12, 11, 14, 16. Kết quả rời rạc hóa với 4 đoạn (interval) nào sau đây là kết quả của phương pháp historam analysis dùng equal width?

a. Interval 1 = [4, 5] gồm: 4, 9, 6, 4, 5; Interval 2 = [9, 1] gồm: 9, 15, 8, 1, 1; Interval 3 = [3, 10] gồm: 3, 13, 2, 7, 10; Interval 4 = [9, 16] gồm: 9, 12, 11, 14, 16.

b. Interval 1 = [1, 4] gồm: 1, 1, 2, 3, 4; Interval 2 = [4, 8] gồm: 4, 5, 6, 7, 8; Interval 3 = [9, 11] gồm: 9, 9, 9, 10, 11; Interval 4 = [12, 16] gồm: 12, 13, 14, 15, 16.

c. Interval 1 = [1, 4] gồm: 1, 1, 2, 3, 4, 4; Interval 2 = [5, 8] gồm: 5, 6, 7, 8; Interval 3 = [9, 12] gồm: 9, 9, 9, 10, 11, 12; Interval 4 = [13, 16] gồm: 13, 14, 15, 16.

d. Interval 1 = [4, 9] gồm: 4, 4, 5, 6, 9; Interval 2 = [1, 15] gồm: 1, 1, 8, 9, 15; Interval 3 = [2, 13] gồm: 2, 3, 7, 10, 13; Interval 4 = [9, 16] gồm: 9, 11, 12, 14, 16.

e. Ý kiến khác.

5/23/2026 60

## TRANG 61

Những vấn đề nào có thể gặp phải khi tích hợp dữ liệu từ nhiều nguồn dữ liệu khác nhau vào một kho dữ liệu tập trung?

a. Dư thừa dữ liệu do khả năng dẫn xuất ra nhau giữa dữ liệu của các thuộc tính.

b. Không nhất quán về việc biểu diễn dữ liệu, cấu trúc và ngữ nghĩa của dữ liệu, đơn vị đo lường dữ liệu, mã hóa dữ liệu.

c. Trùng lắp dữ liệu.

d. Giảm độ chính xác của dữ liệu.

e. Ý kiến khác.

5/23/2026 61

## TRANG 62

Hỏi & Đáp …

Tiền xử lý dữ liệu 62
