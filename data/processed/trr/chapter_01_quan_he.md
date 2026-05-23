# Chương 1: Quan hệ

## Nội dung chính
- Định nghĩa quan hệ hai ngôi, quan hệ từ tập $A$ đến tập $B$ và quan hệ trên một tập.
- Các tính chất của quan hệ: phản xạ, đối xứng, phản xứng, bắc cầu.
- Biểu diễn quan hệ bằng ma trận.
- Nhận biết tính chất quan hệ qua ma trận.
- Quan hệ tương đương, lớp tương đương và phân hoạch.
- Đồng dư modulo $m$.
- Quan hệ thứ tự.

## Tổng quan
Quan hệ là công cụ mô tả sự liên hệ giữa các phần tử của một hoặc nhiều tập hợp. Trong toán rời rạc, quan hệ thường được xét dưới dạng tập con của tích Descartes, có thể biểu diễn bằng liệt kê cặp, ma trận hoặc đồ thị có hướng.

## Quan hệ hai ngôi

### Định nghĩa
Cho hai tập $A$ và $B$. Một quan hệ hai ngôi từ $A$ đến $B$ là một tập con của tích Descartes $A \times B$.

$$
R \subseteq A \times B
$$

Nếu $(a,b) \in R$, ta nói $a$ có quan hệ $R$ với $b$, ký hiệu $aRb$.

### Quan hệ trên một tập
Nếu $A = B$, quan hệ $R \subseteq A \times A$ được gọi là quan hệ trên tập $A$.

**Ví dụ:** Quan hệ “$a$ là ước của $b$” trên tập số nguyên dương:

$$
aRb \Leftrightarrow a \mid b
$$

## Các tính chất của quan hệ

### Phản xạ

**Khái niệm chính:**
- Quan hệ $R$ trên $A$ có tính phản xạ nếu mọi phần tử đều có quan hệ với chính nó.

**Công thức / Định lý:**

$$
\forall a \in A,\ (a,a) \in R
$$

**Ví dụ:** Quan hệ chia hết trên tập số nguyên dương có tính phản xạ vì $a \mid a$ với mọi $a$.

### Đối xứng

**Khái niệm chính:**
- Quan hệ $R$ có tính đối xứng nếu khi $a$ liên hệ với $b$ thì $b$ cũng liên hệ với $a$.

**Công thức / Định lý:**

$$
\forall a,b \in A,\ (a,b) \in R \Rightarrow (b,a) \in R
$$

### Phản xứng

**Khái niệm chính:**
- Quan hệ $R$ có tính phản xứng nếu hai phần tử khác nhau không thể đồng thời liên hệ hai chiều.

**Công thức / Định lý:**

$$
\forall a,b \in A,\ ((a,b) \in R \land (b,a) \in R) \Rightarrow a=b
$$

**Ví dụ:** Quan hệ “$\le$” trên tập số có tính phản xứng.

### Bắc cầu

**Khái niệm chính:**
- Quan hệ $R$ có tính bắc cầu nếu từ $aRb$ và $bRc$ suy ra $aRc$.

**Công thức / Định lý:**

$$
\forall a,b,c \in A,\ ((a,b) \in R \land (b,c) \in R) \Rightarrow (a,c) \in R
$$

## Biểu diễn quan hệ bằng ma trận

### Ma trận quan hệ từ $A$ đến $B$
Cho $A=\{a_1,a_2,\ldots,a_m\}$ và $B=\{b_1,b_2,\ldots,b_n\}$. Ma trận biểu diễn quan hệ $R$ từ $A$ đến $B$ là ma trận $M_R = (m_{ij})$ kích thước $m \times n$, trong đó:

$$
m_{ij} =
\begin{cases}
1, & \text{nếu } (a_i,b_j) \in R \\ 0, & \text{nếu } (a_i,b_j) \notin R
\end{cases}
$$

### Ma trận quan hệ trên một tập
Nếu $R$ là quan hệ trên $A$, ma trận $M_R$ là ma trận vuông.

