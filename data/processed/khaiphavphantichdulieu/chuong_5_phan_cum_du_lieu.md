### BÀI 5

#### CHUONG 5 PHAN CUM DU LIEU

Giảng viên: LÊ THỊ HỒNG NHUNG Điện thoại: 0987867486 Email: nhunglth@hvnh. edu. vn

## CHƯƠNG 5: PHÂN CỤM DỮ LIỆU

## Chương 5: Phân cụm dữ liệu

1. Tổng quan về phân cụm dữ liệu

2. Các thuật toán phân cụm dữ liệu

3. Thuật toán phân cụm Kmeans

4. Ví dụminh họa

## LANH

EI

## BAV |HỌC VIỆN ` K

egrets Tinh huong 2 =

- a

ae _ = Sế »Be se Cluster Galt `.

e #.

Cluster 3

ra #

` Ciuster2 i # * # s:

F- #} # $ # bể`.

#” s4 § #ạ * e & š # e # # = ai

income

Tình huống tổng quát

• Cho trước một tập dữ liệu với các thuộc tính khác nhau.

• Hãy tìm các dữ liệu có đặc điểm tương tựnhau?

Phát biểu bài toán phân cụm dữ liệu

Phân cụm dữ liệu là quá trình học không giám sát trên một tập dữ liệu đầu vào nhằm phân chia tập dữ liệu ban đầu thành các tập dữ liệu con có tính chất tương tựnhau.

Đầu vào: Tập dữ liệu D gồm n phần tử trong không gian m chiều.

D = {x1, x2,…,xn} xi = (x1i, x2i,…, xm i) mô tảm thuộc tính của phần tửth ứi.

Đầu ra: Phân các dữ liệu thuộc D thành các cụm sao cho:

Các phần tử trong cùng một cụm có tính chất tương tựnhau (gần nhau).

Các phần tửởcác cụm khác nhau có tính chất khác nhau (xa nhau).

Phát biểu bài toán phân cụm dữ liệu

Minh hoạ kỹ thuật phân cụm

Ứng dụng của bài toán phân cụm

Thương mại: phân đoạn khách hàng…

Ứng dụng của bài toán phân cụm

 Sản xuất: chia nhóm sản phẩm

Ứng dụng của bài toán phân cụm

Sinh học: gom nhóm động thực vật qua các đặc điểm của chúng…

Ứng dụng của bài toán phân cụm

Nông nghiệp

Ứng dụng của bài toán phân cụm

Địa lý

Ứng dụng của bài toán phân cụm

Y học

Ứng dụng của bài toán phân cụm

Thiên văn học

Các phương pháp phân cụm dữ liệu

Phân cụm phân vùng (phân cụm phẳng) Nhằm phân một tập dữ liệu cón phần tửcho trước thành k nhóm dữ liệu sao cho: mỗi phần tử dữ liệu chỉthu ộc về một nhóm dữ liệu và mỗi nhóm dữ liệu có tối thiểu một phần tử dữ liệu.

Tiếp cận: từd ưới lên (gộp dần), từtr ên xuống (chia dần) Độđo tương tự/ khoảng cách K-mean, k-mediod, CLARANS, …

Các phương pháp phân cụm dữ liệu

Phân cụm phân cấp Nhằm phân một tập dữ liệu cón phần tửcho trước thành một cấu trúc có một thứt ựph ân cấp nhất định (thường có dạng hình cây) Độđo tương tự/ khoảng cách

## HAC, CHAMELEON, BIRRCH, CURE…

Các phương pháp phân cụm dữ liệu

Phân cụm dựa theo mật độ Hàm mật độ: Xác định các phần tửchính tại nơi có mật độcao.

Hàm liên kết: Xác định cụm là tập hợp các đối tượng lân cận của một đối tượng dữ liệu theo một ngưỡng nào đó.

Có thểph át hiện ra các cụm dữ liệu với hình thù bất kỳ.

Khắc phục được các phân tửngoại lai hoặc giá trịnhi ễu rất tốt, nhưng việc xác định các tham số mật độr ất khó khăn.

