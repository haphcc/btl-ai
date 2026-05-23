### BÀI 3

#### CHƯƠNG 3 MÔ HÌNH HỒI QUY NHUNG LE

## TRANG 1

## CHƯƠNG 3

## MÔ HÌNH HOI QUY

## TRANG 2

## Nội dung

3.1. Tổng quan về hồi qui 3.2. Hồi qui tuyến tính 3.3. Hồi qui phi tuyến 3.4. Ứng dụng 3.5. Các vấn đề với hồi qui 3.6. Tóm tắt

## TRANG 3

Tài liệu tham khảo

 [1] J. Han and M. Kamber, Data Mining, “Concepts and Techniques”,

Morgan Kaufmann, 3rd Edition, 2011

 [2] Ian H. witten, Eibe Frank, and Marker Hall, “Data Mining - Practical

Machine Learning Tools and Techniques”, Morgan Kaufmann, 2011

 [3] Daniel T. Larose, Discovering Knowledge in Data - An introduction

to Data Mining, John Wiley & Sons, 2005

 [4] Max Bramer, “Principles of Data Mining”, Springer, 2007

 [5] Ho Tu Bao, “Introduction to Knowledge Discovery and Data

Minning”, National Center of Natural Science a Technology, 2010

## TRANG 4

3.0. Tình huống 1

Ngày mai giá cổ phiếu STB sẽ là bao nhiêu???

## TRANG 5

3.0. Tình huống 2

y Y1

Y1’ y = x + 1

X1 x

Mô hình phân bố dữ liệu của y theo x???

## TRANG 6

3.0. Tình huống 3

## Bài toán phân tích giỏ hàng thị trường (market basket analysis)

→ sự kết hợp giữa các mặt hàng?

## TRANG 7

3.0. Tình huống 4

Khảo sát các yếu tố tác động đến xu hướng sử dụng quảng cáo trực tuyến tại Việt Nam Sự giải trí cảm nhận (+0.209) Chất lượng thông tin (+0.261) Chất lượng thông tin cảm nhận (+0.199) Sự khó chịu cảm nhận (-0.175) Sự tin cậy cảm nhận Thái độ về tính riêng tư Sự tương tác (+0.373) Chuẩn chủ quan (+0.254) Nhận thức kiểm soát hành vi (+0.377)

## TRANG 8

3.0. Tình huống …

Hồi qui (regression)

Khai phá dữ liệu có tính dự báo (Predictive data mining)

Tình huống

Khai phá dữ liệu có tính mô tả (Descriptive data mining)

Tình huống

## TRANG 9

3.1. Tổng quan về hồi quy

Định nghĩa - Hồi quy (regression)

J. Han et al (2001, 2006): Hồi quy là kỹ thuật thống kê cho phép dự đoán các trị (số) liên tục.

Wiki (2009): Hồi quy (Phân tích hồi quy - regression analysis) là kỹ thuật thống kê cho phép ư ớc lượng các mối liên kết giữa các biến

R. D. Snee (1977): Hồi quy (Phân tích hồi quy) là kỹ thuật thống kê trong lĩnh vực phân tích dữ liệu và xây dựng các mô hình từ thực nghi ệm, cho phép mô hình hồi qui vừa được khám phá được dùng cho mục đích dự báo (prediction), điều khiển (control), hay học (learn) cơ chế đã tạo ra dữ liệu.

## TRANG 10

3.1. Tổng quan về hồi quy

Mô hình hồi quy (regression model): mô hình mô tả mối liên kết (relationship) giữa một tập các biến dự báo (predictor variables/independent variables) và một hay nhiều đáp ứng (responses/dependent variables).

Phân loại

Hồi quy tuyến tính (linear) và phi tuyến (nonlinear)

Hồi quy đơn biến (single) và đa biến (multiple)

Hồi quy có thông số (parametric), phi thông số (nonparametric), và thông số kết hợp (semiparametric)

Hồi quy đối xứng (symmetric) và bất đối xứng (asymmetric)

## TRANG 11

3.1. Tổng quan về hồi quy

Phân loại Hồi quy tuyến tính (linear) và phi tuyến (nonlinear) Linear in parameters: kết hợp tuyến tính các thông số tạo nên Y Nonlinear in parameters: kết hợp phi tuyến các thông số tạo nên Y Hồi quy đơn biến (single) và đa biến (multiple) Single: X = (X1) Multiple: X = (X1, X2, …, Xk)

## TRANG 12

3.1. Tổng quan về hồi qui

