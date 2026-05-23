### BÀI 4

#### CHUONG 4 PHAN LOP DU LIEU

## CHƯƠNG 4: PHÂN LỚP DỮ LIỆU

## THS. AN PHƯƠNG ĐIỆP T: 093 621 5087

## Chương 3: Phân lớp dữ liệu

1. Tổng quan về phân lớp dữ liệu

2. Các thuật toán phân lớp dữ liệu

3. Phân lớp với cây quyết định

Tình huống phân lớp 1

Ông A (Tid = 100) có khả năng gian lận???

Tình huống phân lớp 2

Với thông tin của một applicant A, xác định liệu ngân hàng có cho 23/05/2026A vay không? Khoa Công nghệ thông tin và kinh tế số 44

Tình huống tổng quát

• Cho trước tập huấn luyện (training set) được chia thành 2 lớp: class A, class B.

• Đối với mẫu/đối tượng mới, làm sao xác định class cho mẫu/đối tượng đó?

• Liệu class đó có thực sựph ù hợp/đúng cho mẫu/đối tượng đó?

Phát biểu bài toán phân lớp dữ liệu

Phân lớp dữ liệu là quá trình học có giám sát trên một tập dữ liệu đầu vào nhằm xây dựng một mô hình đểcó thểd ựđo án xu hướng cho các dữ liệu mới.

• Đầu vào: Tập các dữ liệu có dạng (x,y) = (x1,x2,…,xn, y)

- x là biến độc lập (Independent variable) mô tảcác thuộc

tính của một đối tượng.

- y là biến phụthuộc (Dependent variable) cần tìm hiểu,

phân loại. y còn gọi là thuộc tính nhãn.

• Đầu ra: Một mô hình có khả năng phân loại đúng đắn cho tập các dữ liệu đầu vào.

Quy trình thực hiện phân lớp dữ liệu

Bước học (bước huấn luyện): Xây dựng mô hình • Xác định tập dữ liệu huấn luyện gồm các mẫu đã được gán nhãn y.

• Chạy một thuật toán phân lớp trên tập dữ liệu huấn luyện.

• Mô hình được biểu diễn dưới dạng các luật phân lớp, các cây quyết định hoặc các công thức toán.

Bước phân loại: Sử dụng mô hình: đểg án nhãn thích hợp cho các dữ liệu chưa được gán nhãn.

• Ư ớc lượng độchính xác của mô hình:

- Xác định tập dữ liệu kiểm thửgồm các mẫu đã được gán nhãn y (dữ

liệu kiểm thửvà dữ liệu huấn luyện phải khác nhau đểtr ánh tình trạng quá khớp over-fitting)

- Chạy mô hình với tập dữ liệu kiểm thửthu được nhãn y’

- So sánh y vày’ đểxác định độchính xác của mô hình.

• Nếu mô hình chính xác, sử dụng nó đểd ựđo án nhãn cho các dữ liệu cần gán nhãn.

Quy trình thực hiện phân lớp dữ liệu

Bước 1 - Xây dựng mô hình

Bước 2 - Sử dụng mô hình

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1010

Các loại phân lớp

Phân lớp nhịph ân/ đa lớp • |C| = 2: phân lớp nhịph ân.

Giá trị của thuộc tính nhãn gồm: Có mua hay không mua máy tính?

• |C| > 2: phân lớp đa lớp.

Giá trị của thuộc tính nhãn gồm: Thểthao, Chính trị, Văn hóa, Sức khỏe.

Phân lớp đơn nhãn/ đa nhãn • Đơn nhãn: mỗi mẫu được gán duy nhất vào một lớp.

Tất cảcác mẫu dữ liệu chỉcó một và chỉmột giá trịnh ãn.

• Đa nhãn: một mẫu có thểđược gán nhiều hơn một lớp.

Một bài báo có thểv ừa được gán nhãn Thểthao vừa được gán nhãn Sức khỏe.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1111

Các thuật toán phân lớp dữ liệu

Nhóm thuật toán dựa trên xác suất và lý thuyết thông tin • Phân lớp Na ïve Bayes.

• Phân lớp cực đại Entropy Nhóm thuật toán dựa trên cây • Phân lớp dựa trên cây quyết định.

• Phân lớp rừng ngẫu nhiên (Ra ndom Forest) Nhóm thuật toán dựa trên hồi quy • Hồi quy tuyến tính.

