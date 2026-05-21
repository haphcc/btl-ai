### BÀI 4
#### THAM SỐ ĐẶC TRƯNG CỦA BIẾN NGẪU NHIÊN

**NỘI DUNG CHÍNH:**
- Mode, kỳ vọng, phương sai và độ lệch chuẩn của biến ngẫu nhiên.
- Ý nghĩa thực tế của các tham số đặc trưng.
- Biến ngẫu nhiên rời rạc hai chiều.
- Phân phối biên, phân phối có điều kiện, hiệp phương sai và hệ số tương quan.

## CÁC THAM SỐ ĐẶC TRƯNG CỦA BIẾN NGẪU NHIÊN

Trong thực tế, nhiều khi ta cần các thông tin cô đọng phản ánh đặc điểm quan trọng nhất của một biến ngẫu nhiên. Chẳng hạn, khi xét điểm thi đại học toàn quốc, ta cần biết điểm tập trung quanh giá trị nào và mức độ phân tán của điểm so với giá trị đó. Những thông tin như vậy được gọi là các tham số đặc trưng của biến ngẫu nhiên.

### 1. Mode

Mode của biến ngẫu nhiên $X$, kí hiệu $\operatorname{mod}(X)$, là giá trị $x^*$ được xác định như sau:

- Nếu $X$ rời rạc, thì biến cố $\{X=x^*\}$ có xác suất lớn nhất:

$$
P\{X=x^*\}=\max_j P\{X=x_j\}.
$$

- Nếu $X$ liên tục, thì $x^*$ là giá trị tại đó hàm mật độ đạt cực đại.

Mode là một trong các giá trị mà $X$ dễ nhận nhất.

**Ví dụ:** Cho bảng phân phối:

| $X$ | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| $P$ | $5/30$ | $15/30$ | $9/30$ | $1/30$ |

Ta có:

$$
\operatorname{mod}(X)=1.
$$

**Ví dụ:** Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ:

$$
p(x)=
\begin{cases}
\frac{4x^3}{81}, & 0\le x\le 3,\\
0, & x\notin[0,3].
\end{cases}
$$

Vì $p(x)$ tăng trên $[0,3]$, nên:

$$
\operatorname{mod}(X)=3.
$$

## KỲ VỌNG

### 1. Định nghĩa

Kỳ vọng của biến ngẫu nhiên $X$, kí hiệu $E(X)$, được xác định như sau:

- Nếu $X$ là biến ngẫu nhiên rời rạc với $P\{X=x_j\}=p_j$, thì:

$$
E(X)=\sum_j x_jp_j.
$$

- Nếu $X$ là biến ngẫu nhiên liên tục với hàm mật độ $p(x)$, thì:

$$
E(X)=\int_{-\infty}^{+\infty}xp(x)\,dx.
$$

Kỳ vọng không phải bao giờ cũng tồn tại.

### 2. Ví dụ tính kỳ vọng

**Ví dụ:** Một cơ quan có 60 người, trong đó có 1 người lương 10 triệu, 2 người lương 9 triệu, 3 người lương 7 triệu, 14 người lương 6 triệu, 20 người lương 5 triệu và 20 người lương 4 triệu. Tính giá trị trung bình của lương.

**Giải:** Gọi $X$ là lương của một người trong cơ quan, tính bằng triệu đồng. Bảng phân phối xác suất:

| $X$ | 4 | 5 | 6 | 7 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| $P$ | $20/60$ | $20/60$ | $14/60$ | $3/60$ | $2/60$ | $1/60$ |

Kỳ vọng:

$$
E(X)=4\cdot\frac{20}{60}+5\cdot\frac{20}{60}+6\cdot\frac{14}{60}
+7\cdot\frac{3}{60}+9\cdot\frac{2}{60}+10\cdot\frac{1}{60}
=\frac{313}{60}.
$$

### 3. Ý nghĩa kinh tế của kỳ vọng

Trong kinh tế, trung bình của lợi nhuận trong tương lai được gọi là lợi nhuận kỳ vọng hoặc lãi kỳ vọng. Đây là một tiêu chuẩn dùng để lựa chọn chiến lược kinh doanh.