Hồi qui có thông số (parametric), phi thông số (nonparametric), và thông số kết hợp (semiparametric) Parametric: mô hình hồi qui với hữu hạn thông số Nonparametric: mô hình hồi qui với vô hạn thông số Semiparametric: mô hình hồi qui với hữu hạn thông số được quan tâm Hồi qui đối xứng (symmetric) và bất đối xứng (asymmetric) Symmetric: mô hình hồi qui có tính mô tả (descriptive) (eg.

log-linear models) Asymmetric: mô hình hồi qui có tính dự báo (predictive) (eg. generalized linear models)

## TRANG 13

3.1. Tổng quan về hồi quy

Phương trình hồi quy: Y = f(X, β)

X: các biến dự báo (predictor/independent variables)

Y: các biến đáp ứng (responses/dependent variables)

β: các hệ số hồi quy (regression coefficients)

→X dùng để giải thích sự biến đổi của các đáp ứng Y.

→Y dùng đề mô tả các hiện tượng (phenomenon) được quan tâm/giải thích.

→Quan hệ giữa Y và X được diễn tả bởi sự phụ thuộc hàm của Y đối với X.

→β mô tả sự ảnh hưởng của X đối với Y.

## TRANG 14

3.2. Hồi qui tuyến tính

Hồi qui tuyến tính đơn biến

Hồi qui tuyến tính đa biến

## TRANG 15

Cho N đối tượng đã được quan sát, mô hình hồi qui tuyến tính đơn biến được cho dưới dạng sau với εi dùng giữ phần biến thiên của đáp ứng Y không được giải thích từ X:

-Dạng đường thẳng

## VD: Y= β0 + β1*X1 → Y = 0.636 + 2.018*X

- Dấu của β1 cho biết sự ảnh hưởng của X đối với Y.

## TRANG 16

Hàm mất mát

## Mục tiêu của mô hình hồi quy là tìm ra một hàm số dự báo

mà giá trị của chúng sai khác so với giá trị biến mục tiêu là

nhỏ nhất

Sai khác này được đo lường thông qua các hàm mất mát (loss

function)

Trong bài toán dự báo chúng ta sẽ sử dụng hàm MSE (Mean

Square Error) làm hàm mất mát

## TRANG 17

3.2.1. Hồi qui tuyến tính đơn biến

Ư ớc lượng bộ thông số β () để đạt được mô hình hồi qui tuyến tính đơn biến

Thặng dư (residual)

Tổng thặng dư bình 𝛽1 = (𝑥 ∗𝑦 −𝑥𝑦)2ph ương (sum of (𝑥)2 −𝑥2 squared residuals) → tối thiểu hóa

Trị ư ớc lượng của β

## TRANG 18

## Bài tập thực hành

chúng ta có 15 căn hộ với diện tích (đơn vị m2) và giá tương ứng (tỉ đồng)

