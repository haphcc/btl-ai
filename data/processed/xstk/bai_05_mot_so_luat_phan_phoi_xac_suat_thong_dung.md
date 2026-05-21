### BÀI 5
#### MỘT SỐ LUẬT PHÂN PHỐI XÁC SUẤT THÔNG DỤNG

**NỘI DUNG CHÍNH:**
- Phân phối nhị thức.
- Phân phối siêu bội.
- Phân phối Poisson.
- Phân phối đều.
- Phân phối chuẩn.
- Phân phối Student và phân phối khi bình phương.

## PHÂN PHỐI NHỊ THỨC

### 1. Dãy phép thử Bernoulli

Một dãy $n$ phép thử được gọi là dãy phép thử Bernoulli nếu thỏa hai điều kiện:

- Mỗi phép thử chỉ xét tới biến cố $A$ và biến cố đối $\overline{A}$.
- Xác suất $P(A)$ trong các phép thử đều bằng $p$.

Kí hiệu:

$$
q=1-p.
$$

**Ví dụ:** Trong 100 sản phẩm của một nhà máy có 10 phế phẩm. Kiểm tra lần lượt 5 sản phẩm và sau mỗi lần kiểm tra lại hoàn sản phẩm vào lô hàng. Mỗi lần kiểm tra có hai kết quả: $A=$ "sản phẩm là phế phẩm" và $\overline{A}$. Khi đó $P(A)=0,1$, $P(\overline{A})=0,9$ và các phép thử không ảnh hưởng lẫn nhau.

### 2. Định nghĩa phân phối nhị thức

Xét dãy phép thử Bernoulli gồm $n$ phép thử. Gọi $X$ là số lần xuất hiện biến cố $A$ trong $n$ phép thử. Khi đó:

$$
X(\Omega)=\{0,1,2,\ldots,n\}.
$$

Luật phân phối xác suất của $X$:

$$
P\{X=i\}=C_n^i p^i q^{n-i},\qquad i=0,1,\ldots,n.
$$

Ta nói $X$ có phân phối nhị thức với tham số $n,p$, kí hiệu:

$$
X\sim B(n,p).
$$

### 3. Các tham số đặc trưng

Nếu $X\sim B(n,p)$ thì:

$$
E(X)=np.
$$

$$
V(X)=npq.
$$

Mode thỏa:

$$
(n+1)p-1\le \operatorname{mod}(X)\le (n+1)p.
$$

### 4. Ví dụ

**Ví dụ:** Tỉ lệ người đầu tư vào bất động sản là 60%. Hỏi ý kiến 20 nhà đầu tư được chọn ngẫu nhiên. Gọi $X$ là số người đầu tư vào bất động sản trong 20 người đó.

1. Tính số người đầu tư bất động sản có khả năng nhất và trung bình số người đầu tư bất động sản.
2. Tính $P\{X\le10\}$, $P\{X>12\}$, $P\{X=11\}$.

**Giải:** Ta có:

$$
X\sim B(20,0,6).
$$

Mode thỏa:

$$
(20+1)\cdot0,6-1\le \operatorname{mod}(X)\le (20+1)\cdot0,6.
$$

Suy ra:

$$
\operatorname{mod}(X)=12.
$$

Trung bình:

$$
E(X)=20\cdot0,6=12.
$$

Các xác suất:

$$
P\{X\le10\}=\sum_{i=0}^{10}C_{20}^{i}0,6^i0,4^{20-i}\approx0,2447.
$$

$$
P\{X>12\}=1-P\{X\le12\}
=1-\sum_{i=0}^{12}C_{20}^{i}0,6^i0,4^{20-i}
\approx0,4159.
$$

$$
P\{X=11\}=C_{20}^{11}0,6^{11}0,4^9\approx0,1597.
$$

## PHÂN PHỐI SIÊU BỘI

### 1. Bài toán dẫn nhập

