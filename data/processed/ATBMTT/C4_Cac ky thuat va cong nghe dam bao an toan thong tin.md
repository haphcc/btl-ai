# CHƯƠNG IV
## CÁC KỸ THUẬT VÀ CÔNG NGHỆ ĐẢM BẢO AN TOÀN THÔNG TIN

# Nội dung

## 4.1 Cơ sở toán học
## 4.2 Đảm bảo an toàn thông tin dựa trên mật mã
## 4.3 Các kỹ thuật mã hóa
## 4.4 Hàm băm
## 4.5 Chữ ký số

## 4.1.1 Một số khái niệm trong số học
### 4.1.1.1. Ước chung lớn nhất, Bội chung nhỏ nhất
#### **Khái niệm**
- **Ước số, bội số**
- **Ước chung lớn nhất ($\gcd(a,b)$)**
- **Bội chung nhỏ nhất ($\text{lcm}(a,b)$)**

## 4.1.1.1. **Ước chung lớn nhất, Bội chung nhỏ nhất**

### **Tính chất:**

- $d = \gcd(a_1, a_2, \dots, a_n)$ khi và chỉ khi tồn tại các số $x_1, x_2, \dots, x_n$ sao cho $d = a_1x_1 + a_2x_2 + \dots + a_nx_n$
- $d = \gcd(a_1, a_2, \dots, a_n) \iff \gcd(a_1/d, a_2/d, \dots, a_n/d) = 1$
- $m = \text{lcm}(a_1, a_2, \dots, a_n) \iff \gcd(m/a_1, m/a_2, \dots, m/a_n) = 1$
- $\gcd(m a_1, m a_2, \dots, m a_n) = m * \gcd(a_1, a_2, \dots, a_n)$ (với $m \neq 0$)
- Nếu $\gcd(a, b) = 1$ thì $\text{lcm}(a, b) = a * b$
- Nếu $b > 0, a = bq + r$ thì $\gcd(a, b) = \gcd(b, r)$

### Thuật toán Euclide tìm $\gcd(a,b)$:

**Bài toán:**

- **Đầu vào:** Cho hai số nguyên không âm $a, b, a \ge b$
- **Đầu ra:** $\gcd(a,b)$

### Thuật toán Euclide tìm $\text{gcd}(a,b)$:

- **Thuật toán:**

  cin>>a; cin>>b;
  While (b>0) do
  {
      r := a mod b; a := b; b := r;
  }
  cout<<a;

- **Thuật toán Euclide tìm $\gcd(a,b)$:**
    - **Ví dụ: $\gcd(30,18)$**
    $a=30, b=18; \gcd(30,18) = \gcd(18,12) = \gcd(12,6) = \gcd(6,0) = 6$

| a | b | r | a=b.q+r |
| :--- | :--- | :--- | :--- |
| 30 | 18 | 12 | $30=18.1+12$ |
| 18 | 12 | 6 | $18=12.1+6$ |
| 12 | 6 | 0 | $12=6.2+0$ |

### Thuật toán Euclide mở rộng

**Bài toán:**

- **Đầu vào:** Cho hai số nguyên không âm $a, b, a \ge b$
- **Đầu ra:** $d = \gcd(a,b)$ và $x,y$ sao cho $ax + by = d$

- **Thuật toán:**
cin>>a; cin>>b;
if(b==0) {
    d=a; x=1; y=0; cout<<d<<x<<y;}
else {
    x2=1; x1=0; y2=0; y1=1;
    while (b>0) {
        q=a div b; r=a mod b;
        x=x2 - q*x1; y=y2 - q*y1;
        a=b; b=r; x2=x1; x1=x; y2=y1; y1=y;}
    d=a; x=x2; y=y2;
    cout<<d<<x<<y; }

### 4.1.1.2. Quan hệ đồng dư
- **Khái niệm:**
- **Các tính chất của quan hệ đồng dư**
    - Quan hệ tương đương
    - Tổng và hiệu các đồng dư
    - Tích các đồng dư

## 4.1.3. Số nguyên tố
- **Khái niệm:**

- **Ví dụ**

- **10 số nguyên tố lớn tìm thấy:**

| ran | Prime | Digits | Who | whe | referenc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | $2^{32582657}-1$ | 980835 | G9 | 2006 | Mersenne |
| 2 | $2^{30402457}-1$ | 915205 | G9 | 2005 | Mersenne |
| 3 | $2^{25964951}-1$ | 781623 | G8 | 2005 | Mersenne |
| 4 | $2^{24036583}-1$ | 723573 | G7 | 2004 | Mersenne |
| 5 | $2^{20996011}-1$ | 632043 | G6 | 2003 | Mersenne |
| 6 | $2^{13466917}-1$ | 405394 | G5 | 2001 | Mersenne |
| 7 | $\mathbf{19249 \cdot 2^{13018586}+}$ | 391899 | SB1 | 2007 | |
| 8 | $\mathbf{27653 \cdot 2^{9167433}+1}$ | 275967 | SB8 | 2005 | |
| 9 | $\mathbf{28433 \cdot 2^{7830457}+1}$ | 235720 | SB7 | 2004 | |
| 10 | $\mathbf{33661 \cdot 2^{7031232}+1}$ | 211661 | SB1 | 2007 | |

## 4.1.1.3. Số nguyên tố
❖ **Định lý về số nguyên tố:**

- **Định lý 1:**

- **Định lý Mersenne:** Cho $p=2^k-1$; Nếu $p$ nguyên tố thì cũng phải $k$ nguyên tố.

- **Hàm Euler và định lý hàm Euler**

## 4.1.3. Số nguyên tố

❖ **Phương pháp kiểm tra tính nguyên tố**

- **Phương pháp cổ điển:**

- **Phương pháp xác suất**

    - **Định lý Ferma:** Nếu $p$ là số nguyên tố, $a$ là số nguyên, thì $a^p \equiv a \pmod p$. Nếu $p$ không chia hết $a$, thì $a^{p-1} \equiv 1 \pmod p$

    - **Định lý Euler:** Nếu $\gcd(a, m) = 1$ thì $a^{\phi(m)} \equiv 1 \pmod m$

    - **Hệ quả:** Nếu $\gcd(c, m) = 1$ và $a \equiv b \pmod{\phi(m)}$ với $a, b$ là các số tự nhiên, thì $c^a \equiv c^b \pmod m$ và suy ra $c^a \pmod m = c^{a \pmod{\phi(m)}} \pmod m$

## 4.1.3. Số nguyên tố
### Tính toán đồng dư của lũy thừa lớn
- Trường hợp $a > \Phi(m)$:
- Trường hợp $a < \Phi(m)$:
- Phương pháp bình phương liên tiếp
- **Định lý số dư Trung Quốc**:
Cho tập số nguyên tố cùng nhau từng đôi một $m_1, m_2, \dots, m_r$.
Với mỗi bộ số nguyên bất kỳ $a_1, a_2, \dots, a_r$, hệ phương trình đồng dư:
$x \equiv a_i \pmod{m_i}, (i = 1, 2, \dots, r)$, luôn có **nghiệm duy nhất** theo modulo $m$,
$m = m_1.m_2 \dots m_r$. Nghiệm này có thể tính theo công thức:
$x = a_1 m_2 m_3 \dots m_r b_1 + m_1 a_2 m_3 \dots m_r b_2 + m_1 m_2 a_3 m_3 \dots m_r b_3 + \dots +$
$m_1 m_2 \dots m_{r-1} a_r b_r \pmod{m_1.m_2 \dots m_r}$,
trong đó $b_i = (m_1 m_2 \dots m_{i-1} m_{i+1} \dots m_r)^{-1} \pmod{m_i}$, với mọi $i = 1, 2, \dots, r$.

## Ví dụ

Tính $87^{43} \pmod{103}$

Khai triển số mũ 43 dưới dạng cơ số 2:
$43 = 32 + 8 + 2 + 1 = 2^5 + 2^3 + 2^1 + 2^0$ (*)

Tính liên tiếp các "đồng dư" bình phương như sau:
- $87 \pmod{103} = 87$ (ứng với $2^0$)
- $87^2 \pmod{103} = 50$ (ứng với $2^1$)
- $87^4 \pmod{103} = 50^2 \pmod{103} = 28$
- $87^8 \pmod{103} = 28^2 \pmod{103} = 63$ (ứng với $2^3$)
- $87^{16} \pmod{103} = 63^2 \pmod{103} = 55$
- $87^{32} \pmod{103} = 55^2 \pmod{103} = 38$ (ứng với $2^5$)

Theo khai triển (*), lấy tích của các lũy thừa bậc $2^5, 2^3, 2^1, 2^0$ (rút gọn theo modulo 103), thu được kết quả:
$87^{43} \pmod{103} = 38 * 63 * 50 * 87 \pmod{103} = 85$

## Ví dụ

**Ví dụ**: Tìm nghiệm của hệ phương trình:
$$
\begin{cases}
x \equiv 3118 \pmod{5353} \\
x \equiv 139 \pmod{391} \\
x \equiv 239 \pmod{247}
\end{cases}
$$

Vì các số 5353, 391, 247 nguyên tố cùng nhau, nên theo định lý Trung Quốc về số dư hệ, có nghiệm duy nhất theo modulo $m = 5353 \times 391 \times 247 = 516976681$.

