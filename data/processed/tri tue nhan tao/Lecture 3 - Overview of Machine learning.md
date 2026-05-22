# Lecture 3 - Overview of Machine learning



<!-- page 1 -->

HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# Trí tuệ nhân tạo
## IS54A


<!-- page 2 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Chương 2
## Các khái niệm cơ bản trong Học máy

TS. Vũ Trọng Sinh
sinhvt@hvnh.edu.vn
0975674039


<!-- page 3 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# Nội dung
## 2.1. Các khái niệm cơ bản về Học máy
## 2.2. Các Phương pháp Học máy
## 2.3. Tổng quan về dự án Học máy


<!-- page 4 -->

## 2.1. Các khái niệm cơ bản trong Học máy

There are several approaches to make computers intelligent

One way is to help them **“learn”**

Try to formulate the process of learning from human by mathematical models and convert these models into programming algorithms

In this chapter: *How they learn in detail?*


<!-- page 5 -->

# Định nghĩa Học máy

- Định nghĩa đầu tiên
    - Field of study that gives computers the ability to learn *without being explicitly programmed* (Arthur Samuel - 1959)

| Chương trình máy tính thông thường | Ứng dụng học máy |
| :--- | :--- |
| We have to tell the computer what to do in each single step | We teach the computer how to learn, then do what they learned |

    - A computer program is said to learn from **experience E** with respect to some **task T** and some **performance measure P**, if its performance on T, as measured by P, improves with experience E (Tom Mitchell - 1998)


<!-- page 6 -->

# Ví dụ

You developed an application similar to **Youtube Kids**, where users can post and interact with videos. Since the audiences are kids, you want to remove all the videos containing violent content. At first, you have to watch a video by yourself and mark it as “violent” or “non-violent”. Then your app should have a module that <u>watches you do or do not mark as violent</u>, and based on that observation, it <u>learns how to filter violent videos better</u>. What is task T in this case?

1. Watching you do or do not mark a video as violent
2. Classifying videos as violent or non-violent
3. The number of videos correctly classified as violent/non-violent


<!-- page 7 -->

# Main parts of the definition

- **Task T**: Không phải các tác vụ vật lý (Robot, Cơ khí...), tập trung vào các tác vụ "tư duy".
- **Experience E**: Cách chúng ta trình bày các kinh nghiệm dưới dạng **Data** (dữ liệu).
- **Performance measure P**: Các chỉ số (metrics) để đánh giá thuật toán học (learning algorithm) hay "chương trình máy tính" trong định nghĩa.


<!-- page 8 -->

# Quiz

What are task T, experience E, performance P

- https://www.kaggle.com/datasets/sagaraiarchitect/laptop-price-explorer-the-ml-model
- https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- https://www.kaggle.com/datasets/wardaddy24/marble-surface-anomaly-detection
- https://www.kaggle.com/datasets/zalando-research/fashionmnist
- https://www.kaggle.com/datasets/ronikdedhia/next-word-prediction
- https://www.kaggle.com/datasets/deependraverma13/cardio-activities


<!-- page 9 -->

# Dữ liệu cho Học máy

**Dataset** là tập dữ liệu ghi lại những quan sát (kinh nghiệm) dùng để huấn luyện, kiểm thử, kiểm tra mô hình học máy.

Dữ liệu thường bao gồm một tập hợp các **instance** hoặc **sample**, mỗi instance có thể chứa: **attributes, features** hoặc **labels**.

Trong dữ liệu dạng bảng (**tabular dataset**), mỗi **instance** là một hàng, mỗi cột là một **attribute**.

| Customer ID | Age (yrs) | Annual Income ($k) | Credit Score | Loan Amount ($k) | Approved (Y/N) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 35 | 75 | 720 | 20 | Y |
| 102 | 28 | 50 | 650 | 15 | N |
| 103 | 42 | 110 | 780 | 30 | Y |

- **SAMPLE / INSTANCE (Single Data Point / Row)**
- **FEATURES (Input Variables)**
- **ATTRIBUTE (Column/Characteristic)**
- **LABEL (Target Variable)**
- **Feature Values**
- **Label Value**


