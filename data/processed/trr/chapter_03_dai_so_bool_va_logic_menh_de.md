# Chương 3: Đại số Bool và logic mệnh đề

## Nội dung chính
- Mệnh đề logic, mệnh đề toán học và mệnh đề chứa biến.
- Lượng từ $\forall$ và $\exists$.
- Mệnh đề sơ cấp, mệnh đề phức hợp và bảng chân trị.
- Các phép toán logic: phủ định, hội, tuyển, kéo theo, tương đương.
- Công thức logic, hằng đúng, hằng sai, công thức thực hiện được.
- Luật đối ngẫu, luật thay thế, dạng chuẩn tắc tuyển và hội.
- Các quy tắc suy diễn.
- Đại số Bool, hàm Bool, bảng chân trị và mạch logic.

## Tổng quan
Logic mệnh đề cung cấp ngôn ngữ hình thức để biểu diễn và suy luận về các phát biểu đúng sai. Đại số Bool mở rộng các phép toán logic thành một cấu trúc đại số, có ứng dụng quan trọng trong thiết kế mạch logic và xử lý điều kiện trong máy tính.

## Mệnh đề logic

### Khái niệm chính
Mệnh đề là một câu khẳng định có giá trị chân trị xác định: đúng hoặc sai.

Mệnh đề toán học là mệnh đề diễn đạt nội dung toán học. Mệnh đề chứa biến là câu có biến, chưa xác định đúng sai cho đến khi gán giá trị cho biến.

### Lượng từ
Hai lượng từ thường dùng:

- Với mọi: $\forall$
- Tồn tại: $\exists$

**Ví dụ:**

$$
\forall x \in \mathbb{R},\ x^2 \ge 0
$$

$$
\exists x \in \mathbb{Z},\ x^2 = 4
$$

## Mệnh đề sơ cấp và phức hợp

- Mệnh đề sơ cấp là mệnh đề không được tạo từ các mệnh đề khác bằng phép toán logic.
- Mệnh đề phức hợp được tạo từ các mệnh đề sơ cấp bằng các phép toán logic.

## Các phép toán mệnh đề

### Phủ định
Phủ định của $p$ ký hiệu $\neg p$.

| $p$ | $\neg p$ |
|---|---|
| Đúng | Sai |
| Sai | Đúng |

### Hội
Hội của $p$ và $q$ ký hiệu $p \land q$, đúng khi cả $p$ và $q$ đều đúng.

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| Đúng | Đúng | Đúng |
| Đúng | Sai | Sai |
| Sai | Đúng | Sai |
| Sai | Sai | Sai |

### Tuyển
Tuyển của $p$ và $q$ ký hiệu $p \lor q$, đúng khi ít nhất một trong hai mệnh đề đúng.

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| Đúng | Đúng | Đúng |
| Đúng | Sai | Đúng |
| Sai | Đúng | Đúng |
| Sai | Sai | Sai |

### Kéo theo
Mệnh đề kéo theo $p \to q$ chỉ sai khi $p$ đúng và $q$ sai.

| $p$ | $q$ | $p \to q$ |
|---|---|---|
| Đúng | Đúng | Đúng |
| Đúng | Sai | Sai |
| Sai | Đúng | Đúng |
| Sai | Sai | Đúng |

### Tương đương
Mệnh đề $p \leftrightarrow q$ đúng khi $p$ và $q$ có cùng giá trị chân trị.

| $p$ | $q$ | $p \leftrightarrow q$ |
|---|---|---|
| Đúng | Đúng | Đúng |
| Đúng | Sai | Sai |
| Sai | Đúng | Sai |
| Sai | Sai | Đúng |

## Công thức logic

### Phân loại công thức
- Công thức đồng nhất đúng: luôn đúng với mọi giá trị của biến mệnh đề.
- Công thức đồng nhất sai: luôn sai với mọi giá trị của biến mệnh đề.
- Công thức thực hiện được: đúng với ít nhất một bộ giá trị.
- Hai công thức đồng nhất bằng nhau nếu có cùng bảng chân trị.

### Thứ tự thực hiện phép toán
Một thứ tự thường dùng:

1. Phủ định $\neg$.
2. Hội $\land$.
3. Tuyển $\lor$.
4. Kéo theo $\to$.
5. Tương đương $\leftrightarrow$.

## Một số luật logic

### Luật đối ngẫu
Trong các công thức của đại số logic, có thể đổi $\land$ thành $\lor$, đổi $\lor$ thành $\land$, đổi $0$ thành $1$ và đổi $1$ thành $0$ để thu được công thức đối ngẫu.

### Luật thay thế
Nếu hai công thức tương đương logic, có thể thay công thức này bằng công thức kia trong một biểu thức logic mà không làm thay đổi giá trị chân trị.