• Hồi quy logistic Nhóm thuật toán dựa trên khoảng cách • Phân lớp K láng giềng gần nhất.

• Phân lớp sử dụng máy vecto hỗtr ợSVM • Phân lớp Rocchio Nhóm thuật toán khác • Mạng Neural...

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1212

Phân lớp dữ liệu với cây quyết định

Cây quyết định mô tảmột cấu trúc cây, cho phép người dùng dự đoán nhãn của một đối tượng mới dựa trên tập thuộc tính của nó. Trong đó:

• Các lá đại diện cho các nhãn • Các cành đại diện cho các kết hợp của các thuộc tính dẫn tới phân lớp đó.

Ưu điểm:

• Dễhi ểu, người dùng có thểnhanh chóng hiểu được các luật của cây quyết định.

• Có thể xử lý cả dữ liệu có giá trịb ằng số và dữ liệu có giá trịl à tên thểlo ại.

• Có thểth ẩm định mô hình bằng các kiểm tra thống kê, điều này làm tăng độ tin tưởng của người dùng vào mô hình.

• Có thể xử lý tốt một lượng dữ liệu lớn trong thời gian ngắn…

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1313

Dữ liệu mẫu huấn luyện cây quyết định

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1414

Ví dụ minh họa cây quyết định “buys- computer”

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1515

Xác định các luật phân lớp từc ây quyết định

Ta có thểd ễd àng biểu diễn tri thức thu được từc ây quyết định dưới dạng các luật

## IF-THEN

Mỗi đường đi từn út gốc đến nút lá tương ứng với một luật Giá trị của các thuộc tính trên một đường đi sẽ tạo thành các điều kiện trong IF Nút lá xác định lớp dự đoán trong THEN Ví dụ:

• IF age = “<= 30” AND student=“no” THEN buys_computer = “no” • IF age = “31..40” THEN buys_computer = “yes”

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1616 • IF age= “&gt;40” AND credit_rating=“fair” THEN

Các thuật toán xây dựng cây quyết định

Thuật toán CLS: Được Hovland và Hint giới thiệu vào những năm 50 của thếk ỷ20, theo chiến lược chia đểtr ịt ừtr ên xuống.

Thuật toán ID3: được công bốb ởi Quinlan (trường đại học Syney, Australia) vào cuối thập niên 70 của thếk ỷ20.

• ID3 được xem như là một cải tiến của CLS với khả năng lựa chọn thuộc tính tốt nhất đểti ếp tục triển khai cây tại mỗi bước.

• ID3 xây dựng cây quyết định theo hướng tiếp cận từtr ên - xuống (top-do wn).

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1717

Các thuật toán xây dựng cây quyết định

Thuật toán C4.5: Thuật toán C4.5 được phát triển và công bốb ởi Quinlan vào năm 1996.

• Là một cải tiến từthu ật toán ID3 với việc cho phép xử lý trên tập dữ liệu có các thuộc tính số (numeric atributes) và làm việc được với tập dữ liệu bịthi ếu, bịnhi ễu.

• Nó thực hiện phân lớp tập mẫu dữ liệu theo chiến lược ưu tiên theo chiều sâu (Depth - First).

Thuật toán Ra ndom Forest

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1818

Các thuật toán xây dựng cây quyết định

Thuật toán SLIQ: Được gọi là thuật toán phân lớp leo thang nhanh.

• Có thểáp dụng cho cảhai kiểu thuộc liên tục và thuộc tính rời rạc.

• Sử dụng kỹ thu ật tiền xử lý phân loại (Presorting) trước khi xây dựng cây, do đó giải quyết được vấn đềb ộnh ớcho thuật toán ID3.

• Có sử dụng giải thuật cắt tỉa cây hữu hiệu, phù hợp với các tập dữ liệu lớn.

Thuật toán J4.8 Thuật toán CART … 23/05/2026 Khoa Công nghệ thông tin và kinh tế số 1919

Thuật toán ID3

ID3 là thuật toán cơ bản nhất trong lĩnh vực học cây quyết định, hầu hết các thuật toán học cây quyết định cải tiến sau này đều dựa trên nó.

Nhiệm vụcủa ID3 là học cây quyết định từ một tập các mẫu huấn luyện gồm:

• Đầu vào: Một tập hợp các mẫu, mỗi mẫu bao gồm các thuộc tính mô tảmột đối tượng xác định và một thuộc tính nhãn phân lớp giá trị của nó.

Chú ý: Nếu các thuộc tính có giá trịli ên tục, ví dụTu ổi, ta phải tiến hành biến đổi chúng thành các giá trịr ời rạc, ví dụ chia tuổi thành 3 loại: Trẻ, Trung niên, Già.

• Đầu ra: Cây quyết định có khả năng phân loại

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2020 đúng đắn các mẫu trong tập dữ liệu huấn luyện ả ẫ

Thuật toán ID3(D,C,A)

Đầu vào: Tập mẫu huấn luyện D, thuộc tính phân lớp C, thuộc tính mô tảA.

Đầu ra: Cây quyết định.

Thuật toán:

• B1: Tạo Nút_g ốc cho cây quyết định.

• B2: IF tất cả các mẫu huấn luyện đều có giá trị của nhãn C làP, RETURN cây có một nút duy nhất là Nút_g ốc với nhãn P.

• B3: IF A rỗng, RETURN cây có một nút duy nhất là Nút_g ốc với nhãn là giá trịph ổbi ến nhất của C trong D.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2121

Thuật toán ID3(D,C,A)

• B4: 4.1 Gọi X là thuộc tính của A phân lớp D tốt nhất.

4.2 Gán nhãn cho nút gốc với tên thuộc tính X 4.3 FOREACH giá trị𝑣của X 4.3.1 Thêm một nhánh mới dưới Nút_g ốc với X=v 4.3.2 Xác định tập con Dvứng với X=v 4.3.3 IF Dv rỗng Thêm dưới nhánh mới này một nút lá có nhãn là giá trịph ổbi ến nhất của thuộc tính quyết định trong D

## ELSE

23/05/2026 Khoa Thêm Công nghệc âythông tinconvà kinh tếvàosố dưới nhánh này2222

Cách xác định thuộc tính nút tốt nhất?

Vấn đềquan trọng nhất của thuật toán ID3 là chọn lựa được thuộc tính tốt nhất đểđ ưa vào các nút của cây.

• Sử dụng kết quảcủa lý thuyết thông tin là các độđo Entropy và Infomation Gain.

Entropy có giá trịn ằm trong đoạn [0..1] để đo tính thuần nhất (hay ngược lại là độpha trộn) của một tập hợp.

• Entropy = 0: Tất cảcác phần tửcủa tập hợp đều thuộc cùng một loại, khi đó ta nói tập hợp này là thuần nhất hoặc có độpha trộn là thấp nhất. Khi tập mẫu là thuần nhất thì ta có thểbi ết chắc chắn về giá trịph ân loại của một mẫu thuộc tập

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2323 này, hay ta có lượng thông tin (infomation gain) về tập đó là cao nhất

Cách xác định thuộc tính nút tốt nhất?

• Entropy = 1: Tập mẫu có độpha trộn cao nhất, nghĩa là số lượng các mẫu có cùng giá trịph ân loại là tương đương nhau, khi đó ta không thể đoán chính xác một mẫu có thểcó giá trịph ân loại gì, hay nói khác hơn, lượng thông tin ta có được về tập này là ít nhất.

• 0 < Entropy < 1: Số lượng các mẫu có giá trịph ân loại khác nhau là khác nhau.

Ta phải lựa chọn thuộc tính sao cho có thể chia tập mẫu ban đầu thành các tập mẫu thuần nhất càng nhanh càng tốt.

---&gt; Chọn thuộc tính với độl ợi thông tin (information gain) lớn nhất.23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2424

Độl ợi thông tin - Information Gain

Lượng thông tin kỳv ọng đểph ân lớp một

## phần tử trong tập dữ liệu D- Entropy của D:

• Với pi là xác suất một phần tử dữ liệu trong D thuộc vào lớp Ci.

Di là tập các phần tử dữ liệu trong D thuộc vào lớp Ci.

• m là số lượng các lớp trong D

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2525

Độl ợi thông tin - Information Gain

Giả sử dữ liệu trong D được phân chia theo một thuộc tính A, thuộc tính này có v giá trị rời rạc khác nhau {a1, a2,…,av} • D được chia thành v tập con {D1, D2,…,Dv} với Dj là tập các phần tửcó giá trị của thuộc tính A là ai.