## DBSCAN, OPTICS…

Các phương pháp phân cụm dữ liệu

Phân cụm dựa theo mô hình Giảthi ết: Tồn tại một số mô hình dữ liệu cho phân cụm.

Phương pháp phân cụm dựa trên mô hình cốg ắng khớp giữa dữ liệu với mô hình toán học dựa trên giả định dữ liệu được tạo ra bằng hỗn hợp phân phối xác suất cơ bản nhằm xác định mô hình tốt nhất phù hợp với dữ liệu.

MCLUST, Mạng Nơron

Các phương pháp phân cụm dữ liệu

Phân cụm mờ Giảthi ết: không có phân cụm “cứng” cho dữ liệu và đối tượng có thể thuộc một số cụm.

Sử dụng hàm mờt ừcác đối tượng tới các cụm FCM (Fuzzy CMEANS),…

Các dạng dữ liệu phân cụm

Thuộc tính số(numeric) • ví dụthu nhập Thuộc tính định danh (nominal): Miền giá trịl à một tập hợp hữu hạn và đếm được các phần tử • ví dụngh ềnghiệp Thuộc tính nhịph ân (binominal): Là trường hợp đặc biệt của thuộc tính định danh • miền giá trịch ỉcó hai phần tửnh ư: Yes/No, 0/1, True/False… Thuộc tính văn bản (text)

Tiền xử lý dữ liệu phân cụm

Xử lý dữ liệu thiếu

• Thay thế dữ liệu thiếu bằng giá trị dữ liệu trung bình

• Thay thế dữ liệu thiếu bằng giá trị dữ liệu xuất hiện nhiều nhất

• Thay thế dữ liệu thiếu bằng giá trị dữ liệu xuất hiện ít nhất

• Loại bỏb ản ghi có chứa dữ liệu thiếu… Xử lý dữ liệu nhiễu

• Phát hiện và xử lý tương tự dữ liệu thiếu

Các độđo dữ liệu

Đểph ân cụm, ta phải xác định “khoảng cách” giữa các đối tượng, tức là phép đo độtương tự(Similar) hoặc là độphi tương tự(Dissimilar) giữa các đối tượng dữ liệu.

Độđo cơ bản là độđo metric, xác định “khoảng cách” giữa từng cặp phần tửtheo khoảng cách hình học.

d(x,y) là độđo metric xác định khoảng cách giữa hai

## phần tửx, y nếu:

• d(x,y) > 0 nếu x ≠y • d(x, y) = 0 nếu x =y • d(x,y) = d(y,x) với mọi x,y • d(x,y) ≤d(x,z)+d(z,y)

Công thức tính khoảng cách - Dữ liệu số

Khoảng cách Minskowski:

Khoảng cách Euclide: trường hợp đặc biệt của khoảng cách Minskowski trong trường hợp q=2

Khoảng cách Manhattan: trường hợp đặc biệt của khoảng cách Minskowski trong trường hợp q=1

Công thức tính khoảng cách - Dữ liệu nhịph ân

Xét hai đối tượng x vày có tất cả các thuộc tính đều nhận giá trịnh ịph ân.

Khoảng cách sai lệch giữa hai thuộc tính được tính bởi công thức:

𝑏+𝑐 d(x,y) =

## 𝑎+𝑏+𝑐+𝑑

• a: tổng số thu ộc tính có giá trị1 trong cảx vày

• b: tổng số thu ộc tính có giá trị1 trong x và 0 trong y

• c: tổng số thu ộc tính có giá trị0 trong x và 1 trong y

• d: tổng số thu ộc tính có giá trị0 trong cảx vày

Thuật toán phân cụm Kmeans

Là thuật toán phân cụm phẳng trong đó tâm của mỗi cụm là giá trịtrung bình của tất cả các phần tử trong cụm.

Input:

• Tập dữ liệu D = {x1, x2,…,xn} gồm n phần tử trong không gian m chiều.

• Số cụm k.

Output:

• k cụm dữ liệu D1, D2,…,Dk thỏa mãn điều kiện:

