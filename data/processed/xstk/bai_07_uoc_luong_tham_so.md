### BÀI 7
#### ƯỚC LƯỢNG THAM SỐ

**NỘI DUNG CHÍNH:**
- Đặt vấn đề về ước lượng tham số.
- Ước lượng điểm.
- Ước lượng khoảng.
- Khoảng tin cậy cho kỳ vọng, phương sai và xác suất.
- Xác định độ tin cậy hoặc kích thước mẫu.

## ĐẶT VẤN ĐỀ

Trong nhiều bài toán thống kê, tham số của tổng thể chưa biết và cần được ước lượng từ mẫu.

**Ví dụ:** Cục Du lịch Quốc gia Việt Nam muốn ước lượng trung bình chi tiêu $\mu$ của một khách du lịch tới Phú Quốc. Việc thu thập thông tin của tất cả khách du lịch rất khó và tốn kém. Vì vậy, có thể chọn 500 khách khi họ kết thúc chuyến đi và hỏi chi tiết về chi tiêu.

Khi đó $\mu$ là tham số cần ước lượng. Ta có thể:

- Ước đoán $\mu$ bởi một giá trị $\hat{\mu}$, chẳng hạn trung bình mức chi tiêu của 500 khách. Đây là ước lượng điểm.
- Ước đoán $\mu$ thuộc một khoảng $(a,b)$. Đây là ước lượng khoảng.

Trong thống kê, $\hat{\mu}$ là một ước lượng điểm của $\mu$, còn $(a,b)$ là một ước lượng khoảng của $\mu$.

## ƯỚC LƯỢNG ĐIỂM

Giả sử ta đã biết dạng luật phân phối xác suất của biến ngẫu nhiên $X$ nhưng chưa biết tham số $\theta$. Để ước tính $\theta$, ta đưa ra một hàm:

$$
\hat{\theta}(X_1,X_2,\ldots,X_n),
$$

trong đó $(X_1,X_2,\ldots,X_n)$ là mẫu ngẫu nhiên tổng quát lấy từ $X$. Hàm này được gọi là một ước lượng của $\theta$.

Nếu $(x_1,x_2,\ldots,x_n)$ là mẫu ngẫu nhiên cụ thể, thì:

$$
\hat{\theta}(x_1,x_2,\ldots,x_n)
$$

được gọi là một ước lượng điểm của $\theta$.

### 1. Ước lượng không chệch

Ước lượng $\hat{\theta}(X_1,X_2,\ldots,X_n)$ của $\theta$ được gọi là không chệch nếu:

$$
E[\hat{\theta}(X_1,X_2,\ldots,X_n)]=\theta.
$$

Nếu:

$$
E[\hat{\theta}(X_1,X_2,\ldots,X_n)]\ne\theta,
$$

thì $\hat{\theta}$ được gọi là ước lượng chệch của $\theta$.

### 2. Ước lượng hiệu quả

Ước lượng $\hat{\theta}(X_1,X_2,\ldots,X_n)$ của $\theta$ được gọi là hiệu quả nếu nó là ước lượng không chệch của $\theta$ và có phương sai nhỏ nhất so với mọi ước lượng không chệch khác của $\theta$.

### 3. Ước lượng vững

Ước lượng $\hat{\theta}(X_1,X_2,\ldots,X_n)$ của $\theta$ được gọi là ước lượng vững nếu:

$$
\forall\varepsilon>0,\quad
\lim_{n\to\infty}P\{|\hat{\theta}(X_1,X_2,\ldots,X_n)-\theta|<\varepsilon\}=1.
$$

Ý nghĩa: hầu như chắc chắn $\hat{\theta}$ sai khác $\theta$ không nhiều nếu kích thước mẫu $n$ đủ lớn.

### 4. Các kết quả về ước lượng điểm

- Trung bình mẫu:

$$
\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

là ước lượng không chệch, hiệu quả và vững của $E(X)$.

- Phương sai mẫu:

$$
S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\overline{X})^2
$$

là ước lượng không chệch và vững của $V(X)$.

- Tỉ lệ mẫu:

$$
F=\frac{m}{n}
$$

là ước lượng không chệch, hiệu quả và vững của $P(A)$, nếu $m$ là số lần biến cố $A$ xuất hiện khi phép thử lặp lại $n$ lần.

- Đại lượng:

$$
MS=\frac{1}{n}\sum_{i=1}^{n}(X_i-\overline{X})^2
$$

là ước lượng chệch của $V(X)$.