• Mỗi tập con Dj sẽtương ứng với một nhánh trong cây.

• Dj càng đồng nhất càng tốt, tức là các phần tử trong tập con này đều cùng thuộc về một lớp.

• Cần đo lượng thông tin kỳv ọng đểph ân lớp chính xác các tập con.

• Giá trịn ày càng nhỏth ì độđồng nhất của các tập 23/05/2026con càng cao. Khoa Công nghệ thông tin và kinh tế số 2626

Độl ợi thông tin - Information Gain

Công thức đo độl ợi thông tin:

- Info(D): Lượng thông tin kỳ vọng để phân lớp một phần tử

trong tập dữ liệu D.

- InfoA(D): Lượng thông tin kỳ vọng để phân lớp chính xác các

tập con của thuộc tính A.

• Giá trịGain(A) cho biết độl ợi khi chia dữ liệu theo thuộc tính A.

• Gain(A) càng lớn càng tốt.

• Thuộc tính nào có Gain lớn nhất sẽ được chọn để phân nhánh trong quá trình xây dựng cây quyết định.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2727

Ví dụminh họa

➢Thuộc tính phân lớp C (buys_computer) gồm m = 2 giá trị: yes, no.

➢Trong D có 9 phần tửmang nhãn yes, 5 phần tử mang nhãn no.

Ta có:

• Tính lượng thông tin kỳv ọng của age gồm 3 giá trị: {“<=30”: 2 nhãn yes, 3 nhãn no}; {“31..40”: 4 nhãn yes, 0 nhãn no}; {“&gt;40”: 3 nhãn yes, 2 nhãn no}.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2828

Ví dụminh họa

Chọn “age” làm thuộc tính phân nhánh:

A={income, student, credit_rating}??

?

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 2929

Ví dụminh họa

## D<=30

Xét nhánh “<=30”:

• Tính entropy của D<=30:

3 3 2 2 − log2 − log2 = 0.971 Info(D<=30) = 5 5 5 5 • Tính lượng thông tin kỳv ọng của các thuộc tính:

2 2 2 2 1 1 1 1 1 1 1 − log2 log2 log2 log2 Infoincome(D<=30) = 5(− 2 2) + 5(− 2 2 2 2) + 5(− 1 1) = 0.4 3 3 3 2 2 2 log2 log2 Infostudent(D<=30) = 5(− 3 3) + 5(− 2 2) = 0 3 2 2 1 1 2 1 1 1 1 − - log2 log2 log2 log2 Infocredit_rating(D<=30) = 5(− 3 3 3 3) + 5(− 2 2 2 2) = 0.811 • Tính độl ợi thông tin của các thuộc tính:

Gain(income)=0.971-0.4=0.371; Gain(student)=0.971;

Gain(credit_rating)= 0.16 ---&gt; Chọn Student là thuộc tính phân nhánh 23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3030

Ví dụminh họa

??

Dno Dyes

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3131

Ví dụminh họa

A={income,?? student, credit_rating}

no yes

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3232

Ví dụminh họa

## D31..40

Xét nhánh “31..40”:

• Trong D31..40 tất cả các mẫu đều có nhãn “yes” ---&gt; Gán nhãn “yes” cho nút lá

A={income, student, credit_rating}? yes

yes no 23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3333

Ví dụminh họa

## D&gt;40

Xét nhánh “&gt;40”:

• Tính entropy của D&gt;40:

3 3 2 2 − log2 − log2 = 0.971 Info(D&gt;40) = 5 5 5 5 • Tính lượng thông tin kỳv ọng của các thuộc tính:

3 2 2 1 1 2 1 1 1 1 − - log2 log2 log2 log2 Infoincome(D&gt;40) = 5(− 3 3 3 3) + 5(− 2 2 2 2) = 0.4 2 1 1 1 1 3 2 2 1 1 − - log2 log2 log2 log2 Infostudent(D&gt;40) = 5(− 2 2 2 2) + 5(− 3 3 3 3) = 0.634 3 3 3 2 2 2 log2 log2 Infocredit_rating(D&gt;40) = 5(− 3 3) + 5(− 2 2) = 0 • Tính độl ợi thông tin của các thuộc tính:

Gain(income)=0.971-0.4=0.371; Gain(student)= 0.634;

Gain(credit_rating)= 0.971 ---&gt; Chọn credit_rating là thuộc tính phân nhánh

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3434

Ví dụminh họa

Xét nhánh “&gt;40”:

yes

no yes

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3535

Ví dụminh họa

Xét nhánh “&gt;40”:

yes

yes no yes no

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3636

Đểx ác định máy học đúng thì làm thến ào?

Giống như con người kết quả của quá trình học sẽ được kiểm tra, đánh giá.

Mô hình học máy cũng được kiểm tra, đánh giá để xác định hiệu quả của mô hình học.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3737

Một số thu ật ngữđ ánh giá mô hình học

Overfitting Chính xác trên tập huấn luyện nhưng lại kém chính xác trên tập dữ liệu mới (tập kiểm tra).

Underfitting Normal-fit Không tốt trên Khi mà mô hình ở cả tập dữ liệu trạng thái tối ưu huấn luyện và giữa overfitting tập dữ liệu kiểm và underfitting.

tra

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3838

Kiểm thử mô hình

Chạy thử mô hình đã được xây dựng trên một bộ dữ liệu test.

Các phương pháp xác định dữ liệu test:

Training Set Test Set 70 % 30%

Cross Test Set Training Set Validation 20% 60 % Set 20%

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 3939

Kiểm thử mô hình

• Kiểm thửch éo K-Folds: tập dữ liệu được chia ngẫu nhiên thành k tập (folds) có kích thước xấp xỉ và không giao nhau D1, D2,…,Dk Quá trình huấn luyện và kiểm thửs ẽđược thực hiện k lần.

Tại lần lặp thứi tập dữ liệu Di được dùng làm dữ liệu test, (k-1) tập dữ liệu còn lại được gộp thành tập dữ liệu huấn luyện.

Đảm bảo tính ngẫu nhiên và tính chính xác do bất kỳph ần tửn ào cũng được làm dữ liệu test một lần, làm dữ liệu huấn luyện (k-1) lần.

Kết quảđ ánh giá cuối cùng sẽ được tổng hợp lại từk kết quảth ực nghi ệm

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4040

Độchính xác của mô hình phân lớp

Trong bài toán phân lớp, sau khi mô hình đưa ra được kết quảd ự đoán của mình, làm thến ào có thểbi ết rằng mô hình đã dự đoán chính xác hay không?

Tuy nhiên trong thực tế, mô hình có độchính xác cao là chưa đủ, nó có thểv ẫn gây ra những sai lầm nghiêm trọng khi trong số

## phần trăm thấp còn lại dự đoán nhầm mà lớp nhầm đó có ý nghĩa

quan trọng hơn.

▪Việc dự đoán nhầm email quan trọng thành email spam nguy hiểm hơn là bỏ sót email spam.

▪Trong bài toán chuẩn đoán ung thư, nếu 100 người cần chuẩn đoán có 10 người bịung thư mà mô hình dự đoán cả100 người không bịung thư thì độ chính xác mô hình là 90%, khá cao. Nhưng việc bỏqua 10 người bịung thư thì mô hình không còn đáng tin cậy.

→Đánh giá độchính xác của mô hình sử dụng Ma trận nhầm lẫn

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4141

Ma trận nhầm lẫn

Đểđ ánh giá độchính xác của mô hình phân lớp ta xác định các giá trị của ma trận nhầm lẫn (confusion matrix) sau:

Lớp thực tế Lớp được dự đoán bởi mô hình

Positive Negative

Positive TP FN (sai lầm loại 2)

Negative FP (sai lầm loại I) TN • TP (true positive): Thực tếl à lớp positive và được dự đoán đúng lớp positive.

• TN (true negative): Thực tếl à lớp negative và được dự đoán đúng lớp negative.

• FP (false positive): Thực tếl à lớp negative nhưng bịd ự đoán nhầm sang lớp positive.

• FN (false negative): Thực tếl à lớp positive nhưng bịd ự đoán nhầm sang lớp negative.

Sai lầm loại 1: Bác bỏgi ảthi ết khi giảthi ết đúng 23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4242 Sai lầm loại 2: Không bác bỏgi ảthi ết khi giảthi ết sai

