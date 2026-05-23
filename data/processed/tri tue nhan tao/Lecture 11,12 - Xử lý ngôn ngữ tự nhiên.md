**HỌC VIỆN NGÂN HÀNG**

# IS54A Trí tuệ nhân tạo

TS. VŨ TRỌNG SINH
T: 0975674039
E: sinhvt@hvnh.edu.vn
W: itde.hvnh.edu.vn

1961

# CHƯƠNG 5
# XỬ LÝ NGÔN NGỮ TỰ NHIÊN

# Motivation

- Chúng ta có hiểu chính xác những gì đang nghe/đọc hằng ngày (tiếng Việt/Anh/Pháp/Nhật/v.v.)
- Làm sao để máy tính hiểu được những gì ta nói
- Làm sao để máy tính giao tiếp với con người bằng ngôn ngữ tự nhiên

# Nội dung

## 4.1. Tổng quan về xử lý ngôn ngữ tự nhiên (NLP) và ứng dụng
## 4.2. Các nhiệm vụ (task) của NLP
- Hiểu ngôn ngữ tự nhiên
- Sinh ngôn ngữ tự nhiên
## 4.3. Cách tiếp cận giải quyết các nhiệm vụ trong NLP
- Phương pháp học máy dựa trên thống kê
- Phương pháp học sâu
## 4.4. Mô hình ngôn ngữ lớn

1961

# 4.1. Tổng quan về NLP và ứng dụng

- **Ngôn ngữ** là một hệ thống giao tiếp có cấu trúc được con người sử dụng, bao gồm hai thành phần cơ bản: *lời nói và văn bản*.
- **Ngôn ngữ tự nhiên**, hay ngôn ngữ thông thường, là bất kỳ ngôn ngữ nào xuất hiện một cách tự nhiên trong cộng đồng con người *thông qua quá trình sử dụng, lặp lại và biến đổi* mà không có sự lập kế hoạch hoặc tính toán trước

1961

# Ngôn ngữ tự nhiên vs. không tự nhiên

## Ngôn ngữ tự nhiên
- Tiếng Việt, tiếng Anh, tiếng Pháp, v.v.
- Ngôn ngữ của các dân tộc thiểu số

## Ngôn ngữ không tự nhiên
- Ngôn ngữ lập trình
- Ngôn ngữ hình thức trong Toán, Logic
- Quốc tế ngữ (Esperanto)
- Mã Morse

- Natural Language
- Artificial Language
- Constructed Language

# Máy tính hiểu ngôn ngữ như thế nào?

**Không AI:** Máy tính không hiểu ngôn ngữ của con người, chúng chỉ hiểu các ngôn ngữ lập trình (*programming language*) được biên dịch thành ngôn ngữ máy và các cấu trúc dữ liệu (*data structure*) có sẵn.

**Có AI:** Máy tính không hiểu ngôn ngữ theo cách con người hiểu. Thay vào đó, chúng xử lý ngôn ngữ dựa trên các mô hình thống kê, quy tắc và thuật toán học.

**Xử lý ngôn ngữ tự nhiên (NLP)** là một lĩnh vực liên ngành của khoa học máy tính và truy xuất thông tin, NLP tập trung vào việc giúp máy tính có khả năng hiểu, sinh ngôn ngữ tự nhiên, giao tiếp bằng ngôn ngữ tự nhiên với con người.

# Những thách thức trong NLP

Ngôn ngữ tự nhiên rất khó hiểu
- **Nhập nhằng (Ambiguity)**: I saw a man on the hill with a telescope
- **Phụ thuộc ngữ cảnh (Context dependency)**: Ông già đi nhanh quá
- **Đa ngôn ngữ (Multilingual text)**: Mọi người đừng make it complicated nữa, cứ enjoy cái moment này thôi!
- **Lẫn các thực thể định danh (Named entities)**: Trung Nguyên vừa ra mắt loại cà phê mới
- **Trendy words, teen code**: Getgo, Gato, LOL
- **Ký tự gây nhiễu (Noisy tokens)**: World cup @Quartar số dzáchhhh!! Xem live đã quá trời 🤩 #Quartar #wc22