**Ví dụ:** Viện thiết kế $C$ lập dự án cho hai công ty $A$ và $B$. Dự án được $A$ và $B$ xét duyệt độc lập với xác suất chấp nhận tương ứng là 0,7 và 0,8. Nếu $A$ chấp nhận thì trả 4 triệu, nếu không thì trả 1 triệu. Nếu $B$ chấp nhận thì trả 10 triệu, nếu không thì trả 3 triệu. Chi phí lập dự án là 10 triệu và thuế bằng 10% doanh thu. C có nên nhận thiết kế không?

**Giải:** Gọi $X$ là số lãi của $C$ sau khi trừ chi phí. Bảng phân phối xác suất:

| $X$ (triệu đồng) | -6,4 | -3,7 | -0,1 | 2,6 |
|---|---:|---:|---:|---:|
| $P$ | 0,06 | 0,14 | 0,24 | 0,56 |

Ta có:

$$
E(X)=0,53>0.
$$

Vì lãi kỳ vọng dương nên $C$ có thể nhận thiết kế.

### 4. Tính chất của kỳ vọng

- Nếu $X=\text{const}$ thì $E(X)=X$.
- Với các hằng số $\alpha,\beta$:

$$
E(\alpha X+\beta Y)=\alpha E(X)+\beta E(Y),
$$

nếu vế phải tồn tại.

- Nếu $X$ rời rạc với $P\{X=x_j\}=p_j$, thì:

$$
E[f(X)]=\sum_j f(x_j)p_j.
$$

- Nếu $X$ liên tục với hàm mật độ $p(x)$, thì:

$$
E[f(X)]=\int_{-\infty}^{+\infty}f(x)p(x)\,dx.
$$

## PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN

### 1. Định nghĩa phương sai

Phương sai của biến ngẫu nhiên $X$, kí hiệu $V(X)$, được định nghĩa:

$$
V(X)=E\left(X-E(X)\right)^2.
$$

Nếu $X$ rời rạc với $P\{X=x_j\}=p_j$, thì:

$$
V(X)=\sum_j (x_j-E(X))^2p_j.
$$

Nếu $X$ liên tục với hàm mật độ $p(x)$, thì:

$$
V(X)=\int_{-\infty}^{+\infty}(x-E(X))^2p(x)\,dx.
$$

Phương sai biểu thị mức độ phân tán của biến ngẫu nhiên quanh kỳ vọng.

### 2. Công thức tính thuận lợi

Phương sai còn có thể tính bằng:

$$
V(X)=E(X^2)-[E(X)]^2.
$$

Phương sai không phải bao giờ cũng tồn tại.

### 3. Ý nghĩa thực tế của phương sai

- Trong sản xuất, phương sai biểu thị độ đồng đều của sản phẩm và độ ổn định của năng suất.
- Trong kinh tế, phương sai biểu thị mức độ rủi ro của quyết định.

**Ví dụ:** Hai dự án $A$ và $B$ có khả năng thu hồi vốn sau 2 năm, tính bằng phần trăm, lần lượt là hai biến ngẫu nhiên $X,Y$:

| $X$ | 65 | 67 | 68 | 69 | 70 | 71 | 73 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $P$ | 0,04 | 0,12 | 0,16 | 0,28 | 0,24 | 0,08 | 0,08 |

| $Y$ | 66 | 68 | 69 | 70 | 71 |
|---|---:|---:|---:|---:|---:|
| $P$ | 0,12 | 0,28 | 0,32 | 0,20 | 0,08 |

Kết quả:

$$
E(X)=69,16\%,\quad V(X)=3,0944.
$$

$$
E(Y)=68,72\%,\quad V(Y)=1,8016.
$$

Nếu chọn theo tỷ lệ thu hồi vốn kỳ vọng cao hơn thì chọn $A$. Nếu chọn theo rủi ro thấp hơn thì chọn $B$.

### 4. Tính chất của phương sai

- Nếu $X=\text{const}$ thì $V(X)=0$.
- Nếu $C$ là hằng số thì:

$$
V(CX)=C^2V(X).
$$

### 5. Độ lệch chuẩn

Đơn vị đo của phương sai bằng bình phương đơn vị đo của biến ngẫu nhiên. Vì vậy, để đo độ phân tán theo cùng đơn vị với biến ngẫu nhiên, ta dùng độ lệch chuẩn:

$$
\sigma(X)=\sqrt{V(X)}.
$$

