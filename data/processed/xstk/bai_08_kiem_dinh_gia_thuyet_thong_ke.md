### BÀI 8
#### KIỂM ĐỊNH GIẢ THUYẾT THỐNG KÊ

**NỘI DUNG CHÍNH:**
- Khái niệm giả thuyết thống kê.
- Phương pháp chung để kiểm định giả thuyết.
- Kiểm định giả thuyết về kỳ vọng.
- Kiểm định giả thuyết về phương sai.
- Kiểm định giả thuyết về xác suất.

## KHÁI NIỆM GIẢ THUYẾT THỐNG KÊ

Khi nghiên cứu nhu cầu thị trường về một loại hàng hóa, ta có thể đưa ra các cặp nhận định như:

- $H_0$: Nhu cầu trung bình về loại hàng hóa này là 1000 đơn vị/tháng.
- $H_1$: Nhu cầu trung bình về loại hàng hóa này khác 1000 đơn vị/tháng.

Hoặc:

- $H_0$: 70% người thích dùng loại hàng hóa này.
- $H_1$: Tỉ lệ người thích dùng loại hàng hóa này nhỏ hơn 70%.

Sự đúng sai của các nhận định này không thể biết chắc chắn nếu không khảo sát toàn bộ tổng thể. Muốn chấp nhận hay bác bỏ các nhận định, ta phải dựa vào mẫu. Vì vậy $H_0,H_1$ được gọi là các giả thuyết thống kê.

Một giả thuyết thống kê là một nhận định về tổng thể.

Giả thuyết mà ta nghi ngờ nó sai và muốn bác bỏ được kí hiệu $H_0$, gọi là giả thuyết không. Giả thuyết đối lập với $H_0$ được kí hiệu $H_1$, gọi là đối thuyết.

Việc xuất phát từ mẫu để chấp nhận hoặc bác bỏ các giả thuyết $H_0,H_1$ được gọi là kiểm định giả thuyết.

## PHƯƠNG PHÁP CHUNG ĐỂ KIỂM ĐỊNH GIẢ THUYẾT THỐNG KÊ

Ta cần kiểm định giả thuyết $H_0$. Trước hết giả sử $H_0$ đúng. Dựa vào mẫu ngẫu nhiên tổng quát và một số dương $\alpha$ rất bé cho trước, ta tìm một biến cố $A$ sao cho:

$$
P\{A|H_0\text{ đúng}\}=\alpha.
$$

Theo nguyên lý xác suất nhỏ, $A$ có thể xem như không xảy ra trong một phép thử. Vì vậy, với một mẫu cụ thể:

- Nếu $A$ xảy ra, giả sử $H_0$ đúng là không hợp lý, ta bác bỏ $H_0$ và thừa nhận $H_1$.
- Nếu $A$ không xảy ra, ta chưa có đủ cơ sở bác bỏ $H_0$, nên tạm chấp nhận $H_0$ và bác bỏ $H_1$.

### 1. Tiêu chuẩn kiểm định và miền bác bỏ

Từ giả thiết $H_0$ đúng, ta xây dựng hàm:

$$
T(X_1,X_2,\ldots,X_n).
$$

Sau đó tìm miền $W_\alpha\subset\mathbb{R}$ sao cho:

$$
P\{T(X_1,X_2,\ldots,X_n)\in W_\alpha|H_0\text{ đúng}\}=\alpha.
$$

Ta chọn:

$$
A=\{T(X_1,X_2,\ldots,X_n)\in W_\alpha\}.
$$

Với mẫu cụ thể $(x_1,x_2,\ldots,x_n)$, tính:

$$
T_{qs}=T(x_1,x_2,\ldots,x_n).
$$

Quy tắc kết luận:

- Nếu $T_{qs}\in W_\alpha$, bác bỏ $H_0$ và thừa nhận $H_1$.
- Nếu $T_{qs}\notin W_\alpha$, tạm chấp nhận $H_0$ và bác bỏ $H_1$.

Trong đó:

- $\alpha$ là mức ý nghĩa, thường $\alpha\le0,1$.
- $T(X_1,X_2,\ldots,X_n)$ là tiêu chuẩn kiểm định.
- $W_\alpha$ là miền bác bỏ $H_0$.

### 2. Sai lầm trong kiểm định

Khi lựa chọn giữa $H_0$ và $H_1$, ta có thể mắc hai loại sai lầm:

