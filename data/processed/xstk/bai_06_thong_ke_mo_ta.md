### BÀI 6
#### THỐNG KÊ MÔ TẢ

**NỘI DUNG CHÍNH:**
- Tổng thể và mẫu.
- Mẫu ngẫu nhiên tổng quát và mẫu ngẫu nhiên cụ thể.
- Các cách trình bày một mẫu.
- Một số đặc trưng mẫu: trung bình mẫu, phương sai mẫu, độ lệch chuẩn mẫu, tỉ lệ mẫu.

## THỐNG KÊ LÀ GÌ?

Thống kê là khoa học về các phương pháp thu thập, tổ chức, trình bày, phân tích và xử lí số liệu. Thống kê biến những con số khô khan trong dữ liệu thu thập thành thông tin có ý nghĩa, từ đó hỗ trợ dự báo và ra quyết định.

Có thể nghiên cứu dân số theo các dấu hiệu như tuổi, trình độ văn hóa, giới tính, nghề nghiệp. Tuổi và trình độ văn hóa được biểu thị bằng số nên là dấu hiệu định lượng. Giới tính và nghề nghiệp là dấu hiệu định tính.

Việc nghiên cứu toàn bộ tổng thể thường gặp khó khăn do tốn chi phí, thời gian và có thể bị lặp hoặc sót. Vì vậy, người ta thường chọn ngẫu nhiên một số phần tử để lấy mẫu, sau đó điều tra và xử lí số liệu để suy ra kết luận về tổng thể. Cách làm này nhanh hơn, ít tốn kém hơn nhưng vẫn có thể đảm bảo độ chính xác cần thiết.

## TỔNG THỂ VÀ MẪU

### 1. Tổng thể

Tập hợp gồm tất cả các phần tử là đối tượng nghiên cứu được gọi là tổng thể.

Số phần tử của tổng thể gọi là kích thước của tổng thể.

### 2. Mẫu

$n$ phần tử được lấy ra từ tổng thể được gọi là một mẫu kích thước $n$.

Một mẫu được gọi là mẫu ngẫu nhiên nếu các phần tử của nó được lấy một cách ngẫu nhiên.

**Ví dụ:** Nhà kinh tế học muốn nghiên cứu ảnh hưởng của hoàn cảnh kinh tế gia đình tới kết quả học tập của học sinh tiểu học ở Hà Nội. Tổng thể là toàn bộ học sinh tiểu học ở Hà Nội. Nếu chọn ngẫu nhiên 250 học sinh tiểu học ở Hà Nội để nghiên cứu thì ta có một mẫu ngẫu nhiên kích thước 250.

### 3. Mối quan hệ giữa xác suất và thống kê

Xác suất nghiên cứu tổng thể và nhờ đó hiểu về mẫu. Thống kê nghiên cứu mẫu và nhờ đó hiểu về tổng thể.

### 4. Mẫu ngẫu nhiên tổng quát và mẫu ngẫu nhiên cụ thể

Tiến hành $n$ quan sát về biến ngẫu nhiên $X$. Gọi $X_i$ là quan sát thứ $i$ về $X$. Khi đó:

$$
(X_1,X_2,\ldots,X_n)
$$

được gọi là mẫu ngẫu nhiên tổng quát kích thước $n$. Mẫu này thực chất là $n$ biến ngẫu nhiên độc lập có cùng phân phối xác suất với $X$.

Kí hiệu $x_i$ là kết quả quan sát được ở lần thứ $i$. Khi đó:

$$
(x_1,x_2,\ldots,x_n)
$$

được gọi là mẫu ngẫu nhiên cụ thể. Đây là một giá trị cụ thể của mẫu ngẫu nhiên tổng quát.

**Ví dụ:** Giá của mặt hàng $A$ sau Tết tại 8 cửa hiệu, đơn vị nghìn đồng:

$$
(95,109,99,98,105,99,109,102)
$$

là một mẫu cụ thể.

