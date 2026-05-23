### BÀI 3
#### BIẾN NGẪU NHIÊN

**NỘI DUNG CHÍNH:**
- Khái niệm biến ngẫu nhiên.
- Biến ngẫu nhiên rời rạc và biến ngẫu nhiên liên tục.
- Luật phân phối xác suất của biến ngẫu nhiên.
- Hàm phân bố xác suất và hàm mật độ.

## KHÁI NIỆM BIẾN NGẪU NHIÊN

Những đại lượng như:

- $X$: lượng khách vào một cửa hàng trong ngày.
- $Y$: số khuyết tật của một sản phẩm vừa làm ra.
- $T$: nhiệt độ ở một thời điểm trong ngày.
- $Z$: con số mũi tên trỏ tới trong trò chơi "Chiếc nón kỳ diệu".

có đặc điểm chung là ta không thể đoán trước chắc chắn giá trị mà chúng sẽ nhận. Những đại lượng như vậy được gọi là biến ngẫu nhiên.

Tập hợp các giá trị mà biến ngẫu nhiên $X$ có thể nhận được kí hiệu là $X(\Omega)$.

### 1. Biến ngẫu nhiên rời rạc

Biến ngẫu nhiên $X$ được gọi là rời rạc nếu:

$$
X(\Omega)=\{x_1,x_2,\ldots\}.
$$

**Ví dụ:** Số khuyết tật của một sản phẩm vừa làm ra là biến ngẫu nhiên rời rạc.

### 2. Biến ngẫu nhiên liên tục

Biến ngẫu nhiên $X$ được gọi là liên tục nếu:

- $X(\Omega)$ gồm một hoặc một số khoảng của trục số, thậm chí có thể là cả trục số.
- Với mọi số thực $a$:

$$
P\{X=a\}=0.
$$

**Ví dụ:** Thời điểm một đoàn tàu đến ga là biến ngẫu nhiên liên tục.

## LUẬT PHÂN PHỐI XÁC SUẤT CỦA BIẾN NGẪU NHIÊN

Đối với biến ngẫu nhiên $X$, ta không biết chắc chắn nó sẽ nhận giá trị nào. Vì vậy, ta cần biết xác suất để $X$ nhận một giá trị bất kỳ hoặc nhận giá trị trong một khoảng bất kỳ. Một hình thức cho phép mô tả điều đó được gọi là luật phân phối xác suất của biến ngẫu nhiên.

Các hình thức thường dùng để cho luật phân phối xác suất:

- Xác định xác suất để biến ngẫu nhiên rời rạc nhận giá trị tại từng điểm.
- Hàm phân bố xác suất.
- Hàm mật độ xác suất.

## XÁC SUẤT TẠI TỪNG ĐIỂM CỦA BIẾN NGẪU NHIÊN RỜI RẠC

Đối với biến ngẫu nhiên rời rạc $X$ có:

$$
X(\Omega)=\{x_1,x_2,\ldots\},
$$

ta xác định luật phân phối của $X$ bằng cách tính:

$$
P\{X=x_j\},\qquad \forall x_j\in X(\Omega).
$$

**Ví dụ:** Một máy sản xuất từng sản phẩm một với xác suất sản xuất ra phế phẩm là 10%. Máy được đưa đi sửa ngay sau khi làm ra phế phẩm. Tìm luật phân phối xác suất của số sản phẩm được làm ra cho đến khi máy được đem đi sửa.

**Giải:** Gọi $X$ là số sản phẩm được làm ra cho đến khi máy đem đi sửa. Khi đó:

$$
X(\Omega)=\mathbb{N}^*.
$$

Máy làm ra $i-1$ sản phẩm tốt rồi đến sản phẩm thứ $i$ là phế phẩm, nên:

$$
P\{X=i\}=0,9^{i-1}\cdot0,1,\qquad i\in\mathbb{N}^*.
$$

Với biến ngẫu nhiên rời rạc $X$ nhận hữu hạn $n$ giá trị, luật phân phối xác suất có thể cho bằng bảng:

| $X$ | $x_1$ | $x_2$ | ... | $x_n$ |
|---|---:|---:|---:|---:|
| $P$ | $p_1$ | $p_2$ | ... | $p_n$ |

Trong đó:

$$
p_j=P\{X=x_j\},\qquad p_1+p_2+\cdots+p_n=1.
$$

**Ví dụ:** Một người bán hàng sẽ đến 2 nơi bán, mỗi nơi một sản phẩm. Khả năng bán được sản phẩm ở nơi thứ nhất là 0,3, ở nơi thứ hai là 0,6. Tìm luật phân phối xác suất của số nơi người đó bán được hàng.

**Giải:** Gọi $X$ là số nơi người đó bán được hàng. Khi đó:

$$
X(\Omega)=\{0,1,2\}.
$$

Gọi $A_i$ là biến cố "người đó bán được hàng ở nơi thứ $i$" với $i=1,2$. Khi đó:

$$
P\{X=0\}=P(\overline{A_1}\,\overline{A_2})=0,7\cdot0,4=0,28.
$$

$$
P\{X=1\}=P(A_1\overline{A_2})+P(\overline{A_1}A_2)=0,3\cdot0,4+0,7\cdot0,6=0,54.
$$

$$
P\{X=2\}=P(A_1A_2)=0,3\cdot0,6=0,18.
$$

Bảng phân phối xác suất:

