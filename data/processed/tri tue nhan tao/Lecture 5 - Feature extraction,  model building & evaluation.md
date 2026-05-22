# Lecture 5 - Feature extraction,  model building & evaluation



<!-- page 1 -->

# HC VIN NGN HNG
BANKING ACADEMY OF VIETNAM

# IS54A  TR TU NHN TO


<!-- page 2 -->

# Chương 3
# Machine Learning Pipeline (tiếp)

TS. Vũ Trọng Sinh
sinhvt@hvnh.edu.vn


<!-- page 3 -->

# Nội dung

- Trích xuất đặc trưng (Feature Extraction)
- Xây dựng mô hình (Model Building)
- Đánh giá mô hình (Model Evaluation)


<!-- page 4 -->

# Trích xuất đặc trưng (Feature extraction)

- **Feature extraction** là quá trình biến đổi dữ liệu thô thành một tập các đặc trưng mới (thường có số lượng ít hơn nhưng mang nhiều thông tin hơn)
- Quá trình này giúp đơn giản hóa dữ liệu, làm nổi bật các khía cạnh quan trọng và loại bỏ nhiễu, giúp mô hình học hiệu quả hơn.


<!-- page 5 -->

# Tại sao Feature extraction lại cần thiết

- **Giảm dữ liệu dư thừa:** Loại bỏ thông tin trùng lặp, giúp mô hình tập trung vào các tín hiệu quan trọng nhất.
- **Cải thiện độ chính xác:** Giảm thiểu hiện tượng quá khớp (**Overfitting**) bằng cách loại bỏ các đặc trưng gây nhiễu.
- **Tăng tốc độ học:** Dữ liệu tinh gọn giúp thuật toán hội tụ nhanh hơn.
- **Tối ưu tài nguyên:** Giảm bộ nhớ và năng lượng tính toán cần thiết cho việc xử lý các tác vụ không tạo thêm giá trị.


<!-- page 6 -->

# Trích xuất đặc trưng vs. Kỹ nghệ đặc trưng

**Kỹ nghệ đặc trưng (Feature engineering):** Là quá trình xử lý lại tập dữ liệu để cải thiện việc huấn luyện mô hình. Bằng cách thêm, xóa, kết hợp hoặc biến đổi dữ liệu, các nhà khoa học dữ liệu điều chỉnh dữ liệu huấn luyện để đảm bảo mô hình đáp ứng được mục đích sử dụng trong kinh doanh.

**Trích xuất đặc trưng (Feature extraction):** Là một tập con của kỹ nghệ đặc trưng. Kỹ thuật này được sử dụng khi dữ liệu ở dạng thô không thể sử dụng được trực tiếp.

| | |
| :--- | :--- |
| 💡 | Feature Creation |
| 🖐️ | Feature Transformation |
| 📥 | Feature Extraction |
| 🌐 | Feature Selection |
| ⚖️ | Feature Scaling |


<!-- page 7 -->

# Engineering vs. Extraction

- **Kỹ nghệ đặc trưng (Feature Engineering):**
    - *Hành động:* Bạn nhận thấy dữ liệu có cột Diện tích tầng 1, Diện tích tầng 2 và Diện tích ban công. Bạn tạo một cột mới là **Tổng diện tích = Tầng 1 + Tầng 2 + Ban công**.
    - *Tính chất:* Dựa trên kiến thức thực tế (**Domain knowledge**), đặc trưng mới vẫn giữ nguyên ý nghĩa vật lý ban đầu.

- **Trích xuất đặc trưng (Feature Extraction):**
    - *Hành động:* Bạn sử dụng thuật toán **PCA** trên 10 cột liên quan đến kích thước nhà để tạo ra 2 "thành phần chính" (**Principal Components**).
    - *Tính chất:* Thuật toán toán học tự động nén thông tin. Đặc trưng mới là các con số trừu tượng, không còn tên gọi hay ý nghĩa vật lý rõ ràng như "diện tích" hay "số phòng" nữa.