## Dạng chuẩn

### Tuyển sơ cấp và dạng chuẩn tắc tuyển
Dạng chuẩn tắc tuyển là tuyển của các hội sơ cấp.

### Hội sơ cấp và dạng chuẩn tắc hội
Dạng chuẩn tắc hội là hội của các tuyển sơ cấp.

### Kiểm tra hằng đúng, hằng sai
Các cách kiểm tra:

- Lập bảng chân trị.
- Đưa về dạng chuẩn.
- Suy diễn logic.

## Quy tắc suy diễn

| Quy tắc | Dạng |
|---|---|
| Luật cộng | Từ $p$ suy ra $p \lor q$ |
| Luật rút gọn | Từ $p \land q$ suy ra $p$ |
| Modus ponens | Từ $p$ và $p \to q$ suy ra $q$ |
| Modus tollens | Từ $\neg q$ và $p \to q$ suy ra $\neg p$ |
| Tam đoạn luận rời | Từ $p \lor q$ và $\neg p$ suy ra $q$ |
| Bắc cầu | Từ $p \to q$ và $q \to r$ suy ra $p \to r$ |
| Mâu thuẫn | Suy ra kết luận bằng cách chứng minh giả thiết ngược dẫn đến mâu thuẫn |
| Từng trường hợp | Chứng minh kết luận đúng trong từng trường hợp bao phủ |

## Đại số Bool

### Định nghĩa
Đại số Bool là một cấu trúc đại số với hai phép toán cơ bản thường ký hiệu là $+$ và $\cdot$, cùng phép lấy bù, thỏa mãn các luật như giao hoán, kết hợp, phân phối, phần tử trung hòa và phần tử bù.

### Các tính chất cơ bản
| Tính chất | Công thức |
|---|---|
| Giao hoán | $x+y=y+x$, $xy=yx$ |
| Kết hợp | $(x+y)+z=x+(y+z)$, $(xy)z=x(yz)$ |
| Phân phối | $x(y+z)=xy+xz$, $x+yz=(x+y)(x+z)$ |
| Trung hòa | $x+0=x$, $x\cdot 1=x$ |
| Bù | $x+\bar{x}=1$, $x\bar{x}=0$ |

## Hàm Bool và mạch logic

Hàm Bool là hàm nhận các giá trị đầu vào thuộc $\{0,1\}$ và cho đầu ra thuộc $\{0,1\}$.

Bảng chân trị mô tả giá trị đầu ra của hàm Bool với mọi tổ hợp đầu vào.

Các phép toán Bool tương ứng với cổng logic:

| Phép toán | Cổng logic |
|---|---|
| $\neg$ | NOT |
| $\land$ | AND |
| $\lor$ | OR |

## Tóm tắt chương
- Mệnh đề có giá trị đúng hoặc sai.
- Các phép toán logic cơ bản gồm phủ định, hội, tuyển, kéo theo và tương đương.
- Bảng chân trị giúp xác định giá trị của mệnh đề phức hợp.
- Công thức logic có thể là hằng đúng, hằng sai hoặc thực hiện được.
- Đại số Bool là nền tảng cho hàm Bool và mạch logic.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Mệnh đề | Câu khẳng định có giá trị đúng hoặc sai |
| Bảng chân trị | Bảng liệt kê giá trị của công thức theo các biến |
| Phủ định | Phép đổi đúng thành sai và ngược lại |
| Hội | Phép AND |
| Tuyển | Phép OR |
| Kéo theo | Phép $p \to q$ |
| Tương đương | Phép $p \leftrightarrow q$ |
| Đại số Bool | Cấu trúc đại số cho các giá trị 0 và 1 |
| Hàm Bool | Hàm nhận và trả giá trị Bool |
| Mạch logic | Mạch biểu diễn hàm Bool bằng cổng logic |

## Công thức cần nhớ
- $\neg p$
- $p \land q$
- $p \lor q$
- $p \to q$
- $p \leftrightarrow q$
- $x+\bar{x}=1$
- $x\bar{x}=0$
- $x(y+z)=xy+xz$

## Câu hỏi ôn tập
1. Mệnh đề logic là gì?
2. Mệnh đề chứa biến khác mệnh đề thông thường như thế nào?
3. Lượng từ $\forall$ và $\exists$ có ý nghĩa gì?
4. Lập bảng chân trị cho phép kéo theo.
5. Công thức đồng nhất đúng là gì?
6. Dạng chuẩn tắc tuyển và chuẩn tắc hội khác nhau ra sao?
7. Phát biểu Modus ponens và Modus tollens.
8. Đại số Bool có những tính chất cơ bản nào?
9. Hàm Bool được biểu diễn bằng bảng chân trị như thế nào?
