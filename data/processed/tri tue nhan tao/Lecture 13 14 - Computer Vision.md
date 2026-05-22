# Lecture 13 14 - Computer Vision



<!-- page 1 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# IS544A - Trí tuệ nhân tạo
## Chương 6 – Thị giác máy tính


<!-- page 2 -->

# Nội dung chính

## 6.1. **Tổng quan về dữ liệu hình ảnh và Thị giác máy tính**
## 6.2. Các bài toán chính trong Thị giác máy tính
## 6.3. Các hướng tiếp cận bài toán Thị giác máy tính
## 6.4. Mạng CNN và các biến thể cho CV


<!-- page 3 -->

BAV HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM
1961

# 6.1. Tổng quan về dữ liệu hình ảnh và Thị giác máy tính

## Human Vision System
- **Eye** (sensing device responsible for capturing images of the environment)
- **Brain** (interpreting device responsible for understanding the image content)
- bowl, oranges, bananas, lemons, peaches

## Computer Vision System
- **Input**
- **Sensing device**
- **Interpreting device**
- **Output**: bowl, oranges, bananas, lemons, peaches


<!-- page 4 -->

# Định nghĩa và Mục tiêu của Thị giác máy tính

- **Khái niệm:** Thị giác máy tính (CV – Computer Vision) là lĩnh vực thuộc AI giúp máy tính có khả năng "nhìn" và hiểu nội dung hình ảnh/video như con người.
- **Mục tiêu cốt lõi:** Chuyển đổi dữ liệu phi cấu trúc (pixels) thành thông tin có cấu trúc (labels, bounding boxes, masks)
- **Sự khác biệt:**
    - *Xử lý ảnh (Image Processing):* input là ảnh, output là ảnh (ví dụ: làm nét, lọc nhiễu)
    - *Thị giác máy tính (CV):* input là ảnh, output là tri thức/quyết định (ví dụ: nhận diện hành vi).


<!-- page 5 -->

# Bản chất của dữ liệu hình ảnh (Digital Image)

- **Điểm ảnh (Pixel):** Đơn vị nhỏ nhất của hình ảnh kỹ thuật số
- **Cấu trúc ma trận:** Một bức ảnh thực chất là một ma trận 2D (ảnh xám) hoặc 3D (ảnh màu) chứa các giá trị màu sắc RGB

**Độ phân giải (Resolution):** Số lượng pixel theo chiều ngang và dọc

| | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 157 | 153 | 174 | 168 | 150 | 152 | 129 | 151 | 172 | 161 | 155 | 156 |
| 155 | 182 | 163 | 74 | 75 | 62 | 33 | 17 | 110 | 210 | 180 | 154 |
| 180 | 180 | 50 | 14 | 34 | 6 | 10 | 33 | 48 | 106 | 159 | 181 |
| 206 | 109 | 5 | 124 | 131 | 111 | 120 | 204 | 166 | 15 | 56 | 180 |
| 194 | 68 | 137 | 251 | 237 | 239 | 239 | 228 | 227 | 87 | 71 | 201 |
| 172 | 105 | 207 | 233 | 233 | 214 | 220 | 239 | 228 | 98 | 74 | 206 |
| 188 | 88 | 179 | 209 | 185 | 215 | 211 | 158 | 139 | 75 | 20 | 169 |
| 189 | 97 | 165 | 84 | 10 | 168 | 134 | 11 | 31 | 62 | 22 | 148 |
| 199 | 168 | 191 | 193 | 158 | 227 | 178 | 143 | 182 | 106 | 36 | 190 |
| 205 | 174 | 155 | 252 | 236 | 231 | 149 | 178 | 228 | 43 | 95 | 234 |
| 190 | 216 | 116 | 149 | 236 | 187 | 85 | 150 | 79 | 38 | 218 | 241 |
| 190 | 224 | 147 | 108 | 227 | 210 | 127 | 102 | 36 | 101 | 255 | 224 |
| 190 | 214 | 173 | 66 | 103 | 143 | 96 | 50 | 2 | 109 | 249 | 215 |
| 187 | 196 | 235 | 75 | 1 | 81 | 47 | 0 | 6 | 217 | 255 | 211 |
| 183 | 202 | 237 | 145 | 0 | 0 | 12 | 108 | 200 | 138 | 243 | 236 |
| 195 | 206 | 123 | 207 | 177 | 121 | 123 | 200 | 175 | 13 | 96 | 218 |


