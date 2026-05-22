# Lecture 4 - Machine Learning Pipeline (1).pptx



<!-- page 1 -->

HC VIN NGN HNG
BANKING ACADEMY OF VIETNAM

# IS54A
# TR TU NHN TO


<!-- page 2 -->

# Chương 3 Machine learning pipeline

TS. Vũ Trọng Sinh
Email: sinhvt@hvnh.edu.vn
Mobile: 0975674039


<!-- page 3 -->

## Nội dung chính

### **Thu thập dữ liệu (Data collection):**
- Các nguồn thu thập dữ liệu.
- Bộ dữ liệu chất lượng cao (High quality dataset).
- Kỹ thuật Crawling (Cào dữ liệu web).

### **Tiền xử lý (Preprocess):**
- Mã hóa dữ liệu (Encode data).
- Phát hiện và xử lý dữ liệu thiếu (Missing data).
- Phát hiện và xử lý dữ liệu ngoại lai (Outlier data).


<!-- page 4 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Motivation

## Tầm quan trọng của dữ liệu

- Data Providers
- Select Data
- Raw Data
- Data Processing Tools
- Pre-Processing
- Iterate till data is prepared
- Structured Data
- Machine Learning Algorithms
- Learning Algorithm
- Iterate to get best model
- Candidate Model
- Deploy Selected Model
- Golden Model
- Applications


<!-- page 5 -->

# Tầm quan trọng của dữ liệu

- **Trong quá khứ:** Lượng dữ liệu hạn chế $\rightarrow$ tập trung vào các thuật ngữ Machine Learning truyền thống (như KNN, K-means, Linear Regression, Decision Trees,...) để tận dụng tối đa dữ liệu đó.
- **Kỷ nguyên Big Data:** Các thuật toán Deep Learning hiện đại phát triển để tận dụng lượng dữ liệu khổng lồ và sức mạnh tính toán.
- **Hiện tại:** Deep Learning đã chạm tới một số giới hạn, sự chú ý quay trở lại với dữ liệu (Data-centric AI) — tập trung thu thập dữ liệu chất lượng cao hơn.


<!-- page 6 -->

# Thu thập dữ liệu (Data Collection)

- Dữ liệu không chỉ đến từ tổ chức của bạn mà còn có thể được cấp phép từ bên thứ ba hoặc tạo mới từ đầu.

**Company Data**
- Digital Data
- Physical Paper Data

**External Data**
- Free Datasets
- Licensed Datasets


<!-- page 7 -->

# Quiz

Trong các nguồn dữ liệu sau về thẩm định giá bất động sản, nguồn dữ liệu nào có chất lượng tốt:

A. Dữ liệu thẩm định giá bất động sản trong CSDL của ngân hàng BIDV
B. Hồ sơ thanh toán thuế giao dịch BĐS ở chi cục thuế địa phương
C. Bộ dữ liệu housing_dataset ở competition đã làm ở nhà
D. Dữ liệu crawl từ tin đăng batdongsan.com.vn


<!-- page 8 -->

# Làm thế nào để biết dữ liệu có chất lượng cao

- Dữ liệu được sử dụng để xây dựng các hệ thống AI thường được gọi là **Ground Truth** (Sự thật nền tảng)—đó là sự thật củng cố kiến thức trong một hệ thống AI.
- Các mô hình Supervised Machine Learning được huấn luyện trên dữ liệu **có nhãn** được coi là “Ground Truth” để mô hình xác định các quy luật nhằm dự đoán các nhãn đó trên dữ liệu mới.

**Một bộ dữ liệu chất lượng cao thường có các nhãn gần với Ground Truth trong kịch bản thực tế.**

- Ground Truth tốt thường đến từ hoặc được tạo ra bởi các hệ thống của tổ chức đã được sử dụng.
- Nếu không có dữ liệu hệ thống, cần các chuyên gia lĩnh vực (SMEs) tạo Ground Truth này *thủ công*