<!-- page 10 -->

# Data, attributes and labels, features

Một "**attribute**" là một đặc điểm hoặc tính chất của một instance trong dataset.

"**Label**" là biến hoặc đầu ra mà mô hình đang cố gắng dự đoán (predict).

"**Features**" là các tính chất hoặc đặc điểm đo lường được của các instance dữ liệu.
- Chúng là các biến đầu vào (input variables) mà mô hình **Machine learning** sử dụng để đưa ra dự đoán hoặc phân loại

## MACHINE LEARNING DATASET STRUCTURE: KEY COMPONENTS

| Customer ID | Age (yrs) | Annual Income ($k) | Credit Score | Loan Amount ($k) | Approved (Y/N) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 35 | 75 | 720 | 20 | Y |
| 102 | 28 | 50 | 650 | 15 | N |
| 103 | 42 | 110 | 780 | 30 | Y |

**Chú thích từ sơ đồ:**
- **FEATURES (Input Variables)**: Bao gồm các cột Age (yrs), Annual Income ($k), Credit Score, Loan Amount ($k).
- **ATTRIBUTE (Column/Characteristic)**: Chỉ các cột trong bảng.
- **LABEL (Target Variable)**: Cột Approved (Y/N).
- **SAMPLE / INSTANCE (Single Data Point / Row)**: Chỉ các hàng trong bảng.
- **Feature Values**: Các giá trị nằm trong các cột Features.
- **Label Value**: Các giá trị nằm trong cột Label.


<!-- page 11 -->

# Từ attribute đến feature

Trong số tất cả các **attributes** này, attribute nào quan trọng nhất để dự đoán giá nhà?

- Diện tích (Area)
- Số phòng ngủ (Bedrooms)
- Vị trí (Location)
- Loại nhà (Type)

Chúng ta gọi chúng là **Features**.

---

**Nice 4 bedroom house with lake view for rent in Tay Ho, Hanoi**
$2,600

- Property ID: 5447
- Area: 180 SQM
- Bedrooms: 4
- Bathrooms: 4
- Outdoor: Balcony
- Type: House
- Location: Tay Ho

Add to Favorites | Print

**Description**
Nice 4 bedroom house with lake view for rent in Tay Ho, Hanoi
This quality house showcases a flowing 4 level layout with garage.
- Living and dining space enhanced by sleek finishes
- Kitchen has stone benches, induction cooker and stainless appliances
- Stylish appointed bathroom features walk-in shower
- Study nook, high ceilings, wooden floors and air conditioning
- Close to local eateries, amenities, parklands and transport

**Tina Ho**
Agent
f G+
- Mobile: +84 989311131
- Agent Email: info.livinghanoi@gmail.com
- No. 42/52 To Ngoc Van street, Tay Ho district, Hanoi


<!-- page 12 -->

# Dữ liệu gắn nhãn và không gắn nhãn

**Labelled data**: Dữ liệu đi kèm với một nhãn (**label**).

**Unlabelled data**: Dữ liệu không đi kèm với nhãn.

| Labelled data | Labelled data | Unlabelled data |
| :--- | :--- | :--- |
| Dog | 18 lbs | (Hình ảnh chó) |
| Dog | 14 lbs | (Hình ảnh chó) |
| Cat | 12 lbs | (Hình ảnh mèo) |
| Cat | 9 lbs | (Hình ảnh mèo) |


<!-- page 13 -->

## 2.2. Các phương pháp Học máy

- Trong Machine learning, các kỹ thuật học có thể được phân loại rộng rãi dựa trên bản chất của quá trình học và sự sẵn có của **labelled data**:
    - **Supervised Learning** (Học có giám sát)
    - **Unsupervised Learning** (Học không giám sát)
    - **Semi-Supervised Learning** (Học bán giám sát)
    - **Reinforcement Learning** (Học tăng cường)
    - Khác: **Transfer learning**, **Ensemble learning**, **Self-supervised learning**


<!-- page 14 -->

# Supervised Learning

**Định nghĩa:** "Supervised learning involves learning a function that maps an input to an output based on example input-output pairs. It infers a function from **labeled** training data consisting of a set of training examples."

