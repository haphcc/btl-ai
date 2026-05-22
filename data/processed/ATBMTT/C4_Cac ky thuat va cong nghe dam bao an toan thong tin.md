# 

## Nội dung chính

Cơ sở toán học

## 4. 1

Đảm bảo an toàn thông tin dựa trên mật mã

## 4. 2

Các kỹ thuật mã hóa

## 4. 3

## 4. 4

Hàm băm

## 4. 5

Chữ ký số

## 4. 1. Cơ sở toán học

## 4. 1. 1 Một số khái niệm trong số học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Khái niệm

- Ước số, bội số

- Ước chung lớn nhất (gcd(a, b))

- Bội chung nhỏ nhất (lcm(a, b))

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Tính chất:

- d = gcd(a 1, a 2, …, an) khi và chỉ khi tồn tại các số x 1, x 2, …, xn sao cho d = a 1 x 1+a 2 x 2+…+anxn

- d = gcd(a 1, a 2, …, an) <=>gcd(a 1/d, a 2/d, …, an/d) =1

- m = lcm(a 1, a 2, …, an) <=>gcd(m/a 1, m/a 2, …, m/an) =1

- gcd(m a 1, m a 2, …, m an) = m * gcd(a 1, a 2, …, an)

(với m ≠ 0)

- Nếu gcd(a, b) =1 thì lcm(a, b) = a * b

- Nếu b>0, a = bq+r thì gcd(a, b) = gcd(b, r)

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Thuật toán Euclide tìm gcd(a, b):

- Bài toán:

- Đầu vào: Cho hai số nguyên không âm a, b, a ≥ b

- Đầu ra: gcd(a, b)

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Thuật toán Euclide tìm gcd(a, b):

- Thuật toán:

cin>>a; cin>>b; While (b>0) do { r : = a mod b; a : = b; b : = r; } cout<<a;

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Thuật toán Euclide tìm gcd(a, b):

- Ví dụ: gcd(30, 18)

a=30, b=18; gcd(30, 18) = gcd(18, 12) = gcd(12, 6) = gcd(6, 0) = 6 30=18. 1+12 a b r a=b.q+r 18=12. 1+6 12=6. 2+0

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Thuật toán Euclide mở rộng

- Bài toán:

- Đầu vào: Cho hai số nguyên không âm a, b, a ≥ b

- Đầu ra: d = gcd(a, b) và x, y sao cho ax +by = d

## 4. 1. Cơ sở toán học

## 4. 1. 1. 1. Ước chung lớn nhất, Bội chung nhỏ nhất

- Thuật toán:

cin>>a; cin>>b; if(b==0) { d=a; x=1; y=0; cout<<d<<x<<y; } else { x 2=1; x 1=0; y 2=0; y 1=1; while (b>0) { q=a div b; r=a mod b; x=x 2 - q*x 1; y=y 2 - q*y 1; a=b; b=r; x 2=x 1; x 1=x; y 2=y 1; y 1=y; } d=a; x=x 2; y=y 2; cout<<d<<x<<y; }

## 4. 1. Cơ sở toán học

## 4. 1. 1. 2. Quan hệ đồng dư

- Khái niệm:

- Các tính chất của quan hệ đồng dư

- Quan hệ tương đương

- Tổng và hiệu các đồng dư

- Tích các đồng dư

## 4. 1. Cơ sở toán học

## 4. 1. 1. 3. Số nguyên tố

- Khái niệm:

- Ví dụ

- 10 số nguyên tố lớn tìm thấy:

## 4. 1. Cơ sở toán học

- Định lý về số nguyên tố:

- Định lý 1:

- Định lý Mersenne: Cho p=2^k-1; Nếu p nguyên tố thì cũng phải k nguyên tố

- Hàm Euler và định lý hàm Euler

## 4. 1. 1. 3. Số nguyên tố

## 4. 1. Cơ sở toán học

- Phương pháp kiểm tra tính nguyên tố

- Phương pháp cổ điển:

- Phương pháp xác suất

- Định lý Ferma: Nếu p là số nguyên tố, a là số nguyên, thì a p ≡ a (mod p). Nếu p không chia hết a, thì a p-1 ≡ 1 (mod p)

- Định lý Euler: Nếu gcd(a, m) = 1 thì a phi(m)

≡ 1 (mod m)

- Hệ quả: Nếu gcd(c, m) = 1 và a ≡b (mod phi(m)) với a, b là các sốtựnhiên, thì ca ≡cb (mod m) và suy ra ca mod m = ca mod phi(m) mod m

## 4. 1. 1. 3. Số nguyên tố

## 4. 1. Cơ sở toán học

- Tính toán đồng dư của lũy thừa lớn

