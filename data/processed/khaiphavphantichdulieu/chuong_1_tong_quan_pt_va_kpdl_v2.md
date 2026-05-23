### BÀI 1

#### CHUONG 1 TONG QUAN PT VÀ KPDL V2

## CHƯƠNG 1: TỔNG QUAN VỀ KHAI

## PHÁ DỮ LIỆU

## THS. LÊ THỊ HỒNG NHUNG T: 0987 867 486

## Nội dung chương học

1. Các khái niệm cơ bản

2. Quá trình khai phá tri thức

3. Khai phá dữ liệu và các lĩnh vực liên quan

4. Các yếu tố cơ bản trong khai phá dữ liệu

5. Ứng dụng khai phá dữ liệu

6. Quy trình và các kỹ thuật khai phá

1. Các khái niệm cơ bản

Tình huống

1. Các khái niệm cơ bản

Tình huống 2

Marital Taxable Tid Refund Evade Status Income

1 Yes Single 125K No

2 No Married 100K No

3 No Single 70K No

4 Yes Married 120K No

5 No Divorced 95K Yes

6 No Married 60K No

7 Yes Divorced 220K No

8 No Single 85K Yes

9 No Married 75K No

10 No Single 90K?

|  |  |  | Taxable
Income | Evade |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 125K | No |  |  |  |  |
|  |  | arried | 100K | No |  |  |  |  |
|  | No Si | ngle |  |  |  |  |  |  |
|  |  |  | 70K |  |  |  |  |  |
|  | Yes M
No Di | arried | 120K | No |  |  |  |  |
|  |  |  | 95K |  |  |  |  |  |
|  |  | vorced |  | Ye |  | s |  |  |
|  | No M | arried |  | No |  |  |  |  |
|  |  |  | 60K
220K |  |  |  |  |  |
|  | Yes Di | vorced |  | No |  |  |  |  |
|  | No Si
No M | ngle | 85K | Ye |  | s |  |  |
|  |  | arried | 75K | No |  |  |  |  |
|  | No Si | ngle |  |  |  |  |  |  |
|  |  |  | 90K | ? |  |  |  |  |

|  |  | 2 |
| --- | --- | --- |
|  |  | 3
9 |

1. Các khái niệm cơ bản

Tình huống 3

Ngày mai cổ phiếu STB sẽ tăng???

1. Các khái niệm cơ bản

Tình huống 4

Làm sao xác định được khả năng tốt nghiệp của một sinh viên hiện tại?

1. Các khái niệm cơ bản

Tình huống 5

Làm sao có thể tìm được những loại sản phẩm tương đồng nhau?

1. Các khái niệm cơ bản

Tình huống 6

Làm sao có thể biết một người sẽ định mua mặt hàng gì?

1. Các khái niệm cơ bản

We are data rich, but information poor.

“Necessity is the mother of invention”. - Plato

1. Các khái niệm cơ bản

Dữ liệu (Data): có thể xem là chuỗi các bit, là số, ký tự…mà chúng ta tập hợp hàng ngày trong công việc Thông tin (Information): là tập hợp của những mảnh dữ liệu đã được chắt lọc dùng mô tả, giải thích đặc tính của một đối tượng nào đó Tri thức (Knowledge): là tập hợp những thông tin có liên hệ với nhau, có thể xem tri thức là sựkết tinh từ dữ liệu. Tri thức thểhiện tư duy của con người về một vấn đề.

1. Các khái niệm cơ bản

Quyết định • Promote product A in region Z.

• Mail ads to families of profile P • Cross-sell service B to clients C Tri thức • A quantity Y of product A is used in region Z • Customers of class Y use x% of C during period D

Thông tin • X lives in Z Dữ liệu • S is Y years old • X and S moved • Customer data • W has money in Z • Store data • Demographical Data • Geographical data

2. Quá trình khai phá tri thức

Khám phá tri thức từcơ sở dữ liệu (Knowledge Discovery in Databases - KDD) “KDD là quá trình tựđộng trích rút các tri thức tiềm ẩn trong một lượng dữ liệu lớn” -Fayyad, Platetsky-Shapiro, Smyth (1996).

Khám phá tri thức từcơ sở dữ liệu là quy trình bao gồm nhiều công đoạn như: xác định vấn đề, tập hợp và chọn lọc dữ liệu, khai thác dữ liệu, đánh giá kết quả, giải thích dữ liệu, áp dụng tri thức vào thực tế.

2. Quá trình khai phá tri thức

Pattern Evaluation/ Presentation

Data Mining Patterns

Task-relevant Data

Selection/Transformation Data Warehouse

Data Cleaning Data Integration

Data Sources

2. Quá trình khai phá tri thức

