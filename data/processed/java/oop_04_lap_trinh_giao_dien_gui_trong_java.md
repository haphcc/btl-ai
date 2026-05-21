# Bài 4: Lập trình giao diện GUI trong Java

## Nội dung chính
- Khái niệm lập trình giao diện đồ họa GUI.
- Hai thư viện giao diện trong Java: AWT và Swing.
- Thành phần giao diện (component).
- Vùng chứa (container).
- Bộ quản lý bố cục (layout manager).
- Nguyên tắc xây dựng giao diện và xử lý sự kiện.

## Tổng quan
GUI (Graphic User Interface) là giao diện đồ họa cho phép người dùng tương tác với chương trình thông qua cửa sổ, nút bấm, ô nhập liệu, danh sách và các thành phần trực quan khác. Java hỗ trợ lập trình GUI thông qua AWT và Swing.

## Thư viện GUI trong Java

### AWT
AWT (Abstract Windowing Toolkit) là tập hợp các lớp Java dùng để tạo giao diện đồ họa.

```java
import java.awt.*;
import java.awt.event.*;
```

AWT cung cấp các thành phần giao diện, vùng chứa và cơ chế xử lý sự kiện cơ bản.

### Swing
Swing nằm trong gói `javax.swing.*`. Swing cung cấp nhiều thành phần giao diện phong phú hơn AWT và thường được dùng để xây dựng ứng dụng desktop có giao diện đầy đủ.

```java
import javax.swing.*;
```

## Nguyên tắc xây dựng GUI

Khi xây dựng giao diện Java, có thể thực hiện theo các bước:

1. Chọn vùng chứa như `Frame`, `Window`, `Dialog`, `Applet`.
2. Tạo các điều khiển như nút bấm, vùng nhập văn bản, danh sách, hộp chọn.
3. Đưa các điều khiển vào vùng chứa.
4. Sắp xếp các điều khiển bằng layout.
5. Gắn xử lý sự kiện bằng các listener.

## Component

Component là các thành phần tạo nên giao diện. Ví dụ:

- `Frame`, `Window`, `Dialog`, `Applet`.
- `TextField`, `Label`, `Checkbox`, `TextArea`.
- `Button`, `Choice`, `List`, `Scrollbar`.

## Một số component thường dùng

### Label
`Label` dùng để hiển thị một chuỗi văn bản trên giao diện.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `Label()` | Tạo nhãn rỗng |
| `Label(String s)` | Tạo nhãn có nội dung |
| `Label(String s, int align)` | Tạo nhãn có nội dung và căn chỉnh |
| `setText(String s)` | Thay đổi nội dung nhãn |
| `setAlignment(int align)` | Thay đổi cách căn chỉnh |

### Button
`Button` là nút bấm cho phép người dùng thực hiện một hành động.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `Button()` | Tạo nút rỗng |
| `Button(String s)` | Tạo nút có nhãn |
| `setLabel(String s)` | Đặt nhãn cho nút |
| `getLabel()` | Lấy nhãn của nút |

Để xử lý sự kiện nút bấm, lớp thường cài đặt `ActionListener`.

### TextField
`TextField` là ô nhập liệu một dòng.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `TextField()` | Tạo ô nhập rỗng |
| `setEditable(boolean b)` | Cho phép hoặc không cho phép sửa nội dung |
| `setEchoChar(char c)` | Đặt ký tự hiển thị thay thế, thường dùng cho mật khẩu |

Các sự kiện thường dùng với `TextField` gồm `ActionListener` và `TextListener`.

### Choice
`Choice` cho phép chọn một mục trong danh sách lựa chọn.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `Choice()` | Tạo hộp lựa chọn |
| `addItem(String s)` | Thêm một mục |
| `getItem(int index)` | Lấy mục theo vị trí |
| `getSelectedItem()` | Lấy mục đang được chọn |
| `getSelectedIndex()` | Lấy chỉ số của mục đang chọn |

Sự kiện lựa chọn thường được xử lý bằng `ItemListener`.