**Nguồn:** Russell, S. J., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed., p. 651). Pearson.

**Ví dụ:** **Classification** (gán danh mục cho các instance) và **Regression** (dự đoán các giá trị số)

- Supervised learning
- Unsupervised learning


<!-- page 15 -->

# Unsupervised Learning

**Định nghĩa:** "Unsupervised learning involves finding patterns in data that has **not been labeled or classified**. The goal is to discover hidden structures or to estimate the probability density of the data."
**Nguồn:** Bishop, C. M. (2006). *Pattern Recognition and Machine Learning* (p. 3). Springer.

**Ví dụ:** **Clustering** (nhóm các instance tương tự lại với nhau) và **Dimensionality Reduction** (giảm số lượng features trong khi vẫn giữ lại thông tin liên quan)

| Supervised learning | Unsupervised learning |
| :--- | :--- |
| (Hình ảnh minh họa dữ liệu có nhãn và đường phân cách) | (Hình ảnh minh họa dữ liệu được gom nhóm) |


<!-- page 16 -->

# Example

Vào trang baomoi.com/chu-de.epi để xem danh sách các chủ đề. Đây là kết quả của **Supervised** hay **Unsupervised learning**

### #BÃO NORU
- Bão Noru mạnh lên cấp 12-13, giật cấp 16 (Nhân Dân 14 phút)
- Các tỉnh, thành phố miền Trung triển khai ứng phó khẩn bão Noru (Zing 1 giờ)
- Sẵn sàng ứng phó với bão Noru và mưa lớn (Tiền phong 2 giờ)
- Miền Trung sẵn sàng ứng phó với bão Noru (DCSVN 33 phút)
- Bão Noru khả năng giật cấp 16 khi tiến vào gần bờ biển Thừa Thiên - Huế đến Quảng Ngãi (NGƯỜI LAO ĐỘNG 1 giờ)
- Bão Noru tiếp tục tăng cấp, dự báo đêm mai đổ bộ vào Biển Đông (ausNEWS 2 giờ)

### #LÊ THỊ HIỀN
- Cựu đại úy công an Lê Thị Hiền lĩnh 7 năm tù trong vụ cướp tài sản tại quán bar (NGƯỜI LAO ĐỘNG 6 giờ)
- 'Mồi khách đến quán rồi 'gí bill', cựu đại úy Lê Thị Hiền từng gây náo loạn sân bay lĩnh án (Công Thương 6 giờ)
- Nữ cựu đại úy công an từng gây náo loạn tại Tân Sơn Nhất trả giá đắt vì cướp tài sản (NGƯỜI LAO ĐỘNG 6 giờ)

### #VĂN PHÒNG CHỦ TỊCH NƯỚC
- Văn phòng Chủ tịch nước phải là cơ quan tiên phong trong việc phát động, thực hiện các phong trào thi đua yêu nước (Toquoc 3 giờ)
- Lãnh đạo Đảng, Nhà nước dự lễ kỷ niệm 30 năm tái lập Văn phòng Chủ tịch nước (Quang Ngãi 3 giờ)
- Lãnh đạo Đảng, Nhà nước dự lễ kỷ niệm 30 năm tái lập Văn phòng Chủ tịch nước (Quốc Hội TV 3 giờ)

### #TKCN
- Tin bão NORU và các chỉ đạo ứng phó (Chính Phủ 3 giờ)
- Phần lớn tàu thuyền ở Quảng Trị đã neo đậu an toàn để tránh bão số 4 (Vietnam+ 4 giờ)
- Quảng Ngãi cấm biển khi gió mạnh từ cấp 6 (SAIGON 5 giờ)
- Chủ động ứng phó bão Noru (KHANH HOA 3 giờ)
- Quảng Ngãi ban hành công điện, khẩn trương ứng phó với bão số 4 (Vietnam+ 5 giờ)
- Thanh Hóa chủ động ứng phó cơn bão số 4 (Nhân Dân 5 giờ)