Quá trình khám phá tri thức là một chuỗi lặp gồm các bước:

 Data cleaning (làm sạch dữ liệu)

 Data integration (tích hợp dữ liệu)

 Data selection (chọn lựa dữ liệu)

 Data transformation (biến đổi dữ liệu)

 Data mining (khai phá dữ liệu)

 Pattern evaluation (đánh giá mẫu)

 Knowledge presentation (biểu diễn tri thức)

2. Quá trình khai phá tri thức

Quá trình khám phá tri thức trong thông minh do anh nghiệp

2. Quá trình khai phá tri thức

Tri thức đạt được từqu á trình khai phá:

Tri thức đạt được có thểcó tính mô tảhay dự đoán tùy thuộc vào quá trình khai phá cụ thể.

• Mô tả(Descriptive): có khả năng đặc trưng hóa các thuộc tính chung của dữ liệu được khai phá (Tình huống 5, 6) • Dự đoán (Predictive): có khả năng suy luận từ dữ liệu hiện có đểd ựđo án (Tình huống 1, 2, 3 và 4) Tri thức đạt được có thểcó cấu trúc, bán cấu trúc, hoặc phi cấu trúc.

Tri thức đạt được có thểđược dùng trong việc hỗtr ợra quyết định, điều khiển quy trình, quản lý thông tin, xử lý truy vấn …

3. Khai phá dữ liệu và các lĩnh vực liên quan

Tại sao phải khai phá dữ liệu?

Dữ liệu được thu thập hàng ngày là rất lớn:

Các CSDL khổng lồ.

Dữ liệu từInternet.

Nhà bác học nổi tiếng Karan Sing đã từng nói rằng “Chúng ta đang ngập chìm trong biển dữ liệu nhưng lại đang khát tri thức”.

3. Khai phá dữ liệu và các lĩnh vực liên quan

Khai phá dữ liệu là gì?

Khai phá dữ liệu (Data mining) là một bước trong quy trình khám phá tri thức, nhằm:

Rút trích thông tin hữu ích, chưa biết, tiềm ẩn trong khối dữ liệu lớn.

Phân tích dữ liệu bán tựđộng.

Giải thích dữ liệu trên các tập dữ liệu lớn.

3. Khai phá dữ liệu và các lĩnh vực liên quan

Phân biệt Truy vấn dữ liệu và Khai phá dữ liệu

## Câu hỏi truy vấn dữ liệu:

Hãy hiển thịsốd ư tài khoản của Ông Smith trong ngày mùng 5 tháng 1?

Có bao nhiêu nhà đầu tư nước ngoài mua cổphi ếu X trong tháng trước?

Hiển thịm ọi cổphi ếu trong CSDL với mệnh giá tăng?

--&gt; Cần có một giảthi ết “đầy đủ” về tri thức miền.

3. Khai phá dữ liệu và các lĩnh vực liên quan

Phân biệt Truy vấn dữ liệu và Khai phá dữ liệu

## Câu hỏi khai phá dữ liệu:

Các cổphi ếu tăng giá có đặc trưng gì?

Hy vọng gì về cổphi ếu X trong tuần tiếp theo?

Trong tháng tiếp theo, sẽcó bao nhiêu khách hàng không trảđược nợ của họ?

Những người mua sản phẩm Y có đặc trưng gì?

--&gt; Giảthi ết tri thức “đầy đủ” không còn có tính cốt lõi, cần bổ sung tri thức cho hệth ống -&gt; Nâng cấp miền tri thức!

3. Khai phá dữ liệu và các lĩnh vực liên quan

Các dạng dữ liệu khai phá

3. Khai phá dữ liệu và các lĩnh vực liên quan

Các lĩnh vực liên quan

Hệ thống CSDL Thống kê

Khai phá Học máy Trực quan hóa dữ liệu

Thuật toán Các bộ môn khác

3. Khai phá dữ liệu và các lĩnh vực liên quan

Hệ thống cơ sở dữ liệu với khai phá dữ liệu Khả năng đóng góp của công nghệ cơ sở dữ liệu:

• Công nghệ cơ sở dữ liệu cho việc quản lý dữ liệu được khai phá.

Dữ liệu rất lớn, có thểv ượt quá khả năng của bộnh ớchính (main memory).

Dữ liệu được thu thập theo thời gian.

Các hệ cơ sở dữ liệu có khả năng xử lý hiệu quảl ượng lớn dữ liệu với các cơ chếph ân trang (paging) và hoán chuyển (swapping) dữ liệu vào/ra bộnh ớchính.

Các hệ cơ sở dữ liệu hiện đại có khả năng xử lý nhiều loại dữ liệu phức tạp: spatial, temporal, spatiotemporal, multimedia, text, Web… Các chức năng khác (xử lý đồng thời, bảo mật, hiệu năng, tối ưu hóa, …) của các hệ cơ sở dữ liệu đã được phát triển tốt.