### Checkbox
`Checkbox` biểu diễn một lựa chọn có thể bật hoặc tắt.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `Checkbox()` | Tạo ô chọn |
| `setLabel(String s)` | Đặt nhãn |
| `getState()` | Lấy trạng thái được chọn hay không |

Sự kiện của `Checkbox` thường dùng `ItemListener` và phương thức xử lý `itemStateChanged()`.

### List
`List` cho phép chọn một hoặc nhiều mục.

| Hàm/Phương thức | Ý nghĩa |
|---|---|
| `List()` | Tạo danh sách |
| `List(int items, boolean ms)` | Tạo danh sách với số dòng hiển thị và chế độ chọn nhiều |
| `getSelectedItem()` | Lấy mục được chọn |

`List` có thể dùng `ItemListener` hoặc `ActionListener` để xử lý sự kiện.

### Các component khác
Ngoài các component trên, AWT còn có:

- `TextArea`.
- `Menu`.
- `ScrollBar`.
- `Canvas`.
- `Applet`.

## Container

Container là vùng chứa có thể chứa các component khác. Container có thể vẽ, đặt màu nền và tổ chức các thành phần bên trong.

Một số container:

- `Frame`.
- `Applet`.
- `Panel`.
- `ScrollPane`.
- `Dialog`.
- `FileDialog`.

## Hệ tọa độ giao diện

Giao diện đồ họa sử dụng hệ tọa độ để xác định vị trí và kích thước thành phần. Các thông tin thường dùng gồm:

- Tọa độ `x`.
- Tọa độ `y`.
- Chiều rộng.
- Chiều cao.

## Frame

`Frame` là cửa sổ thường dùng cho ứng dụng Java độc lập.

Đặc điểm của `Frame`:

- Có thanh tiêu đề và đường viền.
- Bố cục mặc định là `BorderLayout`.
- Kế thừa từ `Window`.
- Có thể xử lý sự kiện cửa sổ bằng `WindowListener`.
- Ứng dụng độc lập thường tạo lớp kế thừa từ `Frame`.

## Layout Manager

Layout Manager dùng để sắp xếp các component trong container. Khi giao diện thay đổi kích thước, layout giúp các thành phần được bố trí lại theo quy tắc nhất định.

Nội dung slide nhấn mạnh rằng sau khi tạo component và đưa vào container, cần sắp xếp chúng bằng layout trước khi gắn xử lý sự kiện.

## Xử lý sự kiện

GUI cần phản hồi hành động của người dùng. Java sử dụng các listener để lắng nghe sự kiện:

- `ActionListener` cho hành động như bấm nút.
- `ItemListener` cho lựa chọn trong `Choice`, `Checkbox`, `List`.
- `TextListener` cho thay đổi văn bản.
- `WindowListener` cho sự kiện cửa sổ.

## Tóm tắt bài
- Java hỗ trợ lập trình GUI qua AWT và Swing.
- GUI được xây dựng từ component, container, layout và listener.
- Component là các điều khiển như `Button`, `Label`, `TextField`, `Choice`, `Checkbox`.
- Container như `Frame` hoặc `Panel` dùng để chứa component.
- Listener giúp chương trình phản ứng với thao tác của người dùng.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| GUI | Giao diện đồ họa người dùng |
| AWT | Bộ công cụ giao diện cơ bản của Java |
| Swing | Thư viện giao diện phong phú hơn AWT |
| Component | Thành phần giao diện |
| Container | Vùng chứa các component |
| Layout Manager | Bộ quản lý cách sắp xếp component |
| Listener | Đối tượng lắng nghe và xử lý sự kiện |
| `Frame` | Cửa sổ ứng dụng độc lập |
| `Button` | Nút bấm trên giao diện |
| `TextField` | Ô nhập văn bản một dòng |

## Câu hỏi ôn tập
1. GUI là gì và có vai trò gì trong ứng dụng Java?
2. AWT và Swing được dùng để làm gì?
3. Component và container khác nhau như thế nào?
4. Trình bày các bước cơ bản để xây dựng giao diện Java.
5. `Label`, `Button`, `TextField` dùng trong trường hợp nào?
6. `Frame` có đặc điểm gì?
7. Listener có vai trò gì trong xử lý sự kiện GUI?