Để tìm $x \pmod m$ ta tính:
- $m_1 = m/5353 = 96577 \rightarrow y_1 = 96577^{-1} \pmod{5353} = 5329$
- $m_2 = m/391 = 1322191 \rightarrow y_2 = 1322191^{-1} \pmod{391} = 16$
- $m_3 = m/247 = 2093023 \rightarrow y_3 = 2093023^{-1} \pmod{247} = 238$

$x = 3118 \cdot 96577 \cdot 5329 + 139 \cdot 1322191 \cdot 16 + 239 \cdot 2093023 \cdot 238 \pmod m$
$= 13824 \pmod m$

## 4.1.2 Một số khái niệm trong Đại số
## 4.1.2.1. Cấu trúc nhóm

### Khái niệm nhóm
- **Khái niệm nhóm**: *Nhóm* là một bộ $(G, *)$, trong đó $G \neq \varnothing$, $*$ là *phép toán hai ngôi* trên $G$ thoả mãn ba tính chất sau: Kết hợp, phần tử trung lập và phần tử nghịch đảo
- **Cấp của nhóm**
- **Nhóm Abel**: là nhóm $(G, *)$, trong đó phép toán hai ngôi $*$ có tính giao hoán

### Nhóm con của nhóm

## 4.1.2.2 Nhóm Cyclic

- **Khái niệm:** Là nhóm mà toàn bộ các phần tử của nó được sinh ra bởi một trong các phần tử của nó ($g * g * ... * g = a$), $g$ là phần tử sinh.

- **Cấp của nhóm:** Là số tự nhiên $n$ **nhỏ nhất** mà $g^n = e$.

- **Cấp của 1 phần tử trong nhóm:** Phần tử $\alpha \in G$ được gọi là có **cấp $d$**, nếu $d$ là số nguyên dương **nhỏ nhất** sao cho $\alpha^d = e$.

## 4.1.2.3 Nhóm ($Z_n^*$, phép nhân mod n)
### **Phần tử nghịch đảo đối với phép nhân**
- **Định nghĩa:**

- **Định lý:** $UCLN(a, n) = 1 \iff$ Phần tử $a \in Z_n$ có phần tử nghịch đảo

- **Hệ quả:** Mọi phần tử trong $Z_n^*$ đều có phần tử nghịch đảo

- **Tìm phần tử nghịch đảo bằng Thuật toán Euclid mở rộng**
    - Input: $a \in Z_n$
    - Output: Phần tử nghịch đảo của $a$

- Thuật toán:

```c
int Invert(int a, int n)
{
    g0=n; g1=a; u0=1; u1=0; v0=0; v1=1;
    i=1;
    while (gi ≠ 0)
    {
        y = gi-1 div gi;
        gi+1 = gi-1 - y.gi;
        ui+1 = ui-1 - y.ui;
        vi+1 = vi-1 - y.vi;
        i = i+1;
    }
    t = vi+1;
    if (t > 0) a^(-1) = t;
    else a^(-1) = t + n;
}
```

## 4.1.3. Khái niệm độ phức tạp của thuật toán
## 4.1.3.1 Khái niệm thuật toán

- **Khái niệm bài toán**

- **Khái niệm thuật toán**
    - Quan niệm trực giác
    - Quan niệm toán học

- **Hai mô hình tính toán**
    - Mô hình ứng dụng: Ngôn ngữ tựa Algol
    - Mô hình lý thuyết: Biểu diễn bằng ngôn ngữ máy Turing

## 4.1.3.2 Khái niệm độ phức tạp của thuật toán

- **Chi phí của thuật toán** (*Tính theo một bộ dữ liệu vào*):
- **Độ phức tạp về bộ nhớ**:
- **Độ phức tạp thời gian**
- **Độ phức tạp tiệm cận**
- **Độ phức tạp đa thức**
- **Thuật toán đa thức**

## 4.1.3.3 Phân lớp bài toán theo độ phức tạp

- **Các khái niệm**
    - Dẫn về được
    - Khó tương đương
- **Các lớp bài toán**
    - Lớp bài toán P, NP
    - Lớp Bài toán NP- Hard
    - Lớp bài toán NP- Complete

- **Phân lớp các bài toán**

## 4.1.3.3 Hàm một phía và hàm cửa sập một phía

- **Hàm một phía**: Hàm $f(x)$ được gọi là **hàm một phía** nếu tính “**xuôi**” $y = f(x)$ thì “**dễ**”, nhưng tính “**ngược**” $x = f^{-1}(y)$ lại rất “**khó**”.

- **Hàm cửa sập một phía**: Hàm $f(x)$ được gọi là **hàm cửa sập một phía** nếu tính $y = f(x)$ thì “**dễ**”, tính $x = f^{-1}(y)$ lại rất “**khó**”. Tuy nhiên có **cửa sập z** để tính $x = f^{-1}(y)$ là “**dễ**”.

# 4.2. Đảm bảo ATTT dựa trên mật mã học

## 4.2.1 Khái niệm về mật mã học

- **Mật mã học: bao gồm mã hóa và thám mã**

- **Mã hóa:** Nghiên cứu các thuật toán và phương thức đảm bảo tính bí mật và xác thực của thông tin
- **Thám mã:** Nghiên cứu các phương pháp phá mã hoặc tạo mã giả

- **Khái niệm mã hóa (cryptography):**
    - Che thông tin
    - Giấu thông tin

- **Hệ mã hóa (P,K C,E,D)**

- **Sơ đồ mã hóa và giải mã**

| | | |
| :--- | :--- | :--- |
| Người gửi G | $\rightarrow \rightarrow$ | $e_{ke}(T)$ | $\rightarrow \rightarrow$ Người nhận N |
| (có khóa lập mã $ke$) | | $\uparrow$ | (có khóa giải mã $kd$) |
| | | Tin tặc có thể trộm bản mã $e_{ke}(T)$ | |

### Các cách phân loại

- Theo đặc trưng của Khóa
    - **Mã hóa đối xứng**
    - **Mã hóa công khai**

- Theo đặc trưng bản rõ
    - **Mã hóa khối**
    - **Mã hóa dòng**

### Hệ mã hóa Khóa đối xứng

- **Khái niệm:** là Hệ mã hóa mà biết được khóa lập mã thì có thể “dễ” tính được khóa giải mã và ngược lại

- **Đặc điểm:**
    - **Ưu điểm:**
    - **Nhược điểm:**

- **Nơi sử dụng:**
    - Trong mạng nội bộ
    - Dữ liệu lớn

### Hệ mã hóa Khóa công khai

- **Khái niệm:** là hệ mã hóa có khóa lập mã và khóa giải mã là khác nhau, khóa lập mã là công khai, khóa giải mã là bí mật.

- **Đặc điểm:**
    - **Ưu điểm:**
    - **Nhược:**

- **Nơi sử dụng**
    Trong mạng Internet

### Ứng dụng của mật mã học

- **Bảo mật:**
- **Xác thực**
- **Toàn vẹn**
- **Dịch vụ không thể chối từ**
- **Dịch vụ xác thực danh tính**

## 4.2.2. Các phương pháp mã hóa
### 4.2.2.1. Hệ mã hóa dịch chuyển

- **Sơ đồ**

Đặt $P = C = K = Z_{26}$. Bản mã $y$ và bản rõ $x \in Z_{26}$.

Với khóa $k \in K$, ta định nghĩa:

Hàm Mã hóa: $y = e_k(x) = (x + k) \mod 26$

Hàm Giải mã: $x = d_k(y) = (y - k) \mod 26$

- **Ví dụ**

| T | O | I | | N | A | Y | | T | H | A | | V | I | R | U | S |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 19 | 14 | 8 | 26 | 13 | 0 | 24 | 26 | 19 | 7 | 0 | 26 | 21 | 8 | 17 | 20 | 18 |

| 22 | 17 | 11 | 3 | 16 | 3 | 1 | 3 | 22 | 10 | 3 | 3 | 24 | 11 | 20 | 23 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W | R | L | D | Q | D | B | D | W | K | D | D | Y | L | U | X | V |

- **Độ an toàn: Rất thấp**

## 4.2.2. Hệ mã hóa thay thế

### Sơ đồ

Đặt $P = C = \mathbb{Z}_{26}$. Bản mã $y$ và bản rõ $x \in \mathbb{Z}_{26}$.
Tập khóa $K$ là tập mọi hoán vị trên $\mathbb{Z}_{26}$.
Với khóa $k = \pi \in K$, tức là 1 hoán vị trên $\mathbb{Z}_{26}$, ta định nghĩa:

Mã hóa: $y = e_k(x) = \pi(x)$
Giải mã: $x = d_k(y) = \pi^{-1}(y)$

### Ví dụ:

TOI N AY THA VIRUS
Khóa K là bảng thay thế:

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | X | Y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Y | X | V | U | T | S | R | Q | P | O | N | M | L | K | J | I | H | G | F | E | D | C | B | A | Z |

Bản mã chữ là: **E J P Z K Y V Z E Q Y Z C P G D F**

- **Độ an toàn: duyệt 26!**

## 4.2.2.3. Hệ mã hóa AFFINE

Đặt $P = C = \mathbb{Z}_{26}$. Bản mã $y$ và bản rõ $x \in \mathbb{Z}_{26}$.

Tập khóa $K = \{(a, b), \text{ với } a, b \in \mathbb{Z}_{26}, \text{ UCLN}(a, 26) = 1\}$

Với khóa $k = (a, b) \in K$, ta định nghĩa:

- Phép Mã hóa: $y = e_k(x) = (ax + b) \pmod{26}$
- Phép Giải mã: $x = d_k(y) = a^{-1}(y - b) \pmod{26}$