- Trường hợp a>phi(m):

- Trường hợp a<phi(m):

- Phương pháp bình phương liên tiếp

- Định lý số dư Trung Quốc:

## 4. 1. 1. 3. Số nguyên tố

- Ví dụ

- Ví dụ

## 4. 1. Cơ sở toán học

## 4. 1. 2 Một số khái niệm trong Đại số

## 4. 1. 2. 1. Cấu trúc nhóm

- Khái niệm nhóm

- Khái niệm nhóm: Nhóm là một bộ (G, *), trong đó G !=, * là phép toán hai ngôi trên G thoả mãn ba

## tính chất sau: Kết hợp, phần tử trung lập và phần tử

nghịch đảo

- Cấp của nhóm

- Nhóm Abel: là nhóm (G, *), trong đó phép toán hai ngôi * có tính giao hoán

- Nhóm con của nhóm

## 4. 1. Cơ sở toán học

- Khái niệm: Là nhóm mà toàn bộ các phần tử của nó được sinh ra bởi một trong các phần tử của nó (g * g * … * g = a), g là phần tử sinh

- Cấp của nhóm: Là sốtựnhiên n nhỏnhất mà g n = e.

- Cấp của 1 phần tử trong nhóm: Phần tử  G được gọi là có cấp d, nếu d là sốnguyên dương nhỏnhất sao cho  d = e

## 4. 1. 2. 2 Nhóm Cyclic

## 4. 1. Cơ sở toán học

- Phần tử nghịch đảo đối với phép nhân

- Định nghĩa:

- Định lý: UCLN (a, n) = 1 <=>Phần tửa Zn có phần tửnghịch đảo

- Hệ quả: Mọi phần tửtrong Zn* đều có phần tử nghịch đảo

- Tìm phần tửnghịch đảo bằng Thuật toán Euclid mởrộng

- Input:

a∈Zn

- Output:

Phần tử nghịch đảo của a

## 4. 1. 2. 3 Nhóm (Zn *, phép nhân mod n)

## 4. 1. Cơ sở toán học

- Thuật toán:

int Invert(int a, int n)

{ g 0=n; g 1=a; u 0=1; u 1=0; v 0=0; v 1=1; i=1; while (gi !=0)

{ y = gi-1 div gi; gi+1 = gi+1 - y.gi; ui+1 = ui+1 - y.ui; vi+1 = vi+1 - y.vi; i = i+1; } t = vi+1; if (t > 0) a^(-1) = t; else a^(-1) = t + n; }

- Khái niệm bài toán

- Khái niệm thuật toán

## 4. 1. 3. Khái niệm độ phức tạp của thuật toán

## 4. 1. 3. 1 Khái niệm thuật toán

- Quan niệm trực giác

- Quan niệm toán học

- Hai mô hình tính toán

- Mô hình ứng dụng: Ngôn ngữ tựa Algol

- Mô hình lý thuyết: Biểu diễn bằng ngôn ngữ máy Turing

## 4. 1. Cơ sở toán học

- Chi phí của thuật toán (Tính theo một bộ dữ liệu vào):

- Độ phức tạp về bộ nhớ:

- Độ phức tạp thời gian

- Độphức tạp tiệm cận

- Độphức tạp đa thức

- Thuật toán đa thức

## 4. 1. 3. 2 Khái niệm độ phức tạp của thuật toán

## 4. 1. Cơ sở toán học

- Các khái niệm Dẫn về được Khó tương đương

- Các lớp bài toán

## 4. 1. 3. 3 Phân lớp bài toán theo độ phức tạp

- Lớp bài toán P, NP

- Lớp Bài toán NP- Hard

- Lớp bài toán NP- Complete

- Phân lớp các bài toán

## 4. 1. Cơ sở toán học

- Hàm một phía: Hàm f(x) được gọi là hàm một phía nếu tính “xuôi” y = f(x) thì “dễ”, nhưng tính “ngược” x = f -1 (y) lại rất “khó”

- Hàm cửa sập một phía: Hàm f(x) được gọi là hàm cửa sập một phía nếu tính y = f(x) thì “dễ”, tính x = f -1 (y) lại rất “khó”. Tuy nhiên có cửa sập z để tính x = f -1 (y) là “dễ”.

## 4. 1. 3. 3 Hàm một phía và hàm cửa sập một phía

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

## 4. 2. 1 Khái niệm về mật mã học

- Mật mã học: bao gồm mã hóa và thám mã

- Mã hóa: Nghiên cứu các thuật toán và phương thức đảm bảo tính bí mật và xác thực của thông tin

- Thám mã: Nghiên cứu cá phương pháp phá mã hoặc tạo mã giả

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Khái niệm mã hóa (cryptography):