**Ví dụ:** Khảo sát 500 hộ gia đình ở một tỉnh về lượng tiêu thụ sản phẩm $A$:

| Lượng tiêu thụ A (kg/tháng) | 0 | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Số hộ | 100 | 40 | 70 | 110 | 90 | 60 | 30 |

Giả sử toàn tỉnh có 600 000 hộ tiêu thụ sản phẩm $A$. Có thể dùng trung bình mẫu của bảng khảo sát để ước tính trung bình lượng tiêu thụ sản phẩm $A$ của tỉnh, rồi nhân với 600 000 để ước tính tổng lượng tiêu thụ.

## ƯỚC LƯỢNG KHOẢNG

Phương pháp ước lượng điểm có nhược điểm là khi kích thước mẫu nhỏ, ước lượng điểm có thể sai lệch nhiều so với tham số cần ước lượng và không cho biết khả năng mắc sai lầm. Để khắc phục, ta dùng khoảng tin cậy.

Giả sử ta đã biết dạng luật phân phối xác suất của $X$ nhưng chưa biết tham số $\theta$. Dựa vào mẫu $(X_1,X_2,\ldots,X_n)$, ta tìm hai hàm:

$$
\theta_1^*=\theta_1^*(X_1,X_2,\ldots,X_n),
$$

$$
\theta_2^*=\theta_2^*(X_1,X_2,\ldots,X_n),
$$

sao cho:

$$
P\{\theta_1^*<\theta<\theta_2^*\}=\gamma.
$$

Khi đó:

$$
(\theta_1^*,\theta_2^*)
$$

được gọi là khoảng tin cậy của $\theta$, còn $\gamma$ gọi là độ tin cậy. Số $\gamma$ đo khả năng để $\theta$ rơi vào khoảng này, nên thường chọn $\gamma$ gần 1.

Với mẫu cụ thể $(x_1,x_2,\ldots,x_n)$, ta cũng gọi khoảng:

$$
(\theta_1^*(x_1,\ldots,x_n),\theta_2^*(x_1,\ldots,x_n))
$$

là khoảng tin cậy của $\theta$.

## KHOẢNG TIN CẬY CHO KỲ VỌNG

### 1. Trường hợp $X\sim N(\mu,\sigma^2)$ và đã biết $\sigma$

Gọi $U\sim N(0,1)$. Giá trị $u_\beta$ thỏa:

$$
P\{U>u_\beta\}=\beta
$$

được gọi là giá trị tới hạn chuẩn mức $\beta$. Khi đó:

$$
\Phi(u_\beta)=1-\beta.
$$

Nếu $\alpha_1,\alpha_2\ge0$ và:

$$
\alpha_1+\alpha_2=\alpha=1-\gamma,
$$

thì khoảng tin cậy của $E(X)=\mu$ với độ tin cậy $\gamma$ là:

$$
\left(\overline{X}-u_{\alpha_2}\frac{\sigma}{\sqrt{n}},
\overline{X}+u_{\alpha_1}\frac{\sigma}{\sqrt{n}}\right).
$$

Các khoảng hay dùng:

- Khoảng đối xứng, khi $\alpha_1=\alpha_2=\frac{\alpha}{2}$:

$$
\left(\overline{X}-u_{\alpha/2}\frac{\sigma}{\sqrt{n}},
\overline{X}+u_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right).
$$

- Khoảng bên phải:

$$
\left(\overline{X}-u_{\alpha}\frac{\sigma}{\sqrt{n}},+\infty\right).
$$

- Khoảng bên trái:

$$
\left(-\infty,\overline{X}+u_{\alpha}\frac{\sigma}{\sqrt{n}}\right).
$$

**Ví dụ:** Khối lượng của một loại sản phẩm có phân phối xấp xỉ chuẩn với độ lệch chuẩn 1 g. Cân 25 sản phẩm:

| Khối lượng (g) | 18 | 19 | 20 | 21 |
|---|---:|---:|---:|---:|
| Số sản phẩm | 3 | 5 | 15 | 2 |

Tìm khoảng tin cậy đối xứng của khối lượng trung bình với độ tin cậy 0,95.

**Giải:** Với $\gamma=0,95$:

$$
\frac{\alpha}{2}=\frac{1-\gamma}{2}=0,025,\qquad u_{0,025}\approx1,96.
$$

Ta có $n=25$, $\overline{x}=19,64$, $\sigma=1$. Khoảng tin cậy:

$$
\left(19,64-1,96\frac{1}{\sqrt{25}},
19,64+1,96\frac{1}{\sqrt{25}}\right)
\approx(19,2480;20,0320).
$$