3. Khai phá dữ liệu và các lĩnh vực liên quan

Học máy với khai phá dữ liệu

Học máy:

Machine Learning.

Cách máy tính có thể học (nâng cao năng lực) dựa trên dữ liệu.

Các chương trình máy tính tựđộng học được các mẫu phức tạp và ra quyết định thông minh dựa trên dữ liệu. Ví dụ“học được chữ viết tay trên thư thông qua một tập ví dụ” Là một lĩnh vực nghi ên cứu phát triển nhanh.

3. Khai phá dữ liệu và các lĩnh vực liên quan

Học máy với khai phá dữ liệu Một số nội dung học máy với khai phá dữ liệu:

Học giám sát (supervised learning): dữ liệu huấn luyện đã được gán nhãn.

Học không giám sát (unsupervised learning): dữ liệu huấn luyện không được gán nhãn.

Học bán giám sát (semi-supervised learning): sử dụng cả dữ liệu huấn luyện được gán nhãn và dữ liệu huấn luyện không gán nhãn.

Học tăng cường (Reinforcement learning).

3. Khai phá dữ liệu và các lĩnh vực liên quan

Học máy với khai phá dữ liệu Một số nội dung học máy với khai phá dữ liệu:

Machine Learning

Unsupervised Supervised “Natural groupings” Reinforcement

3. Khai phá dữ liệu và các lĩnh vực liên quan

Trực quan hóa với khai phá dữ liệu  Dữ liệu: 3D cubes,distribution charts, curves, surfaces, link graphs, image frames and movies, parallel coordinates.

 Kết quả(tri thức): pie charts, scatter plots, box plots, association rules, parallel coordinates, dendograms, temporal evolution.

Pie chart Parallel coordinates Temporal evolution

4. Các yếu tốcơ bản trong khai phá dữ liệu

Dữ liệu cụ thểs ẽđược khai phá (task-relevant data) Loại tri thức sẽđ ạt được (kind of knowledge) Tri thức nền (background knowledge) Các độđo (interestingness measures) Các kỹ thu ật biểu diễn tri thức/trực quan hóa mẫu (pattern visualization and knowledge presentation)

4. Các yếu tốcơ bản trong khai phá dữ liệu

Dữ liệu cụ thểs ẽđược khai phá (task-relevant data)

## Phần dữ liệu từcác dữ liệu nguồn được quan tâm.

Tương ứng với các thuộc tính hay chiều dữ liệu được quan tâm.

Bao gồm: tên kho dữ liệu/cơ sở dữ liệu, các bảng dữ liệu hay các khối dữ liệu, các điều kiện chọn dữ liệu, các thuộc tính hay chiều dữ liệu được tâm, các tiêu chí gom nhóm dữ liệu.

4. Các yếu tốcơ bản trong khai phá dữ liệu

Loại tri thức sẽđ ạt được (kind of knowledge) Bao gồm: đặc trưng hóa dữ liệu, phân biệt hóa dữ liệu, mô hình phân tích kết hợp hay tương quan, mô hình phân lớp, mô hình dự đoán, mô hình gom cụm, mô hình phân tích phần tửbi ên, mô hình phân tích tiến hóa.

Tương ứng với tác vụ khai phá dữ liệu cụ thểs ẽđược thực thi.

4. Các yếu tốcơ bản trong khai phá dữ liệu

❖Tri thức nền (background knowledge) • Tương ứng với lĩnh vực cụ thểs ẽđược khai phá.

• Hỗtr ợkhai phá dữ liệu ởnhi ều mức trừu tượng khác nhau

❖Đánh giá các mẫu được tìm thấy.

❖Bao gồm: các phân cấp ý niệm, niềm tin của người sử dụng về các mối quan hệcủa dữ liệu.

4. Các yếu tốcơ bản trong khai phá dữ liệu

Các kỹ thu ật biểu diễn tri thức/trực quan hóa mẫu (pattern visualization and knowledge presentation)

• Xác định dạng các mẫu/tri thức được tìm thấy đểth ểhiện đến người sử dụng.

• Bao gồm: luật (rules), bảng (tables), báo cáo (reports), biểu đồ (charts), đồth ị(graphs), cây (trees), và khối (cubes).

5. Ứng dụng khai phá dữ liệu

5. Ứng dụng khai phá dữ liệu

Ứng dụng: Gợi ý và quảng cáo trực tuyến

5. Ứng dụng khai phá dữ liệu

Phân tích xu hướng thông tin

5. Ứng dụng khai phá dữ liệu

Phân tích và nhận biết nội dung ảnh

5. Ứng dụng khai phá dữ liệu