## 4. 2. 1 Khái niệm về mật mã học

- Che thông tin

- giấu thông tin

- Sơ đồ mã hóa và giải mã

- Hệ mã hóa (P, K C, E, D)

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Các cách phân loại

## 4. 2. 1 Khái niệm về mật mã học

- Theo đặc trưng của Khóa

- Mã hóa đối xứng

- Mã hóa công khai

- Theo đặc trưng bản rõ

- Mã hóa khối

- Mã hóa dòng

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Khái niệm: là Hệ mã hóa mà biết được khóa lập mã thì có thể “dễ” tính được khóa giải mã và ngược lại

- Đặc điểm:

- Ưu điểm:

- Nhược:

- Nơi sử dụng:

- Trong mạng nội bộ

- Dữ liệu lớn

- Hệ mã hóa Khóa đối xứng

## 4. 2. 1 Khái niệm về mật mã học

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Khái niệm: là hệ mã hóa có khóa lập mã và khóa giải mã là khác nhau, khóa lập mã là công khai, khóa giải mã là bí mật

- Đặc điểm:

- Ưu điểm:

- Nhược:

- Nơi sử dụng Trong mạng Internet

- Hệ mã hóa Khóa công khai

## 4. 2. 1 Khái niệm về mật mã học

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Bảo mật:

- Xác thực

- Toàn vẹn

- Dịch vụ không thể chối từ

- Dịch vụ xác thực danh tính

- Ứng dụng của mật mã học

## 4. 2. 1 Khái niệm về mật mã học

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Sơ đồ

## 4. 2. 2. Các phương pháp mã hóa

## 4. 2. 2. 1. Hệ mã hóa dịch chuyển

- Ví dụ

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Độ an toàn: Rất thấp T O I N A Y T H A V I R U S

## 19 14 8 26 13 0 24 26 19 7 0 26 21 8 17 20 18

## 22 17 11 3 16

## 3 1

## 22 10 3 3 24 11 20 23 21

W R L D Q D B D W K D D Y L U X V

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Sơ đồ

- Ví dụ:

## 4. 2. 2. 2. Hệ mã hóa thay thế

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

TOI N AY THA VIRUS Khóa K là bảng thay thế:

- Độ an toàn: duyệt 26!

Bản mã chữlà: E J P Z K Y V Z E Q Y Z C P G D F

- Sơ đồ

- Ví dụ

## 4. 2. 2. 3. Hệ mã hóa AFFINE

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

CHIEUNAYOVUONHOA k = (a, b) = (3, 6)

Bản rõ số:

x = 2 7 8 4 20 13 0 24 14 21 20 14 13 7 14 0 Bản mã số:

y = 12 1 4 18 14 19 6 0 22 17 14 22 19 1 22 6 Bản mã chữ: MBESOTGAWROWTBWG

- Độ an toàn: Rất thấp vì số các khóa có thể là 312

- Sơ đồ

- Ví dụ

## 4. 2. 2. 4. Hệ mã hóa VIGENERE

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

THISISACRYPTOSYSTEM, k = “KWORD” = {10, 22, 14, 17, 3}

## 19 7 8 18 8 18 0 2 17 24 15 19 14 18 24 18 19 4 12

Bản mã số:

## 3 3 22 9 11 2 22 16 8 1 25 15 2 9 1 2 15 18 3

Bản mã chữ: DDWJLCWQIBZPCJBCPSD

- Độ an toàn: Tương đối cao

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Sơ đồ

- Độ an toàn: Tương đối cao, phải ktra số khóa là:

## 1 ! + 2! + 3 ! + … + m ! trong đó m  26.

- Ví dụ

## 4. 2. 2. 5 Hệ mã hóa hoán vị cục bộ

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Sơ đồ

- Ví dụ

## 4. 2. 2. 6. Hệ mã hóa HILL

## 4. 2. Đảm bảo ATTT dựa trên mật mã học

- Độ an toàn: Cao

## 4. 3. Các kỹ thuật mã hóa

- Giới thiệu:

## 4. 3. 1 Hệ mã hóa đối xứng DES

- Quy trình mã hóa theo DES

## 4. 3. Các kỹ thuật mã hóa

- Quy trình lập mã DES Bản mã: 64 bit L16 = R15 R16 = L15 f (R15, k 16)

IP-1 f R15 = L14 f ( R14, k 15)

L15 = R14 R1 = L0 f ( R0, k 1)

L1 = R0 f R2 = L1 f ( R1, k 2)

L2 = R1 L0 R0 Bản rõ: 64 bit IP f k 1 k 2 k 16

- Thực hiễn mã hóa DES theo sơ đồ