| Lớp thực tế | Lớp được dự đoán bởi mô hình |  |
| --- | --- | --- |
|  | Positive | Negative |
| Positive | TP | FN (sai lầm loại 2) |
| Negative | FP (sai lầm loại I) | TN |

Đánh giá độchính xác của mô hình phân lớp

• Độchính xác (precision): được tính bằng số tài liệu phân lớp đúng trên tổng số tài liệu được phân vào lớp đó.

𝑇𝑃 𝑆ố𝑝ℎầ𝑛𝑡ử𝑑ự đ𝑜á𝑛𝑑ư ơ𝑛𝑔đ ú𝑛𝑔 P = 𝑇𝑃+𝐹𝑃x 100% = 𝑇ổ𝑛𝑔𝑠ố𝑝ℎầ𝑛𝑡ử đư ợ𝑐𝑑ự đ𝑜á𝑛𝑣à𝑜𝑙ớ𝑝𝑑ư ơ𝑛𝑔

Mô hình đã dự đoán chính xác bao nhiêu giá trị Positive thực sự • Độh ồi tưởng (recall): được tính bằng số tài liệu phân lớp đúng trên tổng số tài liệu thực chất thuộc về lớp đó.

𝑇𝑃 𝑆ố𝑝ℎầ𝑛𝑡ử𝑑ự đ𝑜á𝑛𝑑ư ơ𝑛𝑔đ ú𝑛𝑔 R = x 100% = 𝑇𝑃+𝐹N 𝑇ổ𝑛𝑔𝑠ố𝑝ℎầ𝑛𝑡ử𝑐ủ𝑎𝑙ớ𝑝𝑑ư ơ𝑛𝑔

Mô hình đã bỏl ỡbao nhiêu giá trịPositive thực sự

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4343

Đánh giá độchính xác của mô hình phân lớp

• Độđo tổng hợp (F-measure):

2 x P x R F = x 100% P+R Độđo tổng hợp F xác định sực ân bằng giữa độchính xác và độh ồi tưởng:

F lớn khi độchính xác và độh ồi tưởng lớn và cân bằng.

F nhỏkhi độchính xác và độh ồi tưởng nhỏho ặc không cân bằng.

## Mục tiêu: F càng cao càng tốt.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4444

Minh họa xác định độchính xác của mô hình

Xét bài toán phân loại thư rác gồm 100 thư, trong đó có 90 thư thường (negative) và 10 thư rác (positive). Mô hình dự đoán đúng 2/10 thư rác.

## • P = 2/(2+0) = 100% R = 2/(2+8) = 20%

## F = 2*0.2*1/(0.2+1)=33%

• Tỷ lệ chính xác khi xác định 1 mail là thư rác là 100% (mô hình dự đoán 2 thư là thư rác thì cả2 dự đoán đều chính xác).

• Tuy nhiên 8/10 thư rác bịb ỏqua →recall 20% rất thấp.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4545

Đánh giá thuật toán phân lớp

• Bài tập tính độchính xác và độh ồi tưởng:

Xét mô hình dự đoán số người rời bỏ dịch vụm ạng Viettel. Bộ dữ liệu test bao gồm 250 mẫu lớp 1 (positive) và 83 mẫu lớp 0 (negative). Kết quảtest mô hình cho kết quảnh ư sau:

- Trong 250 mẫu lớp 1 thì có 214 mẫu test nhận giá trịđúng.

- Trong 83 mẫu lớp 0 thì có 45 mẫu test nhận giá trịđúng.

• Hãy xây dựng ma trận nhầm lẫn và tính độ chính xác, độh ồi tưởng của mô hình?

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4646

## Bài tập

Xây dựng cây quyết định đối với tập dữ liệu sau:

Bước 1: Nhập dữ liệu Nhiệt độl à các con số phù hợp với giá trị của nhiệt độ.

Bước 2: Tiền xử lý dữ liệu Nhiệt độvềki ểu định danh gồm 3 giá trị: Nóng, ấm, mát hoặc hai giá trịNóng, lạnh tương ứng với các mốc nhiệt độSV tựch ọn.

Bước 3: Xây dựng cây quyết định theo thuật toán phân lớp ID3.

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4747

Thực hành Phân lớp trên ngôn ngữPython

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4848

23/05/2026 Khoa Công nghệ thông tin và kinh tế số 4949
