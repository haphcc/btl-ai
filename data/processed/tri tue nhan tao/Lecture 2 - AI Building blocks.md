HC VIN NGN HNG
BAV 1961

# TR TU NHN TO
## IS54A

BAV HỌC VIỆN NGÂN HÀNG
1961

# Motivation

## MOTIVATION: FROM USER TO CREATOR

| USER (AI as Magic) | HOW IT WORKS? | CREATOR (AI Building Blocks) |
| :--- | :---: | :--- |
| Interacting with results | $\rightarrow$ | Understanding the components |

# Chương 1: Tổng quan về Trí tuệ nhân tạo (tiếp)

TS. Vũ Trọng Sinh
sinhvt@hvnh.edu.vn
0975674039

BAV HỌC VIỆN NGÂN HÀNG
1961

# Contents
## 1.5. AI Building blocks
## 1.6. AI techniques

# 1.5. AI Building blocks

### INPUTS
- 1 Structured Data
- 2 Unstructured Data

### PROCESSES
- 3 Pre-Processes
    - Natural Language Understanding (NLU)
    - Computer Vision
- 4 Main Processes
    - Problem Solving
    - Reasoning
    - Machine Learning

### OUTPUTS
- 6 Information
    - Natural Language Generation (NLG)
    - Image Generation
    - Robotics

**5 Knowledge Base**

Artificial intelligence: Building blocks and an innovation typology, Ulrich Paschen (2020)
https://www.sciencedirect.com/science/article/abs/pii/S000768131930151X https://www.diva-portal.org/smash/get/diva2:1400547/FULLTEXT01.pdf

# AI CYCLE: PERCEIVE, ANALYZE, REACT

## PERCEIVE (Nhận thức)
### INPUT (Đầu vào)

- **DATA ACQUISITION & SENSING**
- Gathering raw data from the environment (Visual, Audio, Sensor Data)

## ANALYZE (Phân tích)
### PROCESS (Xử lý)

- **DATA FLOW**
- **Pattern Recognition**
- **Reasoning & Problem Solving**
- **Knowledge Representation**
- **Machine Learning**
- Processing & Interpreting data (Algorithms, Models, Knowledge Base)

## REACT (Phản ứng)
### OUTPUT (Đầu ra)

- **DECISION / ACTION**
- Executing actions or providing information (Physical Action, Information, Decisions)
- Recommended Action: Slow Down
- Warning: Obstacle Detected

---

**LEARNING & ADAPTATION**

# Dữ liệu có cấu trúc

Dữ liệu được **chuẩn hóa** và tổ chức theo lược đồ định sẵn

VD:
- nhân khẩu học khách hàng, dữ liệu duyệt web hoặc dữ liệu giao dịch (dữ liệu nội bộ)
- đánh giá trên mạng xã hội hoặc giao dịch chứng khoán (dữ liệu bên ngoài)

### Tabular Data

| Player | Minutes | Points | Rebounds | Assists |
| :--- | :--- | :--- | :--- | :--- |
| A | 41 | 20 | 6 | 5 |
| B | 30 | 29 | 7 | 6 |
| C | 22 | 7 | 7 | 2 |
| D | 26 | 3 | 3 | 9 |
| E | 20 | 19 | 8 | 0 |
| F | 9 | 6 | 14 | 14 |
| G | 14 | 22 | 8 | 3 |
| I | 22 | 36 | 0 | 9 |
| J | 34 | 8 | 1 | 3 |

*Ghi chú: columns = attributes for those observations; Rows = observations*

# Dữ liệu phi cấu trúc

Dữ liệu không được chuẩn hóa hoặc tổ chức theo một lược đồ định sẵn.

**Dữ liệu phi cấu trúc ngày càng lớn.**
IoT, mạng xã hội và thiết bị di động rất phổ biến, chúng tạo ra dòng chảy dữ liệu vô tận hầu hết là phi cấu trúc.

Ví dụ: ngôn ngữ con người ở dạng viết, như blog, bài đăng, đánh giá, bình luận, hoặc tweet; lời nói, như âm thanh trong nội dung do người dùng tạo, và hình ảnh mô tả đối tượng hoặc con người.

# Unstructured data – sources and types

## Unstructured data sources

- Customer/Member Transactions
- Chat
- Online Communities
- Notes & Text Fields
- Surveys
- Email
- Social Media
- Voice Transcriptions
- Call Center
- Ratings & Reviews

## Unstructured data types