## CÁC CÁCH TRÌNH BÀY MỘT MẪU

### 1. Trường hợp mẫu có ít giá trị khác nhau

Nếu trong $n$ giá trị $x_1,x_2,\ldots,x_n$ có nhiều giá trị trùng lặp, ta chọn mỗi giá trị khác nhau làm đại diện và sắp xếp:

$$
x'_1<x'_2<\cdots<x'_k.
$$

Tần số $n_i$ là số phần tử trong mẫu trùng với $x'_i$.

Bảng thu gọn mẫu:

| $X$ | $x'_1$ | $x'_2$ | ... | $x'_k$ |
|---|---:|---:|---:|---:|
| Tần số | $n_1$ | $n_2$ | ... | $n_k$ |

Trong đó:

$$
n_1+n_2+\cdots+n_k=n.
$$

**Ví dụ:** Giá mặt hàng $A$ sau Tết tại 8 cửa hiệu:

$$
(95,109,99,98,105,99,109,102).
$$

Thu gọn:

| Giá hàng A | 95 | 98 | 99 | 102 | 105 | 109 |
|---|---:|---:|---:|---:|---:|---:|
| Số cửa hàng | 1 | 1 | 2 | 1 | 1 | 2 |

### 2. Trường hợp mẫu có nhiều giá trị khác nhau

Khi mẫu có nhiều giá trị khác nhau, ta chọn các tập hợp $\mathcal{D}_i$ với $i=1,\ldots,k$ là đoạn, khoảng hoặc nửa khoảng rời nhau sao cho:

$$
\bigcup_{i=1}^{k}\mathcal{D}_i
$$

chứa mẫu.

Bảng thu gọn mẫu:

| $X$ | $\mathcal{D}_1$ | $\mathcal{D}_2$ | ... | $\mathcal{D}_k$ |
|---|---:|---:|---:|---:|
| Tần số | $n_1$ | $n_2$ | ... | $n_k$ |

Trong đó $n_i$ là số phần tử trong mẫu thuộc $\mathcal{D}_i$.

**Ví dụ:** Đo chiều cao của 36 sinh viên nam:

$$
160,161,161,162,162,162,163,163,163,
$$

$$
164,164,164,164,165,165,165,165,165,
$$

$$
166,166,166,166,167,167,168,168,168,
$$

$$
168,169,169,170,171,171,172,172,174.
$$

Có thể thu gọn:

| Chiều cao | $(159,5;162,5)$ | $(162,5;165,5)$ | $(165,5;168,5)$ | $(168,5;171,5)$ | $(171,5;174,5)$ |
|---|---:|---:|---:|---:|---:|
| Tần số | 6 | 12 | 10 | 5 | 3 |

Cũng có thể ghép vào các đoạn:

| Chiều cao | $[160;162]$ | $[163;165]$ | $[166;168]$ | $[169;171]$ | $[172;174]$ |
|---|---:|---:|---:|---:|---:|
| Tần số | 6 | 12 | 10 | 5 | 3 |

### 3. Số lớp hợp lý

Nếu số lớp quá ít thì các đặc điểm cơ bản của số liệu bị che lấp. Nếu số lớp quá nhiều thì mô hình phức tạp với các tần số cao thấp xen kẽ. Theo đề nghị của Sturges, số lớp hợp lý:

$$
k=1+\log_2 n\approx 1+3,32\log n.
$$

### 4. Đại diện lớp trong mẫu ghép nhóm

Ở mẫu ghép nhóm, trong khoảng thứ $i$ ta chọn một số $x'_i$ làm đại diện, thường lấy $x'_i$ là trung điểm của hai đầu mút khoảng.

**Ví dụ:** Với bảng chiều cao trên, các trung điểm là:

| Chiều cao đại diện | 161 | 164 | 167 | 170 | 173 |
|---|---:|---:|---:|---:|---:|
| Tần số | 6 | 12 | 10 | 5 | 3 |