Trong 100 sản phẩm của một nhà máy có 10 phế phẩm. Kiểm tra lần lượt 5 sản phẩm, sau mỗi lần kiểm tra không hoàn lại. Gọi $X$ là số phế phẩm trong 5 sản phẩm được kiểm tra.

Do kết quả của mỗi lần kiểm tra ảnh hưởng đến các lần kiểm tra còn lại nên dãy phép thử này không phải dãy Bernoulli. Vì vậy phân phối của $X$ không phải phân phối nhị thức.

Ta có:

$$
X(\Omega)=\{0,1,2,3,4,5\}.
$$

Với $i\in X(\Omega)$:

$$
P\{X=i\}=\frac{C_{10}^{i}C_{90}^{5-i}}{C_{100}^{5}}.
$$

### 2. Định nghĩa phân phối siêu bội

Xét một tập gồm $N$ đối tượng, trong đó có $M$ đối tượng có tính chất $T$ và $N-M$ đối tượng không có tính chất $T$.

Chọn ngẫu nhiên $n$ đối tượng theo kiểu không hoàn lại. Gọi $X$ là số đối tượng được chọn có tính chất $T$. Khi đó:

$$
P\{X=i\}=\frac{C_M^iC_{N-M}^{n-i}}{C_N^n},
$$

với:

$$
\max\{0,n+M-N\}\le i\le \min\{M,n\}.
$$

Ta nói $X$ có phân phối siêu bội với tham số $(N,M,n)$, kí hiệu:

$$
X\sim H(N,M,n).
$$

Nếu chọn ngẫu nhiên $n$ đối tượng đồng thời thì luật phân phối của $X$ vẫn là $H(N,M,n)$.

### 3. Các tham số đặc trưng

Nếu $X\sim H(N,M,n)$ thì:

$$
E(X)=n\frac{M}{N}.
$$

$$
V(X)=n\frac{M}{N}\frac{N-M}{N}\frac{N-n}{N-1}.
$$

### 4. Ví dụ

**Ví dụ:** Trong 500 vé xổ số bán ra có 50 vé trúng thưởng. Một người mua 20 vé. Tính:

1. Xác suất người đó có đúng 3 vé trúng thưởng.
2. Trung bình số vé trúng thưởng.

**Giải:** Gọi $X$ là số vé trúng thưởng. Khi đó:

$$
X\sim H(500,50,20).
$$

Xác suất có đúng 3 vé trúng:

$$
P\{X=3\}=\frac{C_{50}^{3}C_{450}^{17}}{C_{500}^{20}}\approx0,194.
$$

Trung bình:

$$
E(X)=20\cdot\frac{50}{500}=2.
$$

### 5. Xấp xỉ nhị thức

Khi $n$ rất bé so với $N$, chẳng hạn $n<0,05N$, ta có:

$$
\frac{C_M^iC_{N-M}^{n-i}}{C_N^n}
\approx C_n^i\left(\frac{M}{N}\right)^i
\left(1-\frac{M}{N}\right)^{n-i}.
$$

Khi đó việc lấy không hoàn lại có thể tính xấp xỉ như lấy có hoàn lại.

**Ví dụ:** Trong một thành phố có 10 000 người, trong đó có 6500 người thích xem bóng đá. Chọn ngẫu nhiên 12 người. Tính xác suất có 5 người thích xem bóng đá.

**Giải:** Gọi $X$ là số người thích xem bóng đá trong 12 người được chọn. Khi đó:

$$
P\{X=5\}=\frac{C_{6500}^{5}C_{3500}^{7}}{C_{10000}^{12}}
\approx C_{12}^{5}\left(\frac{6500}{10000}\right)^5
\left(1-\frac{6500}{10000}\right)^7
\approx0,0591.
$$

## PHÂN PHỐI POISSON

### 1. Định nghĩa

Biến ngẫu nhiên $X$ được gọi là có phân phối Poisson với tham số $\lambda$, kí hiệu:

$$
X\sim \operatorname{Poisson}(\lambda),
$$

nếu:

$$
X(\Omega)=\mathbb{N}
$$

và:

$$
P\{X=k\}=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,2,\ldots,
$$

trong đó $\lambda>0$.

Phân phối Poisson thường dùng để mô hình số lần xảy ra của một sự kiện trong một khoảng thời gian hoặc không gian nhất định, chẳng hạn số khách vào cửa hàng trong một ngày, số xe qua trạm quan sát trong một giờ, số cây trên một đơn vị diện tích rừng.

### 2. Các tham số đặc trưng

Nếu $X\sim \operatorname{Poisson}(\lambda)$ thì:

$$
E(X)=V(X)=\lambda.
$$

Mode thỏa:

$$
\lambda-1\le \operatorname{mod}(X)\le \lambda.
$$

### 3. Ví dụ

**Ví dụ:** Nếu khách vào một cửa hàng ngẫu nhiên, độc lập với nhau và trung bình một giờ có 4,5 khách, thì số khách vào cửa hàng trong 1 giờ có thể xem xấp xỉ phân phối Poisson:

$$
P\{X=k\}=e^{-4,5}\frac{4,5^k}{k!}.
$$

**Ví dụ:** Trung bình một ngày Ngân hàng Nhà nước hủy 10 triệu đồng tiền cũ và phát hành 11 triệu đồng tiền mới. Việc phát hành và hủy tiền độc lập. Tính xác suất trong một ngày số tiền bị hủy và số tiền phát hành đều là 10 triệu đồng.

**Giải:** Gọi $X$ là số tiền bị hủy, $Y$ là số tiền phát hành trong ngày. Khi đó:

$$
X\sim \operatorname{Poisson}(10),\qquad Y\sim \operatorname{Poisson}(11).
$$

Do độc lập:

$$
P\{X=10,Y=10\}=P\{X=10\}P\{Y=10\}.
$$

$$
=e^{-10}\frac{10^{10}}{10!}\cdot e^{-11}\frac{11^{10}}{10!}
\approx0,1251\cdot0,1194\approx0,0149.
$$

**Ví dụ:** Một gara cho thuê ô tô thấy số người đến thuê ô tô vào ngày thứ Bảy là $X\sim\operatorname{Poisson}(2)$. Gara có 4 ô tô. Tính xác suất:

1. Không phải tất cả 4 chiếc đều được thuê.
2. Tất cả 4 ô tô đều được thuê.
3. Gara không đáp ứng được yêu cầu.
4. Gara cần ít nhất bao nhiêu ô tô để xác suất không đáp ứng nhu cầu bé hơn 2%.

**Giải:**

1. Không phải tất cả đều được thuê nghĩa là $X\le3$:

$$
P\{X\le3\}=\sum_{k=0}^{3}e^{-2}\frac{2^k}{k!}\approx0,8571.
$$

2. Tất cả 4 ô tô đều được thuê:

$$
P\{X\ge4\}=1-P\{X\le3\}\approx0,1429.
$$

3. Gara không đáp ứng được yêu cầu khi $X>4$:

$$
P\{X>4\}=1-P\{X\le4\}\approx1-0,9473=0,0527.
$$

4. Cần tìm $n$ nhỏ nhất sao cho $P\{X>n\}<0,02$, tức $P\{X\le n\}>0,98$. Vì $P\{X\le4\}=0,9473$ và $P\{X\le5\}=0,9834$, nên $n=5$.

## PHÂN PHỐI ĐỀU

### 1. Bài toán dẫn nhập

Khi mới kinh doanh, một người chỉ dự kiến doanh số hàng tháng tối thiểu là 20 triệu và tối đa là 40 triệu. Nếu không có thêm thông tin, ta quan niệm doanh số nhận các giá trị trong $[20,40]$ với khả năng đều nhau.

Gọi $X$ là doanh số hàng tháng. Khi đó hàm mật độ:

$$
p(x)=
\begin{cases}
k, & x\in[20,40],\\
0, & x\notin[20,40].
\end{cases}
$$

Vì tổng xác suất bằng 1:

$$
1=\int_{20}^{40}k\,dx=20k,
$$

nên:

$$
k=\frac{1}{20}.
$$

Xác suất đạt doanh số từ 35 triệu trở lên:

$$
P\{X>35\}=\int_{35}^{40}\frac{1}{20}\,dx=0,25.
$$

### 2. Định nghĩa

Biến ngẫu nhiên $X$ được gọi là có phân phối đều trên đoạn $[a,b]$, kí hiệu:

$$
X\sim U[a,b],
$$

nếu hàm mật độ:

$$
p(x)=
\begin{cases}
\frac{1}{b-a}, & x\in[a,b],\\
0, & x\notin[a,b].
\end{cases}
$$

### 3. Các tham số đặc trưng

Nếu $X\sim U[a,b]$ thì:

$$
E(X)=\frac{a+b}{2}.
$$

$$
V(X)=\frac{(b-a)^2}{12}.
$$

Mode là giá trị bất kỳ trong $[a,b]$, và trung vị:

$$
md=\frac{a+b}{2}.
$$

## PHÂN PHỐI CHUẨN

### 1. Định nghĩa

Nhiều đại lượng trong thực tế có phân phối gần dạng chuông như chỉ số chứng khoán, tỷ suất sinh lợi, chỉ số IQ, chiều cao. Mô hình chung thường dùng là phân phối chuẩn.

Biến ngẫu nhiên $X$ được gọi là có phân phối chuẩn với tham số $\mu$ và $\sigma^2$ với $\sigma>0$, kí hiệu:

$$
X\sim N(\mu,\sigma^2),
$$

nếu hàm mật độ:

$$
p(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}.
$$

### 2. Các tham số đặc trưng

Nếu $X\sim N(\mu,\sigma^2)$ thì:

$$
E(X)=\mu,\qquad V(X)=\sigma^2,\qquad \operatorname{mod}(X)=\mu.
$$

### 3. Phân phối chuẩn tắc

Khi $Z\sim N(0,1)$, ta nói $Z$ có phân phối chuẩn tắc. Hàm phân phối của $Z$ kí hiệu là $\Phi(z)$:

$$
\Phi(z)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{z}e^{-\frac{x^2}{2}}\,dx.
$$

Hàm mật độ chuẩn tắc:

$$
\varphi(z)=\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}.
$$

Ta có:

$$
\Phi(z)=0,5+\frac{1}{\sqrt{2\pi}}\int_0^z e^{-\frac{x^2}{2}}\,dx
=0,5+\Phi_0(z),
$$

trong đó $\Phi_0(z)$ là hàm Laplace.

Với $z<0$:

$$
\Phi_0(z)=-\Phi_0(-z).
$$

Với $z>3,39$, có thể xem $\Phi_0(z)\approx0,5$.

### 4. Chuẩn hóa biến ngẫu nhiên chuẩn

Nếu $X\sim N(\mu,\sigma^2)$ thì:

$$
F(x)=P\{X<x\}=\Phi\left(\frac{x-\mu}{\sigma}\right)
=0,5+\Phi_0\left(\frac{x-\mu}{\sigma}\right).
$$

Với $a<b$:

$$
P\{a<X<b\}
=\Phi\left(\frac{b-\mu}{\sigma}\right)
-\Phi\left(\frac{a-\mu}{\sigma}\right).
$$

Định lý này cho phép đưa các tính toán liên quan đến $X\sim N(\mu,\sigma^2)$ về phân phối chuẩn tắc.

### 5. Ví dụ

**Ví dụ:** Giá cổ phiếu của ngân hàng Florida vào cuối giao dịch mỗi ngày trong năm qua tuân theo phân phối chuẩn. Có 240 ngày giao dịch, giá trung bình là 42 USD và độ lệch chuẩn là 2,25 USD.