<!-- page 9 -->

# Dữ liệu nội bộ (Company Data)

- Dữ liệu số (Digital Data): Hệ thống Sales, CRM, HRM, Log files...

Các hệ thống thông tin này có thể sản sinh dữ liệu theo nhiều dạng (structured database to unstructured log files)

Structured Data + Textual Data, Image File, Video, Audio + XML Data, JSON Data, Sensor Data + Metadata

Có thể lưu trữ toàn bộ dữ liệu để sử dụng trong tương lai, hoặc cung cấp cho các nhà khoa học dữ liệu để phân tích và xây dựng các hệ thống thông minh một cách liên tục (continuously).


<!-- page 10 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Types of data storage in an organization

## Structured databases:
- Excel format
- Database Management Systems (DBMS): SQL Server, MySQL, Oracle, ...

## Unstructured databases:
- MongoDB, NoSQL
- Data warehouse, Data lake


<!-- page 11 -->

# Internal Data Collection: Digital

*Nếu bạn muốn xây dựng một hệ thống AI nhưng chưa bắt đầu thu thập dữ liệu? Ngay cả trong kịch bản này, bạn có thể đã có nhiều dữ liệu hơn bạn nghĩ*

- Liệt kê tất cả các hệ thống kỹ thuật số hiện có trong tổ chức
    - Dữ liệu được lưu trữ rõ ràng (ví dụ: hồ sơ khách hàng).
    - Dữ liệu sử dụng hệ thống được lưu trong các tệp nhật ký (VD: dữ liệu truy cập hệ thống để phát hiện bất thường)
- Kiểm tra xem dữ liệu này có dễ dàng truy cập (accessible) hoặc xuất ra (export) để sử dụng cho hệ thống AI đang xây dựng hay không.


<!-- page 12 -->

## Collect dữ liệu qua API

- Best option: Hệ thống hiện tại cung cấp một API được tài liệu hóa rõ ràng để truy cập dữ liệu.
  - API được ưu tiên vì chúng **an toàn**, dễ **truy cập** về mặt lập trình và cung cấp quyền truy cập dữ liệu theo **thời gian thực**.
  - API có thể cung cấp các khả năng tiện lợi trên nền dữ liệu thô đang được lưu trữ, chẳng hạn như số liệu thống kê tổng hợp (roll-up statistics) hoặc dữ liệu phái sinh khác.

E.g. Google API, Facebook API, ...


<!-- page 13 -->

# File Export

Khả năng này thường nằm trong giao diện người dùng của hệ thống và cho phép người dùng cuối xuất dữ liệu ở định dạng tiêu chuẩn như CSV, XML.

## Nhược điểm:
- Chỉ một số dữ liệu nhất định mới có thể xuất được.
- Dữ liệu có cấu trúc nội bộ phức tạp có thể khó xuất ra trong một tệp duy nhất.
- Phải được export thủ công theo định kỳ.


<!-- page 14 -->

BAV HỌC VIỆN
NGÂN HÀNG
1961
BANKING ACADEMY OF VIETNAM

## Direct Database Connection

Thiết lập một kết nối an toàn đến cơ sở dữ liệu mà hệ thống sử dụng để truy cập trực tiếp các bảng cơ sở dữ liệu, có thể bao gồm cả các quan hệ giữa các bảng
- Một điểm quan trọng cần lưu ý là bạn nên truy cập dữ liệu này theo cách "chỉ đọc" (**readonly**) để không vô tình ảnh hưởng đến ứng dụng

Secure Connection (Read-Only)

*   Enterprise System
    *   No Supported Data Export
*   Internal Database
    *   SQL
    *   IMPORTANT: 👁️ **Read-Only Access!**
*   Machine Learning Platform
    *   Access Database Tables Directly


<!-- page 15 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# Internal Data Collection: Physical