- Bước 1: Bản rõ x được hoán vị theo phép hoán vị IP, thành IP(x)

- Bước 2: Thực hiện 16 vòng mã hóa với những phép toán giống nhau

- Bước 3: Thực hiện phép hoán vị ngược

- Tính các Khóa con Ki

- Sơ đồ K PC - 1 LS16 LS16 PC - 2 k 16 LS1 LS1 LS2 LS2 PC - 2 k 1 PC - 2 k 2 C0 D0 C1 D1 C2 D2 C16 D16

- Tính khóa Ki :

- Khoá K là xâu dài 64 bit, trong đó 56 bit là khoá và

## 8 bit đểkiểm tra tính chẵn lẻnhằm phát hiện sai

- Cách tính:

+ Với khoá K độdài 64 bit, loại bỏcác bit kiểm tra tính chẵn lẻ, hoán vị 56 bit còn lại theo phép hoán vị PC-1:

PC-1 (K ) = C0 D0 + Tính: Ci = LSi ( Ci-1 ), Di = LSi ( Di-1 ) với i=1, 2, …, 16 + Với i=1, 2, …., 16 k i được tính theo hoán vị PC-2 từ CiDi: ki= PC-2 (Ci Di )

(48 bit)

## 4. 3. Các kỹ thuật mã hóa

- Tính hàm f(Ri-1, ki)

- Sơ đồ Ri-1 k i E + E(Ri-1)

P f (Ri-1, ki)

B8 B1 B7 B6 B2 B3 B4 B5 S8 S1 S7 S6 S2 S3 S4 S5 C8 C1 C7 C6 C2 C3 C4 C5

- Tính hàm f(Ri-1, Ki)

- Mởrộng R 32 bit thành 48 bit theo hàm mởrộng E

- Tính E(R) k, trong đó E(R) (48 bit) và k (48 bit). Kết quảchia thành B = B1 B2 B3 B4 B5 B6 B7 B8

- Tính Cj = Sj (Bj), j = 1, … , 8

- Ta nhận được xâu C = C1 C2 … C8 (32 bit). Sau hoán vị P, cho kết quả P (C), đó chính là f (R, k)

 Trong đó:

Phép hoán vị PC-1 Phép hoán vị PC-2

## 57 49 41 33 25 17 9

## 1 58 50 42 34 26 18

## 10 2 59 51 43 35 27

## 19 11 3 60 52 44 36

## 63 55 47 39 31 23 15

## 7 62 54 46 38 30 22

## 14 6 61 53 45 37 29

## 21 13 5 28 20 12 4

## 14 17 11 24 1 5

## 3 28 15 6 21 10

## 23 19 12 4 26 8

## 16 7 27 20 13 2

## 41 52 31 37 47 55

## 30 40 51 45 33 48

## 44 49 39 56 34 53

## 46 42 50 36 29 32

## 4. 3. Các kỹ thuật mã hóa

Hàm mở rộng E Phép hoán vị P

## 16 7 20 21 29 12 28 17

## 1 15 23 26 5 18 31 10

## 2 8 24 14 32 27 3 9

## 19 13 30 6 22 11 4 25

## 32 1 2 3 4 5

## 4 5 6 7 8 9

## 8 9 10 11 12 13

## 12 13 14 15 16 17

## 16 17 18 19 20 21

## 20 21 22 23 24 25

## 24 25 26 27 28 29

## 28 29 30 31 32 1

## 4. 3. Các kỹ thuật mã hóa

Bảng hoán vị IP Bảng hoán vị

 và các bảng S:

- Quy trình giải mã DES theo sơ đồ Qui trình giải mã của DES tương tự như qui trình lập mã, nhưng dùng các khóa theo thứ tự ngược lại : k 16 , k 15, … , k 1. Xuất phát (đầu vào)

từ bản mã y, kết quả (đầu ra) là bản rõ x

- Ví dụ:

X = 0 1 2 3 4 5 6 7 8 9 A B C D E F X= 0000 0001 0010 0011 0100 0101 0110 0111

## 1000 1001 1010 1011 1100 1101 1110 1111

Bước 1: Bản rõ x được hoán vị theo phép hoán vị IP, thành IP (x) ta được

## 4. 3. Các kỹ thuật mã hóa

Bước 2: Thực hiện 16 vòng mã hóa:

Lấy khóa K gốc: K = 133457799 BBCDFF1 (64 bit)

= 0001 0011 0011 0100 0101 0111 0111 1001

## 1001 1011 1011 1100 1101 1111 1111 0001

=> k 1 = 000110 110000 001011 101111 111111

## 000111 000001 110010

## 4. 3. Các kỹ thuật mã hóa