| $X$ | 0 | 1 | 2 |
|---|---:|---:|---:|
| $P$ | 0,28 | 0,54 | 0,18 |

## HÀM PHÂN BỐ XÁC SUẤT

Hàm phân bố xác suất, hay hàm phân bố, của biến ngẫu nhiên $X$ được định nghĩa:

$$
F(x)=P\{X<x\}.
$$

### 1. Ví dụ hàm phân bố của biến ngẫu nhiên rời rạc

Với biến ngẫu nhiên ở ví dụ trên:

| $X$ | 0 | 1 | 2 |
|---|---:|---:|---:|
| $P$ | 0,28 | 0,54 | 0,18 |

Ta có:

$$
F(x)=
\begin{cases}
0, & x\le 0,\\
0,28, & 0<x\le 1,\\
0,82, & 1<x\le 2,\\
1, & 2<x.
\end{cases}
$$

Ngoài ra:

$$
P\{0,5\le X<4\}=P\{X=1\}+P\{X=2\}=0,54+0,18=0,72.
$$

Và:

$$
P\{0,5\le X<4\}=F(4)-F(0,5).
$$

### 2. Tổng quát cho biến ngẫu nhiên rời rạc

Nếu $X$ là biến ngẫu nhiên rời rạc có tập giá trị sắp thứ tự:

$$
x_1<x_2<x_3<\cdots
$$

và:

$$
P\{X=x_j\}=p_j,
$$

thì:

$$
F(x)=0,\quad x\le x_1.
$$

$$
F(x)=p_1,\quad x_1<x\le x_2.
$$

$$
F(x)=p_1+p_2,\quad x_2<x\le x_3.
$$

Tổng quát:

$$
F(x)=p_1+p_2+\cdots+p_{k-1},\quad x_{k-1}<x\le x_k.
$$

### 3. Tính chất của hàm phân bố

Hàm phân bố $F(x)$ có các tính chất:

1. Tập xác định là $\mathbb{R}$.
2. $0\le F(x)\le 1$.
3. $\lim_{x\to-\infty}F(x)=0$ và $\lim_{x\to+\infty}F(x)=1$.
4. Nếu $x_1<x_2$ thì $F(x_1)\le F(x_2)$.
5. $P\{a\le X<b\}=F(b)-F(a)$.

## HÀM MẬT ĐỘ XÁC SUẤT

Đối với biến ngẫu nhiên liên tục $X$ có hàm phân bố $F(x)$, hàm không âm $p(x)$ được gọi là hàm mật độ xác suất của $X$ nếu:

$$
F(x)=\int_{-\infty}^{x}p(t)\,dt.
$$

### 1. Tính chất của hàm mật độ

Cho biến ngẫu nhiên liên tục $X$ với hàm mật độ $p(x)$. Khi đó:

1. Nếu $p(x)$ liên tục tại $x_0$, thì:

$$
F'(x_0)=p(x_0).
$$

2. Với mọi $a<b$:

$$
P\{a<X<b\}=P\{a\le X\le b\}=P\{a\le X<b\}=P\{a<X\le b\}
=\int_a^b p(x)\,dx.
$$

3. Tổng xác suất trên toàn trục số bằng 1:

$$
\int_{-\infty}^{+\infty}p(x)\,dx=1.
$$

4. Hàm phân bố $F(x)$ liên tục trên $\mathbb{R}$.

### 2. Ý nghĩa thực tế của hàm mật độ

Giá trị $p(a)$ càng lớn thì các giá trị mà $X$ có thể nhận càng tập trung nhiều quanh $a$. Nếu $p(a)=0$ thì $X$ không tập trung tại giá trị $a$.

## TÍCH PHÂN VỚI CẬN VÔ CỰC

### 1. Định nghĩa trên $[a,+\infty)$

Giả sử $f(x)$ là một hàm sao cho tồn tại $\int_a^t f(x)\,dx$ trên mỗi đoạn $[a,t]$. Nếu tồn tại giới hạn hữu hạn:

$$
\lim_{t\to+\infty}\int_a^t f(x)\,dx=I,
$$

thì $I$ được gọi là tích phân suy rộng của $f(x)$ trên $[a,+\infty)$ và kí hiệu:

$$
I=\int_a^{+\infty}f(x)\,dx.
$$

### 2. Các định nghĩa tương tự

Ta định nghĩa:

$$
\int_{-\infty}^{a}f(x)\,dx
=\lim_{t\to-\infty}\int_t^a f(x)\,dx.
$$

Và:

$$
\int_{-\infty}^{+\infty}f(x)\,dx
=\lim_{\substack{t\to+\infty\\t'\to-\infty}}\int_{t'}^{t}f(x)\,dx.
$$

### 3. Chú ý

Khi $\int_{-\infty}^{+\infty}f(x)\,dx$ tồn tại và $a<b<\cdots<c<d$, ta có thể tách tích phân thành tổng các tích phân trên từng khoảng:

$$
\int_{-\infty}^{+\infty}f(x)\,dx
=\int_{-\infty}^{a}f(x)\,dx+\int_a^b f(x)\,dx+\cdots+\int_c^d f(x)\,dx+\int_d^{+\infty}f(x)\,dx.
$$

Ngoài ra:

$$
\int_{-\infty}^{+\infty}0\,dx=0,\qquad \int_{-\infty}^{a}0\,dx=0,\qquad \int_a^{+\infty}0\,dx=0.