- Sai lầm loại 1: Bác bỏ $H_0$ khi thực ra $H_0$ đúng.
- Sai lầm loại 2: Chấp nhận $H_0$ khi thực ra $H_0$ sai.

Khả năng mắc sai lầm loại 1 chính là $\alpha$. Người ta thường chọn sai lầm nghiêm trọng hơn làm sai lầm loại 1 và kiểm soát nó bằng cách chọn $\alpha$ nhỏ.

**Ví dụ:** Khi định đầu tư vào một lĩnh vực, có thể đưa ra hai nhận định: "đầu tư bị lỗ" và "đầu tư có lãi". Sai lầm bác bỏ nhận định "đầu tư bị lỗ" có thể rất nghiêm trọng vì có thể dẫn đến phá sản. Vì vậy, nên chọn $H_0$ là "đầu tư bị lỗ".

## KIỂM ĐỊNH GIẢ THUYẾT VỀ KỲ VỌNG

Giả sử chưa biết kỳ vọng $\mu$ của biến ngẫu nhiên $X$. Với mẫu $(x_1,x_2,\ldots,x_n)$ rút ra từ $X$ và $\mu_0$ cho trước, ta kiểm định một trong ba cặp giả thuyết:

1. $H_0:\mu=\mu_0$, $H_1:\mu\ne\mu_0$.
2. $H_0:\mu\le\mu_0$, $H_1:\mu>\mu_0$.
3. $H_0:\mu\ge\mu_0$, $H_1:\mu<\mu_0$.

### 1. Trường hợp $X\sim N(\mu,\sigma^2)$ và đã biết $\sigma$

Tiêu chuẩn kiểm định:

$$
T=\frac{(\overline{X}-\mu_0)\sqrt{n}}{\sigma}.
$$

Miền bác bỏ tương ứng:

1. Với $H_1:\mu\ne\mu_0$:

$$
W_\alpha=(-\infty,-u_{\alpha/2})\cup(u_{\alpha/2},+\infty).
$$

2. Với $H_1:\mu>\mu_0$:

$$
W_\alpha=(u_\alpha,+\infty).
$$

3. Với $H_1:\mu<\mu_0$:

$$
W_\alpha=(-\infty,-u_\alpha).
$$

**Ví dụ:** Nếu một máy hoạt động bình thường thì khối lượng sản phẩm có phân phối xấp xỉ chuẩn với độ lệch chuẩn 2 kg và trung bình 20 kg. Nghi ngờ máy hoạt động không bình thường làm thay đổi trung bình khối lượng, cân thử 100 sản phẩm:

| Khối lượng (kg) | 18 | 19 | 20 | 21 | 22 |
|---|---:|---:|---:|---:|---:|
| Số sản phẩm | 5 | 25 | 40 | 20 | 10 |

Với mức ý nghĩa $\alpha=0,05$, kết luận về nghi ngờ trên.

**Giải:** Gọi $X$ là khối lượng hiện giờ của một sản phẩm. Ta cần kiểm định:

$$
H_0:\mu=20,\qquad H_1:\mu\ne20.
$$

Ta có:

$$
n=100,\quad \overline{x}=20,05,\quad \sigma=2,\quad u_{0,025}\approx1,96.
$$

Giá trị quan sát:

$$
T_{qs}=\frac{(20,05-20)\sqrt{100}}{2}=0,25.
$$

Miền bác bỏ:

$$
W_\alpha=(-\infty,-1,96)\cup(1,96,+\infty).
$$

Vì $T_{qs}\notin W_\alpha$, ta tạm chấp nhận $H_0$, tức là cho rằng máy hoạt động bình thường.

### 2. Trường hợp $X\sim N(\mu,\sigma^2)$ và chưa biết $\sigma$

Tiêu chuẩn kiểm định:

$$
T=\frac{(\overline{X}-\mu_0)\sqrt{n}}{S}.
$$

Miền bác bỏ:

1. Với $H_1:\mu\ne\mu_0$:

$$
W_\alpha=(-\infty,-t_{\alpha/2}^{(n-1)})\cup(t_{\alpha/2}^{(n-1)},+\infty).
$$

2. Với $H_1:\mu>\mu_0$:

$$
W_\alpha=(t_\alpha^{(n-1)},+\infty).
$$

3. Với $H_1:\mu<\mu_0$:

$$
W_\alpha=(-\infty,-t_\alpha^{(n-1)}).
$$