## BIẾN NGẪU NHIÊN RỜI RẠC HAI CHIỀU

### 1. Khái niệm

Một cặp gồm hai biến ngẫu nhiên được xét đồng thời $(X,Y)$ được gọi là một biến ngẫu nhiên hai chiều. Khi $X$ và $Y$ đều là biến ngẫu nhiên rời rạc, ta gọi $(X,Y)$ là biến ngẫu nhiên rời rạc hai chiều.

**Ví dụ:** Một máy sản xuất giấy in. Kích thước của mỗi tờ giấy được đo bằng chiều dài $X$ và chiều rộng $Y$. Khi đó ta xét cặp biến ngẫu nhiên $(X,Y)$.

### 2. Phân phối xác suất đồng thời

Khi thiết lập phân phối xác suất của biến ngẫu nhiên rời rạc hai chiều $(X,Y)$, ta liệt kê tất cả các cặp giá trị $(x_i,y_j)$ mà $(X,Y)$ có thể nhận cùng với xác suất:

$$
p_{ij}=P\{(X,Y)=(x_i,y_j)\}.
$$

Tổng tất cả các $p_{ij}$ bằng 1.

Bảng phân phối có dạng:

| $X \backslash Y$ | $y_1$ | $y_2$ | ... | $y_m$ |
|---|---:|---:|---:|---:|
| $x_1$ | $p_{11}$ | $p_{12}$ | ... | $p_{1m}$ |
| $x_2$ | $p_{21}$ | $p_{22}$ | ... | $p_{2m}$ |
| ... | ... | ... | ... | ... |
| $x_n$ | $p_{n1}$ | $p_{n2}$ | ... | $p_{nm}$ |

**Ví dụ:** Theo dõi chi phí quảng cáo $X$ và doanh số bán hàng $Y$ của một công ty, đơn vị đều là triệu đồng/tháng:

| $X \backslash Y$ | 100 | 200 | 300 |
|---|---:|---:|---:|
| 1 | 0,15 | 0,10 | 0,04 |
| 1,5 | 0,05 | 0,20 | 0,15 |
| 2 | 0,01 | 0,05 | 0,25 |

### 3. Phân phối biên

Từ bảng phân phối đồng thời của $(X,Y)$, ta có phân phối biên.

Phân phối của $X$:

$$
p(x_i)=\sum_j p_{ij}.
$$

Phân phối của $Y$:

$$
p(y_j)=\sum_i p_{ij}.
$$

Trong ví dụ trên, phân phối biên của $Y$:

| $Y$ | 100 | 200 | 300 |
|---|---:|---:|---:|
| $P$ | 0,21 | 0,35 | 0,44 |

Kết quả:

$$
E(Y)=223,\qquad V(Y)=5971.
$$

Phân phối biên của $X$:

| $X$ | 1 | 1,5 | 2 |
|---|---:|---:|---:|
| $P$ | 0,29 | 0,40 | 0,31 |

Kết quả:

$$
E(X)=1,51,\qquad V(X)=0,1499.
$$

### 4. Phân phối có điều kiện và kỳ vọng có điều kiện

Phân phối của $X$ với điều kiện $\{Y=y_j\}$ có xác suất:

$$
p(x_i|y_j)=\frac{p_{ij}}{p(y_j)}.
$$

Kỳ vọng có điều kiện:

$$
E(X|Y=y_j)=x_1p(x_1|y_j)+x_2p(x_2|y_j)+\cdots+x_np(x_n|y_j).
$$

Tương tự, phân phối của $Y$ với điều kiện $\{X=x_i\}$:

$$
p(y_j|x_i)=\frac{p_{ij}}{p(x_i)}.
$$

Kỳ vọng có điều kiện:

$$
E(Y|X=x_i)=y_1p(y_1|x_i)+y_2p(y_2|x_i)+\cdots+y_mp(y_m|x_i).
$$

**Ví dụ:** Trong bảng trên, nếu muốn doanh số là 300 triệu đồng thì trung bình chi phí quảng cáo là bao nhiêu?

**Giải:** Vì $p(Y=300)=0,44$, nên:

| $X|Y=300$ | 1 | 1,5 | 2 |
|---|---:|---:|---:|
| $P$ | $4/44$ | $15/44$ | $25/44$ |

Do đó:

$$
E(X|Y=300)\approx 1,738.
$$