**CHIEUNAYOVUONHOA**
$k = (a, b) = (3, 6)$
Bản rõ số:
$x = 2 \quad 7 \quad 8 \quad 4 \quad 20 \quad 13 \quad 0 \quad 24 \quad 14 \quad 21 \quad 20 \quad 14 \quad 13 \quad 7 \quad 14 \quad 0$
Bản mã số:
$y = 12 \quad 1 \quad 4 \quad 18 \quad 14 \quad 19 \quad 6 \quad 0 \quad 22 \quad 17 \quad 14 \quad 22 \quad 19 \quad 1 \quad 22 \quad 6$
Bản mã chữ: **MBESOTGAWROWTBWG**

- Độ an toàn: **Rất thấp vì số các khóa có thể là 312**

## 4.2.2.4. Hệ mã hóa VIGENERE

Đặt $P = C = K = (\mathbb{Z}_{26})^m$, $m$ là số nguyên dương, các phép toán thực hiện trong $\mathbb{Z}_{26}$.

Bản mã $Y$ và bản rõ $X \in (\mathbb{Z}_{26})^m$. Khoá $k = (k_1, k_2, \dots, k_m)$ gồm $m$ phần tử.

Mã hóa $Y = (y_1, y_2, \dots, y_m) = e_k(x_1, x_2, \dots, x_m) = (x_1 + k_1, x_2 + k_2, \dots, x_m + k_m) \pmod m$.

Giải mã $X = (x_1, x_2, \dots, x_m) = d_k(y_1, y_2, \dots, y_m) = (y_1 - k_1, y_2 - k_2, \dots, y_m - k_m) \pmod m$.

**THISISACRYPTOSYSTEM**,
k = “KWORD” = {10, 22, 14, 17, 3}

19 7 8 18 8 18 0 2 17 24 15 19 14 18 24 18 19 4 12
Bản mã số:
3 3 22 9 11 2 22 16 8 1 25 15 2 9 1 2 15 18 3
Bản mã chữ: **DDWJLCWQIBZPCJBCPSD**

- **Độ an toàn:** Tương đối cao

## 4.2.5 Hệ mã hóa hoán vị cục bộ

- Đặt $P = C = \mathbb{Z}_{26}^m$, $m$ là số nguyên dương. **Bản mã Y** và **bản rõ X** $\in (\mathbb{Z}_{26})^m$.
- Tập khóa $K$ là tập tất cả các hoán vị của $\{1, 2, \dots, m\}$.
- Với mỗi khóa $k = \pi \in K$, $k = (k_1, k_2, \dots, k_m)$ gồm $m$ phần tử, ta định nghĩa:
    - * Mã hóa $Y = (y_1, y_2, \dots, y_m) = e_k (x_1, x_2, \dots, x_m) = (x_{k(1)}, x_{k(2)}, \dots, x_{k(m)})$
    - * Giải mã $X = (x_1, x_2, \dots, x_m) = d_k (y_1, y_2, \dots, y_m) = (y_{k(1)}^{-1}, y_{k(2)}^{-1}, \dots, y_{k(m)}^{-1})$
    - Trong đó $k^{-1} = \pi^{-1}$ là hoán vị ngược của $\pi$.

### Độ an toàn:
Tương đối cao, phải ktra số khóa là:
$1! + 2! + 3! + \dots + m!$ trong đó $m \leq 26$.

Bản rõ chữ $CX = \text{SHESELISSEASASHO}$

Đặt $P = C = Z_{26}^m$, trong đó $m = 6$.

Chọn khoá $k$ là một hoán vị $\pi$ của $(1, 2, 3, 4, 5, 6)$:

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 3 | 5 | 1 | 6 | 4 | 2 |

Hoán vị ngược là $\pi^{-1}$ là:

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 3 | 6 | 1 | 5 | 2 | 4 |

* Mã hóa: Tách bản rõ thành từng nhóm 6 kí tự:

$\text{SHESEL} \mid \text{ISSEAS} \mid \text{ASHO}$

Với mỗi nhóm 6 ký tự, sắp xếp lại các chữ theo hoán vị $\pi$, ta nhận được:

$\text{EELSH} \mid \text{SALSES} \mid \mid \text{HRAE}$

* Bản mã chữ: $CY = \text{EELSHSALSESHRAE}$

## 4.2.2.6. Hệ mã hóa HILL

Đặt $P = C = Z_{26}^m$, $m$ là số nguyên dương. Bản mã $Y$ và bản rõ $X \in (Z_{26})^m$.

Tập khóa $K = \{K \in Z_{26}^{m \times m} / \det(K, 26) = 1\}$. ($K$ phải có $K^{-1}$)

Mỗi khóa $K$ là một "**Chùm chìa khóa**" (một Ma trận "Các chìa khóa")

Với mỗi $K \in K$, định nghĩa:

- Hàm lập mã: $Y = (y_1, y_2, ..., y_m) = e_k(x_1, x_2, ..., x_m) = (x_1, x_2, ..., x_m) * K$
- Hàm giải mã: $X = (x_1, x_2, ..., x_m) = d_k(y_1, y_2, ..., y_m) = (y_1, y_2, ..., y_m) * K^{-1}$

Bản rõ chữ: **TUDO**

Chọn $m = 2$, khóa $K = \begin{pmatrix} 11 & 8 \\ 3 & 7 \end{pmatrix}$, bảo đảm $\text{det}(K, 26) = 1$, tính $K^{-1} = \begin{pmatrix} 7 & 18 \\ 23 & 11 \end{pmatrix}$

* Bản rõ số: 19 20 | 3 14
  $x_1$ $x_2$ | $x_1$ $x_2$

Với mỗi bộ rõ số $(x_1, x_2)$, theo hàm lập mã $(y_1, y_2) = (x_1, x_2) * K$, ta tính được:
$y_1 = 11 * x_1 + 3 * x_2$ , $y_2 = 8 * x_1 + 7 * x_2$

* Bản mã số: 9 6 | 23 18

❖ **Độ an toàn:** Cao

## 4.3.1 Hệ mã hóa đối xứng DES

- **Giới thiệu:**

- **Quy trình mã hóa theo DES**

Giai đoạn 1: **Bản Rõ chữ** =====> **Bản Rõ số** (Dạng nhị phân)
Chia thành
Giai đoạn 2: **Bản Rõ số** =====> **Các đoạn 64 bit Rõ số**

Giai đoạn 3: **64 bit Rõ số** =====> **64 bit Mã số**
Kết nối
Giai đoạn 4: **Các đoạn 64 bit Mã số** =====> **Bản Mã số** (Dạng nhị phân)

Giai đoạn 5: **Bản Mã số** =====> **Bản Mã chữ**

## Quy trình lập mã DES

- **Bản rõ**: 64 bit
- IP
- $L_0$
- $R_0$
- $f$
- $k_1$
- $L_1 = R_0$
- $R_1 = L_0 \oplus f(R_0, k_1)$
- $f$
- $k_2$
- $L_2 = R_1$
- $R_2 = L_1 \oplus f(R_1, k_2)$
- $L_{15} = R_{14}$
- $R_{15} = L_{14} \oplus f(R_{14}, k_{15})$
- $f$
- $k_{16}$
- $R_{16} = L_{15} \oplus f(R_{15}, k_{16})$
- $L_{16} = R_{15}$
- $IP^{-1}$
- **Bản mã**: 64 bit

### Thực hiện mã hóa DES theo sơ đồ

- Bước 1: Bản rõ x được hoán vị theo phép hoán vị IP, thành IP(x)
- Bước 2: Thực hiện 16 vòng mã hóa với những phép toán giống nhau
- Bước 3: Thực hiện phép hoán vị ngược

## Tính các Khóa con $K_i$
- Sơ đồ

K
|
PC - 1
|
$C_0$ | $D_0$
|
$LS_1$ | $LS_1$
|
$C_1$ | $D_1$ -------- PC - 2 -------- $k_1$
|
$LS_2$ | $LS_2$
|
$C_2$ | $D_2$ -------- PC - 2 -------- $k_2$
-----------------------------------
|
$LS_{16}$ | $LS_{16}$
|
$C_{16}$ | $D_{16}$ -------- PC - 2 -------- $k_{16}$

- **Tính khóa $K_i$:**
    - **Khoá K** là xâu dài 64 bit, trong đó 56 bit là khoá và 8 bit để kiểm tra tính chẵn lẻ nhằm phát hiện sai
    - **Cách tính:**
        - Với khoá K độ dài 64 bit, loại bỏ các bit kiểm tra tính chẵn lẻ, hoán vị 56 bit còn lại theo phép hoán vị **PC-1**:
          $PC-1(K) = C_0 D_0$
        - Tính: $C_i = LS_i(C_{i-1})$, $D_i = LS_i(D_{i-1})$ với $i=1, 2, \dots, 16$
        - Với $i=1, 2, \dots, 16$ $k_i$ được tính theo hoán vị **PC-2** từ $C_iD_i$:
          $k_i = PC-2(C_i D_i)$ (48 bit)

## Tính hàm $f(R_{i-1}, k_i)$
- **Sơ đồ**

| | | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $B_1$ | $B_2$ | $B_3$ | $B_4$ | $B_5$ | $B_6$ | $B_7$ | $B_8$ |
| $S_1$ | $S_2$ | $S_3$ | $S_4$ | $S_5$ | $S_6$ | $S_7$ | $S_8$ |
| $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ | $C_6$ | $C_7$ | $C_8$ |