### 2. Trường hợp $X\sim N(\mu,\sigma^2)$ và chưa biết $\sigma$

Khi chưa biết $\sigma$, dùng độ lệch chuẩn mẫu $S$ và phân phối Student. Khoảng tin cậy của $E(X)$:

$$
\left(\overline{X}-t_{\alpha_2}^{(n-1)}\frac{S}{\sqrt{n}},
\overline{X}+t_{\alpha_1}^{(n-1)}\frac{S}{\sqrt{n}}\right).
$$

Trong đó $t_\beta^{(k)}$ thỏa:

$$
P\{T>t_\beta^{(k)}\}=\beta,
$$

với $T$ có phân phối Student $k$ bậc tự do.

Khoảng đối xứng:

$$
\left(\overline{X}-t_{\alpha/2}^{(n-1)}\frac{S}{\sqrt{n}},
\overline{X}+t_{\alpha/2}^{(n-1)}\frac{S}{\sqrt{n}}\right).
$$

**Ví dụ:** Chiều cao của thanh niên một vùng có phân phối xấp xỉ chuẩn. Đo 16 thanh niên:

$$
172,173,173,174,174,175,175,176,
$$

$$
166,167,165,173,171,170,171,170.
$$

Tìm khoảng tin cậy đối xứng của chiều cao trung bình với độ tin cậy 0,95.

**Giải:** Từ mẫu:

$$
n=16,\qquad \overline{x}=171,5625,\qquad s\approx3,2857.
$$

Với $\gamma=0,95$:

$$
t_{0,025}^{(15)}\approx2,1314.
$$

Khoảng tin cậy:

$$
\left(\overline{x}-t_{0,025}^{(15)}\frac{s}{\sqrt{n}},
\overline{x}+t_{0,025}^{(15)}\frac{s}{\sqrt{n}}\right)
\approx(169,8117;173,3133).
$$

### 3. Trường hợp phân phối không nhất thiết chuẩn và mẫu lớn

Khi kích thước mẫu $n\ge30$, khoảng tin cậy xấp xỉ cho $E(X)$ là:

$$
\left(\overline{X}-u_{\alpha_2}\frac{S}{\sqrt{n}},
\overline{X}+u_{\alpha_1}\frac{S}{\sqrt{n}}\right).
$$

Khoảng đối xứng:

$$
\left(\overline{X}-u_{\alpha/2}\frac{S}{\sqrt{n}},
\overline{X}+u_{\alpha/2}\frac{S}{\sqrt{n}}\right).
$$

**Ví dụ:** Đo ngẫu nhiên 35 cây bạch đàn:

| Chiều cao (m) | $(6,5;7,0)$ | $(7,0;7,5)$ | $(7,5;8)$ | $(8;8,5)$ | $(8,5;9)$ | $(9;9,5)$ |
|---|---:|---:|---:|---:|---:|---:|
| Số cây | 2 | 4 | 10 | 11 | 5 | 3 |

Với độ tin cậy 0,95, tìm khoảng cho chiều cao trung bình.

**Giải:** Lấy trung điểm các khoảng:

| $x_i$ | 6,75 | 7,25 | 7,75 | 8,25 | 8,75 | 9,25 |
|---|---:|---:|---:|---:|---:|---:|
| $n_i$ | 2 | 4 | 10 | 11 | 5 | 3 |

Ta có:

$$
n=35,\qquad \overline{x}=8,0643,\qquad s\approx0,6427.
$$

Với $u_{0,025}\approx1,96$, khoảng tin cậy:

$$
\left(\overline{x}-1,96\frac{s}{\sqrt{35}},
\overline{x}+1,96\frac{s}{\sqrt{35}}\right)
\approx(7,8514;8,2772).
$$

## KHOẢNG TIN CẬY CHO PHƯƠNG SAI

Giả sử $X\sim N(\mu,\sigma^2)$ nhưng chưa biết $\sigma$.

### 1. Trường hợp $\mu$ đã biết

Đặt:

$$
S_*^2=\frac{1}{n}\sum_{i=1}^{n}(X_i-\mu)^2.
$$

Khoảng tin cậy của $V(X)$ với độ tin cậy $\gamma$:

$$
\left(\frac{nS_*^2}{\chi_{\alpha_2}^{2}(n)},
\frac{nS_*^2}{\chi_{1-\alpha_1}^{2}(n)}\right).
$$

Ở đây $\chi_\beta^2(k)$ thỏa:

$$
P\{G>\chi_\beta^2(k)\}=\beta,
$$