- Dữ liệu ở dạng vật lý phải được số hóa trước khi có thể sử dụng để tạo hệ thống AI, nhưng **số hóa không phải là một nhiệm vụ đơn giản** → cần xem xét
    - Lượng thời gian và chi phí cần thiết để số hóa dữ liệu.
    - Liệu việc bắt đầu thu thập dữ liệu số kể từ bây giờ trở đi có đủ không?

Nếu dữ liệu vật lý có giá trị → nên bắt đầu thay thế nó bằng một hệ thống kỹ thuật số.


<!-- page 16 -->

## **Data Collection via Licensing**

- Nếu bạn chưa thu thập dữ liệu hoặc cần dữ liệu mà bạn không thể thu thập nội bộ □ Licensing
    - Các công ty có mô hình kinh doanh bán dữ liệu, VD: Nielsen (dữ liệu hành vi người tiêu dùng), Bloomberg/Reuters (dữ liệu tài chính)
    - Bộ dữ liệu miễn phí (có thể không hoàn toàn phù hợp với mục đích của bạn):
        - https://www.kaggle.com/
        - https://project-awesome.org/awesomedata/awesomedata/awesome-public-datasets
        - https://www.data.gov/
    - Các công ty cấp phép dữ liệu (Scale AI, Statistica).
    - Các nguồn khác tùy thuộc vào lĩnh vực (địa lý, nông nghiệp, vận tải, ...) -> có thể cần chi phí hoặc quan hệ


<!-- page 17 -->

BAV HỌC VIỆN
NGÂN HÀNG
1961
BANKING ACADEMY OF VIETNAM

## **Datasets từ Kaggle**

https://www.www.kaggle.com/datasets

- Một cộng đồng trực tuyến dành cho các nhà khoa học dữ liệu và những người thực hành machine learning.
- Cho phép người dùng:
    - Tìm kiếm và công bố các bộ dữ liệu.
    - Khám phá và xây dựng mô hình trong môi trường khoa học dữ liệu dựa trên web.
    - Làm việc với các nhà khoa học dữ liệu và kỹ sư machine learning khác.
    - Tham gia các cuộc thi để giải quyết các thách thức về khoa học dữ liệu.


<!-- page 18 -->

## Lưu ý khi thu thập dữ liệu qua cấp phép

- Chi phí dữ liệu thường rất lớn, nên có thể thương lượng dựa trên cách bạn dự định sử dụng dữ liệu.
    - Định giá theo quy mô (Scale-based pricing)
- Tránh việc bị lệ thuộc quá mức vào công ty cấp phép vì dữ liệu của họ:
    - Công ty đó đột ngột ngừng dịch vụ.
    - Họ sử dụng dữ liệu đã cấp phép để "vỗ béo" hệ thống của chính họ
- → **Sử dụng dữ liệu được cấp phép để xây dựng hệ thống ban đầu, nhưng bắt đầu tự thu thập dữ liệu từ hệ thống AI của riêng bạn để sử dụng sau này.**


<!-- page 19 -->

# Thu thập dữ liệu qua Crowdsourcing

- Các nền tảng Crowdsourcing thường gồm 2 loại người dùng:
  - **Người dùng có câu hỏi cần được trả lời:** Đưa dữ liệu chưa được gán nhãn của bạn lên thị trường crowdsourcing.
  - **Người dùng sẽ trả lời những câu hỏi này:** Được trả tiền để trả lời các câu hỏi nhanh chóng và với độ chính xác cao.
- Lưu ý:
  - Thông thường, cùng một câu hỏi được hỏi cho nhiều người để đảm bảo tính nhất quán.
  - Nếu có sự sai lệch cho một câu hỏi duy nhất, có thể là do hình ảnh đó mơ hồ.
  - Nếu một người dùng cụ thể có nhiều sai lệch, điều này có nghĩa là người dùng đó đang trả lời ngẫu nhiên và nên bị loại khỏi công việc hoặc người dùng đó không hiểu yêu cầu.
