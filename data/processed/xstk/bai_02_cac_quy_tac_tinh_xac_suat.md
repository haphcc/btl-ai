### BÀI 2
#### CÁC QUY TẮC TÍNH XÁC SUẤT

**NỘI DUNG CHÍNH:**
- Quy tắc cộng xác suất và quy tắc cộng tổng quát.
- Xác suất có điều kiện.
- Quy tắc nhân xác suất và tính độc lập.
- Công thức xác suất đầy đủ và công thức Bayes.

## CÁC QUY TẮC TÍNH XÁC SUẤT

### 1. Quy tắc cộng xác suất

Nếu các biến cố $A_1,A_2,\ldots,A_n$ liên quan đến phép thử $\mathcal{T}$ và xung khắc từng đôi một, thì:

$$
P\left(\bigcup_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}P(A_i).
$$

**Ví dụ:** Trong két có 100 tờ tiền, trong đó có 60 tờ mệnh giá 100 nghìn và 12 tờ mệnh giá 200 nghìn. Chọn ngẫu nhiên một tờ. Tính xác suất để tờ này có mệnh giá 100 hoặc 200 nghìn.

**Giải:** Gọi $A$ là biến cố "tờ được chọn có mệnh giá 100 nghìn", $B$ là biến cố "tờ được chọn có mệnh giá 200 nghìn". Hai biến cố $A$ và $B$ xung khắc, nên:

$$
P(A\cup B)=P(A)+P(B)=\frac{60}{100}+\frac{12}{100}=0,72.
$$

Hệ quả:

$$
P(A)+P(\overline{A})=1.
$$

Ngoài ra:

$$
P(AB)+P(\overline{A}B)=P(B).
$$

### 2. Quy tắc cộng xác suất tổng quát

Nếu các biến cố $A_1,A_2,\ldots,A_n$ liên quan đến phép thử $\mathcal{T}$, không nhất thiết xung khắc, thì:

$$
P\left(\bigcup_{i=1}^{n}A_i\right)
=\sum_{i=1}^{n}P(A_i)
-\sum_{1\le i<j\le n}P(A_iA_j)
+\sum_{1\le i<j<k\le n}P(A_iA_jA_k)
-\cdots+(-1)^{n-1}P(A_1A_2\cdots A_n).
$$

**Ví dụ:** Một ngân hàng sử dụng hai loại thẻ thanh toán $M$ và $N$. Tỉ lệ khách sử dụng thẻ $M$, thẻ $N$ và cả hai loại lần lượt là 60%, 55% và 30%. Chọn ngẫu nhiên một khách hàng của ngân hàng. Tính xác suất:

1. Người đó có sử dụng thẻ của ngân hàng.
2. Người đó không sử dụng thẻ của ngân hàng.
3. Người đó chỉ sử dụng một loại thẻ.
4. Người đó chỉ sử dụng thẻ $M$.

**Giải:** Gọi $A$ là biến cố "người đó sử dụng thẻ $M$", $B$ là biến cố "người đó sử dụng thẻ $N$".

Ta có:

$$
P(A)=0,6,\qquad P(B)=0,55,\qquad P(AB)=0,3.
$$

1. Xác suất có sử dụng thẻ:

$$
P(A\cup B)=P(A)+P(B)-P(AB)=0,6+0,55-0,3=0,85.
$$

2. Xác suất không sử dụng thẻ:

$$
1-P(A\cup B)=1-0,85=0,15.
$$

3. Xác suất chỉ sử dụng một loại thẻ:

$$
P(A\overline{B})+P(\overline{A}B)=(0,6-0,3)+(0,55-0,3)=0,55.
$$

4. Xác suất chỉ sử dụng thẻ $M$:

$$
P(A\overline{B})=P(A)-P(AB)=0,6-0,3=0,3.
$$

## XÁC SUẤT CÓ ĐIỀU KIỆN

### 1. Khái niệm

Có những biến cố mà sự xảy ra của chúng ảnh hưởng đến nhau. Khi biết một biến cố đã xảy ra, xác suất của biến cố khác có thể thay đổi.

Giả sử $P(A)>0$. Xác suất có điều kiện của biến cố $B$ với điều kiện biến cố $A$ đã xảy ra, kí hiệu $P(B|A)$, được định nghĩa:

$$
P(B|A)=\frac{P(AB)}{P(A)}.
$$

**Ví dụ:** Theo điều tra của một ngân hàng về sử dụng thẻ tín dụng ở một công ty, có 50% người dùng thẻ $M$, 30% dùng thẻ $N$, 20% dùng cả hai loại. Tính xác suất để chọn ngẫu nhiên một người thì người đó dùng thẻ $N$, và xác suất người đó dùng thẻ $N$ nếu biết người đó dùng thẻ $M$.

**Giải:** Gọi $A$ là biến cố "người đó dùng thẻ $M$", $B$ là biến cố "người đó dùng thẻ $N$". Khi đó:

$$
P(B)=0,3.
$$

Nếu biết $A$ đã xảy ra:

$$
P(B|A)=\frac{P(AB)}{P(A)}=\frac{20\%}{50\%}=0,4.
$$

Xác suất chọn được người dùng thẻ $N$ phụ thuộc vào việc đã biết người đó dùng thẻ $M$ hay chưa.

### 2. Tính trực tiếp xác suất có điều kiện

Xác suất có điều kiện có thể tính trực tiếp từ bối cảnh bài toán.

**Ví dụ:** Hộp kín có 6 thẻ ATM của ACB và 4 thẻ ATM của Vietcombank. Lấy ngẫu nhiên lần lượt 2 thẻ, không hoàn lại. Tính xác suất lần thứ hai lấy được thẻ Vietcombank nếu biết lần thứ nhất đã lấy được thẻ ACB.

**Giải:** Sau khi lần thứ nhất đã lấy được thẻ ACB, trong hộp còn 9 thẻ, trong đó có 4 thẻ Vietcombank. Vậy:

$$
P(B|A)=\frac{4}{9}.
$$

Nếu dùng định nghĩa, với $A=$ "lần 1 rút được thẻ ACB", $B=$ "lần 2 rút được thẻ Vietcombank":

$$
P(B|A)=\frac{P(AB)}{P(A)}=\frac{6\cdot4/90}{6\cdot9/90}=\frac{4}{9}.
$$

### 3. Một số chú ý

Ta có:

$$
P(\overline{B}|A)=1-P(B|A).
$$

Nhưng nói chung:

$$
P(B|\overline{A})\ne 1-P(B|A).
$$

Nếu $A\subset B$ thì $P(B|A)=1$.

Nếu $B\subset A$ thì:

$$
P(B|A)=\frac{P(B)}{P(A)}.
$$

## QUY TẮC NHÂN XÁC SUẤT

### 1. Quy tắc nhân hai biến cố

Từ định nghĩa xác suất có điều kiện:

$$
P(B|A)=\frac{P(AB)}{P(A)},\qquad P(A)>0,
$$

suy ra:

$$
P(AB)=P(A)P(B|A).
$$

### 2. Quy tắc nhân tổng quát

Nếu $P(A_1A_2\cdots A_{n-1})>0$ với $n>1$, thì:

$$
P(A_1A_2\cdots A_n)
=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)\cdots P(A_n|A_1A_2\cdots A_{n-1}).
$$

**Ví dụ:** Một lô hàng gồm 100 sản phẩm, trong đó có 10 phế phẩm. Rút ngẫu nhiên lần lượt 4 sản phẩm, không hoàn lại. Nếu cả 4 sản phẩm đều tốt thì lô hàng được nhận. Tìm xác suất để lô hàng được nhận.

**Giải:** Gọi $A_i$ là biến cố "lần rút thứ $i$ được sản phẩm tốt", $i=1,2,3,4$. Khi đó:

$$
P(A_1A_2A_3A_4)
=\frac{90}{100}\cdot\frac{89}{99}\cdot\frac{88}{98}\cdot\frac{87}{97}
\approx 0,6516.
$$

## CÁC BIẾN CỐ ĐỘC LẬP

### 1. Hai biến cố độc lập

Hai biến cố $A$ và $B$ liên quan đến một phép thử $\mathcal{T}$ được gọi là độc lập nếu:

$$
P(B)=P(B|A),
$$

hay tương đương:

$$
P(AB)=P(A)P(B).
$$

Quan hệ độc lập là quan hệ đối xứng: nếu $A$ độc lập với $B$ thì $B$ độc lập với $A$.

Nếu $A$ và $B$ độc lập thì các cặp sau cũng độc lập:

- $A$ và $\overline{B}$.
- $\overline{A}$ và $B$.
- $\overline{A}$ và $\overline{B}$.

### 2. Độc lập toàn phần

Các biến cố $A_1,A_2,\ldots,A_n$ được gọi là độc lập toàn phần nếu chúng độc lập từng đôi và mỗi biến cố độc lập với tích của một số tùy ý các biến cố còn lại.

Nếu $A_1,A_2,\ldots,A_n$ độc lập toàn phần thì:

$$
P(A_1A_2\cdots A_n)=P(A_1)P(A_2)\cdots P(A_n).
$$

**Ví dụ:** Một lô hàng gồm 100 sản phẩm, trong đó có 10 phế phẩm. Rút ngẫu nhiên lần lượt 4 sản phẩm, sau mỗi lần rút kiểm tra xong lại hoàn sản phẩm vào lô hàng. Nếu cả 4 sản phẩm đều tốt thì lô hàng được nhận.

**Giải:** Các lần rút là độc lập, xác suất mỗi lần rút được sản phẩm tốt là $\frac{90}{100}$. Vậy:

$$
P(H)=\left(\frac{90}{100}\right)^4=0,6561.
$$