| Tính chất | Dấu hiệu trên ma trận |
|---|---|
| Phản xạ | Mọi phần tử trên đường chéo chính bằng 1 |
| Đối xứng | Ma trận đối xứng qua đường chéo chính: $m_{ij}=m_{ji}$ |
| Phản xứng | Với $i \ne j$, không đồng thời có $m_{ij}=1$ và $m_{ji}=1$ |

## Quan hệ tương đương

### Định nghĩa
Quan hệ $R$ trên tập $A$ là quan hệ tương đương nếu $R$ có đủ ba tính chất:

- Phản xạ.
- Đối xứng.
- Bắc cầu.

### Lớp tương đương
Với $a \in A$, lớp tương đương của $a$ theo quan hệ $R$ là tập các phần tử có quan hệ với $a$.

$$
[a] = \{x \in A \mid xRa\}
$$

### Đồng dư modulo $m$
Quan hệ đồng dư modulo $m$ trên tập số nguyên được định nghĩa:

$$
a \equiv b \pmod m \Leftrightarrow m \mid (a-b)
$$

Quan hệ này là quan hệ tương đương.

## Phân hoạch

Một phân hoạch của tập $A$ là một họ các tập con không rỗng, đôi một rời nhau và hợp của chúng bằng $A$.

Các lớp tương đương của một quan hệ tương đương tạo thành một phân hoạch của tập hợp.

## Quan hệ thứ tự

### Định nghĩa
Quan hệ $R$ trên $A$ là quan hệ thứ tự nếu có các tính chất:

- Phản xạ.
- Phản xứng.
- Bắc cầu.

Nếu mọi cặp phần tử trong $A$ đều so sánh được với nhau, đó là quan hệ thứ tự toàn phần. Nếu không, đó là quan hệ thứ tự bộ phận.

## Tóm tắt chương
- Quan hệ hai ngôi từ $A$ đến $B$ là tập con của $A \times B$.
- Quan hệ trên $A$ là tập con của $A \times A$.
- Các tính chất quan trọng gồm phản xạ, đối xứng, phản xứng và bắc cầu.
- Ma trận là cách biểu diễn quan hệ rõ ràng và thuận tiện để nhận biết tính chất.
- Quan hệ tương đương tạo ra các lớp tương đương và phân hoạch tập hợp.
- Quan hệ thứ tự có phản xạ, phản xứng và bắc cầu.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Quan hệ hai ngôi | Tập con của tích Descartes |
| Phản xạ | Mọi phần tử liên hệ với chính nó |
| Đối xứng | Nếu $aRb$ thì $bRa$ |
| Phản xứng | Nếu $aRb$ và $bRa$ thì $a=b$ |
| Bắc cầu | Nếu $aRb$ và $bRc$ thì $aRc$ |
| Quan hệ tương đương | Quan hệ phản xạ, đối xứng, bắc cầu |
| Lớp tương đương | Tập các phần tử tương đương với một phần tử |
| Quan hệ thứ tự | Quan hệ phản xạ, phản xứng, bắc cầu |

## Công thức cần nhớ
- $R \subseteq A \times B$
- $\forall a \in A,\ (a,a) \in R$
- $(a,b) \in R \Rightarrow (b,a) \in R$
- $((a,b)\in R \land (b,a)\in R) \Rightarrow a=b$
- $((a,b)\in R \land (b,c)\in R) \Rightarrow (a,c)\in R$
- $a \equiv b \pmod m \Leftrightarrow m \mid (a-b)$

## Câu hỏi ôn tập
1. Quan hệ hai ngôi từ $A$ đến $B$ được định nghĩa như thế nào?
2. Quan hệ trên một tập khác gì quan hệ từ $A$ đến $B$?
3. Nêu điều kiện để một quan hệ có tính phản xạ.
4. Phân biệt đối xứng và phản xứng.
5. Làm thế nào nhận biết quan hệ phản xạ bằng ma trận?
6. Quan hệ tương đương cần những tính chất nào?
7. Lớp tương đương là gì?
8. Quan hệ đồng dư modulo $m$ được định nghĩa như thế nào?