$$f(R_{i-1}, k_i)$$

## Tính hàm $f(R_{i-1}, K_i)$

- Mở rộng R 32 bit thành 48 bit theo hàm mở rộng E
- Tính $E(R) \oplus K$, trong đó $E(R)$ (48 bit) và $K$ (48 bit). Kết quả chia thành $B = B_1 B_2 B_3 B_4 B_5 B_6 B_7 B_8$
- Tính $C_j = S_j (B_j)$, $j = 1, \dots, 8$
- Ta nhận được xâu $C = C_1 C_2 \dots C_8$ (32 bit). Sau hoán vị P, cho kết quả $P(C)$, đó chính là $f(R, K)$

Trong đó:

## Phép hoán vị PC-1

| | | | | | | |
|---|---|---|---|---|---|---|
| 57 | 49 | 41 | 33 | 25 | 17 | 9 |
| 1 | 58 | 50 | 42 | 34 | 26 | 18 |
| 10 | 2 | 59 | 51 | 43 | 35 | 27 |
| 19 | 11 | 3 | 60 | 52 | 44 | 36 |
| 63 | 55 | 47 | 39 | 31 | 23 | 15 |
| 7 | 62 | 54 | 46 | 38 | 30 | 22 |
| 14 | 6 | 61 | 53 | 45 | 37 | 29 |
| 21 | 13 | 5 | 28 | 20 | 12 | 4 |

## Phép hoán vị PC-2

| | | | | | |
|---|---|---|---|---|---|
| 14 | 17 | 11 | 24 | 1 | 5 |
| 3 | 28 | 15 | 6 | 21 | 10 |
| 23 | 19 | 12 | 4 | 26 | 8 |
| 16 | 7 | 27 | 20 | 13 | 2 |
| 41 | 52 | 31 | 37 | 47 | 55 |
| 30 | 40 | 51 | 45 | 33 | 48 |
| 44 | 49 | 39 | 56 | 34 | 53 |
| 46 | 42 | 50 | 36 | 29 | 32 |

## Hàm mở rộng E

| | | | | | |
|---|---|---|---|---|---|
| 32 | 1 | 2 | 3 | 4 | 5 |
| 4 | 5 | 6 | 7 | 8 | 9 |
| 8 | 9 | 10 | 11 | 12 | 13 |
| 12 | 13 | 14 | 15 | 16 | 17 |
| 16 | 17 | 18 | 19 | 20 | 21 |
| 20 | 21 | 22 | 23 | 24 | 25 |
| 24 | 25 | 26 | 27 | 28 | 29 |
| 28 | 29 | 30 | 31 | 32 | 1 |

## Phép hoán vị P

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 16 | 7 | 20 | 21 | 29 | 12 | 28 | 17 |
| 1 | 15 | 23 | 26 | 5 | 18 | 31 | 10 |
| 2 | 8 | 24 | 14 | 32 | 27 | 3 | 9 |
| 19 | 13 | 30 | 6 | 22 | 11 | 4 | 25 |

## Bảng hoán vị IP

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 58 | 50 | 42 | 34 | 26 | 18 | 10 | 2 |
| 60 | 52 | 44 | 36 | 28 | 20 | 12 | 4 |
| 62 | 54 | 46 | 38 | 30 | 22 | 14 | 6 |
| 64 | 56 | 48 | 40 | 32 | 24 | 16 | 8 |
| 57 | 49 | 41 | 33 | 25 | 17 | 9 | 1 |
| 59 | 51 | 43 | 35 | 27 | 19 | 11 | 3 |
| 61 | 53 | 45 | 37 | 29 | 21 | 13 | 5 |
| 63 | 55 | 47 | 39 | 31 | 23 | 15 | 7 |

## Bảng hoán vị $IP^{-1}$

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| 40 | 8 | 48 | 16 | 56 | 24 | 64 | 32 |
| 39 | 7 | 47 | 15 | 55 | 23 | 63 | 31 |
| 38 | 6 | 46 | 14 | 54 | 22 | 62 | 30 |
| 37 | 5 | 45 | 13 | 53 | 21 | 61 | 29 |
| 36 | 4 | 44 | 12 | 52 | 20 | 60 | 28 |
| 35 | 3 | 43 | 11 | 51 | 19 | 59 | 27 |
| 34 | 2 | 42 | 10 | 50 | 18 | 58 | 26 |
| 33 | 1 | 41 | 9 | 49 | 17 | 57 | 25 |

và các bảng S:

### $S_1$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 4 | 13 | 1 | 2 | 15 | 11 | 8 | 3 | 10 | 6 | 12 | 5 | 9 | 0 | 7 |
| 0 | 15 | 7 | 4 | 14 | 2 | 13 | 1 | 10 | 6 | 12 | 11 | 9 | 5 | 3 | 8 |
| 4 | 1 | 14 | 8 | 13 | 6 | 2 | 11 | 15 | 12 | 9 | 7 | 3 | 10 | 5 | 0 |
| 15 | 12 | 8 | 2 | 4 | 9 | 1 | 7 | 5 | 11 | 3 | 14 | 10 | 0 | 6 | 13 |

### $S_2$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 1 | 8 | 14 | 6 | 11 | 3 | 4 | 9 | 7 | 2 | 13 | 12 | 0 | 5 | 10 |
| 3 | 13 | 4 | 7 | 15 | 2 | 8 | 14 | 12 | 0 | 1 | 10 | 6 | 9 | 11 | 5 |
| 0 | 14 | 7 | 11 | 10 | 4 | 13 | 1 | 5 | 8 | 12 | 6 | 9 | 3 | 2 | 15 |
| 13 | 8 | 10 | 1 | 3 | 15 | 4 | 2 | 11 | 6 | 7 | 12 | 0 | 5 | 14 | 9 |

### $S_3$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | 0 | 9 | 14 | 6 | 3 | 15 | 5 | 1 | 13 | 12 | 7 | 11 | 4 | 2 | 8 |
| 13 | 7 | 0 | 9 | 3 | 4 | 6 | 10 | 2 | 8 | 5 | 14 | 12 | 11 | 15 | 1 |
| 13 | 6 | 4 | 9 | 8 | 15 | 3 | 0 | 11 | 1 | 2 | 12 | 5 | 10 | 14 | 7 |
| 1 | 10 | 13 | 0 | 6 | 9 | 8 | 7 | 4 | 15 | 14 | 3 | 11 | 5 | 2 | 12 |

### $S_4$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | 13 | 14 | 3 | 0 | 6 | 9 | 10 | 1 | 2 | 8 | 5 | 11 | 12 | 4 | 15 |
| 13 | 8 | 11 | 5 | 6 | 15 | 0 | 3 | 4 | 7 | 2 | 12 | 1 | 10 | 14 | 9 |
| 10 | 6 | 9 | 0 | 12 | 11 | 7 | 13 | 15 | 1 | 3 | 14 | 5 | 2 | 8 | 4 |
| 3 | 15 | 0 | 6 | 10 | 1 | 13 | 8 | 9 | 4 | 5 | 11 | 12 | 7 | 2 | 14 |

### $S_5$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 12 | 4 | 1 | 7 | 10 | 11 | 6 | 8 | 5 | 3 | 15 | 13 | 0 | 14 | 9 |
| 14 | 11 | 2 | 12 | 4 | 7 | 13 | 1 | 5 | 0 | 15 | 10 | 3 | 9 | 8 | 6 |
| 4 | 2 | 1 | 11 | 10 | 13 | 7 | 8 | 15 | 9 | 12 | 5 | 6 | 3 | 0 | 14 |
| 11 | 8 | 12 | 7 | 1 | 14 | 2 | 13 | 6 | 15 | 0 | 9 | 10 | 4 | 5 | 3 |

### $S_6$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 1 | 10 | 15 | 9 | 2 | 6 | 8 | 0 | 13 | 3 | 4 | 14 | 7 | 5 | 11 |
| 10 | 15 | 4 | 2 | 7 | 12 | 9 | 5 | 6 | 1 | 13 | 14 | 0 | 11 | 3 | 8 |
| 9 | 14 | 15 | 5 | 2 | 8 | 12 | 3 | 7 | 0 | 4 | 10 | 1 | 13 | 11 | 6 |
| 4 | 3 | 2 | 12 | 9 | 5 | 15 | 10 | 11 | 14 | 1 | 7 | 6 | 0 | 8 | 13 |

### $S_7$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 11 | 2 | 14 | 15 | 0 | 8 | 13 | 3 | 12 | 9 | 7 | 5 | 10 | 6 | 1 |
| 13 | 0 | 11 | 7 | 4 | 9 | 1 | 10 | 14 | 3 | 5 | 12 | 2 | 15 | 8 | 6 |
| 1 | 4 | 11 | 13 | 12 | 3 | 7 | 14 | 10 | 15 | 6 | 8 | 0 | 5 | 9 | 2 |
| 6 | 11 | 13 | 8 | 1 | 4 | 10 | 7 | 9 | 5 | 0 | 15 | 14 | 2 | 3 | 12 |

### $S_8$

| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 2 | 8 | 4 | 6 | 15 | 11 | 1 | 10 | 9 | 3 | 14 | 5 | 0 | 12 | 7 |
| 1 | 15 | 13 | 8 | 10 | 3 | 7 | 4 | 12 | 5 | 6 | 11 | 0 | 14 | 9 | 2 |
| 7 | 11 | 4 | 1 | 9 | 12 | 14 | 2 | 0 | 6 | 10 | 13 | 15 | 3 | 5 | 8 |
| 2 | 1 | 14 | 7 | 4 | 10 | 8 | 13 | 15 | 12 | 9 | 0 | 3 | 5 | 6 | 11 |