Mở rộng xâu R0 (32 bit) thành xâu E(R0 ) (48 bit), theo hàm mở rộng E:

E: R0 →E(R0 ):

=>E(R0 ) = 011110 100001 010101 010101 011110

## 100001 010101 010101

=> E(R0 ) k 1 = B1 B2 B3 B4 B5 B6 B7 B8 = 011000 010001 100010 110010 100001

## 100110 010100 100111

## 4. 3. Các kỹ thuật mã hóa

Tính C1 = S1 (B1), dùng bảng S1.

B1 = b 1 b 2 b 3 b 4 b 5 b 6 = 011000 b 1 b 6 = (00)2 = (00)10 = Hàng 0 trong S1 .

b 2 b 3 b 4 b 5 = (1100)2 = (12)10 = Cột 12 trong S1 .

C1 = S1 (0, 12) = (5)10 = (0101)2 Tương tự cho các Cj => C = 0101 1100 1000

## 0010 1011 0101 1001 0111

Hoán vị P được P(C), đó chính là f (R0, k 1)

f (R0, k 1) = P(C) = 0010 0011 0100 1010 1010

## 1001 1011 1011

## 4. 3. Các kỹ thuật mã hóa

Bước 3: Sử dụng hoán vị IP-1 => Kết quả là bản mã : 85 E813540 F0 AB405 Lặp lại 16 lần như vậy rồi chuyển sang bước 3

- Độ an toàn: Có liên quan đến các Sj

- Ngoại trừ các bảng S, mọi tính toán trong DES đều tuyến tính, tức là việc tính phép hoặc loại trừ của hai đầu ra cũng giống như phép hoặc loại trừ của hai đầu vào, rồi tính toán đầu ra

- Các bảng S chứa đựng nhiều thành phần phi tuyến của hệ mật, là yếu tố quan trọng nhất đối với độ mật của hệ thống

- Tiêu chuẩn xây dựng các hộp S không được biết đầy đủ. Và có thể các hộp S này có thể chứa các “cửa sập” được giấu kín. Và đó cũng là một điểm đảm bảo tính bảo mật của hệ DES .

- Hạn chế: Kích thước không gian khóa

- Số khóa có thể là , không gian này là nhỏ để đảm bảo an toàn thực sự. Nhiều thiết bị chuyên dụng đã được đề xuất nhằm phục vụ cho phép tấn công với bản rõ đã biết. Phép tấn công này chủ yếu thực hiện theo phương pháp “vét cạn”

- Giới thiệu

## 4. 3. 2 Hệ mã hóa RSA

## 4. 3. Các kỹ thuật mã hóa

- Tạo cặp khóa (bí mật, công khai) (a, b)

- Chọn bí mật số nguyên tố lớn p, q , tính n = p * q, công khai n, đặt P = C = Zn

- Tính bí mật phi(n) = (p-1)(q-1) Chọn khóa công khai b < phi(n), nguyên tố với phi(n)

- Khóa bí mật a là phần tử nghịch đảo của b theo mod phi(n): a*b  1 (mod phi(n)

- Tập cặp khóa (bí mật, công khai) ) K = (a, b)/ a, b  Zn , a*b  1 (mod phi(n)).

- Hàm Mã hóa:

- Hàm Giải mã:

Với x là bản rõ, y là bản mã , ta có:

- Tạo cặp khóa (bí mật, công khai) ) (a, b)

## Ví dụ: Cho bản rõ chữ x=RENAISSANCE

- Chọn bí mật số nguyên tố lớn p=53, q=61 => n = 3233, công khai n, đặt P = C = Zn

- Tính bí mật phi(n) = (p-1)(q-1) = 3120 Chọn khóa công khai b =71.