# Những thách thức trong NLP

## Thách thức kỹ thuật:
- Dữ liệu văn bản và âm thanh rất lớn, chứa nhiều nhiễu
- Các kỹ thuật biểu diễn ngôn ngữ tự nhiên trong máy tính và thuật toán học ngày càng phức tạp (từ học máy thống kê đến học sâu RNN và Transformers)
- Đòi hỏi năng lực tính toán (computational resource) rất mạnh của máy tính (CPU, GPU, TPU, NPU, parallel computing)

# Một số ứng dụng của NLP trong business

- Chatbot & Trợ lý ảo
- Phân tích ý kiến khách hàng
- Dịch thuật tự động
- Tóm tắt & trích xuất thông tin
- Nhận diện giọng nói & Chuyển đổi giọng nói thành văn bản
- Phát hiện gian lận & Kiểm duyệt nội dung

1961

## 4.2. Các nhiệm vụ (task) của NLP

- **NLP**: Natural Language Processing
- **NLU**: Natural Language Understanding
- **NLG**: Natural Language Generating

# Hiểu ngôn ngữ tự nhiên

❖ NLU thường bao gồm các mức hiểu ngôn ngữ tự nhiên như sau:
- Morphological analysis – mức từ vựng
- Syntactic analysis – mức ngữ pháp
- Semantic analysis – mức ngữ nghĩa
- Discourse – mức ẩn dụ

# Phân tích từ vựng

- **Tokenization**: phân tách đoạn văn bản thành các “token”
- **Word segmentation**: Phân tách đoạn văn bản thành các “từ”

• Ông ấy nói: “tốc độ truyền thông tin ngày càng cao”.
$\downarrow$ Tokenize
• Ông ấy nói : “ tốc độ truyền thông tin ngày càng cao ” .
$\downarrow$ Word segmentation
• Ông_ấy nói : “ tốc_độ truyền thông_tin ngày_càng cao ” .
$\downarrow$ POS tagging
• Ông_ấy/N nói/V :/sym “/sym tốc_độ/N truyền/V thông_tin/N ngày_càng/adv cao/Adv ” .

# Phân tích ngữ pháp

## Lemmatization (Chuẩn hóa từ gốc)
Là nhiệm vụ loại bỏ các hậu tố biến đổi từ nhưng vẫn giữ lại dạng từ gốc có trong từ điển, còn được gọi là **lemma**.

## Stemming (Rút gọn từ gốc)
Là quá trình đưa các từ có biến đổi (hoặc đôi khi là từ phát sinh) về một dạng gốc. Ví dụ, **"close"** là gốc của các từ **"closed"**, **"closing"**, **"closer"**, v.v.

## Part-of-speech tagging (Gán nhãn từ loại)
Xác định loại từ (danh từ, động từ, tính từ, v.v.) cho từng từ trong một câu.

## Parsing (Phân tích quan hệ phụ thuộc & phân tích cấu trúc)
Xác định cây phân tích cú pháp (biểu diễn quan hệ ngữ pháp) của một câu đã cho.

# Phân tích ngữ pháp

## ❖ Ví dụ:

- Ông ấy nói: “tốc độ truyền thông tin ngày càng cao”.
  $\downarrow$ Tokenize
- Ông ấy nói : “ tốc độ truyền thông tin ngày càng cao ” .
  $\downarrow$ Word segmentation
- Ông_ấy nói : “ tốc_độ truyền thông_tin ngày_càng cao ” .
  $\downarrow$ POS tagging
- Ông_ấy/N nói/V :/sym “/sym tốc_độ/N truyền/V thông_tin/N ngày_càng/adv cao/Adv ” .

**Sơ đồ phân tích cú pháp:**