1. Tính xác suất giá cuối ngày trên 45 USD và ước tính số ngày có giá trên 45 USD.
2. Tính tỉ lệ ngày có giá từ 38 USD đến 40 USD.
3. Tìm mức giá ứng với 15% ngày có giá thấp nhất.

**Giải:** Gọi $X$ là giá cổ phiếu cuối ngày. Khi đó:

$$
X\sim N(42,2,25^2).
$$

1. Xác suất giá trên 45 USD:

$$
P\{X>45\}=1-\Phi\left(\frac{45-42}{2,25}\right)
\approx1-\Phi(1,3333)\approx0,0912.
$$

Số ngày ước tính:

$$
240\cdot0,0912\approx22.
$$

2. Xác suất giá từ 38 đến 40 USD:

$$
P\{38\le X\le40\}
=\Phi\left(\frac{40-42}{2,25}\right)-\Phi\left(\frac{38-42}{2,25}\right)
\approx0,1494.
$$

Vậy khoảng $14,94\%$ số ngày có giá trong khoảng này.

3. Gọi $T$ thỏa $P\{X\le T\}=15\%$. Khi đó:

$$
\Phi\left(\frac{T-42}{2,25}\right)\approx0,15.
$$

Suy ra:

$$
\frac{T-42}{2,25}\approx -1,0364,\qquad T\approx39,6681.
$$

### 6. Quy tắc hai sigma và ba sigma

Nếu $X\sim N(\mu,\sigma^2)$ thì:

$$
P\{\mu-2\sigma<X<\mu+2\sigma\}\approx0,9544.
$$

$$
P\{\mu-3\sigma<X<\mu+3\sigma\}\approx0,9972.
$$

Ứng dụng:

- Một biến ngẫu nhiên chưa biết luật phân phối nhưng thỏa một trong hai quy tắc trên có thể xem xấp xỉ phân phối chuẩn.
- Nếu $X\sim N(\mu,\sigma^2)$ thì theo nguyên lý xác suất lớn, hầu như chắc chắn $X$ nhận giá trị trong $(\mu-2\sigma,\mu+2\sigma)$ hoặc $(\mu-3\sigma,\mu+3\sigma)$.

**Ví dụ:** Kích thước chi tiết có phân phối xấp xỉ chuẩn với $\mu=50$ cm. Kích thước thực tế không nhỏ hơn 32 cm và không lớn hơn 68 cm. Tìm xác suất lấy ngẫu nhiên được một chi tiết có kích thước lớn hơn 55 cm.

**Giải:** Xem $(32,68)$ là khoảng ba sigma:

$$
\mu-3\sigma\approx32,\qquad \mu+3\sigma\approx68.
$$

Suy ra:

$$
\sigma\approx6.
$$

Vậy:

$$
P\{X>55\}=1-\Phi\left(\frac{55-50}{6}\right)
\approx1-\Phi(0,8333)\approx0,2023.
$$

## PHÂN PHỐI STUDENT

Biến ngẫu nhiên $T$ được gọi là có phân phối Student với $n$ bậc tự do nếu hàm mật độ có dạng:

$$
p(x)=C\left(1+\frac{x^2}{n}\right)^{-\frac{n+1}{2}},
$$

trong đó $C$ là hằng số chuẩn hóa.

Phân phối Student được dùng nhiều trong ước lượng và kiểm định khi phương sai tổng thể chưa biết.

## PHÂN PHỐI KHI BÌNH PHƯƠNG

Biến ngẫu nhiên $X$ được gọi là có phân phối $\chi^2$ với $n$ bậc tự do nếu hàm mật độ:

$$
p(x)=
\begin{cases}
0, & x\le0,\\
Cx^{\frac{n}{2}-1}e^{-\frac{x}{2}}, & x>0.
\end{cases}
$$

Phân phối $\chi^2$ được dùng nhiều trong ước lượng và kiểm định phương sai.