Diện tích 73.5 75 76.5 79 81.5 82.5 84 Giá (tỉ đồng) 1.49 1.5 1.51 1.54 1.58 1.59 1.6 Diện tích 85 86.5 87.5 89 90 91.5 Giá (Tỉ đồng 1.62 1.63 1.64 1.66 1.67 1.68

Xây dựng phương trình hồi qui tuyến tính đơn biến giữa diện tích và giá nhà.

| Diện tích | 73.5 | 75 | 76.5 | 79 | 81.5 | 82.5 | 84 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Giá (tỉ đồng) | 1.49 | 1.5 | 1.51 | 1.54 | 1.58 | 1.59 | 1.6 |
| Diện tích | 85 | 86.5 | 87.5 | 89 | 90 | 91.5 |  |
| Giá (Tỉ đồng | 1.62 | 1.63 | 1.64 | 1.66 | 1.67 | 1.68 |  |

## TRANG 19

3.2.2. Hồi qui tuyến tính đa biến

Hồi qui tuyến tính đa biến: phân tích mối quan hệ giữa biến phụ thuộc (response/dependent variable) và hai hay nhiều biến độc lập (independent variables) yi = b0 + b1xi1 + b2xi2 + … + bkxik i = 1..n với n là số đối tượng đã quan sát k = số biến độc lập (số thuộc tính/tiêu chí/yếu tố…) Y = biến phụ thuộc X = biến độc lập b0 = trị của Y khi X = 0 b1..k = trị của các hệ số hồi qui

## TRANG 20

3.2.2. Hồi qui tuyến tính đa biến

x  + b Trị ước lượng của Y y ˆ = b0 + b1 x1 + b2 x2 + k k

−1 T T Trị ước lượng của b = X X X Y () bộ thông số b

 Y1  1 x1,1 x1,2  x1, k   b0        1 x x Y 2,1 2 2,2  x2, k b1       Y =, X =, b =              x n,1 n,2  xn, k Yn  1 x   bk 

## TRANG 21

24 Thực hành

Quay trở lại bài toán trên, nếu chúng ta thêm thông tin về khoảng cách tới trung tâm.

KCTT (km) = [20,18,17,16,15,14,12,10,8,7,5,2,1]

## TRANG 22

Dự báo hồi quy

a. Dự báo giá trị trung bình:

Cho X =X0, tìm E(Y/X0).

- Dự báo điểm của E(Y/X0) là:

Yˆ = β ˆ + β ˆ X 0 1 2 0 là: - Dự báo khoảng của E(Y/X0)

− X) 2 (n − 2) 1 (X 0 ˆ E(Y / X) = Y  ,  = s t + 0 0 e / 2 2 2 n X − n X 

## TRANG 23

Dự báo hồi quy

b. Dự báo giá trị cá biệt:

Cho X =X0, tìm Y0.

− X) 2 (n − 2) 1 (X 0 ˆ Y = Y  ,  = s t 1 + + 0 0 e / 2 2 2 n X − n X 

## TRANG 24

Y dải tin cậy của giá trị cá biệt

dải tin cậy của giá trị trung bình

X X

Đặc điểm của dự báo khoảng

## TRANG 25

28 Đánh giá MHHQTT đa biến

Ngoài MSE là hàm mất mát dùng để làm mục tiêu tối ưu loss function thì chúng ta có thể dựa trên nhiều chỉ số khác để đánh giá một mô hình hồi qui tuyến tính đa biến, trong đó phổ biến sử dụng 2 loại chỉ số sau:

• Chỉ số R-squared • Chỉ số MAE và MAPE

## TRANG 26

29 Chỉ số R_Squared

R-squared cho ta biết mức độ các biến đầu vào sẽ giải thích được bao nhiêu phần trăm các biến mục tiêu.

R-squared càng lớn thì mô hình càng tốt.

Miền xác định của R2:

0  R2  1 R2 → 1: hàm hồi qui càng phù hợp.

R2 → 0: hàm hồi qui càng ít phù hợp

## TRANG 27

30 Chỉ số R_Squared

R-squared được xây dựng dựa trên ba chỉ số:

Trong đó:

TSS: Tổng bình phương sai số (Total sum squared) RSS: Tổng bình phương sai số ngẫu nhiên (Residual sum squared) ESS: Tổng bình phương sai số được giải thích bởi mô hình (Explained sum squared)

## TRANG 28

31 Chỉ số R_Squared

Bằng toán học chứng minh được rằng:

## TSS= RSS+ESS

## 𝐸𝑆𝑆 𝑅𝑆𝑆

R_Squared = 𝑇𝑆𝑆= 1 − 𝑇𝑆𝑆

## TRANG 29

32 Chỉ số MAE

MAE là chỉ số đo lường trung bình trị tuyệt đối sai số giữa giá trị dự báo và giá trị thực tế.

Khi MAE càng nhỏ thì khoảng cách giữa giá trị dự báo và giá trị thực tế càng nhỏ và mô hình càng tốt.

Tuy nhiên giá trị MAE không bao hàm được sự khác biệt về mặt đơn vị

## TRANG 30

33 Chỉ số MAPE

Để loại bỏ sự khác biệt về đơn vị MAPE (mean absolute percentage error) là chỉ số đo lường tỷ lệ phần trăm sai số giữa giá trị dự báo và giá trị thực tế

Ví dụ: Khi một mô hình có MAPE=5% ta nói rằng mô hình có trung bình sai số là 5% so với giá trị trung bình.

## TRANG 31

34 Hiện tượng overfitting

Overfitting là hiện tượng mà mô hình chỉ khớp tốt trên tập dữ liệu huấn luyện nhưng không dự báo tốt trên dữ liệu kiểm tra.

Có nhiều nguyên nhân dẫn tới Overfitting.

• Tập dữ liệu huấn luyện và dữ liệu dự báo có phân phối khác xa nhau dẫn tới các qui luật học được ở dữ liệu huấn luyện không còn đúng trên dữ liệu dự báo.

• Mô hình có quá nhiều tham số nên khả năng biểu diễn dữ liệu của nó không mang tính đại diện.

## TRANG 32

35 Hiện tượng overfitting

Regularization là kĩ thuật tránh overfiting bằng cách cộng thêm vào loss function thành phần hiệu chuẩn • Ridge regression • Lasso regression

## TRANG 33

36 Overfitting

✓Trong trường hợp dữ liệu bịqu á khớp nặng thì cần giảm quá khớp bằng cách gia tăng ảnh hưởng của thành phần điều chuẩn (regularization term) thông qua tăng hệsố𝛼.

✓Nếu mô hình không bịqu á khớp thì có thểl ựa chọn 𝛼g ần 0. Trường hợp 𝛼=0 thì phương trình hồi qui tương đương với hồi qui tuyến tính đa biến.

## TRANG 34

3.3. Hồi qui phi tuyến

Y = f(X, β)

Hồi quy là phi tuyến tính khiít nhất một trong các tham số của nó xuất hiện phi tuyến tính

Ví dụ: hàm mũ, hàm logarit, hàm Gauss, …

Xác định bộ thông số β tối ưu: các giải thuật tối ưu hóa

Tối ưu hóa cục bộ

Tối ưu hóa toàn cục cho tổng thặng dư bình phương (sum of squared residuals)

37

## TRANG 35

38 3.3. Hồi qui phi tuyến

Mô hình hồi quy phi tuyến đượcứng dụng nhiều nhất là Hồi quy logistic f (x) = logit (x) = log (x / (1-x)) Ngoài ra còn có các hàm như:

Michaelis-Menten: y = ax / (1 + bx) Hàm mũ 2 tham số tiệm cận: y = a (1 - e-bx) Cấp số nhân tiệm cận 3 tham số: y = a−be−cx

## TRANG 36

39 3.4. Ứng dụng

Quá trình khai phá dữ liệu ➢Giai đoạn tiền xử lý dữ liệu ➢Giai đoạn khai phá dữ liệu ✓Khai phá dữ liệu có tính mô tả ✓Khai phá dữ liệu có tính dự báo

Các lĩnh vựcứng dụng:

➢Tài chính: Mô hình tài sản giá vốn sử dụng hồi quy tuyến tính để phân tích và định lượng rủi ro hệ thống của một khoản đầu tư.

➢Sinh học: Hồi quy tuyến tính được sử dụng để mô hình hóa mối quan hệ nhân quả giữa các thông số trong hệ thống sinh học.

## TRANG 37

40 3.4. Ứng dụng

Đường xu hướng: Đường xu hướng biểu thịs ựthay đổi của một số dữ liệu định lượng theo thời gian (như GDP, giá dầu, v. v.). Các xu hướng này thường tuân theo một mối quan hệtuy ến tính. Do đó, hồi quy tuyến tính có thểđược áp dụng đểd ựđo án các giá trịtrong tương lai. Tuy nhiên, phương pháp này thiếu giá trị khoa học trong trường hợp các thay đổi tiềm ẩn khác có thểảnh hưởng đến dữ liệu.

Kinh tế học: Hồi quy tuyến tính là công cụth ực nghi ệm chủy ếu trong kinh tế học.

Ví dụ: nó được sử dụng đểd ựđo án chi tiêu tiêu dùng, chi tiêu đầu tư cố định, đầu tư hàng tồn kho, mua hàng xuất khẩu của một quốc gia, chi tiêu cho nhập khẩu, nhu cầu nắm giữt ài sản lưu động, nhu cầu lao động và cung lao động.

## TRANG 38

41 3.5. Các vấn đề với hồi qui

Các giả định (assumptions) đi kèm với bài toán hồi qui.

Lượng dữ liệu được xử lý.

Đánh giá mô hình hồi qui.

Các kỹ thuật tiên tiến cho hồi qui:

Artificial Neural Network (ANN)

Support Vector Machine (SVM)

## TRANG 39

42 3.6. Tóm tắt

Hồi qui

Kỹ thuật thống kê, được áp dụng cho các thuộc tính liên tục (continuous attributes/features)

Có lịch sử phát triển lâu đời

Đơn giản nhưng rất hữu dụng, đượcứng dụng rộng rãi

Cho thấy sự đóng góp đáng kể của lĩnh vực thống kê trong lĩnh vực khai phá dữ liệu

Các dạng mô hình hồi qui: tuyến tính/phi tuyến, đơn biến/đa biến, có thông số/phi thông số/thông số kết hợp, đối xứng/bất đối xứng

## TRANG 40

Ẽ

## [BaV |HocviỆN\=E NGÂN HÀNG