- S
    - NP
        - N
            - Tốc độ
    - VP
        - V
            - Truyền
        - NP
            - N
                - Thông_tin
        - AP
            - adv
                - Ngày_càng
            - adv
                - cao

Tốc_độ/N truyền/V thông_tin/N ngày_càng/adv cao/adv

# Phân tích ngữ nghĩa

## **Named Entity Recognition (NER) - Nhận diện thực thể có tên**
Xác định các thực thể có tên trong một đoạn văn bản, chẳng hạn như *tên người, địa điểm, tổ chức*, và phân loại chúng theo loại tương ứng (ví dụ: **người, địa danh, tổ chức**).

## **Word-Sense Disambiguation (WSD) - Phân biệt nghĩa của từ**
Nhiều từ có nhiều hơn một nghĩa, vì vậy cần chọn nghĩa phù hợp nhất dựa trên ngữ cảnh.

## **Relationship Extraction - Trích xuất mối quan hệ**
Xác định mối quan hệ giữa các thực thể có tên trong văn bản, ví dụ: "Ai kết hôn với ai?", "Công ty nào sở hữu thương hiệu nào?".

## **Semantic Parsing - Phân tích ngữ nghĩa**
Chuyển đổi một đoạn văn bản (thường là một câu) thành một biểu diễn ngữ nghĩa chính thức, có thể ở dạng *đồ thị (như AMR parsing)* hoặc tuân theo một hệ thống logic nhất định.

# Phân tích ẩn dụ

Nghiên cứu cách các câu trong một văn bản liên kết với nhau để tạo thành một nội dung mạch lạc.

## Coreference Resolution - Giải quyết đồng tham chiếu
Xác định các từ hoặc cụm từ trong một câu hoặc văn bản lớn hơn để cập đến cùng một thực thể. Ví dụ: Trong câu "Mai nói rằng cô ấy sẽ đi du lịch", hệ thống cần xác định "cô ấy" chính là "Mai".

## Sentiment Analysis - Phân tích cảm xúc
Trích xuất thông tin mang tính chủ quan từ văn bản, thường được sử dụng để phân loại đánh giá trực tuyến thành các mức cảm xúc như **tích cực, tiêu cực hoặc trung tính**. Ví dụ: "Sản phẩm này rất tuyệt!" có cảm xúc tích cực, trong khi "Dịch vụ quá tệ!" mang cảm xúc tiêu cực.

## Recognizing Textual Entailment - Nhận diện hàm ý văn bản
Xác định mối quan hệ logic giữa hai đoạn văn bản (**Entailment, Contradiction, Neutral**)

# Sinh ngôn ngữ tự nhiên

## Natural Language Generation (NLG) - Sinh ngôn ngữ tự nhiên
Chuyển đổi thông tin từ cơ sở dữ liệu hoặc ý định ngữ nghĩa thành văn bản dễ đọc bằng ngôn ngữ con người. Ví dụ: **Viết báo cáo tài chính từ dữ liệu thô**.

- **Automatic Summarization (Tóm tắt tự động)**
Tạo một bản tóm tắt súc tích, dễ đọc từ một đoạn văn bản dài, giúp người dùng nắm bắt nội dung chính nhanh chóng.
- **Machine Translation (MT) - Dịch máy**
Dịch tự động văn bản từ một ngôn ngữ sang ngôn ngữ khác, ví dụ: Google Translate.
- **Caption Generation (Gắn chú thích ảnh)**
Tạo chú thích cho hình ảnh hoặc video.

# Một số nhiệm vụ khác có liên quan