<!-- page 6 -->

# Không gian màu và Kênh hình ảnh (Channels)

- **Grayscale (Ảnh xám)**: Mỗi pixel gồm 1 kênh giá trị duy nhất từ **0** (Đen) đến **255** (Trắng)
- **RGB (Ảnh màu)**: Kết hợp từ 3 kênh màu: **Red**, **Green**, **Blue**. Mỗi pixel là một vector $[R, G, B]$

Pixel (1, 0)
red:6 green:250 blue:7
(i.e. shade of green)

Pixel (4, 2)
red:241 green:252 blue:23

Pixel (2, 3):
red:247 green:250 blue:237


<!-- page 7 -->

# Dữ liệu đầu vào cho AI

Một bức ảnh màu kích thước 28 x 28 thực chất là một Tensor có shape là (28, 28, 3) tương đương 784 input

**Mỗi input có thể coi như một features?**

- RGB
    - R: Red
    - G: Green
    - B: Blue

7


<!-- page 8 -->

# Những thách thức chính

## TẠI SAO THỊ GIÁC MÁY TÍNH LẠI KHÓ?
### NHỮNG THÁCH THỨC CỐT LÕI (CORE CHALLENGES)

| THAY ĐỔI GÓC NHÌN (Viewpoint Variation) | ĐIỀU KIỆN ÁNH SÁNG (Illumination) | BIẾN DẠNG (Deformation) |
| :--- | :--- | :--- |
| ![Mug](https://via.placeholder.com/50) <br> Vật thể nhìn từ các hướng khác nhau tạo ra ma trận pixel hoàn toàn khác nhau. | **THIẾU SÁNG** -> $\checkmark$ <br> **NGƯỢC SÁNG** -> $\checkmark$ <br> **CHUẨN** -> $\times$ <br> Cùng một khuôn mặt ở điều kiện ánh sáng khác nhau làm khó việc trích xuất đặc trưng. | ![Human](https://via.placeholder.com/50) <br> Vật thể mềm thay đổi hình dáng nhưng vẫn là cùng một đối tượng. |

**THỊ GIÁC MÁY TÍNH - TỔNG QUAN**


<!-- page 9 -->

# Những thách thức về Bối cảnh

## THÁCH THỨC BỐI CẢNH (CONTEXTUAL CHALLENGES)

| CHE KHUẤT (Occlusion) | NHIỄU NỀN (Background Clutter) | ĐA DẠNG NỘI TẠI (Intra-class Variation) |
| :--- | :--- | :--- |
| ![Hình ảnh xe hơi bị che khuất bởi cây] | ![Hình ảnh con tắc kè ngụy trang] | ![Hình ảnh các loại ghế khác nhau] |
| **Vật thể bị che mất một phần** (ví dụ: xe hơi bị khuất sau cái cây). | **Vật thể có màu sắc hoặc cấu trúc tương đồng với môi trường xung quanh** (ngụy trang). | "Cái ghế" có hàng nghìn kiểu dáng, màu sắc khác nhau nhưng AI phải học được đặc trưng chung của "ghế". |


<!-- page 10 -->

# Ứng dụng thực tiễn của CV

- **Tài chính - Ngân hàng:** Nhận diện khuôn mặt (eKYC), đọc ký tự trên hóa đơn/hợp đồng (OCR)
- **An ninh:** Phát hiện hành vi bất thường, giám sát giao thông
- **Y tế:** Chẩn đoán bệnh qua ảnh X-quang, MRI.
- **Sản xuất:** Kiểm tra lỗi sản phẩm trên dây chuyền tự động.


<!-- page 11 -->

# Nội dung chính

6.1. Tổng quan về dữ liệu hình ảnh và Thị giác máy tính
## 6.2. Các bài toán chính trong Thị giác máy tính
6.3. Các hướng tiếp cận bài toán Thị giác máy tính
6.4. Mạng CNN và các biến thể cho CV


<!-- page 12 -->

# 6.2. Các bài toán chính trong Thị giác máy tính

## Core Computer Vision Tasks

| | | |
| :--- | :--- | :--- |
| **Recognition** | **Segmentation** | **Detection** |
| ![Dog](https://via.placeholder.com/50) | ![Person](https://via.placeholder.com/50) | ![Cat in box](https://via.placeholder.com/50) |
| Identify what it is | Divide into parts | |
| **Classification** | **Retrieval** | **Generation / Transformation** |
| ![Dog, Cat, Bird](https://via.placeholder.com/50) | ![Search](https://via.placeholder.com/50) | ![Faces](https://via.placeholder.com/50) |
| Sort into categories | Find & return similar | Create or modify |

- **Recognition**: Identify what it is
- **Segmentation**: Divide into parts
- **Detection**: (Hiển thị hình ảnh đối tượng trong khung)
- **Classification**: Sort into categories
- **Retrieval**: Find & return similar
- **Generation / Transformation**: Create or modify


<!-- page 13 -->

# 6.2. Các bài toán chính trong Thị giác máy tính

| object recognition | object detection | semantic segmentation | image captioning |
| :--- | :--- | :--- | :--- |
| ![cat](https://via.placeholder.com/100x80?text=cat) | ![cat_ball](https://via.placeholder.com/100x80?text=cat_ball) | ![segmentation](https://via.placeholder.com/100x80?text=segmentation) | ![caption](https://via.placeholder.com/100x80?text=caption) |
| Cat | cat, ball | Red: cat<br>Green: ball<br>Blue: background | A cat is playing a ball. |
| (1) | (2) | (3) | (4) |

| image question answering | image generator | LiLi |
| :--- | :--- | :--- |
| ![qa](https://via.placeholder.com/100x80?text=qa) | A cat is playing a ball.<br>![gen](https://via.placeholder.com/100x80?text=gen) | 10001111100010<br>10110100101110<br>Input Image -> R (LPN) -> 10111111101110 (Output Image) |
| Q: How many balls are there in the image?<br>A: One. | | |
| (5) | (6) | (7) |

**Tìm một số bộ dataset phổ biến cho mỗi bài toán (1) – (5) này**


<!-- page 14 -->

# Phân loại hình ảnh (Image Classification)

- **Định nghĩa:** Gán một nhãn (label) duy nhất cho toàn bộ bức ảnh. Trả lời câu hỏi: "Đối tượng chính trong ảnh này là gì?"
- **Đặc điểm:** Không quan tâm đến vị trí hay số lượng vật thể. Chỉ quan tâm đến xác suất cao nhất của một lớp (class)
- **Ví dụ:** Hệ thống phân loại ảnh X-quang là "Bình thường" hay "Viêm phổi"


<!-- page 15 -->

# Phân loại hình ảnh + Localization (Classification + Localization)

- **Định nghĩa:** Không chỉ cho biết ảnh có gì mà còn chỉ ra vị trí của đối tượng đó bằng một khung hình chữ nhật (**Bounding Box**)
- **Đầu ra (Output):** Bao gồm nhãn lớp (Class) và tọa độ (x, y, w, h) của box
- **Ứng dụng:** Thường dùng khi trong ảnh chỉ có một đối tượng chính cần quan tâm đặc biệt (ví dụ: định vị khối u trong ảnh y tế)

15


<!-- page 16 -->

# Phát hiện vật thể (Object Detection)

- **Định nghĩa:** Xác định vị trí và phân loại **nhiều vật thể** thuộc các lớp khác nhau trong cùng một khung hình.
- **Thử thách:** Phải xử lý được sự chồng lấn giữa các vật thể và biến động về kích thước (Scalability).
- **Thuật toán tiêu biểu:** YOLO (You Only Look Once), SSD, Faster R-CNN.
- **Ví dụ:** Camera giao thông đếm số lượng xe máy, ô tô và người đi bộ tại ngã tư.


<!-- page 17 -->

# Discussion

So far, we know some evaluation metrics:
- MAE, MSE for regression tasks
- Accuracy, Precision, Recall, F1-score for classification tasks
- BLEU, ROUGH for some NLP tasks

How to evaluate an object detection model?


<!-- page 18 -->

# Object detection evaluation

https://www.v7labs.com/blog/intersection-over-union-guide

- **Ground-truth Bounding Box**
- **Predicted Bounding Box**

$$IoU = \frac{\text{Area of Overlap}}{\text{Area of Union}}$$

- A
- B
- $A \cap B$
- $A \cup B$


<!-- page 19 -->

# Object detection evaluation

Mathematically
$$Intersection\ over\ Union\ (IoU) = \frac{|A \cap B|}{|A \cup B|}$$

But for binary classification, it is written as:
$$Intersection\ over\ Union\ (IoU) = \frac{TP}{TP + FN + FP}$$

- **TP**= True Positive.
- **FN**= False Negative.
- **FP**= False Positive.


<!-- page 20 -->

# Object detection evaluation - Exercise

- **Excelent**
- **Good**
- **Poor**

IoU= 0.95
IoU= 0.79
IoU= 0.45

$$y = (p_c, b_x, b_y, b_h, b_w, c)$$

$b_w$
$b_h$
$(b_x, b_y)$

ground_truth = [
(50, 50, 40, 60),
(30, 30, 20, 20),
(70, 80, 30, 40)
]

model_a_preds = [
(48, 52, 42, 58),
(32, 31, 18, 19),
(69, 79, 31, 41)
]

model_b_preds = [
(45, 55, 30, 50),
(28, 30, 22, 20),
(75, 85, 28, 38)
]


<!-- page 21 -->

# Phân vùng ngữ nghĩa (Semantic Segmentation)

- **Định nghĩa:** Phân loại từng điểm ảnh (**pixel-level**) vào một lớp cụ thể. Trả lời câu hỏi: "Pixel này thuộc về thực thể nào?".
- **Đặc điểm:** Không phân biệt các cá thể trong cùng một lớp. Ví dụ: 5 con chó đứng cạnh nhau sẽ được tô cùng một màu (lớp "Chó").
- **Ứng dụng:** Xe tự lái nhận diện đâu là vùng "đường đi", đâu là "vỉa hè".


<!-- page 22 -->

# Phân vùng thực thể (Instance Segmentation)

- **Định nghĩa:** Kết hợp giữa Object Detection và Semantic Segmentation.
- **Đặc điểm:** Không chỉ phân loại pixel theo lớp mà còn tách biệt từng cá thể riêng lẻ. Ví dụ: Mỗi con chó trong 5 con chó sẽ được tô một màu khác nhau.
- **Thuật toán tiêu biểu:** Mask R-CNN.
- **Ví dụ:** Đếm chính xác số lượng tế bào trong ảnh vi sinh và xác định ranh giới của từng tế bào.


<!-- page 23 -->

# Nhận diện điểm đặc trưng (Keypoint Detection)

- **Định nghĩa:** Xác định vị trí của các điểm mấu chốt cấu thành nên cấu trúc của vật thể.
- **Ứng dụng phổ biến nhất:** Human Pose Estimation (Ước lượng dáng người) bằng cách tìm các khớp vai, khuỷu tay, đầu gối.


<!-- page 24 -->

# Một số bài toán liên quan đến khuôn mặt

## Đâu là bài toán đơn giản / phức tạp nhất?

- **Facial Recognition** (Nhận diện khuôn mặt)
    - Jane Doe (26, F)
    - John Smith (27, M)
- **Face Detection** (Phát hiện khuôn mặt)

- **Face verification** (Xác thực khuôn mặt)
    - Hệ thống so sánh hai ảnh đầu vào và đưa ra kết quả: "Sundar" hoặc "Not Sundar".
- **Face identification** (Nhận dạng khuôn mặt)
    - Hệ thống so sánh ảnh đầu vào với cơ sở dữ liệu và đưa ra kết quả: "Sundar", "Sachin", hoặc "Didn't see it earlier".

24


<!-- page 25 -->

# Nhận diện ký tự quang học (OCR)

- **Định nghĩa:** Chuyển đổi dữ liệu hình ảnh chứa văn bản (viết tay hoặc in) sang định dạng văn bản máy tính có thể chỉnh sửa.
- **Các bước chính:** Phát hiện vùng chứa văn bản (Text Detection) và Nhận dạng ký tự (Text Recognition).
- **Ứng dụng:** Tự động hóa nhập liệu hóa đơn, đọc biển số xe (ALPR), số hóa tài liệu lưu trữ của ngân hàng.


<!-- page 26 -->

# Phân tích hành động và Video (Action Recognition)

- **Định nghĩa:** Hiểu sự thay đổi của vật thể qua các khung hình liên tiếp (Temporal dimension).
- **Yếu tố then chốt:** Sự kết hợp giữa đặc trưng không gian (Spatial) từ CNN và đặc trưng thời gian (Temporal) từ RNN/LSTM hoặc 3D-CNN.
- **Ví dụ:** Phân biệt hành động "đặt túi xách xuống" và "bỏ chạy" trong an ninh công cộng.

26


<!-- page 27 -->

# Nội dung chính

### 6.1. Tổng quan về dữ liệu hình ảnh và Thị giác máy tính
### 6.2. Các bài toán chính trong Thị giác máy tính
### 6.3. Các hướng tiếp cận bài toán Thị giác máy tính
### 6.4. Mạng CNN và các biến thể cho CV


<!-- page 28 -->

# Phân loại các hướng tiếp cận chính

- **Thị giác máy tính truyền thống (Traditional/Classical CV)**: Dựa trên các thuật toán toán học và xử lý tín hiệu số để trích xuất đặc trưng thủ công.
- **Thị giác máy tính hiện đại (Deep Learning-based CV)**: Sử dụng các mạng thần kinh nhân tạo sâu để tự động học các đặc trưng từ dữ liệu thô.

→ Từ "Feature Engineering" (Kỹ nghệ đặc trưng) sang "Feature Learning" (Học đặc trưng)


<!-- page 29 -->

# Hướng tiếp cận truyền thống - Đặc trưng thủ công

- **Khái niệm:** Các chuyên gia xác định các đặc trưng quan trọng (cạnh, góc, màu sắc) và viết thuật toán để trích xuất chúng.
- **Quy trình:** Ảnh đầu vào -> Trích xuất đặc trưng (SIFT, HOG) -> Thuật toán phân loại (SVM, Random Forest) -> Kết quả


<!-- page 30 -->

# Các thuật toán truyền thống tiêu biểu

- **SIFT (Scale-Invariant Feature Transform):** Tìm các điểm đặc trưng không thay đổi khi vật thể bị xoay, phóng to hay thu nhỏ.
- **HOG (Histogram of Oriented Gradients):** Tập trung vào cấu hình hình học và hướng của các cạnh.
- **Ứng dụng:** Rất mạnh trong việc so khớp ảnh (image stitching) hoặc nhận diện vật thể đơn giản.

30


<!-- page 31 -->

# Các thuật toán truyền thống tiêu biểu

- **Haar Cascades:** Sử dụng các bộ lọc hình chữ nhật đơn giản để phát hiện sự thay đổi cường độ sáng
- **Ưu điểm:** Tốc độ cực nhanh, có thể chạy trên các phần cứng có cấu hình rất yếu.
- **Hạn chế:**
    - **Tính mong manh (Fragility):** Dễ thất bại khi điều kiện ánh sáng, góc nhìn hoặc bối cảnh thay đổi
    - **Thiếu tính tổng quát:** Một bộ trích xuất đặc trưng được thiết kế cho "xe hơi" khó có thể dùng tốt cho "tế bào y tế"
    - **Giới hạn của con người:** Con người khó có thể định nghĩa hết các đặc trưng phức tạp trong các bức ảnh tự nhiên


<!-- page 32 -->

# Hướng tiếp cận hiện đại - Deep Learning

- **Khái niệm:** Mô hình nhận vào ảnh thô và trả ra kết quả cuối cùng. Các tầng trong mạng thần kinh sẽ tự đảm nhiệm việc tìm ra đặc trưng nào là quan trọng nhất.

## MACHINE LEARNING
Input $\rightarrow$ Feature extraction $\rightarrow$ Classification $\rightarrow$ Output
(Hình ảnh minh họa: Xe hơi $\rightarrow$ Người trích xuất đặc trưng $\rightarrow$ Mạng thần kinh $\rightarrow$ CAR / NOT CAR)

## DEEP LEARNING
Input $\rightarrow$ Feature extraction + Classification $\rightarrow$ Output
(Hình ảnh minh họa: Xe hơi $\rightarrow$ Mạng thần kinh $\rightarrow$ CAR / NOT CAR)


<!-- page 33 -->

# Cơ chế học đặc trưng phân cấp

- **Các tầng thấp (Lower layers):** Học các đặc trưng cơ bản như cạnh (edges), nét gạch, màu sắc đơn nhất.
- **Các tầng giữa (Middle layers):** Kết hợp các cạnh thành các hình khối, họa tiết (textures, shapes)
- **Các tầng cao (Higher layers):** Kết hợp các hình khối thành các bộ phận vật thể (mắt, mũi, bánh xe) và đối tượng hoàn chỉnh


<!-- page 34 -->

# Deep Learning thống trị Thị giác máy tính

- **Hiệu suất vượt trội:** Kể từ cuộc cách mạng AlexNet (2012), độ chính xác của Deep Learning đã bỏ xa các phương pháp truyền thống
- **Tính bền vững (Robustness):** Chịu được nhiễu, che khuất và biến đổi góc nhìn tốt hơn nhờ học từ hàng triệu ví dụ
- **Tính linh hoạt:** Một kiến trúc mạng (như ResNet) có thể áp dụng cho nhiều miền dữ liệu khác nhau chỉ bằng cách thay đổi dữ liệu huấn luyện


<!-- page 35 -->

# Thực hành 1

https://www.kaggle.com/datasets/zalando-research/fashionmnist

**Fashion clothes classification**
Input: a 28x28 image in grayscale
Output: which kind of clothes:

- 0 T-shirt/top
- 1 Trouser
- 2 Pullover
- 3 Dress
- 4 Coat
- 5 Sandal
- 6 Shirt
- 7 Sneaker
- 8 Bag
- 9 Ankle boot

| | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Shirt | Sandal | Ankle boot | Sneaker | Trouser | Sneaker |
| Sneaker | Trouser | Dress | Dress | Sandal | Ankle boot |
| T_shirt/top | Shirt | Pullover | Sandal | Sneaker | Pullover |
| Bag | Ankle boot | Bag | Sneaker | Sneaker | Coat |


<!-- page 36 -->

# Thực hành 1

https://www.kaggle.com/code/hatomugi/svm-with-0-9-accuracy

Build a handwritten digit recognition model with SVM

- Tải mã nguồn đi kèm bài 12 trên Google Drive, thực hành theo kịch bản cho trước trong file .ipynb
- Xây dựng lại mô hình SVM phân loại ảnh với trích xuất đặc trưng theo kiểu HOG
- Nộp lại notebook trên classroom và giải thích (cộng 1 contribution cho 3 bạn đầu tiên nộp và có giải thích)


<!-- page 37 -->

# Thực hành 2

## Face Detection using Cascade Classifier using OpenCV - Python
- Phát hiện khuôn mặt dựa vào đặc trưng Haar Cascade (Pretrained)
- Thử nghiệm với ảnh tự upload và nhận xét kết quả

https://www.geeksforgeeks.org/python/face-detection-using-cascade-classifier-using-opencv-python/

37


<!-- page 38 -->

# Nội dung chính

6.1. Tổng quan về dữ liệu hình ảnh và Thị giác máy tính
6.2. Các bài toán chính trong Thị giác máy tính
6.3. Các hướng tiếp cận bài toán Thị giác máy tính
6.4. **Mạng CNN và các biến thể cho CV**


<!-- page 39 -->

# Tại sao không dùng MLP cho hình ảnh

- **Vấn đề về tham số:** Một ảnh màu $224x224 \sim 150k$ input. Nếu tầng ẩn có 1000 neurons, mạng MLP cần **150 triệu tham số** chỉ cho tầng đầu tiên $\rightarrow$ Quá tải tính toán, dễ Overfitting.
- **Mất cấu trúc không gian:** MLP "làm phẳng" (flatten) ảnh thành vector, làm mất đi mối liên hệ giữa các pixel cạnh nhau.
$\rightarrow$ CNN Sử dụng kết nối cục bộ (Local Connectivity) và chia sẻ trọng số (Weight Sharing)

| Input image | Convolutions | Pooling | Fully Connected |
| :--- | :--- | :--- | :--- |


<!-- page 40 -->

# Tầng Convolution (Tích chập)

- **Cơ chế:** Một bộ lọc (Kernel/Filter) trượt trên ảnh để thực hiện phép nhân vô hướng từng phần.
- **Vai trò:** Trích xuất các đặc trưng như cạnh, góc, họa tiết.
- **Tham số quan trọng:**

**Kernel Size:** Kích thước bộ lọc
**Stride:** Bước nhảy của bộ lọc.
**Padding:** Thêm viền (thường là số 0) để giữ nguyên kích thước ảnh sau tích chập.


<!-- page 41 -->

# Tầng Pooling (Gộp) - Giảm chiều dữ liệu

- **Cơ chế:** Down-sampling để giảm kích thước không gian của bản đồ đặc trưng (Feature Map)
    - **Max Pooling:** Lấy giá trị lớn nhất trong cửa sổ (giữ lại đặc trưng mạnh nhất)
    - **Average Pooling:** Lấy giá trị trung bình
- **Lợi ích:** Giảm khối lượng tính toán và giúp mô hình "bất biến" hơn với những dịch chuyển nhỏ của vật thể

### Max Pooling

| | | | |
|---|---|---|---|
| 29 | 15 | 28 | 184 |
| 0 | 100 | 70 | 38 |
| 12 | 12 | 7 | 2 |
| 12 | 12 | 45 | 6 |

**2 x 2 pool size**

| | |
|---|---|
| 100 | 184 |
| 12 | 45 |

### Average Pooling

| | | | |
|---|---|---|---|
| 31 | 15 | 28 | 184 |
| 0 | 100 | 70 | 38 |
| 12 | 12 | 7 | 2 |
| 12 | 12 | 45 | 6 |

**2 x 2 pool size**

| | |
|---|---|
| 36 | 80 |
| 12 | 15 |

41


<!-- page 42 -->

# Tầng Fully Connected

- **Fully Connected (FC) Layer:** Nằm ở cuối mạng, tổng hợp tất cả các đặc trưng đã học được để đưa ra quyết định phân loại cuối cùng (thường kết hợp với hàm **Softmax**)

42


<!-- page 43 -->

# Kiến trúc ResNet-34

| VGG-19 | 34-layer plain | 34-layer residual |
| :--- | :--- | :--- |
| image | image | image |
| 3x3 conv, 64 | 7x7 conv, 64, /2 | 7x7 conv, 64, /2 |
| 3x3 conv, 64 | pool, /2 | pool, /2 |
| pool, /2 | 3x3 conv, 64 | 3x3 conv, 64 |
| 3x3 conv, 128 | 3x3 conv, 64 | 3x3 conv, 64 |
| 3x3 conv, 128 | 3x3 conv, 64 | 3x3 conv, 64 |
| pool, /2 | 3x3 conv, 64 | 3x3 conv, 64 |
| 3x3 conv, 256 | 3x3 conv, 64 | 3x3 conv, 64 |
| 3x3 conv, 256 | 3x3 conv, 64 | 3x3 conv, 64 |
| 3x3 conv, 256 | 3x3 conv, 64 | 3x3 conv, 64 |
| pool, /2 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| pool, /2 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| 3x3 conv, 512 | 3x3 conv, 128 | 3x3 conv, 128 |
| pool, /2 | 3x3 conv, 256, /2 | 3x3 conv, 256, /2 |
| fc 4096 | 3x3 conv, 256 | 3x3 conv, 256 |
| fc 4096 | 3x3 conv, 256 | 3x3 conv, 256 |
| fc 1000 | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 256 | 3x3 conv, 256 |
| | 3x3 conv, 512, /2 | 3x3 conv, 512, /2 |
| | 3x3 conv, 512 | 3x3 conv, 512 |
| | 3x3 conv, 512 | 3x3 conv, 512 |
| | avg pool | avg pool |
| | fc 1000 | fc 1000 |

https://www.geeksforgeeks.org/deep-learning/residual-networks-resnet-deep-learning/


<!-- page 44 -->

# CÁC KIẾN TRÚC CNN KINH ĐIỂN

| Kiến trúc | Đặc điểm đột phá | Ưu điểm | Nhược điểm | Ứng dụng phù hợp |
| :--- | :--- | :--- | :--- | :--- |
| **VGGNet** | Đồng nhất bộ lọc 3x3 | Kiến trúc đơn giản, dễ hiểu, dễ cài đặt. | Rất nặng, tiêu tốn nhiều bộ nhớ và tham số. | Bài toán đơn giản, Transfer Learning cơ bản. |
| **ResNet** | Skip Connection (Phần dư) | Giải quyết triệt tiêu Gradient, mạng cực sâu. | Độ phức tạp tính toán tăng dần theo số tầng. | Hầu hết các bài toán CV hiện đại (Base model). |
| **Inception** | Multi-scale (Nhiều size filter) | Hiệu quả tham số cao, trích xuất đa đặc trưng. | Kiến trúc phức tạp, khó tùy chỉnh/mở rộng. | Nghiên cứu sâu về trích xuất đặc trưng đa dạng. |
| **MobileNet** | Depthwise Separable Conv | Cực nhẹ, tốc độ xử lý nhanh. | Độ chính xác thấp hơn một chút so với ResNet. | Thiết bị di động, IoT, Camera thời gian thực. |
| **EfficientNet** | Compound Scaling | Cân bằng tối ưu giữa Depth, Width & Resolution. | Yêu cầu kỹ thuật huấn luyện và tài nguyên GPU tốt. | Khi cần độ chính xác SOTA với tài nguyên vừa phải. |


<!-- page 45 -->

# Tự đọc & thảo luận

- Cho bài đọc tại https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks/
- Nếu chúng ta có một ảnh đầu vào kích thước 32x32x3, thực hiện tích chập với 10 bộ lọc 5x5, s=1, p=0 thì kích thước Output đầu ra là bao nhiêu?
- Tính số lượng tham số cần học cho lớp Max Pooling với pooling size = 2x2


<!-- page 46 -->

# Thực hành 3

## Xây dựng CNN Baseline
- Sử dụng dataset CIFAR-10.
- Tự thiết kế một kiến trúc CNN đơn giản (3-4 layer Conv).
- **Yêu cầu:**
    - Vẽ đồ thị Loss/Accuracy và Confusion Matrix.
    - So sánh thời gian huấn luyện và inference giữa việc sử dụng CPU và GPU (trên môi trường Google Colab)


<!-- page 47 -->

# Thực hành 4

## Transfer Learning với ResNet50

- Vẫn sử dụng CIFAR-10 hoặc sử dụng một tập dữ liệu thực tế hơn (ví dụ: Phân loại các loại phương tiện giao thông hoặc khẩu trang).
- Thực hành kỹ thuật Fine-tuning và Feature Extraction (đóng băng layers).
- So sánh thời gian huấn luyện và inference giữa việc sử dụng CPU và GPU (trên môi trường Google Colab).