- Khóa bí mật a là phần tử nghịch đảo của b theo mod phi(n): a*b  1 (mod phi(n) => a=791

- Quy ước chuyển ký tự thành số

- Bản rõ được thể hiện:

Bản mã số :

- Để nhận lại được bản rõ thì ta áp dụng giải mã:

- Hệmã hóa RSA là tất định, tức là với một bản rõ x và một khóa bí mật a, thì chỉcó một bản mã y

- Hệmật RSA an toàn, khi giữđược bí mật khoá giải mã a, p, q, phi(n)

=>Độan toàn của Hệmật RSA dựa vào khảnăng

## giải bài toán phân tích sốnguyên dương n thành

tích của 2 sốnguyên tốlớn p và q

- Độ an toàn của RSA

## 4. 4. Đại diện tài liệu và hàm băm

## 4. 4. 1 Tổng quan về Hàm băm

- Khái niệm:

## Hàm băm là thuật toán không dùng khóa để mã

hóa (ở đây dùng thuật ngữ “băm” thay cho “mã hóa”), nó có nhiệm vụ “lọc” (băm) tài liệu (bản tin)

và cho kết quả là một giá trị “băm” có kích thước cố định, còn gọi là “đại diện tài liệu” hay “đại diện bản tin”, “đại diện thông điệp”

## 4. 4. Đại diện tài liệu và hàm băm

- Đặc tính của Hàm băm :

- Với tài liệu đầu vào (bản tin gốc) x, chỉ thu được giá trị băm duy nhất z = h(x)

- Nếu dữ liệu trong bản tin x bị thay đổi hay bị xóa để thành bản tin x’, thì giá trị băm h(x’) != h(x)

- Nội dung của bản tin gốc “khó” thể suy ra từ giá trị hàm băm của nó

- Ứng dụng của hàm băm :

- Giảm bộ nhớ lưu giữ chữ ký và thời gian truyền chữ ký trên mạng

- Hàm băm dùng để xác định tính toàn vẹn dữ liệu

- Hàm băm dùng để bảo mật một số dữ liệu đặc

## biệt, ví dụ bảo vệ mật khẩu, bảo vệ khóa mật mã,

…

- Các tính chất của hàm băm :

- Tính chất 1: Hàm băm h là không va chạm yếu

- Tính chất 2: Hàm băm h là không va chạm mạnh

- Tính chất 3: Hàm băm h là hàm một chiều

- Các hàm băm :

- Các hàm băm dòng MD: MD2, MD4, MD5.

- Hàm băm an toàn SHA

## 4. 4. 2 Hàm băm MD4

- Chuẩn bịcác tham số:

- “Thông điệp đệm” (Messege Padding) là xâu bit có độ dài chia hết cho 512

- “Thông điệp đệm” được lưu trong mảng M = M[0]

M[1] … M[N-1] , với N 0 mod 16.

- M được xây dựng từ Bản tin gốc a bằng thuật toán

## 4. 4. Đại diện tài liệu và hàm băm

Trong đó

- Thuật toán băm MD4 :

- Input: Thông điệp là một xâu a có độ dài b bit.

- Output: Bản băm, đại diện cho thông điệp gốc, độ dài cố định 128 bit

- Bài toán:

- Bước 1: Khởi tạo các thanh ghi A, B, C, D.

- Bước 2: Xử lý thông điệp a trong 16 khối word, có nghĩa là xử lý cùng một lúc 16 word = 16 * 32 bit = 512 bit. Chia mảng M thành các khối 512 bit, đưa từng khối 512 bit vào mảng T[j]. Mỗi lần xử lý một khối 512 bit. Lặp lại N/16 lần.

- Tư tưởng:

- Thuật toán:

 Kết quả ra là đoạn mã có độ dài 128 bit, được thu gọn từ thông điệp a có độ dài b bit. Đoạn mã này thu được từ 4 thanh ghi A, B, C, D: bắt đầu từ byte thấp của thanh ghi A cho đến byte cao của thanh ghi D

 Trong đó: Vòng 1

 Vòng 2

 Vòng 3

## 4. 5. Chữ ký số

- Khái niệm

- Sơ đồ chữ ký (P, A, K, S, V)

- Phân loại chữký theo đặc trưng kiểm tra chữký

- Chữký khôi phục thông điệp : Là loại chữký, trong đó người gửi chỉcần gửi “chữký”, người nhận có thểkhôi phục lại được thông điệp, đã được “ký” bởi “chữký” này

- Chữký đi kèm thông điệp : Là loại chữký, trong đó người gửi gửi “chữký”, phải gửi kèm cảthông điệp đã được “ký” bởi “chữký” này. Ngược lại, người nhận sẽkhông có được thông điệp gốc

- Phân loại chữký theo mức an toàn

- Chữký “không thểphủnhận” (Chaum - van Antverpen)

- Chữký “một lần”

- Phân loại chữ ký theo ứng dụng đặc trưng

- Chữký “mù” (Blind Signature)

- Chữ ký “nhóm” (Group Signature)

- Chữ ký “bội” (Multy Signature)

- Chữ ký “mù nhóm” (Blind Group Signature)

- Chữ ký “mù bội” (Blind Multy Signature)

## 4. 5. 1 Chữ ký RSA

- Tạo cặp khóa

- Chọn bí mật số nguyên tố lớn p, q , tính n = p * q, công khai n, đặt P = C = Zn

- Tính bí mật phi(n) = (p-1)(q-1) Chọn khóa công khai b < phi(n), nguyên tố với phi(n)

- Khóa bí mật a là phần tử nghịch đảo của b theo mod phi(n): a*b  1 (mod phi(n)

- Tập cặp khóa (bí mật, công khai) ) K = (a, b)/ a, b  Zn , a*b  1 (mod phi(n)).

## 4. 5. Chữ ký số

- Ký số: Chữký trên x là:

- Kiểm tra chữký:

- Tạo cặp khóa (bí mật, công khai) ) (a, b)