- **Optical Character Recognition (OCR)** - Nhận diện ký tự quang học: Chuyển đổi văn bản từ hình ảnh (chẳng hạn như ảnh chụp sách, tài liệu in) thành văn bản kỹ thuật số.
- **Speech Recognition - Nhận diện giọng nói**: Chuyển đổi âm thanh giọng nói thành văn bản. VD: Google Speech-to-Text, Whisper
- **Speech Segmentation - Phân đoạn giọng nói**: Tách một đoạn âm thanh thành từng từ hoặc từng câu riêng biệt.
- **Text-to-Speech (TTS) - Chuyển văn bản thành giọng nói**: Chuyển đổi văn bản thành âm thanh giọng nói con người. Công nghệ này hỗ trợ người khiếm thị hoặc giúp tạo giọng đọc nhân tạo cho sách nói, trợ lý ảo. VD: Google TTS, Amazon Polly, ElevenLabs.
- **Text-to-Image Generation - Sinh ảnh từ văn bản**: Tạo hình ảnh dựa trên mô tả bằng văn bản
- **Text-to-Video - Sinh video từ văn bản**: Tạo video từ mô tả bằng văn bản mà không cần quay phim thực tế

# 4.3 Cách tiếp cận giải quyết các task trong NLP

- Phương pháp dựa trên thống kê
    - Parallel Sentence pairs
    - Alignment
    - my son is going to school
    - con trai tôi đang đi học
    - e1 e2 e3 e4 e5 e6
    - v1 v2 v3 v4 v5 v6
    - $P(e\_i1|v\_j) =$
    - $P(e\_i2|v\_j) =$
    - $P(e\_i3|v\_j) =$
    - $e\_1, e\_2, \dots, e\_n$
    - Start, end

- Phương pháp dựa trên học sâu
    - encoder
    - my son is going to school
    - con trai ...
    - `<s>` con

# Phương pháp dựa trên thống kê

Con người **hiểu (phân loại) văn bản** như thế nào?

"I love this movie. I've seen it many times and it's still awesome." $\rightarrow$ 👍

"This movie is bad. I don't like it it all. It's terrible." $\rightarrow$ 👎

**Sentiment Analysis Challenges**
- Theoretical
    - Negation
    - Extracting Topic Features
    - World Knowledge
    - Spam or fake reviews
    - Domain Dependance
- Technical
    - NLP Overheads
    - Thwarted Expectations
    - Huge lexicon
    - Temporal Relations
    - Bi-polar words

# Trích xuất “đặc trưng” từ văn bản

- Các đoạn văn/câu văn trên có những thuộc tính (**attribute**) hay đặc trưng (**feature**) như dữ liệu dạng bảng khi phân lớp?
- Những keyword đóng vai trò gì?

$\rightarrow$ Phương pháp đơn giản nhất: xem xét sự **có mặt/vắng mặt** của các từ trong văn bản như là “đặc trưng” của văn bản đó

# Chuyển hóa văn bản thành vector

- Trong bài toán phân loại review phim thành Positive/Negative, xét 3 review sau:
    - “this is a good movie”
    - “good movie, good actors”
    - “a bad movie”
- **Vocabulary**: (7 từ khác nhau)
    - ["this", "is", "a", "good", "movie", "actors", "bad"]
- **Chuyển hóa thành vector**:
    - “this is a good movie” $\rightarrow [1, 1, 1, 1, 1, 0, 0]$
    - “good movie, good actors” $\rightarrow [0, 0, 0, 1, 1, 1, 0]$
    - “a bad movie” $\rightarrow [0, 0, 1, 0, 1, 0, 1]$

# Chuyển hóa văn bản thành vector

- Trong thực tế, thuật toán dựa trên việc có/không xuất hiện một từ chỉ là thuật toán đơn giản nhất
- Phiên bản “thống kê” hơn: **CountVectorizer**:

**Vocabulary**: (7 từ khác nhau)
`["this", "is", "a", "good", "movie", "actors", "bad"]`

"this is a good movie" $\rightarrow$ $[1, 1, 1, 1, 1, 0, 0]$
"**good movie, good actors**" $\rightarrow$ $[0, 0, 0, 2, 1, 1, 0]$
"a bad movie" $\rightarrow$ $[0, 0, 1, 0, 1, 0, 1]$