Khi $n>2$, từ điều kiện các biến cố độc lập từng đôi chưa thể kết luận:

$$
P(A_1A_2\cdots A_n)=P(A_1)P(A_2)\cdots P(A_n).
$$

## CÔNG THỨC XÁC SUẤT ĐẦY ĐỦ

### 1. Nhóm đầy đủ các biến cố

Các biến cố $H_1,H_2,\ldots,H_n$ được gọi là một nhóm đầy đủ các biến cố nếu:

$$
H_iH_j=\varnothing \quad (i\ne j),
$$

và:

$$
\bigcup_{i=1}^{n}H_i=\Omega.
$$

### 2. Công thức xác suất đầy đủ

Giả sử $H_1,H_2,\ldots,H_n$ là một nhóm đầy đủ các biến cố có xác suất khác 0 và $A$ là một biến cố cùng phép thử. Khi đó:

$$
P(A)=\sum_{i=1}^{n}P(H_i)P(A|H_i).
$$

**Ví dụ:** Có ba hộp:

| Hộp | Chính phẩm | Phế phẩm |
|---|---:|---:|
| 1 | 6 | 4 |
| 2 | 10 | 5 |
| 3 | 15 | 5 |

Lấy ngẫu nhiên một hộp, rồi từ đó lấy ngẫu nhiên một sản phẩm. Tìm xác suất lấy được chính phẩm.

**Giải:** Gọi $A$ là biến cố "lấy được chính phẩm", $H_i$ là biến cố "lấy hộp thứ $i$". Khi đó:

$$
P(H_1)=P(H_2)=P(H_3)=\frac{1}{3}.
$$

Các xác suất có điều kiện:

$$
P(A|H_1)=\frac{6}{10},\qquad P(A|H_2)=\frac{10}{15},\qquad P(A|H_3)=\frac{15}{20}.
$$

Do đó:

$$
P(A)=\frac{1}{3}\cdot\frac{6}{10}
+\frac{1}{3}\cdot\frac{10}{15}
+\frac{1}{3}\cdot\frac{15}{20}
=\frac{121}{180}.
$$

Nếu phép thử gồm hai giai đoạn và biến cố $A$ liên quan đến giai đoạn sau, thì các kết quả có thể có của giai đoạn đầu thường tạo thành một nhóm đầy đủ.

## CÔNG THỨC BAYES

Giả sử $H_1,H_2,\ldots,H_n$ là một nhóm đầy đủ các biến cố có xác suất khác 0 và $A$ là một biến cố cùng phép thử với $P(A)\ne0$. Với mỗi $j=1,2,\ldots,n$:

$$
P(H_j|A)=\frac{P(H_j)P(A|H_j)}
{\sum_{i=1}^{n}P(H_i)P(A|H_i)}.
$$

Công thức Bayes thường được dùng cùng công thức xác suất đầy đủ. Nó cho phép cập nhật xác suất của các biến cố $H_i$ sau khi đã biết biến cố $A$ xảy ra.

**Ví dụ:** Với ba hộp ở ví dụ trên, lấy ngẫu nhiên một hộp rồi lấy một sản phẩm, thấy đó là chính phẩm. Tìm xác suất sản phẩm đó thuộc hộp 1.

**Giải:** Theo công thức Bayes:

$$
P(H_1|A)=\frac{P(H_1)P(A|H_1)}{P(A)}
=\frac{\frac{1}{3}\cdot\frac{6}{10}}{\frac{121}{180}}
=\frac{36}{121}.
$$

**Ví dụ:** Phỏng vấn 200 khách hàng về một sản phẩm sắp đưa ra thị trường:

| Trả lời | Số người | Tỉ lệ thực sự mua theo kinh nghiệm |
|---|---:|---:|
| Sẽ mua | 34 | 40% |
| Có thể sẽ mua | 96 | 20% |
| Không mua | 70 | 1% |

1. Đánh giá thị trường tiềm năng của sản phẩm.
2. Trong số khách hàng thực sự mua, có bao nhiêu phần trăm đã trả lời "Sẽ mua"?

**Giải:** Gọi $A$ là biến cố "khách hàng thực sự mua sản phẩm"; $H_1,H_2,H_3$ tương ứng với ba cách trả lời.

Ta có:

$$
P(H_1)=\frac{34}{200}=0,17,\quad
P(H_2)=\frac{96}{200}=0,48,\quad
P(H_3)=\frac{70}{200}=0,35.
$$

Và:

$$
P(A|H_1)=0,4,\quad P(A|H_2)=0,2,\quad P(A|H_3)=0,01.
$$

Theo công thức xác suất đầy đủ:

$$
P(A)=0,17\cdot0,4+0,48\cdot0,2+0,35\cdot0,01=0,1675.
$$

Vậy thị trường tiềm năng là $16,75\%$.

Theo công thức Bayes:

$$
P(H_1|A)=\frac{0,17\cdot0,4}{0,1675}\approx 40,597\%.
$$