- VD: Roboflow, LinkedIn, Microworkers, v.v.


<!-- page 20 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

## Leveraging the Power of Existing Systems

Một số hệ thống thông minh có sẵn có thể được sử dụng để tạo ra một bộ dữ liệu, **e.g. Google, Flickr**

Google
daytime pictures
All Images Videos News Maps More Tools Collections
sky night city space time cartoon sun cloudy sky wallpaper moon

**Case study:** sử dụng Google Images với tìm kiếm “masked face” (khuôn mặt có đeo khẩu trang) và sau đó sử dụng tiện ích mở rộng trình duyệt để tải xuống tất cả hình ảnh trên trang đó


<!-- page 21 -->

# Cào dữ liệu từ các trang web public (Crawl data)

- Một trình cào web (web crawler, spider) hoặc bot của công cụ tìm kiếm sẽ tải xuống và lập chỉ mục nội dung từ khắp nơi trên Internet.
- **Quy trình 4 Bước**
  - **Request**: Gửi yêu cầu HTTP GET/POST.
  - **Parse**: Phân giải cấu trúc HTML/JSON.
  - **Extract**: Trích xuất qua CSS/XPath.
  - **Save**: Lưu vào SQL/CSV/NoSQL.
- Một số công cụ hữu ích: ***BeautifulSoup, Selenium / Playwright, Scrapy***


<!-- page 22 -->

## Bài tập thực hành

- Cào ít nhất 1.000 mẫu dữ liệu cho dự đoán giá bất động sản Hà Nội và ghi kết quả vào các tệp csv
    - Đề xuất các trang web có thể cào
    - Quan sát cấu trúc trang web và lập quy tắc cào dữ liệu
    - Lựa chọn và áp dụng công cụ cào dữ liệu
    - Thực hiện và lưu file kết quả
    - **Nộp link source code và kết quả csv trên danh sách lớp, sheet Bài tập**


<!-- page 23 -->

## **Tiền xử lý dữ liệu (Data Preprocessing)**

- Mã hóa dữ liệu (Encode data)
- Phát hiện và xử lý dữ liệu thiếu (Detect and handle missing data)
- Phát hiện và xử lý dữ liệu ngoại lai (Detect and handle outlier data)


<!-- page 24 -->

## Mã hóa dữ liệu (Encode data)

*   Mã hóa dữ liệu trong machine learning đề cập đến quá trình chuyển đổi dữ liệu phân loại hoặc không phải số sang định dạng số có thể được sử dụng bởi các thuật toán machine learning.
*   Mã hóa dữ liệu rất quan trọng vì:
    *   **Biểu diễn dữ liệu (Data Representation)**: Cách dữ liệu được biểu diễn ảnh hưởng đến hiệu suất mô hình.
    *   **Thuật toán mong đợi đầu vào là số**: Hầu hết các thuật toán machine learning mong đợi đầu vào là số.
    *   **Tránh thiên kiến (Avoiding Bias)**: Mã hóa đúng cách giúp tránh thiên kiến trong các mô hình.


<!-- page 25 -->

## Các loại mã hóa dữ liệu

- Label Encoding
- One-Hot Encoding
- Ordinal Encoding
- Frequency Encoding
- Embedding

https://www.linkedin.com/pulse/useful-encoding-techniques-machine-learning-heba-al-haddad/


<!-- page 26 -->

BAV HỌC VIỆN NGÂN HÀNG
1961 BANKING ACADEMY OF VIETNAM

## Label Encoding

- Label Encoding là một kỹ thuật đơn giản gán một giá trị số nguyên duy nhất cho mỗi danh mục (category)

| | occupation |
|---|---|
| 0 | programmer |
| 1 | data scientist |
| 2 | engineer |
| 3 | manager |
| 4 | ceo |

| | occupation |
|---|---|
| 0 | 4 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 0 |