<!-- page 8 -->

# Feature extraction vs. feature selection

- **Lựa chọn đặc trưng (Feature selection)**: Giữ lại một tập con các đặc trưng quan trọng từ tập đặc trưng ban đầu (không làm thay đổi bản chất đặc trưng)
- **Feature extraction**: Tạo ra các đặc trưng mới bằng cách chiếu hoặc biến đổi dữ liệu gốc sang một không gian không gian mới

| Original Input Features | Select top 3 out of 6 through elimination | Final selected features |
| :--- | :--- | :--- |
| (Hình ảnh 6 ô màu) | (Mũi tên hướng xuống) | (Hình ảnh 3 ô màu) |

| Original Input Features | Create new features through linear combination | Final Created features |
| :--- | :--- | :--- |
| (Hình ảnh 6 ô màu) | (Mũi tên hướng xuống) | (Hình ảnh 3 ô tròn gradient) |

8


<!-- page 9 -->

# Các kỹ thuật Lựa chọn đặc trưng phổ biến

## Feature selection

i. Correlation
ii. Forward Selection
iii. Backward Elimination
iv. Select K Best
v. Missing value Ratio


<!-- page 10 -->

# Các kỹ thuật Trích xuất đặc trưng phổ biến

## Tabular data:

- **Giảm chiều dữ liệu (Dimensionality Reduction)**
    - **PCA (Principal Component Analysis):** Biến đổi dữ liệu sang không gian mới sao cho phương sai được bảo toàn tối đa.
    - **LDA (Linear Discriminant Analysis):** Tìm kiếm không gian mới giúp tối đa hóa sự phân biệt giữa các lớp.
    - **Autoencoder:** Sử dụng mạng thần kinh để nén (**Encode**) dữ liệu về một không gian biểu diễn thu gọn

Đọc thêm:
https://www.analyticsvidhya.com/blog/2021/04/guide-for-feature-extraction-techniques/


<!-- page 11 -->

# Các kỹ thuật Trích xuất đặc trưng theo loại dữ liệu

- **Dữ liệu văn bản (Text data):**
    - TF-IDF, CountVectorizer (Bag of Words), CBOW.
    - Vector nhúng (**Embedding vectors**) như Word2Vec, BERT.
- **Dữ liệu hình ảnh (Image data):**
    - HOG (Histogram of oriented gradients).
    - SIFT (Scale-invariant feature transform).
    - CNNs (Convolutional neural networks) - trích xuất đặc trưng tự động qua các lớp tích chập.
- **Dữ liệu âm thanh (Audio data):**
    - STFT (Short-time Fourier transform), MFCCs (Mel-frequency cepstral coefficients)


<!-- page 12 -->

# Xây dựng mô hình (Model building)

- Chia tập dữ liệu (**Split the dataset**).
- Chọn thuật toán (**Choose algorithm**).
- Tinh chỉnh siêu tham số (**Tune hyper parameters**).


<!-- page 13 -->

# Chia tập dữ liệu (Split the dataset)

- Đây là bước bắt buộc để đảm bảo tính khách quan khi đánh giá mô hình.
- Mô hình được huấn luyện trên một phần dữ liệu, điều chỉnh trên phần khác và cuối cùng được kiểm tra trên một phần hoàn toàn mới để đo lường khả năng tổng quát hóa (**Generalization**).

| Training Set (60%) | Dev Set (20%) | Test Set (20%) |
| :--- | :--- | :--- |

| Training Set (98%) |
| :--- |

- Training Set(98%)
- Dev Set(1%)
- Test Set(1%)


<!-- page 14 -->

# Train-Test Split

- **Mô tả:** Chia dữ liệu thành 2 tập: **Train** (Huấn luyện) và **Test** (Kiểm thử).
- **Tỷ lệ phổ biến:** 80/20 hoặc 70/30.
- **Lưu ý:** Thường dùng cho các bài toán có lượng dữ liệu đủ lớn và không cần tinh chỉnh siêu tham số quá phức tạp.