- Một số thuật toán trích chọn đặc trưng văn bản khác: **TF-IDF, BOW** (thảo luận để biết ý tưởng chính của những thuật toán này)

# **Thực hành với Google Colab**

- Thực hành với bộ dữ liệu giả lập để hiểu rõ thuật toán, cách vector hóa văn bản
- Thực hành với bộ dữ liệu thực tế IMDB movie review: 50.000 câu
  https://www.kaggle.com/lakshmi25npathi/sentiment-analysis-of-imdb-movie-reviews/data

| A review | A sentiment |
|---|---|
| Probably my all-time favorite movie, a story of selflessness, sacrifice and dedication to a noble ca... | positive |
| I sure would like to see a resurrection of a up dated Seahunt series with the tech they have today i... | positive |
| This show was an amazing, fresh & innovative idea in the 70's when it first aired. The first 7 or 8 ... | negative |

# Phương pháp dựa trên học sâu

- Phương pháp dựa trên học máy thống kê vẫn có độ chính xác tương đối cao, nhưng:
    - Không biểu diễn được từ đồng nghĩa
    - Không biểu diễn được thứ tự các từ
    - Không biểu diễn được ngữ cảnh (context) của cả câu
    - Độ dài vector luôn cố định, thường rất lớn và hầu hết là giá trị 0
-> Sử dụng mạng nơron để học ra cách biểu diễn cô đọng hơn của mỗi ký tự/từ/câu/đoạn trong văn bản

# Biểu diễn vector của một từ

- **Word Embeddings (Biểu diễn nén của từ)**
    - Các thuật toán **Word2Vec, GloVe, FastText** giúp chuyển đổi từ thành vector số, thể hiện ý nghĩa ngữ nghĩa.
- https://jalammar.github.io/illustrated-word2vec/

| Word | living being | feline | human | gender | royalty | verb | plural |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| cat | 0.6 | 0.9 | 0.1 | 0.4 | -0.7 | -0.3 | -0.2 |
| kitten | 0.5 | 0.8 | -0.1 | 0.2 | -0.6 | -0.5 | -0.1 |
| dog | 0.7 | -0.1 | 0.4 | 0.3 | -0.4 | -0.1 | -0.3 |
| houses | -0.8 | -0.4 | -0.5 | 0.1 | -0.9 | 0.3 | 0.8 |
| man | 0.6 | -0.2 | 0.8 | 0.9 | -0.1 | -0.9 | -0.7 |
| woman | 0.7 | 0.3 | 0.9 | -0.7 | 0.1 | -0.5 | -0.4 |
| king | 0.5 | -0.4 | 0.7 | 0.8 | 0.9 | -0.7 | -0.6 |
| queen | 0.8 | -0.1 | 0.8 | -0.9 | 0.8 | -0.5 | -0.9 |

**Dimensionality reduction of word embeddings from 7D to 2D**

- Word
- Word embedding
- Dimensionality reduction
- Visualization of word embeddings in 2D

**Danh sách từ trong biểu đồ heatmap:**
- queen
- woman
- girl
- boy
- man
- king
- queen
- water

# Thảo luận

❖ Đọc bài viết đầy đủ giải thích quá trình huấn luyện Word2Vec và trả lời các câu hỏi:
- Cơ chế tạo dữ liệu cho Skip-Gram như thế nào, ví dụ với 1 câu tiếng Việt
- Đây là phương pháp học máy gì, có phải Supervised hay Unsupervised?
- Trong phần đầu bài viết, tác giả đề cập đến "Neural Language Model" với nhiệm vụ dự đoán từ tiếp theo. Tuy nhiên, để tối ưu hiệu suất, Word2vec đã chuyển dịch sang một nhiệm vụ khác gọi là "Negative Sampling". Hãy giải thích nhiệm vụ mới này là gì? Tại sao việc này tăng tốc độ huấn luyện?
- Loss function trong mô hình này được tính như thế nào