### Quy trình giải mã DES theo sơ đồ

Qui trình giải mã của DES tương tự như qui trình lập mã, nhưng dùng các khóa theo thứ tự ngược lại: $k_{16}, k_{15}, \dots, k_1$. Xuất phát (đầu vào) từ bản mã $y$, kết quả (đầu ra) là bản rõ $x$.

❖ **Ví dụ:**

$X = 0\ 1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9\ A\ B\ C\ D\ E\ F$

$\Rightarrow X = 0000\ 0001\ 0010\ 0011\ 0100\ 0101\ 0110\ 0111$
$1000\ 1001\ 1010\ 1011\ 1100\ 1101\ 1110\ 1111$

**Bước 1:** Bản rõ **x** được hoán vị theo phép hoán vị **IP**, thành **IP (x)** ta được:

$L_0 = 1100\ 1100\ 0000\ 0000\ 1100\ 1001\ 1111\ 1111$
$R_0 = 1111\ 0000\ 1010\ 1010\ 1111\ 0000\ 1010\ 1010$

**Bước 2**: Thực hiện 16 vòng mã hóa:
Lấy khóa K gốc: **K = 133457799BBCDFF1** (64 bit)
= 0001 0011 0011 0100 0101 0111 0111 1001 1001 1011 1011 1100 1101 1111 1111 0001

=> **$k_1$ = 000110 110000 001011 101111 111111 000111 000001 110010**

Mở rộng xâu **R0** (32 bit) thành xâu **E(R0)** (48 bit), theo hàm mở rộng **E**:

**E**: **R0** $\rightarrow$ **E(R0)**:

=> **E(R0)** = 011110 100001 010101 010101 011110 100001 010101 010101

=> **E(R0)** $\oplus$ **k1** = **B1 B2 B3 B4 B5 B6 B7 B8**
= 011000 010001 100010 110010 100001 100110 010100 100111

Tính $C_1 = S_1 (B_1)$, dùng bảng $S_1$.
$B_1 = b_1 b_2 b_3 b_4 b_5 b_6 = 011000$
$b_1 b_6 = (00)_2 = (00)_{10} =$ Hàng 0 trong $S_1$.
$b_2 b_3 b_4 b_5 = (1100)_2 = (12)_{10} =$ Cột 12 trong $S_1$.
$\Rightarrow C_1 = S_1 (0, 12) = (5)_{10} = (0101)_2$

Tương tự cho các $C_j \Rightarrow C = 0101\ 1100\ 1000\ 0010\ 1011\ 0101\ 1001\ 0111$

Hoán vị P được $P(C)$, đó chính là $f (R_0, k_1)$
$f (R_0, k_1) = P(C) = 0010\ 0011\ 0100\ 1010\ 1010\ 1001\ 1011\ 1011$

Lặp lại 16 lần như vậy rồi chuyển sang bước 3

**Bước 3**: Sử dụng hoán vị IP-1 => Kết quả là bản mã : 85E813540F0AB405

## 4.3.2 Hệ mã hóa RSA

### Giới thiệu
- Được phát triển bởi **R**ivest, **S**hamir và **A**dleman (1977).
- Là thuật toán mã khối, kích thước khối thay đổi được.
- Dựa trên cơ sở lý thuyết số, đặc biệt là phép toán modulo.

### Tạo cặp khóa (bí mật, công khai) (a, b)

- Chọn bí mật số nguyên tố lớn $p, q$, tính $n = p * q$, công khai $n$, đặt $P = C = Z_n$
- Tính bí mật $\phi(n) = (p-1)(q-1)$ Chọn khóa công khai $b < \phi(n)$, nguyên tố với $\phi(n)$
- Khóa bí mật $a$ là phần tử nghịch đảo của $b$ theo mod $\phi(n)$: $a * b \equiv 1 \pmod{\phi(n)}$
- Tập cặp khóa (bí mật, công khai) $K = \{(a, b) | a, b \in Z_n, a * b \equiv 1 \pmod{\phi(n)}\}$.

Với $x$ là bản rõ, $y$ là bản mã, ta có:

- **Hàm Mã hóa:** $y = e_k(x) = x^b \pmod n$

- **Hàm Giải mã:** $x = d_k(y) = y^a \pmod n$

Ví dụ: Cho bản rõ chữ x=RENAISSANCE

* **Tạo cặp khóa (bí mật, công khai) ) (a, b)**

- Chọn bí mật số nguyên tố lớn p=53, q=61
  => n = 3233, công khai n, đặt P = C = $Z_n$
- Tính bí mật $\phi(n) = (p-1)(q-1) = 3120$ Chọn khóa công khai b =71.
- Khóa bí mật a là phần tử nghịch đảo của b theo mod $\phi(n)$: a*b $\equiv$ 1 (mod $\phi(n)$) => a=791
- Quy ước chuyển ký tự thành số

| A | B | C | ...... | X | Y | Z | Dấu cách |
|---|---|---|---|---|---|---|---|
| 00 | 01 | 02 | ...... | 23 | 24 | 25 | 26 |

- **Bản rõ được thể hiện:**

| R | E | N | A | I | S | S | A | N | C | E | Dấu cách |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 17 | 04 | 13 | 00 | 08 | 18 | 18 | 00 | 13 | 02 | 04 | 26 |
| $m_1$ | $m_2$ | $m_3$ | $m_4$ | $m_5$ | $m_6$ | $m_7$ | $m_8$ | $m_9$ | $m_{10}$ | $m_{11}$ | $m_{12}$ |

Theo phép lập mã: $c_i = m_i^b \mod n = m_i^{71} \mod 3233$, ta nhận được:

**Bản mã số :**

| $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ | $C_6$ | ...... |
|---|---|---|---|---|---|---|
| 3106 | 0100 | 0931 | 2691 | 1984 | 2927 | ...... |

- Để nhận lại được bản rõ thì ta áp dụng giải mã:
$m_i = c_i^a \mod n = c_i^{791} \mod 3233$

## Độ an toàn của RSA

- Hệ mã hóa RSA là tất định, tức là với một bản rõ $x$ và một khóa bí mật $a$, thì chỉ có một bản mã $y$.
- Hệ mật RSA an toàn, khi giữ được bí mật khóa giải mã $a, p, q, \phi(n)$.

=> **Độ an toàn của Hệ mật RSA dựa vào khả năng giải bài toán phân tích số nguyên dương $n$ thành tích của 2 số nguyên tố lớn $p$ và $q$**

# 4.4. Đại diện tài liệu và hàm băm

## 4.4.1 Tổng quan về Hàm băm

- Khái niệm:

**Hàm băm** là thuật toán không dùng khóa để **mã hóa** (ở đây dùng thuật ngữ “băm” thay cho “mã hóa”), nó có nhiệm vụ “lọc” (băm) tài liệu (bản tin) và cho kết quả là một giá trị “băm” có kích thước cố định, còn gọi là **“đại diện tài liệu”** hay “đại diện bản tin”, “đại diện thông điệp”

### **Đặc tính của Hàm băm**:

- Với tài liệu đầu vào (bản tin gốc) $x$, chỉ thu được giá trị băm duy nhất $z = h(x)$
- Nếu dữ liệu trong bản tin $x$ bị thay đổi hay bị xóa để thành bản tin $x'$, thì giá trị băm $h(x') \neq h(x)$
- Nội dung của bản tin gốc “khó” thể suy ra từ giá trị hàm băm của nó

**Ứng dụng của hàm băm:**

- Giảm bộ nhớ lưu giữ chữ ký và thời gian truyền chữ ký trên mạng

- Hàm băm dùng để xác định tính toàn vẹn dữ liệu

- Hàm băm dùng để bảo mật một số dữ liệu đặc biệt, ví dụ bảo vệ mật khẩu, bảo vệ khóa mật mã, ...

❖ **Các tính chất của hàm băm**:

- Tính chất 1: Hàm băm $h$ là **không va chạm yếu**
- Tính chất 2: Hàm băm $h$ là **không va chạm mạnh**
- Tính chất 3: Hàm băm $h$ là **hàm một chiều**

* **Các hàm băm**:

- Các hàm băm dòng MD: MD2, MD4, MD5.
- Hàm băm an toàn SHA

## 4.4.2 Hàm băm MD4

- **Chuẩn bị các tham số:**
    - "**Thông điệp đệm**" (Messege Padding) là xâu bit có độ dài chia hết cho 512
    - "**Thông điệp đệm**" được lưu trong mảng $M = M[0] M[1] \dots M[N-1]$, với $N \equiv 0 \pmod{16}$.
    - $M$ được xây dựng từ **Bản tin gốc** $a$ bằng thuật toán:

1. $d = 447 - (|a| \pmod{512}) \quad (= 512 \text{ nếu } |a| \pmod{512} > 447)$
2. Giả sử $l$ là kí hiệu biểu diễn nhị phân của $|a| \pmod{2^{64}}$, $tl: |l| = 64$.
3. $M = a \parallel 1 \parallel 0^d \parallel l$

Trong đó

- Độ dài của xâu $a \parallel 1 \parallel 0^d$ qui ước là:
$|a| + 1 + d = 448 \pmod{512}$.

- Độ dài của “Thông điệp đệm” $M$ là
$448 \pmod{512} + |1| = 448 \pmod{512} + 64 = 512 \pmod{512}$.