**A**
- Training
- Test
- Single Dataset

**B**
- Training
- Validation
- Test
- Single Dataset


<!-- page 15 -->

# Train-Validation-Test Split

- **Mô tả:** Chia thành 3 tập. Tập **Validation** đóng vai trò là "bài thi thử" để chọn ra siêu tham số tốt nhất trước khi thi thật trên tập **Test**.
- **Tỷ lệ:** 60/20/20 hoặc 70/15/15.
- **Mục đích:** Tránh việc mô hình bị "rò rỉ thông tin" từ tập kiểm thử trong quá trình tối ưu hóa.

**A**
- Training
- Test
- Single Dataset

**B**
- Training
- Validation
- Test
- Single Dataset


<!-- page 16 -->

# Kiểm định chéo (Cross-Validation)

- **Mô tả:** Chia dữ liệu thành nhiều phần, luân phương dùng một phần làm kiểm định, các phần còn lại làm huấn luyện.
- **Ưu điểm:** Tận dụng tối đa dữ liệu, giảm thiểu sai số do việc chia dữ liệu ngẫu nhiên không may mắn. (thường dùng khi bộ dữ liệu có số mẫu ít)

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| **Dataset** | **K = 4** | Fold 1 | Validation | Train | Train | Train |
| | | Fold 2 | Train | Validation | Train | Train |
| | | Fold 3 | Train | Train | Validation | Train |
| | | Fold 4 | Train | Train | Train | Validation |
| | | | Score | Score | Score | Score |


<!-- page 17 -->

# Các biến thể của Kiểm định chéo (Cross-Validation)

- **Leave-One-Out (LOOCV):** Dùng 1 mẫu duy nhất để kiểm tra, lặp lại cho đến hết. Chính xác nhưng cực kỳ tốn thời gian.
- **K-Fold Cross-Validation:** Chia thành **k** phần (thường k=5 hoặc 10). Đây là phương pháp cân bằng và phổ biến nhất.
- **Leave-P-Out:** Để lại **p** mẫu để kiểm định trong mỗi lần lặp.


<!-- page 18 -->

# Phân tách phân tầng (Stratified Split)

- **Mô tả:** Đảm bảo tỷ lệ các nhãn (ví dụ: 70% khách hàng ở lại, 30% rời đi) được duy trì đồng nhất trong tất cả các tập con.
- **Quan trọng:** Cực kỳ cần thiết cho dữ liệu mất cân bằng (**Imbalanced data**) để tránh việc tập huấn luyện không có đủ mẫu của lớp thiểu số.

| | Training Data | Test Data |
| :--- | :--- | :--- |
| **All Data** | **Split 1 score** | **Split 2 score** | **Split 3 score** | **Split 4 score** | **Split 5 score** |

**Average of all split scores**

18


<!-- page 19 -->

# Phân tách theo thời gian (Time-Based Split)

- **Mô tả:** Luôn dùng dữ liệu trong quá khứ để huấn luyện và dữ liệu tương lai để kiểm thử.
- **Tại sao?** Trong dữ liệu chuỗi thời gian, việc dùng dữ liệu tương lai để dự đoán quá khứ là vi phạm tính thực tế (Look-ahead bias).

| Chú thích |
| :--- |
| - Training Data |
| - Test Data |
| - All Homes Values ARIMA Predictions |

19


<!-- page 20 -->

# Chọn thuật toán (Choose algorithm)

- Không có thuật toán nào là tốt nhất cho mọi bài toán (**No Free Lunch Theorem**).
- Lựa chọn phụ thuộc vào: cấu trúc dữ liệu, tài nguyên phần cứng, yêu cầu về độ chính xác và khả năng giải thích.


<!-- page 21 -->

# Các yếu tố chọn thuật toán

