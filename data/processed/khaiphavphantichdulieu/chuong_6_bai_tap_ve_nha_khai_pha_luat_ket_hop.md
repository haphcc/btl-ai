### BÀI 6

#### CHUONG 6 BAI TAP VE NHA KHAI PHA LUAT KET HOP

## Bài tập 1

❖ Cho cơ sở dữ liệu giao dịch bán hàng gồm 5 giao dịch:

Áp dụng thuật toán brute force và apriori tìm tập mục phổ biến với minsup = 40% Áp dụng thuật toán Apriori tìm các luật kết hợp trong giao dịch bán hàng trên với min_supp = 40%; min_conf = 80%.

## Bài tập 2

❖ Cho cơ sở dữ liệu như sau:

Mã Khách hàng Nghề nghiệp Sở thích Thu nhập Mua

Kh01 KD Ca nhạc 10 triệu Có

Kh02 KD Du lịch 7 triệu Không

Kh02 Kỹ sư Du lịch Có

Kh04 Kỹ sư Ca nhạc 20 triệu Có

Kh05 KD Phim 5 triệu Không

Hãy biến đổi tập dữ liệu đã cho về dạng dữ liệu phù hợp với bài toán khai phá luật kết hợp. Tìm các luật kết hợp với độ hỗ trợ tối thiểu min_supp=40%; Độ tin cậy tối thiểu min_conf=70%.

| Mã Khách hàng | Nghề nghiệp |  | Thu nhập | Mua |
| --- | --- | --- | --- | --- |
| Kh01 | KD |  | 10 triệu | Có |
| Kh02 | KD |  | 7 triệu | Không
Có |
| Kh02 | Kỹ sư | Du lịch |  |  |
| Kh04 | Kỹ sư | Ca nhạc | 20 triệu | Có |
| Kh05 | KD | Phim | 5 triệu | Không |

## Bài tập 3

❖ Cho cơ sở dữ liệu như sau:

## Mã KH SP1 SP2 SP3

KH01 Bút Vở KH02 Vở Giấy Kéo KH03 Giấy Kéo Hồ KH02 Hồ Giấy KH04 Bút Giấy Vở

Hãy biến đổi tập dữ liệu đã cho về dạng dữ liệu phù hợp với bài toán khai phá luật kết hợp. Tìm các luật kết hợp với độ hỗ trợ tối thiểu min_supp=40%; Độ tin cậy tối thiểu min_conf=70%.

| Mã KH | SP1 | SP2 | SP3 |
| --- | --- | --- | --- |
| KH01 | Bút | Vở |  |
| KH02 | Vở | Giấy | Kéo |
| KH03 | Giấy | Kéo | Hồ |
| KH02 | Hồ | Giấy |  |
| KH04 | Bút | Giấy | Vở |
