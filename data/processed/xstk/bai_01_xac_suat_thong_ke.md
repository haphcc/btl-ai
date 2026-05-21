### BÀI 1
#### XÁC SUẤT - THỐNG KÊ

**NỘI DUNG CHÍNH:**
- Phép thử ngẫu nhiên và không gian mẫu.
- Biến cố và mối quan hệ giữa các biến cố.
- Xác suất của một biến cố.
- Một số kiến thức tổ hợp dùng trong tính xác suất.

## CÁC ĐỊNH NGHĨA XÁC SUẤT

Trong đời sống thường gặp những phát biểu như "chiều nay có thể mưa", "giá vàng ngày mai có thể giảm", "mua cổ phiếu này có thể thắng lợi". Đó là các nhận định về khả năng xảy ra của sự kiện. Toán học định lượng hóa các khả năng này bằng cách gán cho mỗi sự kiện một số trong đoạn $[0;1]$, gọi là xác suất của sự kiện đó.

Lý thuyết xác suất nghiên cứu các phép thử ngẫu nhiên và được ứng dụng rộng rãi trong kinh tế, y học, sinh học, công nghệ, quân sự, bảo hiểm, đầu tư và nhiều lĩnh vực khác.

## PHÉP THỬ NGẪU NHIÊN VÀ KHÔNG GIAN MẪU

### 1. Phép thử ngẫu nhiên

Một sự kiện mà ta không chắc chắn có xảy ra hay không thường liên quan đến kết quả của một phép thử ngẫu nhiên.

**Ví dụ:** Khi gieo một con xúc xắc cân đối và đồng chất, ta không đoán chắc được số chấm lẻ có xuất hiện hay không. Ta chỉ biết kết quả có thể là một trong các số $1,2,3,4,5,6$.

Ta kí hiệu phép thử ngẫu nhiên bởi chữ $\mathcal{T}$.

### 2. Không gian mẫu

Không gian mẫu của phép thử $\mathcal{T}$, kí hiệu bởi $\Omega$, là tập hợp tất cả các kết quả có thể xảy ra của $\mathcal{T}$.

**Ví dụ:** Với phép thử $\mathcal{T}$ là gieo một con xúc xắc và $i$ là số chấm xuất hiện, ta có:

$$
\Omega=\{1,2,3,4,5,6\}.
$$

Các phép thử ngẫu nhiên thường gặp gồm: quan sát thị trường chứng khoán, chơi xổ số, thống kê tai nạn, bảo hiểm, đếm số khách đến máy ATM, đếm số cuộc gọi đến tổng đài, kiểm tra chất lượng sản phẩm, quan sát thời tiết.

## BIẾN CỐ VÀ MỐI QUAN HỆ GIỮA CHÚNG

### 1. Khái niệm biến cố

Một biến cố liên quan đến phép thử $\mathcal{T}$ là một sự kiện mà việc nó xảy ra hay không xảy ra phụ thuộc vào kết quả của $\mathcal{T}$.

Một kết quả của $\mathcal{T}$ được gọi là kết quả thuận lợi cho biến cố $A$ nếu $A$ xảy ra khi kết quả đó xảy ra. Tập hợp tất cả các kết quả thuận lợi cho $A$ là một tập con của $\Omega$.

**Ví dụ:** Khi gieo một con xúc xắc, biến cố $A$ là "xuất hiện số chấm chẵn" có tập kết quả thuận lợi:

$$
A=\{2,4,6\}.
$$

Ta thường đồng nhất biến cố $A$ với tập hợp các kết quả thuận lợi cho $A$. Khi đó $A\subset\Omega$.

### 2. Biến cố không thể và biến cố chắc chắn

Biến cố không thể là biến cố không bao giờ xảy ra khi thực hiện phép thử $\mathcal{T}$. Tập kết quả thuận lợi của nó là tập rỗng, kí hiệu $\varnothing$.

Biến cố chắc chắn là biến cố luôn xảy ra khi thực hiện $\mathcal{T}$. Tập kết quả thuận lợi của nó chính là không gian mẫu, kí hiệu $\Omega$.

### 3. Quan hệ giữa các biến cố

Biến cố $A$ được gọi là kéo theo biến cố $B$, kí hiệu $A\subset B$, nếu $A$ xảy ra thì $B$ cũng xảy ra.

Biến cố $A$ được gọi là tương đương với biến cố $B$, kí hiệu $A=B$, nếu $A\subset B$ và $B\subset A$.

Biến cố đối của biến cố $A$, kí hiệu $\overline{A}$, là biến cố xảy ra khi và chỉ khi $A$ không xảy ra.

**Ví dụ:** Khi gieo một con xúc xắc:

$$
A=\{2,4,6\}, \qquad \overline{A}=\{1,3,5\}.
$$

Khi đó:

$$
A\cap\overline{A}=\varnothing,\qquad A\cup\overline{A}=\Omega.
$$