- **Loại bài toán:** Phân lớp hay Hồi quy.
- **Kích thước dữ liệu:**
    - Dữ liệu ít: Ưu tiên thuật toán đơn giản (**Naive Bayes**, **Logistic Regression**).
    - Dữ liệu nhiều/phức tạp: Ưu tiên các mô hình mạnh (**Random Forest**, **Deep Learning**, **XGBoost**)


<!-- page 22 -->

# Các yếu tố chọn thuật toán

- **Scalability:** Các mô hình tuyến tính mở rộng rất tốt với hàng triệu mẫu.
- **Interpretability:** Trong các ngành như Tài chính/Y tế, khả năng giải thích "tại sao mô hình đưa ra quyết định đó" (**Explainable AI**) đôi khi quan trọng hơn cả độ chính xác tuyệt đối.


<!-- page 23 -->

# Một số thuật toán điển hình

## Machine Learning

- **Unsupervised Learning**
    - **Clustering**: K-Means, Mean Shift, K-Medoids
    - **Dimensionality Reduction**: Principal Component Analysis (PCA), Feature Selection, Linear Discriminant Analysis (LDA)
- **Supervised Learning**
    - **Regression**: Decision Tree, Linear Regression, Logistic Regression
    - **Classification**: Navie Bayes, SVM, K-Nearest Neighbor
- **Reinforcement Learning**

---

- **Supervised Learning (Học có giám sát):**
    - **Classification (Phân loại):** Logistic Regression, Naive Bayes, SVM, K-Nearest Neighbor, Decision Tree, Random Forest.
    - **Regression (Hồi quy):** Linear Regression, Ridge/Lasso Regression, Decision Tree.
- **Unsupervised Learning (Học không giám sát):**
    - **Clustering:** K-Means, DBSCAN.
    - **Dimensionality Reduction:** PCA, LDA.


<!-- page 24 -->

# Tinh chỉnh siêu tham số (Tune hyper parameters)

- **Tham số (Parameters):** Do mô hình tự học (ví dụ: trọng số của mạng thần kinh).
- **Siêu tham số (Hyperparameters):** Do người dùng cấu hình trước khi học (ví dụ: số cây trong rừng, độ sâu của cây, tốc độ học).
- **Mục tiêu:** Tìm ra "công thức" cấu hình giúp mô hình đạt hiệu suất cao nhất.


<!-- page 25 -->

# Kỹ thuật tuning - Grid Search

- Thử nghiệm mọi tổ hợp có thể trong một lưới giá trị định sẵn.
- **Đặc điểm:** Đảm bảo tìm được điểm tốt nhất trong lưới nhưng cực kỳ chậm nếu có nhiều siêu tham số.
- **Cons:** Computationally expensive, especially for large grids.

| Grid Search | Random Search |
| :--- | :--- |
| (Hình minh họa lưới với các điểm đỏ và điểm xanh lá cây chỉ "Best Result") | (Hình minh họa lưới với các điểm đỏ rải rác và điểm xanh lá cây chỉ "Best Result") |

25


<!-- page 26 -->

# Kỹ thuật tuning - Random Search

- Thử nghiệm ngẫu nhiên các tổ hợp tham số.
- **Đặc điểm:** Thường tìm được kết quả "đủ tốt" nhanh hơn rất nhiều so với Grid Search vì nó không lãng phí thời gian vào các vùng tham số kém tiềm năng.
- **Cons:** May miss the optimal values.

| Grid Search | Random Search |
| :--- | :--- |
| (Hình ảnh lưới các điểm đỏ với một điểm xanh lá cây là "Best Result") | (Hình ảnh lưới với các điểm đỏ phân bố ngẫu nhiên và một điểm xanh lá cây là "Best Result") |


<!-- page 27 -->

# Gradient-Based Optimization

- Sử dụng đạo hàm để tìm hướng thay đổi siêu tham số giúp giảm lỗi nhanh nhất.
- Áp dụng chủ yếu cho các siêu tham số có tính chất liên quan đến cấu trúc toán học của mô hình (như trọng số, bias)

**Cons**: Not applicable to discrete hyperparameters.


<!-- page 28 -->