## Ví dụ: Chữ ký trên x=2

- Chọn bí mật số nguyên tố lớn p=3, q=5 => n = 15, công khai n, đặt P = C = Zn

- Tính bí mật phi(n) = (p-1)(q-1) = 8 Chọn khóa công khai b =3.

- Khóa bí mật a là phần tử nghịch đảo của b theo mod phi(n): a*b  1 (mod phi(n) => a=3

- Chữ ký trên x=2 là:

- Kiểm tra chữ ký:

- Độ an toàn

- Các cách gửi chữký:

o TH1: Ký trước, Mã hóa sau

 o TH2: Mã hóa trước, Ký sau

- H lấy trộm được thông tin trên đường truyền :

- TH1: H có được z, để giả mạo chữ ký y thì phải giải mã được z

- TH2: H có được (u, v), để giả mạo chữ ký v thì H đã có sẵn và thay đổi v thành v’=SigH(u) rồi gửi (u, v’)

cho N => TH2 thì H có thể giả mạo chữ ký mà không cần giải mã

- Kết luận: Ký trước rồi mã hóa cảchữký

## 4. 5. 2 Chữ ký Elgamal

- Tạo cặp khóa:

- Chọn số nguyên tố p sao cho bài toán logarit rời rạc trong Zp là “khó” giải

- Chọn phần tử nguyên thuỷ g Zp*. Đặt P = Z p*, A = Z p* x Z p-1.

- Chọn khóa bí mật là a Zp*

- Tính khóa công khai

- Tập khóa K = {p, g, a, h}, với p, g, h công khai; a bí mật

## 4. 5. Chữ ký số

- Ký số: Dùng khóa a và khóa ngẫu nhiên bí mật rZp-1* => Chữký trên x P là:

- Kiểm tra chữký:

Nếu chữký được tính đúng thì kiểm thửsẽ thành công.

## Ví dụ: Chữký Elgamal trên dữliệu x = 112

- Tạo cặp khóa (bí mật, công khai) ) (a, h)

- Chọn số nguyên tố p=463, Đặt P = Z p*, A = Z p* x Z p-1

- Chọn phần tử nguyên thuỷ g = 2 Zp*.

- Chọn khóa bí mật a = 211 Zp*.

- Tính khóa công khai

- Chọn ngẫu nhiên r = 235 Zp-1*.

- Chữ ký trên dữ liệu x = 112 là ( , ) = (16, 108) với

- Kiểm tra chữ ký:

= > chữ ký là đúng

- Độ an toàn

- Vấn đề giả mạo chữ ký Elgamal :

o TH1: Giả mạo chữ ký không cùng với tài liệu được ký. H cố gắng giả mạo chữ ký trên x, mà không biết khóa bí mật a. H phải tính được  và 

- Nếu chọn trước , H phải tính  theo:

- Nếu chọn trước , H phải tính  theo Hiện nay chưa có cách hữu hiệu 2 trường hợp trên.

## phỏng đoán là khó hơn bài toán logarit rời rạc

 o TH2: Giả mạo chữ ký cùng với tài liệu được ký.

H có thể ký trên tài liệu ngẫu nhiên bằng cách chọn trước đồng thời x, ,  .

Với TH này có 2 cách giả mạo, tuy nhiên không phải tài liệu nào mà người giả mạo cũng được chấp nhận => trong thực tế ít người sử dụng

- Vấn đềPhá khóa theo sơ đồElgamal :

Khoá bí mật a có thểbịphát hiện, nếu khóa ngẫu nhiên r bịlộ, hoặc dùng r cho hai lần ký khác nhau

## 4. 5. 3 Chữ ký DSS

- Giới thiệu :

- Chuẩn chữ ký số (DSS: Digital Signature Standard)

được đề xuất năm 1991

- Là cải biên của sơ đồ chữ ký ElGamal .

- Độ dài chữ ký theo sơ đồ Elgamal là gấp đôi số bit

## của p. Trong khi ứng dụng dùng thẻ thông minh

(Smart card) lại mong muốn có chữ ký ngắn

## 4. 5. Chữ ký số

- Sơ đồChuẩn chữký số DSS :

- Tạo cặp khóa (bí mật, công khai) (a, h)

- Chọn số nguyên tố p sao cho bài toán logarit rời rạc trong Zp là “khó” giải

- Chọn q là ước nguyên tố của p-1 . Tức là p-1 = t * q hay p = t * q + 1

