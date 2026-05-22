# Lecture 6 - Model deployment



<!-- page 1 -->

# HỌC VIỆN NGÂN HÀNG
# BANKING ACADEMY OF VIETNAM

# IS54A
# Trí tuệ nhân tạo


<!-- page 2 -->

# Chương 3
# Machine learning pipeline (tiếp)

TS. Vũ Trọng Sinh
sinhvt@hvnh.edu.vn

2


<!-- page 3 -->

# Nội dung

- Giới thiệu
- Quy trình triển khai (Deployment Workflow)
- Các chiến lược triển khai
- Các thực tiễn tốt nhất (Best Practices)
- Xây dựng ứng dụng Web tương tác với Streamlit


<!-- page 4 -->

# Triển khai mô hình (Model Deployment)

## What is Model Deployment?

Là quá trình làm cho một mô hình máy học (machine learning) đã được huấn luyện sẵn sàng để sử dụng trong môi trường sản phẩm (production environment).

---

### Building Data Pipeline
- Gathering Data
- Cleaning Data
- EDA
- Model Design
- Training and Validation

### Building the ML Model
- ML Algorithm
- Hyperparameters
- Training the Model
- Evaluating the Model

### Using Model for Predictions
- Deploying the Model
- Making Predictions
- Monitoring the Model


<!-- page 5 -->

# Introduction

## Tầm quan trọng của việc triển khai

- Chuyển đổi các mô hình từ thử nghiệm thành các giải pháp thực tế.
- Cho phép dự đoán thời gian thực trên dữ liệu mới.
- Cho phép tích hợp vào các ứng dụng và hệ thống.


<!-- page 6 -->

# Deployment Workflow

| Model Training | Model Selection | Model Serialization | Model Integration | Monitoring & Maintenance |
| :--- | :--- | :--- | :--- | :--- |
| Phát triển và huấn luyện mô hình máy học sử dụng dữ liệu lịch sử | Chọn mô hình hoạt động tốt nhất dựa trên kết quả đánh giá | Tuần tự hóa (đóng gói) mô hình đã huấn luyện để lưu trạng thái của nó cho việc sử dụng sau này | Chọn một framework hoặc nền tảng triển khai phù hợp với các yêu cầu của ứng dụng <br><br> Tích hợp mô hình vào ứng dụng hoặc hệ thống đích | Giám sát hiệu suất của mô hình và cập nhật khi cần thiết để duy trì hiệu quả theo thời gian |


<!-- page 7 -->

# Model Serialization

Tuần tự hóa mô hình đề cập đến quá trình lưu trạng thái của mô hình đã huấn luyện vào đĩa dưới định dạng có thể dễ dàng tải và sử dụng lại sau này

## Techniques:

Các định dạng tuần tự hóa phổ biến bao gồm **pickle** (cho các đối tượng Python), **joblib**, và **HDF5** (cho các mảng số lớn).

Một số thư viện, như scikit-learn, cung cấp sẵn các phương pháp tuần tự hóa tích hợp


<!-- page 8 -->

# Deployment Framework

Một framework hoặc nền tảng triển khai cung cấp cơ sở hạ tầng và các công cụ cần thiết để triển khai các mô hình máy học trong môi trường sản xuất

- Chọn framework triển khai dựa trên các yếu tố như khả năng mở rộng, tính dễ sử dụng, khả năng tương thích với các hệ thống hiện có và chi phí
- Các framework/nền tảng triển khai phổ biến bao gồm: **AWS SageMaker**, **Microsoft Azure ML**, **Google Cloud AI Platform**, và **Docker containers**


<!-- page 9 -->

# Model Integration

Tích hợp mô hình liên quan đến việc đưa mô hình máy học đã triển khai vào ứng dụng hoặc hệ thống đích, nơi nó sẽ được sử dụng để đưa ra dự đoán

- **API:** Cho phép truy cập từ xa vào mô hình để đưa ra dự đoán qua mạng
- **SDK:** Cung cấp các thư viện và công cụ để đơn giản hóa việc tích hợp mô hình vào các ngôn ngữ lập trình hoặc nền tảng cụ thể
- **Nhúng (Embedding):** Liên quan đến việc đưa trực tiếp mã nguồn mô hình vào bên trong ứng dụng, phù hợp cho các triển khai ngoại tuyến (offline)


<!-- page 10 -->

# Monitoring and Maintenance

**Monitoring** Giám sát liên quan đến việc theo dõi liên tục hiệu suất và hành vi của mô hình đã triển khai trong môi trường sản xuất thực tế. Bảo trì đề cập đến việc cập nhật và cải thiện mô hình theo thời gian để đảm bảo tính hiệu quả và phù hợp của nó.

**Monitoring Metrics:**

- Các chỉ số hiệu suất chính (KPIs) như độ chính xác dự đoán, độ trễ, thông lượng và tỷ lệ lỗi
- Các công cụ giám sát và bảng điều khiển (dashboards) có thể giúp trực quan hóa và phân tích các chỉ số này để phát hiện bất thường hoặc suy giảm hiệu suất


<!-- page 11 -->

# Monitoring and Maintenance

## Maintenance Tasks:

- **Định kỳ huấn luyện lại** mô hình với dữ liệu mới để thích ứng với các thay đổi về xu hướng và mẫu dữ liệu
- **Cập nhật mô hình** để kết hợp các tính năng mới, cải thiện thuật toán hoặc giải quyết các vấn đề hiệu suất được xác định trong quá trình giám sát
- **Thực hiện kiểm soát phiên bản** để theo dõi các thay đổi và quay lại các phiên bản trước nếu cần thiết