## CÁC ĐẶC TRƯNG MẪU

Giả sử quan sát $n$ lần biến ngẫu nhiên $X$, ta có mẫu ngẫu nhiên thu gọn:

| $X$ | $x_1$ | $x_2$ | ... | $x_k$ |
|---|---:|---:|---:|---:|
| Tần số | $n_1$ | $n_2$ | ... | $n_k$ |

Gọi:

$$
f_i=\frac{n_i}{n}
$$

là tần suất của giá trị $x_i$.

### 1. Trung bình mẫu

Trung bình mẫu:

$$
\overline{x}=\sum_{i=1}^{k}x_if_i
=\frac{1}{n}\sum_{i=1}^{k}x_in_i.
$$

Đối với mẫu ngẫu nhiên tổng quát $(X_1,X_2,\ldots,X_n)$:

$$
\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i.
$$

### 2. Độ lệch bình phương trung bình

Với mẫu cụ thể:

$$
M_s=\sum_{i=1}^{k}(x_i-\overline{x})^2f_i
=\frac{1}{n}\sum_{i=1}^{k}(x_i-\overline{x})^2n_i.
$$

Có thể chứng minh:

$$
M_s=\frac{1}{n}\sum_{i=1}^{k}x_i^2n_i-(\overline{x})^2.
$$

Nhiều giáo trình kí hiệu độ lệch bình phương trung bình là $\hat{s}^2$ và gọi nó là phương sai mẫu.

Đối với mẫu ngẫu nhiên tổng quát:

$$
MS=\frac{1}{n}\sum_{i=1}^{n}(X_i-\overline{X})^2.
$$

### 3. Phương sai mẫu

Phương sai mẫu của mẫu cụ thể:

$$
s^2=\frac{1}{n-1}\sum_{i=1}^{k}(x_i-\overline{x})^2n_i
=\frac{n}{n-1}M_s.
$$

Nhiều giáo trình gọi $s^2$ là phương sai mẫu điều chỉnh.

Đối với mẫu ngẫu nhiên tổng quát:

$$
S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\overline{X})^2
=\frac{n}{n-1}MS.
$$

### 4. Độ lệch chuẩn mẫu

Độ lệch chuẩn mẫu của mẫu cụ thể:

$$
s=\sqrt{s^2}.
$$

Đối với mẫu ngẫu nhiên tổng quát:

$$
S=\sqrt{S^2}.
$$

### 5. Tỉ lệ mẫu

Xét biến ngẫu nhiên $X$ có tập giá trị $\{0,1\}$. Giả sử quan sát biến ngẫu nhiên này $n$ lần, thấy $m$ lần nó nhận giá trị 1.

Khi $m,n$ là các số cụ thể, ta kí hiệu:

$$
f=\frac{m}{n}.
$$

Khi $m,n$ chưa cụ thể, ta kí hiệu:

$$
F=\frac{m}{n}.
$$

$f$ hoặc $F$ được gọi là tỉ lệ mẫu. Đó lần lượt là tỉ lệ giá trị 1 xuất hiện trong mẫu cụ thể hoặc mẫu tổng quát thu được trong $n$ quan sát.

**Ví dụ:** Khi kiểm tra một sản phẩm, xét biến ngẫu nhiên $X$:

- $X=0$ nếu sản phẩm là phế phẩm.
- $X=1$ nếu sản phẩm là chính phẩm.

Nếu kiểm tra $n$ sản phẩm thì tỉ lệ mẫu là tỉ lệ chính phẩm trong mẫu này.

## GHI CHÚ VỀ TÍNH TOÁN ĐẶC TRƯNG MẪU

Khi dùng máy tính cầm tay để tính đặc trưng mẫu, cần phân biệt giữa $\sqrt{M_s}$ và $s$. Một số máy hiển thị kí hiệu $\sigma$ nhưng giá trị đó là $\sqrt{M_s}$, không phải độ lệch chuẩn mẫu điều chỉnh $s$.