- Chọn g Zp* là căn bậc q của 1 mod p, (g là phần tử sinh của Zp* ). Tính = g^t , chọn khóa bí mật a Zp*, tính khóa công khai:

- Tập khóa K = {p, q, , a, h }, với p, g, h công khai; a bí mật

- Ký số: Dùng khóa a và khóa ngẫu nhiên bí mật rZq* => Chữký trên x P là:

- Kiểm tra chữký: Với thì

## Ví dụ : Chữký DSS trên dữliệu x = 1246

- Tạo cặp khóa (bí mật, công khai) ) (a, h)

- Chọn số nguyên tố p=7649, q=239 là ước nguyên tố của p-1 => t=32

- Chọn phần tử nguyên thuỷ g = 3 Zp* là phần tử sinh

- Chọn khóa mật a = 85, khóa côg khai h là:

- Ký số

- Dùng 2 khóa ký: a và khóa ngẫu nhiên r = 58 Z q* =>

- Chữ ký trên x = 1246 là Sig k’ (x, r) = (, ) = =(115, 87)

- Kiểm tra chữ ký số = > chữ ký là đúng

- Nhận xét:

- !=0 (mod q) đểbảo đảm có -1 mod q trong điều kiện kiểm thử

- Thay vì tính p trước rồi mới tính q, ta sẽtính q trước rồi tìm p

- Nếu dùng chữký RSA với thành phần kiểm thửchữ ký là nhỏ, thì việc kiểm thửnhanh hơn việc ký. Đối với DSS, ngược lại, việc ký nhanh hơn kiểm thử

- Một tài liệu chỉđược ký một lần, nhưng nó lại được

## kiểm thửnhiều lần, nên người ta muốn thuật toán

kiểm thửnhanh hơn.

## 4. 5. 4 Chữ ký không thể phủ định

## 4. 5. 4. 1. Giới thiệu

- Trong các sơ đồtrước, việc kiểm thửtính đúng đắn của chữký là do người nhận thực hiện.

- Nhằm tránh việc nhân bản chữký đểsửdụng nhiều lần, tốt nhất là đểngười gửi tham gia trực tiếp vào việc kiểm thửchữký. Điều đó được thực hiện bằng một giao thức kiểm thử, dưới dạng một giao thức mời hỏi và trảlời

## 4. 5. Chữ ký số

- Vấn đề :

Giả sử tài liệu cùng chữ ký từ G gửi đến N. Khi N yêu cầu G cùng kiểm thử chữ ký, thì một vấn đề nảy sinh là làm sao để ngăn cản G chối bỏ một chữ ký mà anh ta đã ký, G có thể tuyên bố rằng chữ ký đó là giả mạo ?

- Giải quyết :

Cần có thêm giao thức chối bỏ, bằng giao thức này, G có thể chứng minh một chữ ký là giả mạo. Nếu G từ chối tham gia vào giao thức đó, thì có thể xem rằng G không chứng minh được chữ ký đó là giả mạo

## 4. 5. 4. 2 Sơ đồ chữ ký không thể phủ định

(Chaum - van Antverpen)

- Tạo các tham số

- Chọn số nguyên tố p sao cho bài toán logarit rời rạc trong Zp là “khó” giải. Nên chọn p = 2 * q + 1 với q cũng là số nguyên tố

- Gọi P’ là nhóm nhân con của Zp* theo q. Chọn phần tử sinh g của nhóm P’ cấp q. Tính:

- Đặt P = A = P’

- K = (p, g, a, h): a Z q*

## 4. 5. Chữ ký số

- Thuật toán ký: Dùng khoá bí mật k’ = a để ký lên x => Chữ ký là:

- Giao thức kiểm thử: Dùng khoá công khai k” = (p, g, h). Với x, y P, người nhận N cùng người gửi G thực hiện giao thức kiểm thử

- Giao thức chối bỏ

## Ví dụ: Ký trên x = 229

- Chuẩn bịcác tham số

- Chọn số nguyên tố p = 467 = 2 * q + 1, q = 233 cũng là số nguyên tố

- Chọn phần tử sinh của nhóm P’ là g = 4

- Chọn khóa mật a = 121=> Khóa công khai:

- Đặt P = A = P’

- K = (p, g, a, h): a Z q*

- Thuật toán ký: Dùng khoá bí mật k’ = a để ký lên x = 229 => Chữ ký là:

- Giao thức kiểm thử: Dùng khoá công khai k” = (p, g, h) = (467, 4, 422)

- Giao thức chối bỏ: Giả sử G gửi tài liệu x = 226 với chữ ký y = 183. Giao thức chối bỏ thực hiện:

 Thank You !

www.themegallery.com