<!-- page 12 -->

# Các chiến lược triển khai

- **Container hóa (Containerization)** Sử dụng các công nghệ container hóa như Docker để đóng gói mô hình và các thư viện phụ thuộc của nó để dễ dàng triển khai trên các môi trường khác nhau.
- **Điện toán không máy chủ (Serverless Computing)** Tận dụng các nền tảng serverless như AWS Lambda hoặc Google Cloud Functions để triển khai và chạy mô hình mà không cần quản lý máy chủ.


<!-- page 13 -->

# Các chiến lược triển khai (tiếp)

- **API Endpoints**: Công khai mô hình dưới dạng một RESTful API endpoint, cho phép các ứng dụng khác gửi yêu cầu và nhận kết quả dự đoán.
- **Điện toán biên (Edge Computing)**: Triển khai mô hình trực tiếp trên các thiết bị biên (ví dụ: thiết bị IoT hoặc thiết bị di động) để thực hiện dự đoán cục bộ mà không phụ thuộc vào máy chủ trung tâm.


<!-- page 14 -->

# Best Practices

- **Kiểm soát phiên bản (Version Control)** Sử dụng các hệ thống kiểm soát phiên bản (ví dụ: Git) để theo dõi các thay đổi đối với mã nguồn mô hình và cấu hình.
- **Tài liệu hóa (Documentation)** Tài liệu hóa quy trình triển khai, bao gồm các thư viện phụ thuộc, thiết lập môi trường và hướng dẫn triển khai.
- **Bảo mật (Security)** Thực hiện các biện pháp bảo mật để bảo vệ dữ liệu nhạy cảm và ngăn chặn truy cập trái phép vào mô hình đã triển khai.
- **Kiểm thử (Testing)** Tiến hành kiểm thử kỹ lưỡng mô hình đã triển khai để đảm bảo độ tin cậy và chính xác trong các tình huống thực tế (A/B testing)


<!-- page 15 -->

# Xây dựng ứng dụng Web tương tác với Streamlit

- What is Streamlit?
- Getting Started with Streamlit
- Example Streamlit App: Iris Classifier
- Running the App
- Deploy the demo app to Streamlit cloud


<!-- page 16 -->

# What is Streamlit?

Streamlit là một thư viện Python mã nguồn mở để xây dựng các **ứng dụng web tương tác** cho các dự án máy học và khoa học dữ liệu.

## DataFrame Demo

This demo shows how to use `st.write` to visualize Pandas DataFrames. (Data courtesy of the UN Data Explorer.)

**Choose countries**

| | 1961 | 1962 | 1963 | 1964 | 1965 | 1966 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| China | 58.3407 | 60.6909 | 63.9427 | 68.4626 | 74.7479 | 80.4459 |
| United States of America | 89.8166 | 90.2750 | 93.7004 | 94.3237 | 97.7041 | 97.2772 |

**Gross Agricultural Production ($B)**

(Biểu đồ vùng hiển thị dữ liệu sản xuất nông nghiệp theo năm cho China và United States of America)


<!-- page 17 -->

# Bắt đầu với Streamlit

## Installation instructions
https://docs.streamlit.io/get-started/installation

- Command line
- Anaconda

## Run a hello world example

17


<!-- page 18 -->

# Example Streamlit App: Iris Classifier

Tạo một ứng dụng Streamlit đơn giản để phân loại hoa Iris sử dụng một mô hình máy học đã được huấn luyện trước

Tải xuống tài liệu mã nguồn cùng với slide bài giảng


<!-- page 19 -->

# Running the App

Mở terminal và điều hướng đến thư mục chứa tập lệnh (script).

- Run the **iris_classifier.py** script to build a model
- Run the **app.py** to create a demo page
- **streamlit run app.py**

## Iris Classifier

- Sepal Length: 4.42 (4.00 - 8.00)
- Sepal Width: 2.59 (2.00 - 4.50)
- Petal Length: 4.00 (1.00 - 7.00)
- Petal Width: 1.00 (0.10 - 2.50)

## Prediction:
versicolor


<!-- page 20 -->

# Streamlit fundamentals

https://docs.streamlit.io/get-started/fundamentals

- Chạy một ứng dụng: streamlit run / Python module
- Luồng phát triển (Development flow)
- Hiển thị và định dạng dữ liệu
- Các Widgets (thành phần giao diện)
- Bố cục (Layout)


<!-- page 21 -->

# Streamlit tutorial

https://docs.streamlit.io/get-started/tutorials

Làm theo hướng dẫn để xây dựng ứng dụng đơn trang (single-page), ứng dụng đa trang (multi-page)


<!-- page 22 -->

# Deploy the demo app to Streamlit cloud

https://docs.streamlit.io/streamlit-community-cloud/get-started

Your task:
- Huấn luyện mô hình phân loại Iris trên máy của bạn.
- Tuần tự hóa mô hình thành file pickle (.pkl).
- Xây dựng một ứng dụng streamlit demo.
- Triển khai ứng dụng của bạn lên streamlit cloud (làm theo hướng dẫn này: https://docs.streamlit.io/deploy/streamlit-community-cloud)
- https://www.youtube.com/watch?v=HKoOBiAaHGg


<!-- page 23 -->

# Homework

## Create a Streamlit demo app for your Kaggle model

Instructions:
- Train a simple model (select 3-4 simple features) on Kaggle notebook
- Serialize your model to a pickle file
- Download the pickle file
- Write an streamlit app that load the pickle model, display the input form and show the prediction results