| | | | |
| :--- | :--- | :--- | :--- |
| **Text files and documents** | **Server, website and application logs** | **Sensor data** | **Images** |
| **Video files** | **Audio files** | **Emails** | **Social media data** |

# Liệu có dữ liệu lai giữa có cấu trúc và phi cấu trúc?

## Structured Data vs Unstructured Data

| Structured Data | Unstructured Data |
| :--- | :--- |
| **Can be displayed in rows, columns and relational databases** | **Cannot be displayed in rows, columns and relational databases** |
| **Numbers, dates and strings** | **Images, audio, video, word processing files, e-mails, spreadsheets** |
| **Estimated 20% of enterprise data (Gartner)** | **Estimated 80% of enterprise data (Gartner)** |
| **Requires less storage** | **Requires more storage** |
| **Easier to manage and protect with legacy solutions** | **More difficult to manage and protect with legacy solutions** |

# Semi-structured data

- **Dữ liệu bán cấu trúc** là loại dữ liệu không hoàn toàn có cấu trúc, nhưng cũng không hoàn toàn phi cấu trúc.
    - Nó chứa một mức độ tổ chức hoặc cấu trúc nào đó, nhưng không tuân theo một lược đồ hoặc mô hình dữ liệu cứng nhắc, và có thể chứa các yếu tố không dễ dàng phân loại hoặc sắp xếp.
- **Ví dụ: CSV/XML/JSON.**

### Unstructured data
The university has 5600 students.
John's ID is number 1, he is 18 years old and already holds a B.Sc. degree.
David's ID is number 2, he is 31 years old and holds a Ph.D. degree. Robert's ID is number 3, he is 51 years old and also holds the same degree as David, a Ph.D. degree.

### Semi-structured data
<University>
  <Student ID="1">
    <Name>John</Name>
    <Age>18</Age>
    <Degree>B.Sc.</Degree>
  </Student>
  <Student ID="2">
    <Name>David</Name>
    <Age>31</Age>
    <Degree>Ph.D.</Degree>
  </Student>
  ....
</University>

### Structured data

| ID | Name | Age | Degree |
| :--- | :--- | :--- | :--- |
| 1 | John | 18 | B.Sc. |
| 2 | David | 31 | Ph.D. |
| 3 | Robert | 51 | Ph.D. |
| 4 | Rick | 26 | M.Sc. |
| 5 | Michael | 19 | B.Sc. |

# Quiz

# Which of the following is unstructured/structured/semi-structured data?

- https://www.kaggle.com/datasets/deependraverma13/cardio-activities
- https://www.kaggle.com/datasets/sagaraiarchitect/laptop-price-explorer-the-ml-model
- https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- https://www.kaggle.com/datasets/wardaddy24/marble-surface-anomaly-detection
- https://www.kaggle.com/datasets/zalando-research/fashionmnist
- https://www.kaggle.com/datasets/ronikdedhia/next-word-prediction

# Tiền xử lý

- Tiền xử lý bao gồm **làm sạch dữ liệu, chuẩn hóa, chuyển đổi, trích xuất và lựa chọn đặc trưng**, với mục tiêu là dữ liệu còn lại có thể được xử lý theo những cách tạo ra giá trị.

Preprocessing of unstructured data in their various forms is more challenging due to their complexity and capacity

# Tiền xử lý - Natural language understanding

- Trí tuệ nhân tạo sử dụng hiểu ngôn ngữ tự nhiên (NLU) để **gán ý nghĩa cho ngôn ngữ con người**
- 2 forms of natural language: **text and acoustic signal**

---

### Hình ảnh minh họa
- **NLP**: NLP reads the words
- **NLU**: NLU understands the meaning (Keywords, Context)
- **Intent guides the path**
- **Better replies, less confusion**

# Natural language understanding levels

- **Lexical (Từ vựng):** Tách từ (Tokenizing), Phân đoạn từ.
- **Syntactic (Cú pháp):** Phân tích hình thái, Gán nhãn từ loại (POS Tagging).
- **Semantic (Ngữ nghĩa):** Khử mơ hồ nghĩa của từ, Mô hình hóa ngôn ngữ.
- **Discourse (Diễn ngôn):** Cảm xúc ngôn ngữ.

| Lexical | Syntactic | Semantic | Discourse |
| :--- | :--- | :--- | :--- |
| - Tokenizing. | - Morphology analysis | - Word sense disambiguation | - Language affection |
| - Word segmentation | - Part of Speech (POS) Tagging | - Language Modeling | |