Chú ý: Vì $M = a \parallel 1 \parallel 0^d \parallel 1$ nên
$d = |M| - (|a| + 1 + 1) =$
$512 - (|a| + 1 + 64) = 512 - (|a| + 65) = 447 - (|a| \pmod{512})$

### **Thuật toán băm MD4**:

- Bài toán:
    - Input: Thông điệp là một xâu $a$ có độ dài $b$ bit.
    - Output: Bản băm, đại diện cho thông điệp gốc, độ dài cố định 128 bit.

- Tư tưởng:
    - Bước 1: **Khởi tạo các thanh ghi** A,B,C,D.
    - Bước 2: Xử lý thông điệp $a$ trong 16 khối *word*, có nghĩa là xử lý cùng một lúc 16 *word* = 16 * 32 bit = 512 bit. Chia mảng M thành các khối 512 bit, đưa từng khối 512 bit vào mảng T[j]. Mỗi lần xử lý một khối 512 bit. Lặp lại N/16 lần.

- **Thuật toán:**

1/ $A := 67\ 45\ 23\ 01$ $\quad$ $B := ef\ cd\ ab\ 89$
$C := 98\ ba\ dc\ fe$ $\quad$ $D := 10\ 32\ 54\ 76$

2/ **FOR** $i := 0$ **TO** $N/16 - 1$ **DO**
**for** $j := 0$ **to** $15$ **do** $T[j] = M[16\ i + j];$
$AA := A; \quad BB := B;$
$CC := C; \quad DD := D;$
Mỗi lần xử lý 16 từ, mỗi từ 32 bit, tl: 512 bit.