### #CHỐNG THAM NHŨNG
- Kiên quyết xử lý nghiêm các trường hợp né tránh, đùn đẩy, không làm hết trách nhiệm (DCSVN 29 phút)
- Đoàn kiểm tra về phòng, chống tham nhũng, tiêu cực làm việc tại Đồng Nai và TP Hồ Chí Minh (Quân đội nhân dân 1 giờ)
- Không để sai phạm nhỏ tích tụ thành sai phạm lớn (VNEWS 3 giờ)

### #UKRAINE
- Tổng thống Biden cảnh báo sẽ đáp trả Nga vì các cuộc trưng cầu dân ý ở vùng ly khai Ukraine (Tiền phong 2 giờ)
- Trưng cầu dân ý sáp nhập Nga: Sử dụng phiếu giấy, có mời quan sát viên quốc tế (Tiền phong 7 giờ)

### #TUẤN HƯNG
- Khán giả ùn ùn đến hồ Hoàn Kiếm xem liveshow 'Góc ban công' của Tuấn Hưng (PHÁP LUẬT 2 giờ)

### #PHƯƠNG NGA
- Vừa mới khoe ảnh cưới với Á hậu Phương Nga, Bình An đã phải lên tiếng thanh minh vì một sự cố
- Độc quyền: Hé lộ ngày Bình An chính thức rước Phương Nga (SAOstar 8 giờ)

### #CẦU NHƠN TRẠCH
- Khởi công Dự án Thành phần 1A thuộc đường Vành đai 3 TP. Hồ Chí Minh (Taiduchinh 7 giờ)
- Cầu Nhơn Trạch sẽ hoàn thành trong năm 2025 (7 giờ)


<!-- page 17 -->

# Semi-Supervised Learning

**Định nghĩa:** Loại hình học tập này kết hợp các yếu tố của cả **Supervised** và **Unsupervised learning**.

Mô hình được huấn luyện trên một dataset chứa một lượng nhỏ **labeled data** và một lượng lớn **unlabeled data**

**Ví dụ:** Sử dụng một tập nhỏ các hình ảnh có nhãn cùng với một tập lớn các hình ảnh không nhãn để huấn luyện mô hình **Image classification**


<!-- page 18 -->

# Semi-Supervised Learning

Nguyên lý hoạt động khá đơn giản: Thay vì gán nhãn cho toàn bộ dataset, bạn chỉ gán nhãn thủ công cho một phần nhỏ dữ liệu và dùng nó để huấn luyện mô hình, sau đó mô hình này được áp dụng cho biển dữ liệu chưa gán nhãn (**unlabeled data**)

**Self-training:** quy trình mà bạn có thể lấy bất kỳ phương pháp **supervised** nào cho phân loại hoặc hồi quy và sửa đổi nó để hoạt động theo cách **semi-supervised**, tận dụng cả dữ liệu có nhãn và không nhãn


<!-- page 19 -->

# Semi-Supervised Learning

1. Small portion of data with human-made labels -> First Classifier (base model)

2. Lots of unlabeled data -> First Classifier trained on labeled data -> Pseudo-labels

3.
- Original labeled data
- Most confident pseudo-labels
-> New dataset -> Improved Classifier trained on new dataset -> Predictions


<!-- page 20 -->

# Quiz

Đọc bài viết đầy đủ tại:
https://www.altexsoft.com/blog/semi-supervised-learning/

- Giải thích cơ chế iteration trong **self-training**, rủi ro lớn nhất khi sử dụng Pseudo-labeling là gì?
- Giải thích các khái niệm: **Continuity Assumption**, **Cluster Assumption**, và **Manifold Assumption**


<!-- page 21 -->

# Reinforcement Learning

**Định nghĩa: Reinforcement learning** liên quan đến việc một **agent** (tác tử) học cách ra quyết định bằng cách tương tác với môi trường (**environment**)
- **Agent** nhận phản hồi dưới dạng phần thưởng (**rewards**) hoặc hình phạt (**penalties**) dựa trên các hành động (**actions**) nó thực hiện, và mục tiêu là học một chính sách (**policy**) giúp tối đa hóa phần thưởng tích lũy theo thời gian

**Ví dụ:** Huấn luyện thuật toán chơi game hoặc điều khiển hệ thống robot