# Các kỹ thuật Tuning khác & Thư viện

- **Bayesian Optimization:** Học từ các lần thử trước để đoán xem vùng tham số nào tiềm năng nhất (thông minh hơn Random Search).
- **Thư viện phổ biến:** GridSearchCV (Scikit-learn), **Optuna** (rất mạnh mẽ và hiện đại), **Hyperopt**.


<!-- page 29 -->

# Đánh giá mô hình (Evaluation)

Đánh giá không chỉ là xem mô hình đúng bao nhiêu phần trăm, mà là hiểu mô hình sai ở đâu và tại sao.

The choice of evaluation metrics depends on the **type of problem** you are solving (classification, regression, clustering, etc.)


<!-- page 30 -->

# Chỉ số đánh giá cho bài toán Phân loại (Classification)

- **Accuracy:** Dễ hiểu nhưng vô dụng nếu dữ liệu mất cân bằng (ví dụ: 99% mẫu là âm tính, chỉ cần dự đoán âm tính hết là đã đúng 99%).
- **Precision:** Quan trọng khi cái giá của việc "nhầm lẫn dương tính" là rất lớn (ví dụ: lọc thư rác).
- **Recall:** Quan trọng khi cái giá của việc "bỏ sót dương tính" là rất lớn (ví dụ: chẩn đoán ung thư).
- **F1 Score:** Cân bằng giữa Precision và Recall.


<!-- page 31 -->

# HỌC VIỆN NGÂN HÀNG

| | predicted condition | | |
| :--- | :--- | :--- | :--- |
| **total population** | **prediction positive** | **prediction negative** | **Sensitivity** |
| **true condition** | **condition positive** | **True Positive (TP)** | **False Negative (FN)**<br>(Type II error) | **Recall =**<br>$$\frac{\sum TP}{\sum \text{condition positive}}$$ |
| | **condition negative** | **False Positive (FP)**<br>(Type I error) | **True Negative (TN)** | **Specificity =**<br>$$\frac{\sum TN}{\sum \text{condition negative}}$$ |
| | **Accuracy =**<br>$$\frac{\sum TP + \sum TN}{\sum \text{total population}}$$ | **Precision =**<br>$$\frac{\sum TP}{\sum \text{prediction positive}}$$ | | **F1 Score =**<br>$$\frac{2}{\frac{1}{\text{Recall}} + \frac{1}{\text{Precision}}}$$ |


<!-- page 32 -->

# Ma trận nhầm lẫn (Confusion Matrix)

- Cho cái nhìn chi tiết về các loại sai lầm của mô hình.
- Giúp xác định xem mô hình đang bị thiên kiến (**Bias**) về phía lớp nào.

| | academic | government | media | professional | public |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **academic** | 47 | 12 | 0 | 7 | 3 |
| **government** | 4 | 60 | 1 | 7 | 1 |
| **media** | 4 | 6 | 2 | 0 | 2 |
| **professional** | 3 | 0 | 0 | 49 | 1 |
| **public** | 1 | 1 | 0 | 2 | 104 |

*Predicted label*


<!-- page 33 -->

# Đồ thị ROC và Precision-Recall Curve

- **ROC Curve:** Đo lường khả năng phân biệt giữa các lớp. AUC càng gần 1 thì mô hình càng tốt.
- **PR Curve:** Tốt hơn ROC khi làm việc với dữ liệu có sự chênh lệch lớn về số lượng mẫu giữa các lớp.

https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/


<!-- page 34 -->

# Chỉ số đánh giá cho bài toán Hồi quy (Regression)

- **MAE:** Trung bình lỗi tuyệt đối (dễ hình dung đơn vị).
- **MSE:** Phạt nặng các lỗi lớn (do bình phương).
- **RMSE:** Đưa đơn vị lỗi về cùng đơn vị với biến mục tiêu.
- **R-squared:** Cho biết mô hình giải thích được bao nhiêu % sự biến thiên của dữ liệu (càng gần 1 càng tốt).