Khai phá và phân tích quan điểm

5. Ứng dụng khai phá dữ liệu

Phân tích đánh giá người dùng

5. Ứng dụng khai phá dữ liệu

Quản lý và cảnh báo danh tiếng

5. Ứng dụng khai phá dữ liệu

Phân tích và dự báo thủy văn

6. Quy trình và các kỹ thuật khai phá dữ liệu

Quy trình khai phá dữ liệu là một chuỗi lặp (iterative) (và tương tác(interactive)) gồm các bước (giai đoạn) bắt đầu với dữ liệu thô (ra w data) và kết thúc với tri thức (knowledge of interest) đáp ứng được sựquan tâm của người sử dụng.

• Cross Industry Standard Process for Data Mining (CRISP- DM at www. crisp-dm. org) • SEMMA (Sample, Explore, Modify, Model, Assess) at the SAS Institute

6. Quy trình và các kỹ thuật khai phá dữ liệu

Sự cần thiết của một quy trình khai phá dữ liệu

•Cách thức tiến hành (hoạch định và quản lý) dựán khai phá dữ liệu có hệ thống.

•Đảm bảo nỗlực dành cho một dựán khai phá dữ liệu được tối ưu hóa.

•Việc đánh giá và cập nhật các mô hình trong dựán được diễn ra liên tục.

6. Quy trình và các kỹ thuật khai phá dữ liệu

Quy trình CRISP-DM

•Được khởi xướng từ09/1996 và được hỗtr ợb ởi hơn 200 thành viên.

•Chuẩn mở.

•Hỗtr ợcông nghiệp/ứng dụng và công cụkhai phá dữ liệu hiện có.

•Tập trung vào các vấn đềnghiệp vục ũng như phân tích kỹ thu ật.

•Tạo ra một khung thức hướng dẫn qui trình khai phá dữ liệu.

•Có nền tảng kinh nghi ệm từcác lĩnh vựcứng dụng.

6. Quy trình và các kỹ thuật khai phá dữ liệu

Quy trình CRISP-DM

6. Quy trình và các kỹ thuật khai phá dữ liệu

Quy trình CRISP-DM là một quy trình lặp, có khả năng quay lui (backtracking) gồm 6 giai đoạn:

•Tìm hiểu nghiệp vụ(Business understanding)

•Tìm hiểu dữ liệu (Data understanding)

•Chuẩn bị dữ liệu (Data preparation)

•Mô hình hoá (Modeling)

•Đánh giá (Evaluation)

•Triển khai (Deployment)

6. Quy trình và các kỹ thuật khai phá dữ liệu

Các kỹ thu ật khai phá

6. Quy trình và các kỹ thuật khai phá dữ liệu

Các kỹ thu ật khai phá

## Tóm tắt

Khai phá dữ liệu là quá trình khám phá ra các mẫu được quan tâm từl ượng lớn dữ liệu.

•Mẫu kết quảkhai phá được là những mẫu thểhiện tri thức nếu chúng dễ hiểu, hợp lệvới một mức độch ắc chắn, hữu dụng, và mới đối với người dùng.

•Lượng lớn dữ liệu từcác cơ sở dữ liệu truy ền thống/hiện đại, kho dữ liệu, hay từcác nguồn thông tin khác (spatial, time series, text, multimedia, web, …).

•Các tác vụ khai phá dữ liệu bao gồm khai phá mô tảl ớp/khái niệm (đặc trưng hóa và phân biệt hóa dữ liệu), khai phá luật kết hợp/tương quan, phân lớp, dự đoán, gom cụm, phân tích xu hướng, phân tích độl ệch và

## phần tửbiên, phân tích độtương tự, …

## Tóm tắt

Khai phá dữ liệu được xem như là một phần của quá trình khám phá tri thức.

Quá trình khám phá tri thức là một chuỗi lặp gồm các bước: làm sạch dữ liệu, tích hợp dữ liệu, chọn lựa dữ liệu, biến đổi dữ liệu, khai phá dữ liệu, đánh giá mẫu, và biểu diễn tri thức.

Nhiều lĩnh vực khác nhau có liên quan với khai phá dữ liệu: công nghệ cơ sở dữ liệu, lý thuyết thống kê, học máy, khoa học thông tin, trực quan hóa, …

Các vấn đề li ên quan: phương pháp luận khai phá dữ liệu, vấn đề tương tác người dùng, khả năng co giãn dữ liệu và hiệu suất, vấn đề xử lý lượng lớn các kiểu dữ liệu khác nhau, vấn đềkhai thác cácứng dụng khai phá dữ liệu cũng như sựảnh hưởng xã hội của chúng.

## BAV|HỌC VIỆN

## Ce) NGAN HANG L