<!-- page 22 -->

# Tổng quan các phương pháp học máy

## TỔNG QUAN CÁC PHƯƠNG PHÁP HỌC MÁY
**(MACHINE LEARNING METHODS OVERVIEW)**

### MACHINE LEARNING

- **SUPERVISED LEARNING (Học có giám sát)**
    - Dữ liệu có nhãn (Labeled Data)
    - REGRESSION (Hồi quy)
    - CLASSIFICATION (Phân loại)

- **UNSUPERVISED LEARNING (Học không giám sát)**
    - Dữ liệu không nhãn (Unlabeled Data)
    - CLUSTERING (Gom cụm)
    - DIMENSIONALITY REDUCTION (Giảm chiều dữ liệu)

- **SEMI-SUPERVISED LEARNING (Học bán giám sát)**
    - Ít dữ liệu có nhãn + Nhiều không nhãn (Small Labeled + Large Unlabeled)

- **REINFORCEMENT LEARNING (Học tăng cường)**
    - Tương tác & Thưởng/Phạt (Agent, Environment, Reward)


<!-- page 23 -->

# Quiz

Read the following article about training a large language model (section **How Are Large Language Models Trained?**)

https://quiq.com/blog/large-language-models/

**Question:** Họ đã sử dụng loại hình học tập nào để huấn luyện mô hình ngôn ngữ lớn?

23


<!-- page 24 -->

# Machine learning pipeline

1. Data collection
2. Preprocess
3. Feature extraction
4. Model building
5. Evaluation
6. Deployment


<!-- page 25 -->

# Data Collection

**Definition**: This stage involves gathering relevant data for the machine learning task. The quality and quantity of data significantly impact the performance of the model. Data can be collected from various sources, such as databases, APIs, files, or sensors.

Activities:
- Identify and define the problem to determine the required data.
- Collect data from diverse sources, ensuring it represents the problem domain.
- Address issues such as missing data, outliers, and data imbalance.


<!-- page 26 -->

# Preprocess

**Definition**: Data preprocessing involves cleaning, transforming, and organizing raw data into a format suitable for machine learning. It aims to handle missing values, standardize scales, and address any inconsistencies in the data.

Activities:
- Handle missing or duplicated data.
- Normalize or scale numerical features.
- Encode categorical variables.
- Remove outliers and irrelevant information.
- Split the dataset into training and testing sets.


<!-- page 27 -->

# Features extraction

**Definition**: Feature extraction involves selecting or transforming the relevant features (input variables) from the dataset. It aims to reduce dimensionality, enhance model interpretability, and focus on the most informative aspects of the data.

Activities:
- Identify and select relevant features.
- Perform dimensionality reduction techniques (e.g., PCA).
- Create new features that capture important information.


<!-- page 28 -->

# Model building

**Definition**: Model building is the core stage where a machine learning algorithm is selected, trained, and fine-tuned using the prepared dataset. The goal is to learn the underlying patterns and relationships in the data to make accurate predictions or classifications.

Activities:
- Choose an appropriate machine learning algorithm based on the task (classification, regression, etc.).
- Split the data into training and validation sets.
- Train the model on the training set.
- Validate and fine-tune hyperparameters to optimize performance.


<!-- page 29 -->

# Evaluation

**Definition**: The evaluation stage assesses the performance of the trained model using a separate test dataset. Metrics are used to quantify how well the model generalizes to new, unseen data.

Activities:
- Evaluate the model on the test set.
- Measure performance using appropriate metrics (accuracy, precision, recall, F1 score, etc.).
- Compare the model's performance against baseline models or benchmarks.
- Assess the model's ability to generalize to new data.


<!-- page 30 -->

# Deployment

**Definition**: Deployment involves integrating the trained model into a production environment, making it available for making predictions on new, real-world data. This stage ensures that the model is accessible and operational.

Activities:
- Integrate the model into the target system or application.
- Set up monitoring and logging for model performance.
- Implement a feedback loop for continuous improvement.
- Consider scalability, security, and ethical considerations.


<!-- page 31 -->

# Homework

Join this competition on Kaggle:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview

Create your own notebook and make a submission