### 4. Hợp của các biến cố

Nếu $A_1,A_2,\ldots,A_n$ là các biến cố liên quan đến $\mathcal{T}$, thì hợp của chúng, kí hiệu $A_1\cup A_2\cup\cdots\cup A_n$, là biến cố xảy ra nếu có ít nhất một biến cố $A_i$ xảy ra.

### 5. Giao của các biến cố

Nếu $A_1,A_2,\ldots,A_n$ là các biến cố liên quan đến $\mathcal{T}$, thì giao của chúng, kí hiệu $A_1A_2\cdots A_n$ hoặc $A_1\cap A_2\cap\cdots\cap A_n$, là biến cố xảy ra nếu tất cả các biến cố $A_1,A_2,\ldots,A_n$ đều xảy ra.

Hai biến cố $A$ và $B$ được gọi là xung khắc nếu:

$$
AB=\varnothing.
$$

**Ví dụ:** Gieo một con xúc xắc. Gọi:

$$
A_i=\text{"xuất hiện }i\text{ chấm"}, \quad A=\text{"xuất hiện số chấm chẵn"}, \quad B=\text{"xuất hiện số chấm chia hết cho 3"}.
$$

Khi đó:

$$
A=A_2\cup A_4\cup A_6,\qquad B=A_3\cup A_6,\qquad AB=A_6.
$$

Các biến cố $A_1,A_2,\ldots,A_6$ đôi một xung khắc.

### 6. Một số tính chất của phép toán biến cố

Với các biến cố $A,B,C$:

- $A\cup B=B\cup A$, $AB=BA$.
- $A\cup A=A$, $AA=A$.
- $A\cup\Omega=\Omega$, $A\Omega=A$.
- $A\cup\varnothing=A$, $A\varnothing=\varnothing$.
- $(A\cup B)C=(AC)\cup(BC)$.
- $(AB)\cup C=(A\cup C)(B\cup C)$.
- $\overline{\overline{A}}=A$.
- $\overline{A_1\cup A_2\cup\cdots\cup A_n}=\overline{A_1}\,\overline{A_2}\cdots\overline{A_n}$.
- $\overline{A_1A_2\cdots A_n}=\overline{A_1}\cup\overline{A_2}\cup\cdots\cup\overline{A_n}$.

Các phép toán trên biến cố giúp phân tích một biến cố phức tạp thành các biến cố đơn giản hơn.

**Ví dụ:** Một người tham gia đấu thầu hai dự án. Gọi $H_i$ là biến cố "người đó trúng thầu dự án thứ $i$" với $i=1,2$.

- Biến cố người đó trúng thầu cả hai dự án là $H_1H_2$.
- Biến cố người đó chỉ trúng thầu một dự án là $(H_1\overline{H_2})\cup(\overline{H_1}H_2)$.
- Biến cố người đó trúng thầu ít nhất một dự án là $H_1\cup H_2$.

## XÁC SUẤT CỦA MỘT BIẾN CỐ

Xác suất của biến cố $A$, kí hiệu $P(A)$, là một số thuộc $[0;1]$ dùng để đo khả năng xảy ra của biến cố $A$.

### 1. Định nghĩa cổ điển về xác suất

Giả sử phép thử $\mathcal{T}$ có tất cả $n$ kết quả đồng khả năng, trong đó có $m$ kết quả thuận lợi cho biến cố $A$. Khi đó:

$$
P(A)=\frac{m}{n}.
$$

**Ví dụ:** Gieo một con xúc xắc cân đối, đồng chất. Các kết quả là đồng khả năng và $|\Omega|=6$.

Với $A=\text{"xuất hiện số chấm chẵn"}=\{2,4,6\}$:

$$
P(A)=\frac{3}{6}.
$$

Với $B=\text{"xuất hiện số chấm chia hết cho 3"}=\{3,6\}$:

$$
P(B)=\frac{2}{6}.
$$

Từ tính đối xứng của phép thử như đồng tiền cân đối, xúc xắc cân đối, ta suy ra các kết quả của nó đồng khả năng.

**Ví dụ:** Biết cha mẹ của hoàng tử Romeo có hai con và Romeo là một trong hai người con đó. Tính xác suất để Romeo có chị gái hoặc em gái.

**Giải:** Nếu chỉ xét người anh chị em còn lại thì có hai khả năng trai hoặc gái, nên một lời giải cho kết quả $\frac{1}{2}$. Tuy nhiên nếu xét gia đình hai con theo thứ tự sinh, có bốn trường hợp $TT,TG,GT,GG$. Vì biết có Romeo là con trai nên loại $GG$, còn lại $TT,TG,GT$. Trong ba trường hợp này có hai trường hợp có con gái, nên xác suất là $\frac{2}{3}$.

### 2. Định nghĩa xác suất theo thống kê

Trong nhiều bài toán thực tế như khả năng một máy sản xuất ra phế phẩm hoặc khả năng doanh nghiệp đạt doanh số tối thiểu, ta phải dựa vào quan sát thực tế.