- Cẩn thận trọng khi sử dụng Label Encoding với các thuật toán diễn giải các số nguyên được mã hóa như các giá trị có thứ tự, vì nó có thể tạo ra thiên kiến không mong muốn.


<!-- page 27 -->

# One-Hot Encoding

- One-Hot Encoding là một kỹ thuật phổ biến được sử dụng để chuyển đổi các biến phân loại thành một biểu diễn nhị phân. Mỗi danh mục được biến đổi thành một vector nhị phân, với giá trị '1' cho biết sự hiện diện của danh mục đó và '0' cho tất cả các danh mục khác.

**Quá trình One-Hot Encoding:**

| Feature (Color) | | One Hot Encoded Vector | Red | Green | Yellow |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Red | $\rightarrow$ | [1,00] | 1 | 0 | 0 |
| Green | One Hot Encoding | [0,1,0] | 0 | 1 | 0 |
| Yellow | $\rightarrow$ | [0,0,1] | 0 | 0 | 1 |
| Green | | [0,1,0] | 0 | 1 | 0 |
| Red | | [1,00] | 1 | 0 | 0 |

- One-Hot Encoding phù hợp cho các biến định danh (*nominal variables*) không có mối quan hệ thứ tự vốn có giữa các danh mục.


<!-- page 28 -->

## Ordinal Encoding

- Ordinal Encoding lý tưởng cho các biến có thứ tự, nơi các danh mục có thứ tự ý nghĩa nhưng thiếu các biểu diễn số cách đều nhau.
- Không giống như Label Encoding, Ordinal Encoding sử dụng các ánh xạ do người dùng xác định để gán các giá trị số cho các danh mục, bảo toàn mối quan hệ thứ tự giữa chúng.

| Original Encoding | Ordinal Encoding |
| :---------------- | :--------------- |
| Poor              | 1                |
| Good              | 2                |
| Very Good         | 3                |
| Excellent         | 4                |


<!-- page 29 -->

# Frequency Encoding

- **Frequency Encoding**, còn được gọi là **Count Encoding**, thay thế mỗi danh mục bằng tần suất hoặc số lượng tương ứng của nó trong bộ dữ liệu.
    - Kỹ thuật này hữu ích khi xử lý các biến phân loại có số lượng giá trị lớn (**high cardinality**), vì nó nắm bắt được tầm quan trọng của mỗi danh mục dựa trên mức độ phổ biến của nó trong dữ liệu.

| Numerical value | Animal    |
| :-------------- | :-------- |
| 1.5             | cat       |
| 3.6             | cat       |
| 42              | dog       |
| 7.1             | crocodile |

Frequency encoding

| Numerical value | Animal_freq |
| :-------------- | :---------- |
| 1.5             | 0.5         |
| 3.6             | 0.5         |
| 42              | 0.25        |
| 7.1             | 0.25        |


<!-- page 30 -->

# Embedding

* Embedding là một kỹ thuật thường được sử dụng trong các nhiệm vụ Xử lý ngôn ngữ tự nhiên (NLP). Nó ánh xạ các biến phân loại vào các vector dày đặc (dense) trong một không gian liên tục, nắm bắt được các mối quan hệ ngữ nghĩa giữa các danh mục.
    * Embedding cho phép mô hình học được ngữ cảnh và các mối quan hệ bên trong dữ liệu, làm cho nó trở nên mạnh mẽ cho một số ứng dụng machine learning nhất định.

---

**Set of Objects**
* Object 1
* Object 2
* Object 3

**Embedding Model**

**Objects as Vectors**
* `[0.6 | 0.3 | 0.1 | -----]`
* `[0.8 | 0.5 | 0.3 | -----]`
* `[0.4 | 0.2 | 0.9 | -----]`


<!-- page 31 -->

# Phát hiện và xử lý dữ liệu thiếu (Missing data)