**Ví dụ:** Nếu chi phí quảng cáo là 1,5 triệu đồng thì trung bình doanh số là bao nhiêu?

**Giải:** Vì $p(X=1,5)=0,4$, nên:

| $Y|X=1,5$ | 100 | 200 | 300 |
|---|---:|---:|---:|
| $P$ | $1/8$ | $4/8$ | $3/8$ |

Do đó:

$$
E(Y|X=1,5)=225.
$$

### 5. Độc lập của hai biến ngẫu nhiên rời rạc

Hai biến ngẫu nhiên rời rạc $X$ và $Y$ được gọi là độc lập nếu với mọi cặp $(i,j)$:

$$
P\{(X,Y)=(x_i,y_j)\}=P\{X=x_i\}P\{Y=y_j\},
$$

hay:

$$
p_{ij}=p(x_i)p(y_j).
$$

Nếu $X,Y$ độc lập và tồn tại $E(X),E(Y)$ thì:

$$
E(XY)=E(X)E(Y).
$$

Nếu $X,Y$ độc lập và tồn tại $V(X),V(Y)$ thì:

$$
V(X\pm Y)=V(X)+V(Y).
$$

## HIỆP PHƯƠNG SAI VÀ HỆ SỐ TƯƠNG QUAN

### 1. Hiệp phương sai

Khi phân tích thống kê, ta thường muốn biết mối liên hệ giữa hai biến như chi phí quảng cáo và doanh số, giá cả và lợi nhuận, chất lượng sản phẩm và sự hài lòng của khách hàng. Một thước đo phổ biến là hiệp phương sai.

Hiệp phương sai của hai biến ngẫu nhiên $X$ và $Y$, kí hiệu $\operatorname{cov}(X,Y)$, được xác định bởi:

$$
\operatorname{cov}(X,Y)=E(XY)-E(X)E(Y).
$$

Với biến ngẫu nhiên rời rạc hai chiều:

$$
E(XY)=\sum_{i,j}x_iy_jp_{ij}.
$$

### 2. Hệ số tương quan

Tương quan tuyến tính giữa hai biến ngẫu nhiên $X,Y$ là mối quan hệ mà khi biểu diễn các giá trị quan sát trên mặt phẳng $Oxy$, các điểm dữ liệu có xu hướng tạo thành một đường thẳng.

Hệ số tương quan của $X$ và $Y$, kí hiệu $\rho(X,Y)$, được xác định:

$$
\rho(X,Y)=\frac{\operatorname{cov}(X,Y)}{\sigma(X)\sigma(Y)}.
$$

Ta nói $X$ và $Y$ không tương quan nếu:

$$
\operatorname{cov}(X,Y)=0,
$$

hay:

$$
\rho(X,Y)=0.
$$

### 3. Tính chất của hệ số tương quan

1. $|\rho(X,Y)|\le 1$.
2. $|\rho(X,Y)|$ càng gần 1 thì mức độ phụ thuộc tuyến tính giữa $X$ và $Y$ càng rõ.
3. Nếu $|\rho(X,Y)|=1$ thì tồn tại $a\ne0$ và $b$ sao cho:

$$
P\{Y=aX+b\}=1.
$$

4. $\rho(X,Y)$ càng gần 0 thì mức độ phụ thuộc tuyến tính càng không chặt.
5. Nếu $X$ và $Y$ độc lập thì $\rho(X,Y)=0$, nhưng điều ngược lại không đúng.
6. Nếu $\rho(X,Y)>0$ thì khi $X$ tăng, $Y$ có xu hướng tăng; đây là tương quan thuận.
7. Nếu $\rho(X,Y)<0$ thì khi $X$ tăng, $Y$ có xu hướng giảm; đây là tương quan nghịch.

**Ví dụ:** Trong bảng phân phối chi phí quảng cáo và doanh số bán hàng ở trên:

$$
E(XY)=354.
$$

$$
\operatorname{cov}(X,Y)=E(XY)-E(X)E(Y)=17,27.
$$

$$
\rho(X,Y)=\frac{17,27}{\sqrt{0,1499}\sqrt{5971}}\approx 0,577.
$$

Vì $\rho(X,Y)>0$, doanh số $Y$ có xu hướng tăng khi chi phí quảng cáo $X$ tăng.