Các phần tử trong cùng một cụm có tính chất tương tựnhau.

Các phần tử trong các cụm khác nhau có tính chất khác nhau.

Thuật toán phân cụm Kmeans

Thuật toán:

1. Khởi động

Chọn ngẫu nhiên k phần tử trong D làm trọng tâm ci cho cụm Di (i=1,2,…,k)

2. Bước lặp

2.1 Gán =  Di 2.2 Với mọi xD 2.2.1 Tính khoảng cách i=1,2,…,k d(x,ci,) 2.2.2 = nếu nhỏnh ất với i=1,2,…,k Di Dix d(x,ci,) 2.3 Tính lại trọng tâm các cụm i=1,2,…,k Divới 1 ci = σ 𝑥𝑣ớ𝑖xDi |𝐷𝑖|

3. Lặp lại bước 2 cho đến khi quá trình hội tụ(không có sựthay đổi các

## phần tử trong các cụm)

Thuật toán phân cụm Kmeans

Kết quả cuối cùng của K-means phụ thuộc rất nhiều vào cách lựa chọn k ban đầu làm trọng tâm của k cụm.

Ta có thể tiến hành thí nghi ệm một số lần nhất định với giá trị khởi tạo khác nhau và chọn kết quả của lần chạy tối ưu nhất.

Trong thực tế, nếu dữ liệu quá lớn hoặc giải thuật không hội tụ (Thuật toán không dừng) có thể dẫn đến thời gian chạy lớn. Do đó, ta có thể sử dụng thêm các điều kiện dừng như dưới đây:

• Khi số lượng vòng lặp vượt quá một ngưỡng nào đó. Tuy nhiên, điều kiện dừng này có thể làm cho quá trình phân cụm không được tốt do có thể số vòng chạy chưa đạt mức cần thiết • Khi giá trị J nhỏ hơn một ngưỡng nào đó (người lập trình thiết lập ngưỡng chấp nhận được của thuật toán) • Khi hiệu hai giá trị liên tiếp của J nhỏ hơn một ngưỡng nào đó.

Trên thực tế, 3 điều kiện dừng trên có thể được dùng kết hợp với nhau.

Ví dụminh họa phân cụm Kmeans

Giả sử có 4 loại thuốc A,B,C,D

• Mỗi loại thuốc được biểu diễn bởi 2 đặc trưng X vàY.

• Hãy phân nhóm các thuốc đã cho vào hai cụm (k=2) dựa vào các đặc trưng của chúng.

Thuốc Đặc trưng X Đặc trưng Y

## A 1 1

## B 2 1

## C 4 3

## D 5 4

| Thuốc | Đặc trưng X | Đặc trưng Y |
| --- | --- | --- |
| A | 1 | 1 |
| B | 2 | 1 |
| C | 4 | 3 |
| D | 5 | 4 |

Ví dụminh họa phân cụm Kmeans

Bước 1: Khởi tạo trọng tâm cho 2 cụm. Thuố X Y c

• A 1 1 Giảsửch ọn A là tâm cụm 1, ta có: c1= (1,1) B 2 1 • Chọn B là tâm cụm 2, ta có: c2 = (2,1)

## C 4 3

Bước 2: Tính khoảng cách giữa các đối tượng tới D các 5c ụm:4 d(A, c1) = 0 d(A, c2) = (1 −2)2+(1 −1)2 = 1 d(B, c1) = (2 −1)2+(1 −1)2 = 1 d(B, c2) = 0 d(C, c1) = (4 −1)2+(3 −1)2 = 3.61 d(C, c2) = (4 −2)2+(3 −1)2 = 2.83 d(D, c1) = (5 −1)2+(4 −1)2 = 5 d(D, c2) = (5 −2)2+(4 −1)2 = 4.24 Bước 3: Xác định đối tượng cho các cụm:

• Ta có: Cụm 1(A); Cụm 2(B,C,D)

| Thuốc | X | Y |
| --- | --- | --- |
| A | 1 | 1 |
| B | 2 | 1 |
| C | 4 | 3 |
| i các
D | cụm
5 |:
4 |

Ví dụminh họa phân cụm Kmeans

Bước 4: Tính lại trọng tâm cho 2 cụm. Thuố X Y c

• A 1 1 c1= (1,1)

## 2+4+5 1+3+4 B 2 1

• c2 = (,) = (3.67, 2.67) 3 3 C 4 3 Bước 5: Tính khoảng cách giữa các đối tượng Dtới các5 cụm4 mới:

d(A, c1) = 0 d(A, c2) = (1 −3.67)2+(1 −2.67)2 = 3.14 d(B, c1) = 1 d(B, c2) = (2 −3.67)2+(1 −2.67)2 = 2.36 d(C, c1) = 3.61 d(C, c2) = (4 −3.67)2+(3 −2.67)2 = 0.47 d(D, c1) = 5 d(D, c2) = (5 −3.67)2+(4 −2.67)2 = 1.89 Bước 6: Xác định đối tượng cho các cụm:

• Ta có: Cụm 1(A,B); Cụm 2(C,D)

| Thuốc | X | Y |
| --- | --- | --- |
| A | 1 | 1 |
| B | 2 | 1 |
| C | 4 | 3 |
| Dtới | c5ác | cụ4 m |

Ví dụminh họa phân cụm Kmeans

Bước 7: Tính lại trọng tâm cho 2 cụm. Thuố X Y c 1+2 1+1 • A 1 1 c1= (,) = (1.5, 1) 2 2

## 4+5 3+4 B 2 1

• c2 = (,) = (4.5, 3.5) 2 2 C 4 3 Bước 8: Tính khoảng cách giữa các đối tượng Dtới các5 cụm4 mới:

d(A, c1) = (1 −1.5)2+(1 −1)2 = 0.5 d(A, c2) = (1 −4.5)2+(1 −3.5)2 = 4.3 d(B, c1) = (2 −1.5)2+(1 −1)2 = 0.5 d(B, c2) = (2 −4.5)2+(1 −3.5)2 = 3.54 d(C, c1) = (4 −1.5)2+(3 −1)2 = 3.2 d(C, c2) = (4 −4.5)2+(3 −3.5)2 = 0.71 d(D, c1) = (5 −1.5)2+(4 −1)2 = 4.61 d(D, c2) = (5 −4.5)2+(4 −3.5)2 = 0.71 Bước 9: Xác định đối tượng cho các cụm:

• Ta có: Cụm 1(A,B); Cụm 2(C,D) →Đối tượng các cụm không thay đổi →Dừng.

| Thuốc | X | Y |
| --- | --- | --- |
| A | 1 | 1 |
| B | 2 | 1 |
| C | 4 | 3 |
| tới
D | các
5 | cụm
4 |

Ví dụth ực hành

Phân cụm dữ liệu khách hàng tín dụng Mỗi khách hàng được mô tảb ởi 5 thuộc tính Phân cụm khách hàng thành 2 cụm

Thu nhập Nghề Chi tiêu (triệu Tài khoản TID (triệu Tuổi nghiệp đồng/tháng) tiết kiệm đồng/tháng) A 5.5 23 Viên chức 4.5 Không

B 8 25 Tư nhân 4 CóC 10 32 Tư nhân 8 Có

D 12 40 Viên chức 7 Có

E 4 24 Tư nhân 4 Không

F 25 50 Viên chức 12 Có

| TID | Thu nhập
(triệu
đồng/tháng) | Tuổi | Nghề
nghiệp | Chi tiêu (triệu
đồng/tháng) | Tài khoản
tiết kiệm |
| --- | --- | --- | --- | --- | --- |
| A | 5.5 | 23 | Viên chức | 4.5 | Không |
| B | 8 | 25 | Tư nhân | 4 | Có |
| C | 10 | 32 | Tư nhân | 8 | Có |
| D | 12 | 40 | Viên chức | 7 | Có |
| E | 4 | 24 | Tư nhân | 4 | Không |
| F | 25 | 50 | Viên chức | 12 | Có |

Vấn đềch ọn số cụm trong phân cụm Kmeans

Số cụm ít: khoảng cách giữa các đối tượng trong cụm xa.

Vấn đềch ọn số cụm trong phân cụm Kmeans

Số cụm lớn: khoảng cách giữa các cụm quá nhỏ, không mang tính khái quát cao.

Vấn đềch ọn số cụm trong phân cụm Kmeans

Số cụm vừa đủ: khoảng cách giữa các đối tượng trong cụm hợp lý.

Vấn đềch ọn số cụm trong phân cụm Kmeans

Phương pháp elbow trong lựa chọn số cụm Phương pháp Elbow là một cách giúp ta lựa chọn được số lượng các cụm phù hợp dựa vào đồ thị trực quan hoá bằng cách nhìn vào sự suy giảm của hàm biến dạng và lựa chọn ra điểm khuỷ tay (elbow point).

Đánh giá chất lượng phân cụm

• Phụthu ộc vào kinh nghi ệm và mức độhi ểu dữ liệu của người phân tích.

• Tính chất của các cụm:

Compactness - độ cô đọng súc tích: độ dính kết của từng cặp đối tượng trong từng cụm riêng rẽ. Độ tương tự càng cao, độ cô đọng càng lớn.

Isolation - độ cô lập: độ đo về sự tách biệt giữa một cụm với những cụm khác.

Đánh giá chất lượng phân cụm

• Phụthu ộc vào kinh nghi ệm và mức độhi ểu dữ liệu của người phân tích.

• Tính chất của các cụm:

Compactness - độ cô đọng súc tích: độ dính kết của từng cặp đối tượng trong từng cụm riêng rẽ. Độ tương tự càng cao, độ cô đọng càng lớn.

Isolation - độ cô lập: độ đo về sự tách biệt giữa một cụm với những cụm khác.

Đánh giá chất lượng phân cụm

Đánh giá ngoài (external evaluation): chất lượng các cụm được đánh giá thông qua mức độtương đồng giữa các cụm được tạo ra với tập dữ liệu mẫu.

Đánh giá trong (internal evaluation): Chất lượng các cụm được đánh giá bởi chính dữ liệu của chúng thông qua các đại lượng mô tảs ựli ên kết cụm như mật độc ụm, khoảng cách giữa các phần tửb ên trong cụm hay khoảng cách giữa các cụm với nhau...

Đánh giá chất lượng phân cụm

Độđo Silhouette

## 𝑏𝑖−𝑎(𝑖)

𝑠𝑖=

## 𝑚𝑎𝑥𝑎𝑖, 𝑏(𝑖)

Trong đó:

đặt 𝑎(𝑖) là khoảng cách trung bình từ 𝑖t ới tất cả các phần tử trong cùng cụm với 𝑖;

𝑏𝑖l à khoảng cách trung bình ngắn nhất từ 𝑖t ới bất kỳ cụm nào không chứa 𝑖.

𝑠(𝑖) có giá trị nằm trong đoạn −1,1, 𝑖được gọi là phù hợp với cụm nó được phân nếu 𝑠(𝑖) có giá trị gần 1;

𝑖kh ông thể xác định được nó nên thuộc vào cụm nào nếu 𝑠(𝑖) = 0;

𝑖được xác định là phân sai cụm nếu 𝑠(𝑖) có giá trị càng gần -1.

Đánh giá chất lượng phân cụm

Độ đo Davies - Bouldin 𝑘 1 𝛿𝑖+ 𝛿𝑗

## 𝐷𝐵= 𝑘෍ 𝑀𝑎𝑥𝑖≠𝑗 𝑑𝑐𝑖, 𝑐𝑗 𝑖=1

Trong đó:

𝑘l à số cụm.

𝑐𝑖l à trọng tâm của cụm 𝑖.

𝛿𝑖l à trung bình khoảng cách của tất cả các phần tử trong cụm 𝑖t ới trọng tâm 𝑐𝑖.

𝑑𝑐𝑖, 𝑐𝑗l à khoảng cách giữa hai trọng tâm của cụm 𝑖và 𝑗.

Giá trị 𝐷𝐵c àng nhỏ thì chất lượng của bài toán phân cụm càng tốt.

Đánh giá chất lượng phân cụm

Độ đo Dunn

## 𝑑(𝑖, 𝑗)

## 𝐷= 𝑚𝑖𝑛1≤𝑖≤𝑘𝑚𝑖𝑛1≤𝑗≤𝑘,𝑖≠𝑗

## 𝑚𝑎𝑥1≤ℎ≤𝑘𝑑′(ℎ)

Trong đó:

𝑑(𝑖, 𝑗) là khoảng cách giữa hai tâm của hai cụm 𝑖và 𝑗.

𝑑′ ℎl à khoảng cách trung bình của các phần tử bên trong cụm ℎ.

𝑘l à số cụm.

Trong độ đo này 𝐷có giá trị càng lớn thì chất lượng của bài toán phân cụm càng tốt.

Hạn chếcủa thuật toán k-Means

Thuật toán rất nhạy cảm với outliers: Khi xuất hiện outliers thì thường khiến cho tâm cụm bị chệch và do đó dự báo cụm không còn chuẩn xác. Chính vì thế chúng ta cần phải loại bỏ outliers trước khi huấn luyện thuật toán.

Thuật toán nhạy cảm với độ lớn đơn vị của biến: Khiáp dụng thuật toán trên các biến có sự khác biệt về mặt đơn vị thì khoảng cách chủ yếu bị ảnh hưởng bởi các biến có đơn vị lớn hơn và khiến cho kết quả phân cụm bị chệch. Chính vì thế chúng ta cần phải chuẩn hoá biến để loại bỏ sự khác biệt đơn vị trước khi đưa vào huấn luyện mô hình.

Thuật toán k-Means yêu cầu phải tính khoảng cách từ một điểm tới toàn bộ các tâm cụm để tìm ra tâm cụm gần nhất. Như vậy chúng ta cần phải load toàn bộ dữ liệu lên RA M, đối với những bộ dữ liệu kích thước lớn thì sẽ vượt quá khả năng lưu trữ của RA M. Khi đó chúng ta cần phải huấn luyện thuật toán theo phương pháp online learning. Kĩ thuật này sẽ được giới thiệu ở bên dưới.

Xử lý dữ liệu định danh trong phân cụm Kmeans

age income student credit_rating buys_computer <=30 high no fair no <=30 high no excellent no 31..40 high no fair yes >40 medium no fair yes >40 low yes fair yes >40 low yes excellent no 31..40 low yes excellent yes <=30 medium no fair no <=30 low yes fair yes >40 medium yes fair yes <=30 medium yes excellent yes 31..40 medium no excellent yes 31..40 high yes fair yes >40 medium no excellent no

Khoảng cách giữa các đối tượng được tính như thến ào?

| age | income | student | credit ra ting
_ | buys computer
_ |
| --- | --- | --- | --- | --- |
| <=30 | high | no | fair | no |
| <=30 | high | no | excellent | no |
| 31..40 | high | no | fair | yes |
| >40 | medium | no | fair | yes |
| >40 | low | yes | fair | yes |
| >40 | low | yes | excellent | no |
| 31..40 | low | yes | excellent | yes |
| <=30 | medium | no | fair | no |
| <=30 | low | yes | fair | yes |
| >40 | medium | yes | fair | yes |
| <=30 | medium | yes | excellent | yes |
| 31..40 | medium | no | excellent | yes |
| 31..40 | high | yes | fair | yes |
| >40 | medium | no | excellent | no |

Xử lý dữ liệu định danh trong phân cụm Kmeans

Cách 1: Biến đổi dữ liệu định danh về dữ liệu nhịph ân - One hot.

• Xét thuộc tính A có giá trịđược biểu diễn bằng m giá trịr ời rạc p1, p2,…,pm

• Biến đổi thuộc tính A thành m thuộc tính nhịph ân A1,A2,…,Am Ai nhận giá trị1 tại dòng tương ứng với giá trịpi, Nhận giá trị0 trong trường hợp ngược lại.

Xử lý dữ liệu định danh trong phân cụm Kmeans

Ví dụx ét thuộc tính age được biểu diễn bằng 3 giá trị: <=30, 31..40, >40. age age30 age31_40 age40

<=30 1 0 0 • Biến đổi age thành 3 thuộc <=30 1 0 0 tính nhịph ân:

31..40 0 1 0 age30, age31_40, age40 >40 0 0 1

>40 0 0 1 → >40 0 0 1

31..40 0 1 0

<=30 1 0 0

<=30 1 0 0

>40 0 0 1

<=30 1 0 0

31..40 0 1 0

31..40 0 1 0

>40 0 0 1

| age30 | age31 40
_ | age40 |
| --- | --- | --- |
| 1 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |
| 0 | 0 | 1 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

Xử lý dữ liệu định danh trong phân cụm Kmeans

buy- age31_4 student - student - Credit- Credit- no buy- age30 0 age40 income_h income_m income_l no yes fair excellent yes

1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 1 0 0 1 0 0 1 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 1 0 0 1 0 0 1 0 1 1 0 0 1 0 0 1 0 0 1 0 1 0 1 1 0 0 1 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 0 1 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 1 0 0 1 0 0 1 0 1 0 1 0 0 1 1 0

| age30 | age31 4
_
0 | age40 | income h | income m | income l | student -
no | student -
yes | Credit-
fair | Credit-
excellent | buy-
no | buy-
yes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | _
1 | _
0 | _
0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |

Xử lý dữ liệu định danh trong phân cụm Kmeans

Cách 2: Biến đổi dữ liệu định danh về dữ liệu số- Label Encoding.

• Xét thuộc tính A có giá trịđược biểu diễn bằng m giá trịr ời rạc.

• Sắp xếp m giá trịr ời rạc theo thứt ựt ăng dần của bảng chữc ái: p1, p2,…,pm

• Biến đổi các giá trịpi như sau:

p1 nhận giá trị0 p2 nhận giá trị1 ….

pm nhận giá trịm-1

Xử lý dữ liệu định danh trong phân cụm Kmeans

age income student credit_rating buys_computer 0 0 0 1 0 0 0 0 0 0 2 0 0 1 1 1 2 0 1 1 1 1 1 1 1 1 1 1 0 0 2 1 1 0 1 0 2 0 1 0 0 1 1 1 1 1 2 1 1 1 0 2 1 0 1 2 2 0 0 1 2 0 1 1 1 1 2 0 0 0

| age | income | student | credit ra ting
_ | buys computer
_ |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 | 1 |
| 1 | 2 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 1 | 1 | 0 | 1 |
| 0 | 2 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 1 | 1 | 1 |
| 0 | 2 | 1 | 0 | 1 |
| 2 | 2 | 0 | 0 | 1 |
| 2 | 0 | 1 | 1 | 1 |
| 1 | 2 | 0 | 0 | 0 |

Xử lý cơ sở dữ liệu giao dịch trong phân cụm Kmeans

Xét cơ sở dữ liệu giao dịch gồm:

• 4 giao dịch: 1,2,3,4

• Mỗi giao dịch có một số phần tử(items)

Xử lý cơ sở dữ liệu giao dịch trong phân cụm Kmeans

Cách giải quyết: Biến đổi cơ sở dữ liệu giao dịch về dữ liệu nhịph ân.

• m phần tửi1,i2,…,im trong cơ sở dữ liệu giao dịch được biến đổi thành m thuộc tính nhịph ân tương ứng A1,A2,…,Am

• Thuộc tính Ainhận giá trị:

1 tại dòng xuất hiện phần tửii trong giao dịch tương ứng.

0 trong trường hợp ngược lại.

Xử lý cơ sở dữ liệu giao dịch trong phân cụm Kmeans

Xử lý dữ liệu văn bản trong phân cụm Kmeans

Xét hai văn bản sau:

• VB1: Life is not only life!

• VB2: To life is to “fight” Bài toán đặt ra:

• Tính khoảng cách giữa hai văn bản này?

Xử lý dữ liệu văn bản trong phân cụm Kmeans

Cách giải quyết:

• Biểu diễn mỗi văn bản dưới dạng một vecto V(v1, v2,…,vn) trên cùng một tập n từkh óa.

• vi là số lần xuất hiện từkh óa thứi trong tập các văn bản.

→Phải xác định được tất cả các từkh óa xuất hiện trong tổng các văn bản.

Xử lý dữ liệu văn bản trong phân cụm Kmeans

Các bước thực hiện:

• B1: Tiền xử lý văn bản

Loại bỏnh ững từ, những ký hiệu không ảnh hưởng tới nội dung văn bản như:

dấu chấm câu, dấu ngoặc, số, chữhoa, chữth ường…

• B2: Tách từ

Tách nội dung mỗi văn bản thành các từđ ơn, riêng biệt (đối với tiếng Anh tách bằng dấu cách, đối với tiếng Việt tách theo từđ ơn từgh ép).

Xử lý dữ liệu văn bản trong phân cụm Kmeans

• B3: Loại bỏt ừd ừng

Từd ừng là những từxu ất hiện nhiều trong văn bản nhưng không có ý nghĩa về mặt xác định nội dung của văn bản.

Nhằm giảm kích thước dữ liệu biểu diễn trong văn bản.

Một số từd ừng trong tiếng Anh: mạo từ(a, the…), giới từ(in, on…), liên từ (but…), động từph ổbi ến (to, be…)….

Xử lý dữ liệu văn bản trong phân cụm Kmeans

• B4: Xác định không gian vect ơ

Số chi ều của không gian: n=3 Vector T = {t1, t2,…, tn} = {life, only, fight}

• B5: Biểu diễn các văn bản theo không gian vect ơ Mô hình Boolean: Văn bản được biểu diễn dưới dạng vector V(v1,v2,…,vn) trong đó: vi = 1 nếu văn bản có xuất hiện từkh óa ti, bằng 0 trong trường hợp ngược lại.

Vector_VB1 = (1, 1, 0)

Vector_VB2 = (1, 0, 1)

Xử lý dữ liệu văn bản trong phân cụm Kmeans

• B5: Biểu diễn các văn bản theo không gian vect ơ

Mô hình tần suất từkh óa (còn gọi là mô hình TF - Term Frequency): Văn bản được biểu diễn dưới dạng vector V(v1,v2,…,vn) trong đó: vi = số lần xuất hiện từkh óa ti trong văn bản.

Vector TF_VB1 = (2, 1, 0)

Vector TF_VB2 = (1, 0, 1)

Phương pháp này coi số lần xuất hiện một từtrong văn bản tỷl ệthu ận với vai trò của nó đối với văn bản.

→Suy luận này không phải lúc nào cũng đúng, vì có nhiều từxu ất hiện nhiều trong văn bản này nhưng lại không xuất hiện hoặc xuất hiện ít trong văn bản khác.

Xử lý dữ liệu văn bản trong phân cụm Kmeans

• B5: Biểu diễn các văn bản theo không gian vect ơ

Mô hình nghịch đảo tần số văn bản (còn gọi là mô hình IDF - Inverse Do cument Frequency): Văn bản được biểu diễn dưới dạng vector V(v1,v2,…,vn) trong đó:

vi được tính theo công thức sau:

Trong đóm là số lượng văn bản và hi là số lượng văn bản mà từkh óa ti xuất hiện.

Phương pháp này xác định độquan trọng của từkh óa ti trong văn bản thứj. Nếu ti xuất hiện trong ít văn bản thì độhi ếm của nó so với toàn bộcơ sở dữ liệu cao. Tức là nếu nó xuất hiện trong văn bản thứj thì nó là điểm quan trọng để phân biệt văn bản thứj này so với các văn bản khác.

## Bài tập về nhà 1 - Phân cụm dữ liệu với k=3

## Bài tập về nhà 2 - Phân cụm dữ liệu với k=2

Minh họa phân cụm Kmeans trong Python

## BAV |HỌC VIỆN

## Ce) NGAN HANG L