**Ví dụ:** Định mức thời gian hoàn thành một sản phẩm là 14 phút. Theo dõi 25 công nhân:

| Thời gian sản xuất 1 sản phẩm (phút) | $(10;12]$ | $(12;14]$ | $(14;16]$ | $(16;18]$ | $(18;20]$ |
|---|---:|---:|---:|---:|---:|
| Số công nhân | 2 | 6 | 10 | 4 | 3 |

Với mức ý nghĩa $\alpha=0,05$, có cần thay đổi định mức không, biết thời gian hoàn thành có phân phối xấp xỉ chuẩn?

**Giải:** Lấy trung điểm các khoảng:

| $x_i$ | 11 | 13 | 15 | 17 | 19 |
|---|---:|---:|---:|---:|---:|
| $n_i$ | 2 | 6 | 10 | 4 | 3 |

Kiểm định:

$$
H_0:\mu=14,\qquad H_1:\mu\ne14.
$$

Ta có:

$$
n=25,\quad \overline{x}=15,\quad s=2,2361,\quad t_{0,025}^{(24)}=2,0639.
$$

Giá trị quan sát:

$$
T_{qs}=\frac{(15-14)\sqrt{25}}{2,2361}\approx2,2361.
$$

Miền bác bỏ:

$$
W_\alpha=(-\infty,-2,0639)\cup(2,0639,+\infty).
$$

Vì $T_{qs}\in W_\alpha$, bác bỏ $H_0$, tức là cần thay đổi định mức.

### 3. Trường hợp phân phối không nhất thiết chuẩn và $n\ge30$

Nếu biết $\sigma$, dùng:

$$
T=\frac{(\overline{X}-\mu_0)\sqrt{n}}{\sigma}.
$$

Nếu chưa biết $\sigma$, dùng:

$$
T=\frac{(\overline{X}-\mu_0)\sqrt{n}}{S}.
$$

Miền bác bỏ dùng các giá trị tới hạn chuẩn:

1. Hai phía:

$$
W_\alpha=(-\infty,-u_{\alpha/2})\cup(u_{\alpha/2},+\infty).
$$

2. Phía phải:

$$
W_\alpha=(u_\alpha,+\infty).
$$

3. Phía trái:

$$
W_\alpha=(-\infty,-u_\alpha).
$$

**Ví dụ:** Một giám đốc cho biết trung bình lương công nhân là 23,8 triệu đồng/tháng. Chọn ngẫu nhiên 36 công nhân thấy trung bình lương là 23,5 triệu, độ lệch chuẩn 0,4 triệu. Với mức ý nghĩa $\alpha=0,05$, xét xem giám đốc có nói quá lên không.

**Giải:** Kiểm định:

$$
H_0:\mu=23,8,\qquad H_1:\mu<23,8.
$$

Ta có:

$$
n=36,\quad \overline{x}=23,5,\quad s=0,4.
$$

Giá trị quan sát:

$$
T_{qs}=\frac{(23,5-23,8)\sqrt{36}}{0,4}=-4,5.
$$

Miền bác bỏ:

$$
W_\alpha=(-\infty,-u_{0,05})\approx(-\infty,-1,6449).
$$

Vì $T_{qs}\in W_\alpha$, bác bỏ $H_0$, tức là không tin lời giám đốc.

## KIỂM ĐỊNH GIẢ THUYẾT VỀ PHƯƠNG SAI

Giả sử $X\sim N(\mu,\sigma^2)$ nhưng chưa biết $\sigma$. Với mẫu $(x_1,x_2,\ldots,x_n)$ và $\sigma_0$ cho trước, kiểm định một trong ba cặp:

1. $H_0:\sigma^2=\sigma_0^2$, $H_1:\sigma^2\ne\sigma_0^2$.
2. $H_0:\sigma^2\le\sigma_0^2$, $H_1:\sigma^2>\sigma_0^2$.
3. $H_0:\sigma^2\ge\sigma_0^2$, $H_1:\sigma^2<\sigma_0^2$.

Tiêu chuẩn kiểm định:

$$
T=\frac{(n-1)S^2}{\sigma_0^2}.
$$

Miền bác bỏ:

1. Với $H_1:\sigma^2\ne\sigma_0^2$:

$$
W_\alpha=(-\infty,\chi_{1-\alpha/2}^{2}(n-1))\cup(\chi_{\alpha/2}^{2}(n-1),+\infty).
$$