3/**Vòng 1**
**Vòng 2**
**Vòng 3**

4/ $A = A + AA; \quad B = B + BB; \quad C = C + CC; \quad D = D + DD;$

Kết quả ra là đoạn mã có độ dài 128 bit, được thu gọn từ thông điệp a có độ dài b bit. Đoạn mã này thu được từ 4 thanh ghi A, B, C, D: bắt đầu từ byte thấp của thanh ghi A cho đến byte cao của thanh ghi D.

Trong đó: **Vòng 1**

| | |
| :--- | :--- |
| 1. $A = (A + F(B, C, D) + T[0]) <<< 3$ | 2. $D = (D + F(A, B, C) + T[1]) <<< 7$ |
| 3. $C = (C + F(D, A, B) + T[2]) <<< 11$ | 4. $B = (B + F(C, D, A) + T[3]) <<< 19$ |
| 5. $A = (A + F(B, C, D) + T[4]) <<< 3$ | 6. $D = (D + F(A, B, C) + T[5]) <<< 7$ |
| 7. $C = (C + F(D, A, B) + T[6]) <<< 11$ | 8. $B = (B + F(C, D, A) + T[7]) <<< 19$ |
| 9. $A = (A + F(B, C, D) + T[8]) <<< 3$ | 10. $D = (D + F(A, B, C) + T[9]) <<< 7$ |
| 11. $C = (C + F(D, A, B) + T[10]) <<< 11$ | 12. $B = (B + F(C, D, A) + T[11]) <<< 19$ |
| 13. $A = (A + F(B, C, D) + T[12]) <<< 3$ | 14. $D = (D + F(A, B, C) + T[13]) <<< 7$ |
| 15. $C = (C + F(D, A, B) + T[14]) <<< 11$ | 16. $B = (B + F(C, D, A) + T[15]) <<< 19$ |

## Vòng 2

1. $A = (A + G(B, C, D) + T[0] + 5A827999) <<< 3$
2. $D = (D + G(A, B, C) + T[4] + 5A827999) <<< 5$
3. $C = (C + G(D, A, B) + T[8] + 5A827999) <<< 9$
4. $B = (B + G(C, D, A) + T[12] + 5A827999) <<< 13$
5. $A = (A + G(B, C, D) + T[1] + 5A827999) <<< 3$
6. $D = (D + G(A, B, C) + T[5] + 5A827999) <<< 5$
7. $C = (C + G(D, A, B) + T[9] + 5A827999) <<< 9$
8. $B = (B + G(C, D, A) + T[13] + 5A827999) <<< 13$
9. $A = (A + G(B, C, D) + T[2] + 5A827999) <<< 3$
10. $D = (D + G(A, B, C) + T[6] + 5A827999) <<< 5$
11. $C = (C + G(D, A, B) + T[10] + 5A827999) <<< 9$
12. $B = (B + G(C, D, A) + T[14] + 5A827999) <<< 13$
13. $A = (A + G(B, C, D) + T[3] + 5A827999) <<< 3$
14. $D = (D + G(A, B, C) + T[7] + 5A827999) <<< 5$
15. $C = (C + G(D, A, B) + T[11] + 5A827999) <<< 9$
16. $B = (B + G(C, D, A) + T[15] + 5A827999) <<< 13$

**Vòng 3**

1. $A = (A + H(B, C, D) + T[0] + 6ED9EBA1) <<< 3$
2. $D = (D + H(A, B, C) + T[8] + 6ED9EBA1) <<< 9$
3. $C = (C + H(D, A, B) + T[4] + 6ED9EBA1) <<< 11$
4. $B = (B + H(C, D, A) + T[12] + 6ED9EBA1) <<< 15$
5. $A = (A + H(B, C, D) + T[2] + 6ED9EBA1) <<< 3$
6. $D = (D + H(A, B, C) + T[10] + 6ED9EBA1) <<< 9$
7. $C = (C + H(D, A, B) + T[6] + 6ED9EBA1) <<< 11$
8. $B = (B + H(C, D, A) + T[14] + 6ED9EBA1) <<< 15$
9. $A = (A + H(B, C, D) + T[1] + 6ED9EBA1) <<< 3$
10. $D = (D + H(A, B, C) + T[9] + 6ED9EBA1) <<< 9$
11. $C = (C + H(D, A, B) + T[5] + 6ED9EBA1) <<< 11$
12. $B = (B + H(C, D, A) + T[13] + 6ED9EBA1) <<< 15$
13. $A = (A + H(B, C, D) + T[3] + 6ED9EBA1) <<< 3$
14. $D = (D + H(A, B, C) + T[11] + 6ED9EBA1) <<< 9$
15. $C = (C + H(D, A, B) + T[7] + 6ED9EBA1) <<< 11$
16. $B = (B + H(C, D, A) + T[15] + 6ED9EBA1) <<< 15$

## Khái niệm

- Là một định danh điện tử được tạo ra bởi máy tính được các tổ chức sử dụng nhằm đạt được tính hiệu quả và có hiệu lực như là các chữ ký tay.
- Là một cơ chế xác thực hóa cho phép người tạo ra thông điệp đính kèm một mã số vào thông điệp giống như là việc ký một chữ ký lên một văn bản bình thường.
- "**Ký số**" trên "**tài liệu số**" là "**ký**" trên từng bit tài liệu. Đó chính là "**bản mã**" của xâu bit tài liệu.

### Sơ đồ chữ ký (P,A,K,S,V)

- **P** là tập hữu hạn các văn bản có thể.
- **A** là tập hữu hạn các chữ ký có thể.
- **K** là tập hữu hạn các khoá có thể.
- **S** là tập các thuật toán ký.
- **V** là tập các thuật toán kiểm thử.

Với mỗi khóa $k \in K$: có thuật toán ký $Sig_k \in S$, $Sig_k: P \to A$, có thuật toán kiểm tra chữ ký $Ver_k \in V$, $Ver_k: P \times A \to \{đúng, sai\}$ thoả mãn điều kiện sau với mọi $x \in P, y \in A$:

$$Ver_k(x, y) = \begin{cases} \text{Đúng, nếu } y = Sig_k(x) \\ \text{Sai, nếu } y \neq Sig_k(x) \end{cases}$$

## Phân loại chữ ký theo đặc trưng kiểm tra chữ ký

- Chữ ký khôi phục thông điệp: Là loại chữ ký, trong đó người gửi chỉ cần gửi “**chữ ký**”, người nhận có thể khôi phục lại được thông điệp, đã được “**ký**” bởi “**chữ ký**” này.

- Chữ ký đi kèm thông điệp: Là loại chữ ký, trong đó người gửi gửi “**chữ ký**”, phải gửi kèm cả thông điệp đã được “**ký**” bởi “**chữ ký**” này. Ngược lại, người nhận sẽ không có được thông điệp gốc.

### Phân loại chữ ký theo mức an toàn

- Chữ ký “không thể phủ nhận” (Chaum - van Antverpen)
- Chữ ký “một lần”

### Phân loại chữ ký theo ứng dụng đặc trưng

- Chữ ký “mù” (Blind Signature)
- Chữ ký “nhóm” (Group Signature)
- Chữ ký “bội” (Multy Signature)
- Chữ ký “mù nhóm” (Blind Group Signature)
- Chữ ký “mù bội” (Blind Multy Signature)

## 4.5.1 Chữ ký RSA

### Tạo cặp khóa

- Chọn bí mật số nguyên tố lớn $p, q$, tính $n = p * q$, công khai $n$, đặt $P = C = Z_n$
- Tính bí mật $\phi(n) = (p-1)(q-1)$ Chọn khóa công khai $b < \phi(n)$, nguyên tố với $\phi(n)$
- Khóa bí mật $a$ là phần tử nghịch đảo của $b$ theo mod $\phi(n)$: $a*b \equiv 1 \pmod{\phi(n)}$
- Tập cặp khóa (bí mật, công khai) $K = \{(a, b) / a, b \in Z_n, a*b \equiv 1 \pmod{\phi(n)}\}$.

- **Ký số: Chữ ký trên x là:**
$$y = \text{Sig}_k(x) = x^a \pmod n, \quad y \in A$$

- **Kiểm tra chữ ký:**
$$\text{Ver}_k(x, y) = \text{đúng} \iff x \equiv y^b \pmod n$$

## Ví dụ: Chữ ký trên x=2

### Tạo cặp khóa (bí mật, công khai) (a, b)

- Chọn bí mật số nguyên tố lớn $p=3, q=5$
  => $n = 15$, công khai $n$, đặt $P = C = Z_n$
- Tính bí mật $\phi(n) = (p-1)(q-1) = 8$ Chọn khóa công khai $b = 3$.
- Khóa bí mật $a$ là phần tử nghịch đảo của $b$ theo mod $\phi(n)$: $a*b \equiv 1 \pmod{\phi(n)} \Rightarrow a=3$

- **Chữ ký trên x=2 là:**
$y = \text{Sig}_k(x) = x^a \pmod n = 2^3 \pmod{15} = 8, \quad y \in A$

- **Kiểm tra chữ ký:**
$\text{Ver}_k(x, y) = \text{đúng} \iff x \equiv y^b \pmod n$
$\iff 2 \equiv 8^b \pmod{15}$
$\iff 2 \equiv 8^3 \pmod{15}$

## Độ an toàn

- **Các cách gửi chữ ký:**
    - **TH1: Ký trước, Mã hóa sau**
        - G ký trước vào $x$ bằng chữ ký $y = \text{Sig}_G(x)$
        - Mã hoá $x$ và $y$ nhận được $z = e_G(x, y)$
        - G gửi $z$ cho N
        - Nhận được $z$, N giải mã $z$ để được $x, y$
        - Kiểm tra chữ ký $\text{Ver}_N(x, y) = \text{true}$ ?

- **TH2: Mã hóa trước, Ký sau**

Mã hoá trước $x$ bằng $u = e_G(x)$

Ký vào $u$ bằng chữ ký $v = Sig_G(u)$

$G$ gửi $(u, v)$ cho $N$.

Nhận được $(u, v)$, $N$ giải mã $u$ được $x$.

Kiểm tra chữ ký $Ver_N(u, v) = \text{true}$ ?

❖ **H lấy trộm được thông tin trên đường truyền :**

- TH1: H có được $z$, để giả mạo chữ ký $y$ thì phải giải mã được $z$
- TH2: H có được $(u,v)$, để giả mạo chữ ký $v$ thì H đã có sẵn và thay đổi $v$ thành $v'=Sig_H(u)$ rồi gửi $(u,v')$ cho N

=> TH2 thì H có thể giả mạo chữ ký mà không cần giải mã

❖ **Kết luận: Ký trước rồi mã hóa cả chữ ký**

## 4.5.2 Chữ ký Elgamal

### Tạo cặp khóa:

- Chọn số nguyên tố $p$ sao cho bài toán logarit rời rạc trong $Z_p$ là “khó” giải
- Chọn phần tử nguyên thuỷ $g \in Z_p^*$. Đặt $P = Z_p^*$, $A = Z_p^* \times Z_{p-1}$.
- Chọn khóa bí mật là $a \in Z_p^*$
- Tính khóa công khai $h \equiv g^a \pmod p$
- Tập khóa $K = \{p, g, a, h\}$, với $p, g, h$ công khai; $a$ bí mật

- **Ký số:** Dùng khóa $a$ và khóa ngẫu nhiên bí mật $r \in Z_{p-1}^* \Rightarrow$ Chữ ký trên $x \in P$ là:
  $$y = \text{Sig}_k (x, r) = (\gamma, \delta), y \in A$$
  $$\gamma = g^r \pmod p$$
  $$\delta = (x - a * \gamma) * r^{-1} \pmod{p - 1}$$

- **Kiểm tra chữ ký:**
  $$\text{Ver}_k (x, \gamma, \delta) = \text{đúng} \iff h^\gamma * \gamma^\delta \equiv g^x \pmod p$$

Nếu chữ ký được tính đúng thì kiểm tra sẽ thành công.

*Ví dụ: Chữ ký Elgamal trên dữ liệu $x = 112$*

❖ **Tạo cặp khóa (bí mật, công khai) ) (a, h)**

- Chọn số nguyên tố $p=463$,
  Đặt $P = Z_p^*$, $A = Z_p^* \times Z_{p-1}$
- Chọn phần tử nguyên thuỷ $g = 2 \in Z_p^*$.
- Chọn khóa bí mật $a = 211 \in Z_p^*$.
- Tính khóa công khai
  $h = g^a \mod p = 2^{211} \mod 463 = 249$
- Chọn ngẫu nhiên $r = 235 \in Z_{p-1}^*$.

- **Chữ ký trên dữ liệu x = 112 là $(\gamma, \delta) = (16, 108)$ với**
  $$\gamma = g^r \mod p = 2^{235} \mod 463 = 16$$
  $$\delta = (x - a * \gamma) * r^{-1} \mod (p - 1) =$$
  $$(112 - 211 * 16) * 289 \mod 462 = 108$$

- **Kiểm tra chữ ký:**
  $$\text{Ver}_k (x, \gamma, \delta) = \text{đúng} \iff h^\gamma * \gamma^\delta \equiv g^x \mod p$$
  $$h^\gamma * \gamma^\delta = 249^{16} * 16^{108} \mod 463 = 132$$
  $$g^x \mod p = 2^{112} \mod 463 = 132$$

**= > chữ ký là đúng**

## Độ an toàn
- **Vấn đề giả mạo chữ ký Elgamal :**
    - **TH1:** **Giả mạo chữ ký không cùng với tài liệu được ký.** H cố gắng giả mạo chữ ký trên $x$, mà không biết khóa bí mật $a$. H phải tính được $\gamma$ và $\delta$.
        - Nếu chọn trước $\gamma$, H phải tính $\delta$ theo:
            $$h^\gamma * \gamma^\delta \equiv g^x \pmod p$$
            $$\gamma^\delta \equiv g^x h^{-\gamma} \pmod p$$
            $$\Leftrightarrow \delta \equiv \log_\gamma g^x h^{-\gamma} \pmod p$$

- Nếu chọn trước $\delta$, H phải tính $\gamma$ theo

$$h^\gamma * \gamma^\delta \equiv g^x \pmod p$$

Hiện nay chưa có cách hữu hiệu 2 trường hợp trên. Phỏng đoán là khó hơn bài toán logarit rời rạc

## 4.5. Chữ ký số

- **TH2: Giả mạo chữ ký cùng với tài liệu được ký.** H có thể ký trên tài liệu ngẫu nhiên bằng cách chọn trước đồng thời $x, \gamma, \delta$.

Với TH này có 2 cách giả mạo, tuy nhiên không phải tài liệu nào mà người giả mạo cũng được chấp nhận => trong thực tế ít người sử dụng

### Vấn đề Phá khóa theo sơ đồ Elgamal:

Khoá bí mật $a$ có thể bị phát hiện, nếu khóa ngẫu nhiên $r$ bị lộ, hoặc dùng $r$ cho hai lần ký khác nhau.

## 4.5.3 Chữ ký DSS

### Giới thiệu:

- Chuẩn chữ ký số (DSS: Digital Signature Standard) được đề xuất năm 1991
- Là cải biên của sơ đồ chữ ký ElGamal.
- Độ dài chữ ký theo sơ đồ ElGamal là gấp đôi số bit của $p$. Trong khi ứng dụng dùng thẻ thông minh (Smart card) lại mong muốn có chữ ký ngắn

## Sơ đồ Chuẩn chữ ký số DSS:

- **Tạo cặp khóa (bí mật, công khai) (a, h)**
    - Chọn số nguyên tố $p$ sao cho bài toán logarit rời rạc trong $Z_p$ là “khó” giải
    - Chọn $q$ là ước nguyên tố của $p-1$. Tức là $p-1 = t * q$ hay $p = t * q + 1$
    - Chọn $g \in Z_p^*$ là căn bậc $q$ của $1 \pmod p$, ($g$ là phần tử sinh của $Z_p^*$). Tính $\alpha = g^t$, chọn khóa bí mật $a \in Z_p^*$, tính khóa công khai:
      $$h \equiv \alpha^a \pmod p$$
    - Tập khóa $K = \{p, q, \alpha, a, h\}$, với $p, g, h$ công khai; $a$ bí mật

- **Ký số**: Dùng khóa $a$ và khóa ngẫu nhiên bí mật $r \in Z_q^*$ => Chữ ký trên $x \in P$ là:
$y = \text{Sig}_k (x, r) = (\gamma, \delta), y \in A$
$\gamma = (\alpha^r \mod p) \mod q$
$\delta = ((x + a * \gamma) * r^{-1} \mod q)$

- **Kiểm tra chữ ký**: Với
$e_1 = x * \delta^{-1} \mod q, e_2 = \gamma * \delta^{-1} \mod q$
thì
$\text{Ver}_{k'} (x, \gamma, \delta) = \text{đúng} \iff (\alpha^{e_1} * h^{e_2} \mod p) \mod q = \gamma$

*Ví dụ : Chữ ký DSS trên dữ liệu x = 1246*

- **Tạo cặp khóa (bí mật, công khai) ) (a, h)**
    - Chọn số nguyên tố p=7649, q=239 là ước nguyên tố của p-1 => t=32
    - Chọn phần tử nguyên thuỷ g = 3 $\in$ Zₚ* là phần tử sinh
        $\alpha = g^t \mod p = 3^{32} \mod 7649 = 7098$.
    - Chọn khóa mật a = 85, khóa công khai h là:
        $h = \alpha^a \mod p = 7098^{85} \mod 7649 = 5387$

### Ký số

- Dùng 2 khóa ký: **a** và khóa ngẫu nhiên $r = 58 \in Z_q^*$
  => $r^{-1} \mod q = 136$.

- Chữ ký trên $x = 1246$ là **Sig k’ (x, r) = (γ, δ) = (115, 87)**
  $\gamma = (\alpha^r \mod p) \mod q$
  $= (7098^{58} \mod 7649) \mod 239$
  $= 593 \mod 239 = 115$.

  $\delta = (x + a * \gamma) * r^{-1} \mod q$
  $= (1246 + 85 * 115) * 136 \mod 239 = 87$

### Kiểm tra chữ ký số

$e_1 = x * \delta^{-1} \mod q = 1246 * 11 \mod q = 83$

$e_2 = \gamma * \delta^{-1} \mod q = 115 * 11 \mod q = 70$

$=> (\alpha^{e_1} * h^{e_2} \mod p) \mod q$

$= (7098^{83} * 5387^{70} \mod 7649) \mod 239$

$= 593 \mod 239 = 115 = \gamma$

$=> \text{Ver}_{K'} (x, \gamma, \delta) = \text{đúng}$

**=> chữ ký là đúng**

### Nhận xét:

- $\delta \neq 0 \pmod q$ để bảo đảm có $\delta^{-1} \pmod q$ trong điều kiện kiểm thử.
- Thay vì tính $p$ trước rồi mới tính $q$, ta sẽ tính $q$ trước rồi tìm $p$.
- Nếu dùng chữ ký RSA với thành phần kiểm thử chữ ký là nhỏ, thì việc kiểm thử nhanh hơn việc ký. Đối với DSS, ngược lại, việc ký nhanh hơn kiểm thử.
- Một tài liệu chỉ được ký một lần, nhưng nó lại được kiểm thử nhiều lần, nên người ta muốn thuật toán kiểm thử nhanh hơn.

## 4.5.4 Chữ ký không thể phủ định
### 4.5.4.1. Giới thiệu

- Trong các sơ đồ trước, việc kiểm thử tính đúng đắn của chữ ký là do người nhận thực hiện.

- Nhằm tránh việc nhân bản chữ ký để sử dụng nhiều lần, tốt nhất là để người gửi tham gia trực tiếp vào việc kiểm thử chữ ký. Điều đó được thực hiện bằng một giao thức kiểm thử, dưới dạng một giao thức mời hỏi và trả lời.

### Vấn đề :
Giả sử tài liệu cùng chữ ký từ G gửi đến N. Khi N yêu cầu G cùng kiểm thử chữ ký, thì một vấn đề nảy sinh là làm sao để ngăn cản G chối bỏ một chữ ký mà anh ta đã ký, G có thể tuyên bố rằng chữ ký đó là giả mạo ?

### Giải quyết :
Cần có thêm giao thức chối bỏ, bằng giao thức này, G có thể chứng minh một chữ ký là giả mạo. Nếu G từ chối tham gia vào giao thức đó, thì có thể xem rằng G không chứng minh được chữ ký đó là giả mạo.

## 4.5.4.2 Sơ đồ chữ ký không thể phủ định (Chaum - van Antverpen)

### Tạo các tham số

- Chọn số nguyên tố $p$ sao cho bài toán logarit rời rạc trong $Z_p$ là “khó” giải. Nên chọn $p = 2 * q + 1$ với $q$ cũng là số nguyên tố.
- Gọi $P'$ là nhóm nhân con của $Z_p^*$ theo $q$. Chọn phần tử sinh $g$ của nhóm $P'$ cấp $q$. Tính:
  $$h \equiv g^a \pmod p$$
- Đặt $P = A = P'$
- $K = \{(p, g, a, h): a \in Z_q^*\}$

- **Thuật toán ký:** Dùng khoá bí mật $k' = a$ để ký lên $x$
=> **Chữ ký là:**
$$y = \text{Sig}_{k'} (x) = x^a \pmod p$$

- **Giao thức kiểm thử:** Dùng khoá công khai $k'' = (p, g, h)$. Với $x, y \in P$, người nhận $N$ cùng người gửi $G$ thực hiện giao thức kiểm thử
    1/ $N$ chọn ngẫu nhiên $e_1, e_2 \in Z_q^*$
    2/ $N$ tính $c = y^{e_1} h^{e_2} \pmod p$, và gửi cho $G$.
    3/ $G$ tính $d = c^{a^{-1} \pmod q} \pmod p$ và gửi cho $N$
    4/ $N$ chấp nhận $y$ là chữ ký đúng, nếu $d \equiv x^{e_1} g^{e_2} \pmod p$

### Giao thức chối bỏ

1/ N chọn ngẫu nhiên $e_1, e_2 \in Z_q^*$
2/ N tính $c = y^{e_1} h^{e_2} \pmod p$, và gửi cho G
3/ G tính $d = c^{a^{-1} \pmod q} \pmod p$ và gửi cho N
4/ N thử điều kiện $d \neq x^{e_1} g^{e_2} \pmod p$
5/ N chọn ngẫu nhiên $f_1, f_2 \in Z_q^*$
6/ N tính $C = y^{f_1} * \beta^{f_2} \pmod p$ và gửi cho G
7/ G tính $D = C^{a^{-1} \pmod q} \pmod p$ và gửi cho N
8/ N thử điều kiện $D \neq x^{f_1} g^{f_2} \pmod p$
9/ N kết luận $y$ là chữ ký **giả mạo** nếu:
$(d * \alpha^{-e_2})^{f_1} \equiv (D * \alpha^{-f_2})^{e_1} \pmod p$ (với $\alpha$ bằng $g$)

**Ví dụ: Ký trên $x = 229$**

* **Chuẩn bị các tham số**

- Chọn số nguyên tố $p = 467 = 2 * q + 1, q = 233$ cũng là số nguyên tố
- Chọn phần tử sinh của nhóm $P'$ là $g = 4$
- Chọn khóa mật $a = 121 \Rightarrow$ Khóa công khai:
  $h \equiv g^a \pmod p = 4^{121} \pmod{467} = 422$
- Đặt $P = A = P'$
- $K = \{(p, g, a, h): a \in Z_q^*\}$

## 4.5. Chữ ký số

- **Thuật toán ký:** Dùng khoá bí mật $k' = a$ để ký lên $x = 229$ => Chữ ký là:

$$y = \text{Sig}_{k'} (x) = x^a \pmod p$$
$$= 229^{121} \pmod{467} = 9$$

- **Giao thức kiểm thử:** Dùng khoá công khai $k = (p, g, h) = (467, 4, 422)$

1/ N chọn ngẫu nhiên $e_1 = 48, e_2 = 213 \in Z_q^*$

2/ N tính $c = y^{e_1} h^{e_2} \pmod p = 116$ và gửi cho G.

3/ G tính $d = c^{a^{-1} \pmod q} \pmod p = 235$ và gửi cho N.

4/ N chấp nhận $y$ là chữ ký đúng, nếu $d \equiv x^{e_1} g^{e_2} \pmod p$

N thử điều kiện $d \equiv x^{e_1} g^{e_2} \pmod p$.

Rõ ràng $235 \equiv 229^{48} * 4^{213} \pmod{467}$

N chấp nhận $y = 9$ đúng là chữ ký của G trên $x = 229$

- **Giao thức chối bỏ:** Giả sử G gửi tài liệu $x = 226$ với chữ ký $y = 183$. Giao thức chối bỏ thực hiện:

1/ N chọn ngẫu nhiên $e_1 = 47, e_2 = 137 \in Z_q^*$

2/ N tính $c = y^{e_1} h^{e_2} \pmod p = 306$, và gửi cho G.

3/ G tính $d = c^{a^{-1} \pmod q} \pmod p = 184$, và gửi cho N

4/ N thử điều kiện $d \neq x^{e_1} g^{e_2} \pmod p$
$184 \neq 226^{47} * 4^{137} \equiv 145 \pmod{467}$

5/ N chọn ngẫu nhiên $f_1 = 225, f_2 = 19 \in Z_q^*$

6/ N tính $C = y^{f_1} * \beta^{f_2} \pmod p = 348$, và gửi cho G

7/ G tính $D = C^{a^{-1} \pmod q} \pmod p = 426$, và gửi cho N

8/ N thử điều kiện $D \equiv x^{f1} g^{f2} \pmod p$
$x^{f1} g^{f2} \pmod p = 226^{225} * 4^{19} \equiv 295 \pmod{467}$
Điều kiện 8 là đúng, nên N thực hiện bước 9

9/ N kết luận y là chữ ký **giả mạo** nếu:
$(d * \alpha^{-e2})^{f1} \equiv (D * \alpha^{-f2})^{e1} \pmod p$ (với $\alpha$ bằng $g$)

$(d * \alpha^{-e2})^{f1} \equiv (184 * 4^{-137})^{225} \equiv 79 \pmod{467}$
$(D * \alpha^{-f2})^{e1} \equiv (426 * 4^{-19})^{47} \equiv 79 \pmod{467}$

Hai giá trị đó bằng nhau. Kết luận chữ ký y là **giả mạo**

# Thank You !