Giả sử phép thử $\mathcal{T}$ có thể lặp lại rất nhiều lần trong những điều kiện giống nhau. Nếu trong $n$ lần thực hiện $\mathcal{T}$, biến cố $A$ xuất hiện $m$ lần, thì tỉ số:

$$
\frac{m}{n}
$$

được gọi là tần suất xuất hiện của biến cố $A$ trong $n$ phép thử.

Khi $n$ tăng dần, nếu $\frac{m}{n}$ dần tới một số $p$, ta định nghĩa:

$$
P(A)=p.
$$

Trong thực tế, với $n$ đủ lớn:

$$
P(A)\approx\frac{m}{n}.
$$

**Ví dụ:** Theo dõi $100\,000$ sản phẩm do một máy sản xuất thấy có $138$ phế phẩm. Xác suất để máy sản xuất ra một phế phẩm xấp xỉ:

$$
\frac{138}{100000}.
$$

### 3. Một số tính chất cơ bản

Với mọi biến cố $A$:

$$
0\le P(A)\le 1.
$$

Ngoài ra:

$$
P(\varnothing)=0,\qquad P(\Omega)=1.
$$

Nếu $P(A)>P(B)$ thì khả năng xuất hiện của $A$ cao hơn khả năng xuất hiện của $B$.

### 4. Nguyên lý xác suất nhỏ và xác suất lớn

Nguyên lý xác suất nhỏ: Nếu một biến cố có xác suất rất nhỏ thì trong thực tế có thể xem như biến cố đó không xảy ra trong một phép thử.

Nguyên lý xác suất lớn: Nếu một biến cố có xác suất gần bằng $1$ thì trong thực tế có thể xem như biến cố đó sẽ xảy ra trong một phép thử.

Hai nguyên lý này được ứng dụng khi đánh giá độ tin cậy của một nhận định hoặc khi lựa chọn phương án có rủi ro nhỏ.

## MỘT SỐ KIẾN THỨC VỀ TỔ HỢP

Phần tổ hợp cung cấp cách tính gián tiếp số phần tử của một tập hợp hữu hạn, từ đó hỗ trợ tính xác suất theo định nghĩa cổ điển.

### 1. Quy tắc cộng

Giả sử một việc $V$ được hoàn thành khi và chỉ khi một trong $n$ việc $V_1,V_2,\ldots,V_n$ khác nhau được hoàn thành. Nếu mỗi việc $V_i$ có $k_i$ cách làm, thì số cách thực hiện $V$ là:

$$
k_1+k_2+\cdots+k_n.
$$

**Ví dụ:** Đi từ tỉnh $A$ đến tỉnh $B$ bằng một trong bốn phương tiện: ô tô, tàu hỏa, tàu thủy, máy bay. Nếu mỗi ngày có 10 chuyến ô tô, 5 chuyến tàu hỏa, 3 chuyến tàu thủy và 2 chuyến máy bay, thì có:

$$
10+5+3+2=20
$$

cách đi.

### 2. Quy tắc nhân

Giả sử một việc $V$ được hoàn thành khi và chỉ khi toàn bộ $n$ việc $V_1,V_2,\ldots,V_n$ khác nhau được hoàn thành. Nếu mỗi việc $V_i$ có $k_i$ cách làm, thì số cách thực hiện $V$ là:

$$
k_1k_2\cdots k_n.
$$

**Ví dụ:** Một ổ khóa số gồm 3 vòng, mỗi vòng có 10 chữ số từ 0 đến 9. Số cách cài mã là:

$$
10^3.
$$

### 3. Chỉnh hợp và hoán vị

Một tập con gồm $k$ phần tử có xét thứ tự của một tập $n$ phần tử được gọi là chỉnh hợp chập $k$ của $n$ phần tử.

Số chỉnh hợp chập $k$ của $n$ phần tử là:

$$
A_n^k=n(n-1)(n-2)\cdots(n-k+1).
$$

Đặc biệt, chỉnh hợp chập $n$ của $n$ phần tử được gọi là hoán vị. Số hoán vị của $n$ phần tử là:

$$
P_n=n!.
$$

**Ví dụ:** Chọn 2 trong 3 người đi làm nhiệm vụ, trong đó một người làm đội trưởng, có:

$$
A_3^2=3\cdot2=6
$$

cách chọn.

### 4. Tổ hợp

Một tập con gồm $k$ phần tử không xét thứ tự của một tập $n$ phần tử được gọi là tổ hợp chập $k$ của $n$ phần tử.

Số tổ hợp chập $k$ của $n$ phần tử là:

$$
C_n^k=\frac{n!}{k!(n-k)!}.
$$

**Ví dụ:** Chọn 2 trong 3 người đi làm nhiệm vụ, không xét vai trò, có:

$$
C_3^2=3
$$

cách chọn.