- Dữ liệu thiếu được định nghĩa là các giá trị hoặc dữ liệu không được lưu trữ (hoặc không hiện diện) cho một hoặc một số biến trong bộ dữ liệu đã cho.

**Nguyên nhân:**
- Dữ liệu trong quá khứ có thể bị hỏng do bảo trì không đúng cách.
- Các quan sát không được ghi lại cho một số trường nhất định vì một số lý do. Có thể có sự thất bại trong việc ghi lại các giá trị do lỗi con người.
- Người dùng cố tình không cung cấp các giá trị


<!-- page 32 -->

# Phát hiện và xử lý dữ liệu thiếu (Missing data)

- Nhiều thuật toán machine learning sẽ fail nếu bộ dữ liệu chứa các giá trị thiếu *(chỉ một số thuật toán như K-nearest và Naive Bayes hỗ trợ dữ liệu có giá trị thiếu)*
- Mô hình machine learning có thể bị thiên kiến, dẫn đến kết quả sai nếu các giá trị thiếu không được xử lý

Check for missing values in Python: **isnull().sum()**


<!-- page 33 -->

# Xử lý các giá trị thiếu (Handling Missing Values)

- **Xóa các giá trị thiếu (Deleting):**
  - Xóa toàn bộ hàng (listwise deletion)
  - Xóa toàn bộ cột
- **Điền khuyết các giá trị thiếu (Imputing):**
  - Thay thế bằng một giá trị tùy ý
  - Thay thế bằng giá trị trung bình (mean)
  - Thay thế bằng giá trị yếu vị (mode)
  - Thay thế bằng giá trị trung vị (median)
  - Thay thế bằng giá trị kế tiếp, giá trị trước đó, ...

https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/


<!-- page 34 -->

# Phát hiện và xử lý dữ liệu ngoại lai (Outlier data)

- Outliers là những điểm dữ liệu khác biệt đáng kể so với phần còn lại của bộ dữ liệu. Chúng thường là những quan sát bất thường làm lệch phân phối dữ liệu, và phát sinh do việc nhập liệu không nhất quán hoặc các quan sát sai sót.
- Ví dụ:
  - Trong một bộ dữ liệu về giá nhà, nếu bạn tìm thấy một vài ngôi nhà có giá khoảng 1,5 triệu đô la—cao hơn nhiều so với giá nhà trung vị, chúng có khả năng là outliers.
  - Tuy nhiên, nếu bộ dữ liệu chứa một lượng lớn đáng kể các ngôi nhà có giá từ 1 triệu đô la trở lên—chúng có thể là dấu hiệu của xu hướng tăng giá nhà. Trong trường hợp này, việc gắn nhãn tất cả chúng là outliers sẽ là sai lầm. Trong trường hợp này, bạn cần một số kiến thức về lĩnh vực bất động sản.


<!-- page 35 -->

# Phát hiện dữ liệu ngoại lai (Detect outlier data)

- Outliers là những điểm dữ liệu khác biệt đáng kể so với phần còn lại của bộ dữ liệu. Chúng thường là những quan sát bất thường làm lệch phân phối dữ liệu, và phát sinh do việc nhập liệu không nhất quán hoặc các quan sát sai sót.


<!-- page 36 -->

# Phương pháp phát hiện dữ liệu ngoại lai

- Phát hiện Outliers sử dụng độ lệch chuẩn (Standard Deviation)
- Phát hiện Outliers sử dụng Z-Score
- Phát hiện sử dụng Khoảng tứ phân vị (IQR)
- Phát hiện Outliers sử dụng Phân vị (Percentile)

https://www.freecodecamp.org/news/how-to-detect-outliers-in-machine-learning/


<!-- page 37 -->

# Discussion

https://www.kaggle.com/code/leonidvashchyn/house-md-eda-ensemble#Cleaning

- Phân tích và xem các kỹ thuật tiền xử lý nào được sử dụng trong link Kaggle về làm sạch dữ liệu giá nhà (House MD EDA Ensemble).