với $G$ có phân phối khi bình phương $k$ bậc tự do.

**Ví dụ:** Mức hao phí nguyên liệu có phân phối xấp xỉ chuẩn với trung bình 20 g. Cân 25 sản phẩm:

| Hao phí nguyên liệu (g) | 19,5 | 20,0 | 20,5 |
|---|---:|---:|---:|
| Số sản phẩm | 5 | 18 | 2 |

Với độ tin cậy 0,90, ước lượng mức độ phân tán.

**Giải:** Ta có:

$$
n=25,\qquad s_*^2=\frac{1}{n}\sum_{i=1}^{3}(x_i-20)^2n_i=0,07.
$$

Với $\gamma=0,90$:

$$
\frac{\alpha}{2}=0,05,\quad \chi_{0,05}^{2}(25)=37,6525,\quad \chi_{0,95}^{2}(25)=14,6114.
$$

Khoảng tin cậy:

$$
\left(\frac{25\cdot0,07}{37,6525},\frac{25\cdot0,07}{14,6114}\right)
\approx(0,0464;0,1198).
$$

### 2. Trường hợp $\mu$ chưa biết

Khoảng tin cậy của $V(X)$:

$$
\left(\frac{(n-1)S^2}{\chi_{\alpha_2}^{2}(n-1)},
\frac{(n-1)S^2}{\chi_{1-\alpha_1}^{2}(n-1)}\right).
$$

Khoảng hai phía đối xứng khi $\alpha_1=\alpha_2=\frac{\alpha}{2}$:

$$
\left(\frac{(n-1)S^2}{\chi_{\alpha/2}^{2}(n-1)},
\frac{(n-1)S^2}{\chi_{1-\alpha/2}^{2}(n-1)}\right).
$$

**Ví dụ:** Với cùng số liệu hao phí nguyên liệu nhưng chưa biết $\mu$, ta có:

$$
n=25,\qquad s^2\approx0,0692.
$$

Với $\gamma=0,90$:

$$
\chi_{0,05}^{2}(24)=36,4150,\qquad \chi_{0,95}^{2}(24)=13,8484.
$$

Khoảng tin cậy:

$$
\left(\frac{24s^2}{36,4150},\frac{24s^2}{13,8484}\right)
\approx(0,0456;0,1199).
$$

## KHOẢNG TIN CẬY CHO XÁC SUẤT

Giả sử chưa biết $p=P(A)$. Quan sát phép thử lặp $n$ lần, thấy biến cố $A$ xuất hiện $m$ lần. Tần suất:

$$
F=\frac{m}{n}.
$$

Với điều kiện:

$$
nF>10,\qquad n(1-F)>10,
$$

khoảng tin cậy của $p$ với độ tin cậy $\gamma$ là:

$$
\left(F-u_{\alpha_2}\frac{\sqrt{F(1-F)}}{\sqrt{n}},
F+u_{\alpha_1}\frac{\sqrt{F(1-F)}}{\sqrt{n}}\right).
$$

Khoảng đối xứng:

$$
\left(F-u_{\alpha/2}\frac{\sqrt{F(1-F)}}{\sqrt{n}},
F+u_{\alpha/2}\frac{\sqrt{F(1-F)}}{\sqrt{n}}\right).
$$

**Ví dụ:** Đưa vào lưu thông thêm 200 tờ bạc giả đã đánh dấu. Sau một thời gian, kiểm tra 600 tờ bạc giả loại này thấy có 15 tờ được đánh dấu. Với độ tin cậy 95%, ước lượng số tờ bạc giả loại này.

**Giải:** Kí hiệu $N$ là số tờ bạc giả loại này ban đầu. Tỉ lệ bạc giả đã đánh dấu trong số bạc giả đang lưu hành:

$$
p=\frac{200}{N+200}.
$$

Tỉ lệ mẫu:

$$
f=\frac{15}{600}=0,025.
$$

Với $\gamma=0,95$, $u_{0,025}\approx1,96$. Khoảng tin cậy của $p$:

$$
0,025-0,0125<p<0,025+0,0125.
$$

Suy ra:

$$
0,0125<\frac{200}{N+200}<0,0375.
$$

Do đó:

$$
5133<N<15800.
$$

**Ví dụ:** Kiểm tra ngẫu nhiên 400 sản phẩm do một máy sản xuất, thấy có 20 phế phẩm. Tỉ lệ phế phẩm không vượt quá bao nhiêu với độ tin cậy 0,95?

**Giải:** Gọi $p$ là tỉ lệ phế phẩm. Ta có:

$$
n=400,\qquad f=\frac{20}{400}=0,05.
$$

Với $\gamma=0,95$, $\alpha=0,05$, $u_{0,05}\approx1,6449$.

Cận trên:

$$
f+u_\alpha\frac{\sqrt{f(1-f)}}{\sqrt{n}}
=0,05+1,6449\frac{\sqrt{0,05\cdot0,95}}{\sqrt{400}}
\approx0,0679.
$$

Vậy với độ tin cậy 0,95, tỉ lệ phế phẩm không vượt quá $6,79\%$.

## XÁC ĐỊNH ĐỘ TIN CẬY HOẶC KÍCH THƯỚC MẪU

### 1. Đối với ước lượng kỳ vọng

Với $n\ge30$:

$$
P\left\{|\mu-\overline{X}|<u_{\alpha/2}\frac{S}{\sqrt{n}}\right\}\approx\gamma.
$$

Đặt:

$$
\varepsilon=u_{\alpha/2}\frac{S}{\sqrt{n}}.
$$

$\varepsilon$ được gọi là độ chính xác khi ước lượng $E(X)$ bởi $\overline{X}$.

Độ tin cậy:

$$
\gamma=2\Phi(u_{\alpha/2})-1.
$$

Ba đại lượng độ tin cậy $\gamma$, kích thước mẫu $n$ và độ chính xác $\varepsilon$ liên hệ chặt chẽ. Với $\gamma$ cho trước, nếu $n$ càng lớn thì $\varepsilon$ càng nhỏ.

**Ví dụ:** Đo đường kính 100 chi tiết:

| Đường kính (cm) | 9,75 | 9,80 | 9,85 | 9,90 |
|---|---:|---:|---:|---:|
| Số chi tiết | 5 | 37 | 42 | 16 |

1. Với độ chính xác $\varepsilon=0,006$, xác định độ tin cậy của ước lượng cho đường kính trung bình.
2. Muốn độ chính xác không quá 0,003 và độ tin cậy 95%, cần đo thêm ít nhất bao nhiêu chi tiết?

**Giải:** Từ mẫu có $s\approx0,04$.

1. Với $n=100$:

$$
u_{\alpha/2}\approx\frac{\varepsilon\sqrt{n}}{s}
=\frac{0,006\sqrt{100}}{0,04}=1,5.
$$

Vậy:

$$
\gamma=2\Phi(1,5)-1\approx2\cdot0,9332-1=0,8664.
$$

2. Với $\gamma=0,95$, $u_{0,025}\approx1,96$. Cần:

$$
n_{\text{new}}\ge\left(\frac{1,96S_{\text{new}}}{0,003}\right)^2.
$$

Lấy $S_{\text{new}}\approx s\approx0,04$:

$$
n_{\text{new}}\ge\left(\frac{1,96\cdot0,04}{0,003}\right)^2.
$$

Do đó cần kích thước mẫu ít nhất 683, tức phải kiểm tra thêm:

$$
683-100=583
$$

chi tiết.

### 2. Đối với ước lượng xác suất

Với điều kiện $nF>10$ và $n(1-F)>10$:

$$
P\left\{|p-F|<u_{\alpha/2}\frac{\sqrt{F(1-F)}}{\sqrt{n}}\right\}\approx\gamma.
$$

Đặt:

$$
\varepsilon=u_{\alpha/2}\frac{\sqrt{F(1-F)}}{\sqrt{n}}.
$$

$\varepsilon$ là độ chính xác khi ước lượng $p$ bởi $F$.

**Ví dụ:** Giám đốc một ngân hàng lấy mẫu 100 khách, thấy có 30 người được chi trả theo tuần. Để ước tính tỉ lệ khách được chi trả theo tuần với độ chính xác không quá 5% và độ tin cậy 90%, cần kích thước mẫu ít nhất bao nhiêu?

**Giải:** Từ mẫu ban đầu:

$$
f=\frac{30}{100}=0,3.
$$

Với $\gamma=0,90$:

$$
\frac{\alpha}{2}=0,05,\qquad u_{0,05}\approx1,6449.
$$

Cần:

$$
n_{\text{new}}\ge
\left(\frac{1,6449\sqrt{F(1-F)}}{0,05}\right)^2.
$$

Lấy $F\approx f=0,3$:

$$
n_{\text{new}}\ge
\left(\frac{1,6449\sqrt{0,3(1-0,3)}}{0,05}\right)^2.
$$

Do đó kích thước mẫu ít nhất là 226.