## Mạng nơ-ron nhân tạo cho NLP

* Với đặc trưng dữ liệu dạng chuỗi (sequence), một số kiến trúc Neural network thường dùng cho NLP như:
  - **RNN** (Recurrent Neural Network) - Mạng nơ-ron hồi quy
  - **LSTM** (Long Short-Term Memory) - Mạng bộ nhớ dài ngắn
  - **Transformer** thay thế RNN bằng cơ chế **Self-Attention**, giúp xử lý văn bản song song, nhanh và hiệu quả hơn.
  - **BERT** (Bidirectional Encoder Representations from Transformers) hiểu ngữ cảnh tốt hơn bằng cách đọc văn bản theo cả hai chiều.

# A Simple RNN Language Model

$\hat{y}^{(4)} = P(x^{(5)} | \text{the students opened their})$

**output distribution**
$\hat{y}^{(t)} = \text{softmax} (Uh^{(t)} + b_2) \in \mathbb{R}^{|V|}$

**Core idea: Apply the same weights $W$ repeatedly**

**hidden states**
$h^{(t)} = \sigma (W_h h^{(t-1)} + W_e e^{(t)} + b_1)$
$h^{(0)}$ is the initial hidden state

**word embeddings**
$e^{(t)} = E x^{(t)}$

**words / one-hot vectors**
$x^{(t)} \in \mathbb{R}^{|V|}$

**Note: this input sequence could be much longer now!**

# Vấn đề "Biến mất đạo hàm" (Vanishing Gradient)

- Khi huấn luyện với các chuỗi dài (văn bản dài), tín hiệu lỗi (Gradient) phải truyền ngược lại qua rất nhiều bước thời gian
- Gradient được tính bằng phép nhân liên tiếp cùng trọng số $W_h$, nếu $W_h < 1$, sau rất nhiều bước thì $gradient \sim 0$
- Càng ở xa điểm cuối, các từ ở đầu câu càng ít có tác động đến việc cập nhật trọng số $\rightarrow$ Mạng không học được ngữ cảnh xa

"Tôi sinh ra ở **Việt Nam**, lớn lên trong một gia đình nghèo... [nhiều câu khác]... Tôi nói thành thạo tiếng **[?]**."

BAV HỌC VIỆN NGÂN HÀNG 1961 BANKING ACADEMY OF VIETNAM

# Cấu trúc LSTM (Long Short-Term Memory)

LSTM Memory Cell
Forget gate
Input gate
Output gate
$C_{t-1}$
$h_{t-1}$
$X_t$
$\sigma$
tanh
$C_t$
$h_t$

## Cơ chế:

**Cell State:** sổ tay chứa thông tin quan trọng được lưu giữ từ quá khứ

**Cơ chế "Cổng" (Gates):**

**Cổng Quên (Forget Gate):** "Cái này có còn quan trọng không? Không thì xóa!"

**Cổng Nhập (Input Gate):** "Thông tin mới này có hay không? Có thì ghi thêm vào sổ!"

**Cổng Xuất (Output Gate):** "Chắt lọc gì từ sổ tay để trả lời cho bước này?"

# Các giải pháp kỹ thuật khác (đọc thêm)

*   Hàm kích hoạt ReLU:
*   Gradient Clipping
*   Khởi tạo trọng số (Weight Initialization):

## Sự tiến hóa của Representation

*   **Hạn chế của Word2vec:**
    *   Static Embedding: Mỗi từ chỉ có một vector duy nhất.
    *   Vấn đề từ đồng âm: Từ "bank" trong "river bank" (bờ sông) và "bank account" (tài khoản ngân hàng) có vector giống hệt nhau trong Word2vec
*   **Bước ngoặt:** Chúng ta cần những vector "động", thay đổi theo ngữ cảnh xung quanh
*   **RNN/LSTM → Attention mechanism → Transformers architecture**