# Ví dụ NLU

## Natural language understanding tasks

- Ông ấy nói: “tốc độ truyền thông tin ngày càng cao”.
  $\downarrow$ Tokenize
- **Ông** **ấy** **nói** **:** **“** **tốc** **độ** **truyền** **thông** **tin** **ngày** **càng** **cao** **”** **.**
  $\downarrow$ Word segmentation
- **Ông_ấy** nói : “ **tốc_độ** truyền **thông_tin** **ngày_càng** cao ” .
  $\downarrow$ POS tagging
- **Ông_ấy**/N nói/V :/sym “/sym **tốc_độ**/N truyền/V **thông_tin**/N **ngày_càng**/adv cao/Adv ” .

# Tiền xử lý – Speech Recognition

- Trước khi AI có thể hiểu ngôn ngữ nói, lời nói trước tiên cần được chuyển thành văn bản; bước này thường được gọi là **nhận dạng giọng nói**.

## SPEECH RECOGNITION PROCESS

Voice $\rightarrow$ Speech Enhancement $\rightarrow$ Feature Extraction $\rightarrow$ Phonetic Unit Recognition $\leftarrow$ Acoustic Modeling $\rightarrow$ Hello... (Text)

# Tiền xử lý – Thị giác máy tính

- **Computer Vision (CV)** là lĩnh vực khoa học giúp máy tính có khả năng "nhìn" và hiểu được thế giới thực thông qua hình ảnh kỹ thuật số (ảnh tĩnh, video).
- **Mục tiêu**: Tự động hóa các nhiệm vụ mà hệ thống thị giác của con người (mắt + não bộ) có thể làm được.

# Một số task tiêu biểu trong thị giác máy tính