2. Với $H_1:\sigma^2>\sigma_0^2$:

$$
W_\alpha=(\chi_{\alpha}^{2}(n-1),+\infty).
$$

3. Với $H_1:\sigma^2<\sigma_0^2$:

$$
W_\alpha=(-\infty,\chi_{1-\alpha}^{2}(n-1)).
$$

**Ví dụ:** Kiểm tra độ chính xác của một máy đóng gói, cân một số gói và thu được khối lượng:

$$
60,\ 60,2,\ 70,\ 60,8,\ 50,6,\ 50,8,\ 50,9,\ 60,1,
$$

$$
50,3,\ 60,5,\ 60,1,\ 60,2,\ 60,3,\ 50,8,\ 60,\ 70.
$$

Với mức ý nghĩa $\alpha=0,05$, xét máy có hoạt động bình thường không, biết khối lượng một bao có phân phối xấp xỉ chuẩn và phương sai thiết kế $\sigma_0^2=0,04$.

**Giải:** Kiểm định:

$$
H_0:\sigma^2\le0,04,\qquad H_1:\sigma^2>0,04.
$$

Từ mẫu:

$$
n=16,\qquad s^2\approx39,894.
$$

Giá trị quan sát:

$$
T_{qs}=\frac{15\cdot39,894}{0,04}=14960,25.
$$

Miền bác bỏ:

$$
W_\alpha=(\chi_{0,05}^{2}(15),+\infty)\approx(24,9958,+\infty).
$$

Vì $T_{qs}\in W_\alpha$, bác bỏ $H_0$, hay cho rằng máy hoạt động không bình thường.

## KIỂM ĐỊNH GIẢ THUYẾT VỀ XÁC SUẤT

Giả sử chưa biết $p=P(A)$. Thực hiện phép thử $n$ lần, thấy $A$ xuất hiện $m$ lần. Tần suất:

$$
F=\frac{m}{n}.
$$

Với mức ý nghĩa $\alpha$ và $p_0$ cho trước, kiểm định một trong ba cặp:

1. $H_0:p=p_0$, $H_1:p\ne p_0$.
2. $H_0:p\le p_0$, $H_1:p>p_0$.
3. $H_0:p\ge p_0$, $H_1:p<p_0$.

Với điều kiện:

$$
np_0\ge5,\qquad n(1-p_0)\ge5,
$$

dùng tiêu chuẩn kiểm định:

$$
T=\frac{(F-p_0)\sqrt{n}}{\sqrt{p_0(1-p_0)}}.
$$

Miền bác bỏ:

1. Hai phía:

$$
W_\alpha=(-\infty,-u_{\alpha/2})\cup(u_{\alpha/2},+\infty).
$$

2. Phía phải:

$$
W_\alpha=(u_\alpha,+\infty).
$$

3. Phía trái:

$$
W_\alpha=(-\infty,-u_\alpha).
$$

**Ví dụ:** Một báo cáo nói rằng 18% thanh niên sử dụng dịch vụ mạng của VNPT. Để tìm hiểu tỉ lệ này trong sinh viên, chọn ngẫu nhiên 80 sinh viên, thấy có 22 sinh viên sử dụng dịch vụ mạng của VNPT. Với mức ý nghĩa $\alpha=0,02$, kiểm định xem tỉ lệ sinh viên sử dụng dịch vụ mạng của VNPT có cao hơn tỉ lệ chung hay không.

**Giải:** Gọi $p$ là tỉ lệ sinh viên sử dụng dịch vụ mạng của VNPT. Kiểm định:

$$
H_0:p=0,18,\qquad H_1:p>0,18.
$$

Điều kiện:

$$
80\cdot0,18\ge5,\qquad 80\cdot0,82\ge5.
$$

Ta có:

$$
n=80,\qquad f=\frac{22}{80}=0,275,\qquad p_0=0,18.
$$

Giá trị quan sát:

$$
T_{qs}=\frac{(0,275-0,18)\sqrt{80}}{\sqrt{0,18\cdot0,82}}
\approx2,2117.
$$

Miền bác bỏ:

$$
W_\alpha=(u_{0,02},+\infty)\approx(2,0537,+\infty).
$$

Vì $T_{qs}\in W_\alpha$, bác bỏ $H_0$. Có thể cho rằng tỉ lệ sinh viên sử dụng dịch vụ mạng của VNPT cao hơn tỉ lệ chung.