# 4.4. Mô hình ngôn ngữ lớn

## Mô hình nền tảng sau ChatGPT, Gemini là gì?

### Evolutionary Tree

*   **Legend:**
    *   Open-Source
    *   Closed-Source

*   **2023:**
    *   GLM (Google) - Open-Source
    *   Flan UL2 (Google) - Open-Source
    *   LLaMA (Meta) - Open-Source
    *   Bard (Google) - Closed-Source
    *   GPT-4 (OpenAI) - Closed-Source
    *   Jurassic-2 (AI21labs) - Closed-Source
    *   Claude (Anthropic) - Closed-Source

*   **20

# Mô hình ngôn ngữ lớn (LLM) là gì

- Mô hình ngôn ngữ lớn (Large Language Model - LLM) là mô hình AI được huấn luyện để hiểu và tạo văn bản giống con người.
    - Được huấn luyện trên **lượng dữ liệu khổng lồ** gồm sách, bài viết, hội thoại.
    - **Ví dụ:** GPT-3.5, GPT-4o, Gemini, Gemma, Llama, Claude, Qwen.
- Tưởng tượng: LLM như một học sinh đọc hàng triệu cuốn sách, học cách dự đoán những từ có thể sử dụng trong một ngữ cảnh
- **Sự bùng nổ về tham số:**
    - **BERT (2018):** ~110 triệu tham số (Hiểu ngữ cảnh hai chiều).
    - **GPT-3 (2020):** 175 tỷ tham số (Khả năng tạo văn bản như người).
    - **GPT-4 / Gemini:** Hàng nghìn tỷ tham số.

# LLM hoạt động như thế nào

*   **Học từ dữ liệu:** LLM đọc hàng tỷ từ để học cách con người viết và nói. (thử tìm hiểu xem GPT-3.5 đã học từ bao nhiêu dữ liệu văn bản?)
*   **Dự đoán từ tiếp theo:** Khi nhập một câu, mô hình đoán từ/câu tiếp theo dựa trên ngữ cảnh.
*   **Hiểu ngữ nghĩa sâu hơn:** Nhờ các thuật toán thông minh (Transformers, Attention), mô hình có thể nắm bắt ý nghĩa của câu.
*   **Ví dụ:**
    *   "Trí tuệ nhân tạo là..."
    *   🤖: "...công nghệ giúp máy tính suy nghĩ như con người."

# Hạn chế của LLM
- **Không phải lúc nào cũng đúng** – Đôi khi mô hình có thể tạo ra thông tin sai (**hallucination**).
- **Thiên vị dữ liệu** – LLM có thể bị ảnh hưởng bởi thông tin không chính xác trong dữ liệu huấn luyện.
- **Bảo mật & riêng tư** – Cần cẩn trọng khi chia sẻ thông tin cá nhân với AI.
- **Tốn tài nguyên** – Đào tạo LLM đòi hỏi **máy tính mạnh**, **dữ liệu lớn** và năng lượng cao.

# Tương lai của LLM

-   **LLM ngày càng thông minh hơn**, giúp cải thiện giao tiếp giữa con người và máy tính.
-   **Ứng dụng rộng rãi** trong giáo dục, y tế, sáng tạo nội dung, và nhiều lĩnh vực khác.
-   **Xu hướng:** LLM kết hợp với **trí tuệ nhân tạo đa phương thức (multimodal AI)** để hiểu cả hình ảnh, âm thanh, và video.

## Thảo luận:
*Tìm những mô hình Multimodal AI và ứng dụng của chúng?*

1961 BANKING ACADEMY OF VIETNAM

## Bài tập thực hành

* Xây dựng model phân loại review comment tiếng Việt với bộ dữ liệu Vietnamese_comments.csv theo 2 phương pháp: học máy thống kê và deep learning
* Nộp 2 notebook tương ứng
* Chỉ ra sự khác biệt với bài tập IMDB_reviews ở buổi trước