| object recognition | object detection | semantic segmentation | image captioning |
| :--- | :--- | :--- | :--- |
| ![cat and ball](https://i.imgur.com/w5y1y5S.png) | ![cat and ball with boxes](https://i.imgur.com/w5y1y5S.png) | ![segmentation map](https://i.imgur.com/w5y1y5S.png) | ![cat and ball](https://i.imgur.com/w5y1y5S.png) |
| Cat | cat, ball | Red: cat<br>Green: ball<br>Blue: background | A cat is playing a ball. |
| (1) | (2) | (3) | (4) |

| image question answering | image generator | LiLi |
| :--- | :--- | :--- |
| ![cat and ball](https://i.imgur.com/w5y1y5S.png) | A cat is playing a ball.<br>![cat and ball](https://i.imgur.com/w5y1y5S.png) | Input Image: 1000111100010 / 10110100101110<br>LPN: R<br>Output Image: 1011111101110 |
| Q: How many balls are there in the image?<br>A: One. | | |
| (5) | (6) | (7) |

# Main processes

- **Áp dụng logic để đưa ra kết luận từ dữ liệu có sẵn**

Theory $\rightarrow$ Hypothesis $\rightarrow$ Patterns $\rightarrow$ Confirmation

*Ví dụ:*
- Tiên đề 1: Tất cả con người đều ăn rau.
- Tiên đề 2: Suresh là con người.
- Kết luận: Suresh ăn rau.

https://www.javatpoint.com/reasoning-in-artificial-intelligence

# Main processes – Problem solving

- Giải quyết vấn đề liên quan đến việc **chọn giải pháp tốt nhất từ một loạt các lựa chọn thay thế** để đạt được mục tiêu.
- Trong khoa học máy tính, thuật ngữ **"giải quyết vấn đề"** đề cập đến các phương pháp trí tuệ nhân tạo, có thể bao gồm việc xây dựng công thức đảm bảo sự phù hợp, sử dụng thuật toán và tiến hành phân tích nguyên nhân gốc rễ để xác định các giải pháp hợp lý.
- **Các kỹ thuật giải quyết vấn đề:**
    - Heuristics (Kinh nghiệm học)
    - Thuật toán tìm kiếm
    - Thuật toán di truyền

# Main processes – Machine learning

- **Học máy (ML)** bao gồm các kỹ thuật cho phép máy tính học từ kinh nghiệm, tức là dần dần cải thiện hiệu suất của chúng, mà không cần một tập hợp các quy tắc được xác định trước, rõ ràng được lưu trữ trong bộ nhớ.

| TRAINING DATA | Algorithm | Learning | Trained model | Results |
| :--- | :--- | :--- | :--- | :--- |
| (Biểu tượng kính lúp) | (Biểu tượng mạch điện) | (Biểu tượng bánh răng) | (Biểu tượng biểu đồ) | (Biểu tượng tài liệu) |

# Information output

- **Dạng đơn giản**: Kết quả dự đoán → Đầu ra API.
- **Dạng phức tạp**:
    - Tạo ngôn ngữ tự nhiên (NLG). Ví dụ: ChatGPT, Google Translate.
    - Tạo hình ảnh. Ví dụ: Stable Diffusion.
    - Robot action.

# Knowledge base

- Cơ sở tri thức (Knowledge Base - KB) là một kho lưu trữ thông tin tập trung, được cấu trúc hóa, chứa các **sự kiện (facts)**, **quy tắc (rules)**, và **mối quan hệ ngữ nghĩa (heuristics)** về một lĩnh vực cụ thể. Dữ liệu trong KB được biểu diễn dưới dạng hình thức (formal representation) để máy tính có thể truy xuất và sử dụng cho các quá trình suy luận tự động.

[Hình ảnh sơ đồ tri thức]

- **Programmer** -> profession -> Andy
- 1983 -> date of birth -> Andy
- Amy -> wife -> Andy
- Andy -> born in -> Washington
- Bob -> brother -> Andy
- 1986 -> date of birth -> Aileen
- Teacher -> profession -> Aileen
- Aileen -> wife -> Bob
- Bob -> born in -> Washington (đường kẻ đỏ)
- Lawyer -> profession -> Bob
- 1981 -> date of birth -> Bob
- Aileen -> born in -> New York
- Washington -> population -> 50K
- Washington -> capital of -> the United States

# Ví dụ - Chatbot trong ngân hàng

## AI BUILDING BLOCKS: BANKING CHATBOT FLOW

### AI CORE PROCESSING

- **USER VOICE INPUT** ("Kiểm tra số dư...")
- **1. INPUT DATA** (Unstructured Audio + Structured CRM Info)
- **2. PREPROCESSING** (Speech-to-Text, NLP, Entity Extraction)
- **3. KNOWLEDGE BASE & DATA** (Bank Rules, Interest Rates, Customer DB)
- **4. KEY PROCESSES** (ML Intent Classification, Reasoning & Security Check)
- **5. OUTPUT GENERATION** (NLG, Text-to-Speech)
- **AUDIO RESPONSE** ("Số dư là 50 triệu...")

# Discussion

- Take an AI application (e.g. ChatGPT, self-driving car, ...) and analyze its building blocks
- Những công nghệ nào cần thiết cho mỗi khối.

## 1.6. AI techniques

- **Máy móc không phải là con người, chúng ta không thể đưa cho chúng một cuốn sách và bảo chúng học.**
- Biểu diễn đầu vào/đầu ra/xử lý để chúng có thể hiểu.
- Dạy chúng cách tính toán/xử lý/thực hiện hành động/...
- Khi nào nên tuân theo quy tắc, khi nào nên tự đưa ra quyết định.
- Giải pháp có phải là tốt nhất không / Có thể cải thiện được không?

# Techniques used in AI

## Representation (knowledge representation):

Computer can not understand Vietnamese, can not watch Youtube tutorial

**They only understand 0 and 1**

- Anything must be converted to 0 and 1? → No, we have **Programming Language** & **Data Structure**

- Định nghĩa vấn đề theo ngôn ngữ lập trình, chuyển đổi dữ liệu (số, phân loại, văn bản, hình ảnh, video, ...) sang các cấu trúc dữ liệu phù hợp.

# Techniques used in AI

## Learning:
**We even simulate how our brains work by programming language**

- Automatically build up the knowledge from the environment

# Learning – mạng CNN trong thị giác máy tính

- **convolution + nonlinearity**
- **max pooling**
- **convolution + pooling layers**
- **vec**
- **fully connected layers**
- **Nx binary classification**

Các nhãn phân loại:
- bird: $p_{bird}$
- sunset: $p_{sunset}$
- dog: $p_{dog}$
- cat: $p_{cat}$
- ...

# Techniques used in AI

**Rules:**
- Tường minh: được tạo ra bởi chuyên gia con người.
- Ngầm định: tự động thu được thông qua học tập.

**Search:**
- Tìm kiếm chuỗi các trạng thái dẫn đến giải pháp nhanh hơn, hoặc tìm kiếm một tập hợp tối ưu các trọng số kết nối trong mạng nơ-ron

# Homework

Join this competition on Kaggle:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview

Create your own notebook and make a submission
