# Bài 5: Kết nối cơ sở dữ liệu JDBC

## Nội dung chính
- Khái niệm JDBC và vai trò trong kết nối cơ sở dữ liệu.
- Kiến trúc JDBC và Driver Manager.
- Các loại JDBC driver.
- Các bước truy cập cơ sở dữ liệu từ Java.
- Nạp trình điều khiển, thiết lập kết nối và tạo `Statement`.
- Thực thi câu lệnh SQL và xử lý kết quả.

## Tổng quan
JDBC là API của Java dùng để kết nối và làm việc với cơ sở dữ liệu. Thông qua JDBC, chương trình Java có thể gửi câu lệnh SQL đến hệ quản trị cơ sở dữ liệu, nhận kết quả truy vấn và xử lý dữ liệu trả về.

## Cơ sở dữ liệu và JDBC driver

Các hệ quản trị cơ sở dữ liệu thường gặp gồm:

- SQL Server.
- MySQL.
- Oracle.
- Microsoft Access.
- FoxPro.

Mỗi hệ quản trị cơ sở dữ liệu cần có trình điều khiển JDBC tương ứng. Driver chuyển đổi lời gọi JDBC trong Java thành lệnh mà hệ quản trị cơ sở dữ liệu có thể hiểu.

## Kiến trúc JDBC

JDBC gồm hai lớp chính:

1. JDBC API chuyển câu lệnh SQL từ chương trình Java đến JDBC Driver Manager.
2. JDBC Driver API liên hệ với driver cụ thể của từng hệ quản trị cơ sở dữ liệu.

Quy trình cơ bản:

1. Mở kết nối.
2. Thực thi câu lệnh SQL.
3. Xử lý kết quả.
4. Đóng kết nối.

## Các loại JDBC driver

| Loại driver | Đặc điểm |
|---|---|
| JDBC-ODBC Bridge | Kết nối qua cầu nối ODBC |
| Native-API Driver | Chuyển lời gọi JDBC sang API riêng của hệ quản trị cơ sở dữ liệu |
| JDBC-Net, Pure Java | Chuyển lời gọi JDBC sang dạng trung gian, middleware tiếp tục chuyển đến hệ quản trị cụ thể |
| Native-Protocol, Pure Java | Chuyển lời gọi JDBC trực tiếp sang giao thức riêng của hệ quản trị cơ sở dữ liệu |

### JDBC-ODBC Bridge
JDBC-ODBC Bridge cho phép Java truy cập cơ sở dữ liệu thông qua ODBC. Driver thường được nhắc đến trong slide là:

```java
sun.jdbc.odbc.JdbcOdbcDriver
```

Khi dùng Windows, có thể tạo ODBC Data Source bằng công cụ quản trị ODBC, đặt tên nguồn dữ liệu và chọn đường dẫn đến file cơ sở dữ liệu.

### Native-API Driver
Native-API Driver chuyển lời gọi JDBC sang API hoặc thư viện hàm riêng của từng hệ quản trị cơ sở dữ liệu. Driver này thường do nhà cung cấp hệ quản trị cơ sở dữ liệu cung cấp.

### JDBC-Net, Pure Java
Loại driver này có thể dùng cùng một driver để truy cập nhiều hệ quản trị cơ sở dữ liệu. Driver chuyển lời gọi JDBC sang dạng chuẩn, sau đó middleware chuyển tiếp sang lời gọi tương ứng với hệ quản trị cụ thể.

### Native-Protocol, Pure Java
Loại driver này chuyển lời gọi JDBC trực tiếp sang mã lệnh theo giao thức riêng của hệ quản trị cơ sở dữ liệu. Driver được viết bằng Java thuần và không cần mã native riêng tại thời điểm chạy.

## Các bước truy cập cơ sở dữ liệu

1. Nạp driver.
2. Thiết lập kết nối.
3. Tạo đối tượng `Statement`.
4. Thực thi truy vấn hoặc lệnh cập nhật.
5. Xử lý kết quả.
6. Đóng kết nối.

## Nạp trình điều khiển

Driver được nạp bằng `Class.forName()`.

```java
try {
    Class.forName("Database driver name");
} catch (ClassNotFoundException e) {
    System.out.println("Driver not found: " + e.getMessage());
}
```

Một số tên driver trong slide:

```java
Class.forName("org.gjf.mm.mysql.Driver");
Class.forName("oracle.jdbc.driver.OracleDriver");
Class.forName("com.sybase.jdbc.SybDriver");
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
```

## Thiết lập kết nối

Kết nối được tạo bằng phương thức tĩnh `getConnection()` của lớp `DriverManager`. Phương thức này trả về một đối tượng `Connection`.

```java
String username = "sa";
String password = "secret";
Connection con = DriverManager.getConnection(dbUrl, username, password);
```

Trong đó:

- `dbUrl` là chuỗi kết nối đến cơ sở dữ liệu.
- `username` là tên người dùng.
- `password` là mật khẩu đăng nhập.

### Ví dụ chuỗi kết nối

```java
String host = "dbhost.yourcompany.com";
String dbName = "someName";
int port = 1234;

String oracleURL = "jdbc:oracle:thin:@" + host + ":" + port + ":" + dbName;
String sybaseURL = "jdbc:sybase:Tds:" + host + ":" + port + ":" + "?SERVICEid=" + dbName;
```

### Ví dụ kết nối qua JDBC-ODBC

```java
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
Connection conn = DriverManager.getConnection("jdbc:odbc:<DataSourceName>");
```

`DataSourceName` là tên ODBC Data Source được tạo trên Microsoft Windows.

## Tạo đối tượng Statement

Đối tượng `Statement` dùng để gửi câu lệnh SQL đến cơ sở dữ liệu.

```java
Statement s = con.createStatement();
```

Một đối tượng `Statement` có thể dùng cho nhiều câu lệnh SQL khác nhau.

Các phương thức thực thi thường dùng:

| Phương thức | Mục đích |
|---|---|
| `executeQuery()` | Thực hiện truy vấn và trả về kết quả |
| `executeUpdate()` | Thực hiện lệnh cập nhật dữ liệu |
| `execute()` | Thực hiện câu lệnh SQL tổng quát |

## Ví dụ tạo Statement và vấn tin

**Ví dụ:** Slide đưa ví dụ nạp driver, tạo kết nối, tạo `Statement` và thực hiện câu lệnh `SELECT`.

```java
import java.sql.*;

public class TestDatabase {
    public static void main(String[] arguments) {
        String data = "jdbc:odbc:Driver={Microsoft Access Driver (*.mdb)};DBQ="
                + "D:/JAVA/LamBTJava/AddressBook.mdb";

        try {
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");

            Connection conn = DriverManager.getConnection(
                    data, "Vo Tan Dung", "abc");

            Statement st = conn.createStatement();
            ResultSet rec = st.executeQuery("SELECT * FROM AddressBook");
        }
    }
}
```

**Giải thích:** Trích đoạn trên nạp driver JDBC-ODBC, tạo kết nối đến cơ sở dữ liệu Access, tạo `Statement` và thực hiện câu lệnh `SELECT` để nhận kết quả trong `ResultSet`.

## Đóng kết nối

Sau khi làm việc với cơ sở dữ liệu, cần đóng các đối tượng đã sử dụng:

```java
rec.close();
st.close();
conn.close();
```

Việc đóng kết nối giúp giải phóng tài nguyên và tránh giữ kết nối không cần thiết.

## Tóm tắt bài
- JDBC cho phép chương trình Java làm việc với cơ sở dữ liệu.
- Driver là thành phần trung gian giữa JDBC API và hệ quản trị cơ sở dữ liệu.
- Quy trình JDBC cơ bản gồm nạp driver, kết nối, tạo `Statement`, thực thi SQL, xử lý kết quả và đóng kết nối.
- `Connection`, `Statement` và `ResultSet` là các đối tượng quan trọng khi làm việc với JDBC.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| JDBC | API của Java dùng để kết nối và thao tác với cơ sở dữ liệu |
| Driver | Trình điều khiển giúp Java giao tiếp với hệ quản trị cơ sở dữ liệu |
| Driver Manager | Thành phần quản lý các driver JDBC |
| `Connection` | Đối tượng biểu diễn kết nối đến cơ sở dữ liệu |
| `Statement` | Đối tượng gửi câu lệnh SQL |
| `ResultSet` | Đối tượng chứa kết quả truy vấn |
| `executeQuery()` | Thực hiện truy vấn trả về dữ liệu |
| `executeUpdate()` | Thực hiện lệnh cập nhật dữ liệu |
| JDBC-ODBC Bridge | Kiểu driver kết nối Java với cơ sở dữ liệu thông qua ODBC |

## Câu hỏi ôn tập
1. JDBC dùng để làm gì trong chương trình Java?
2. Vì sao cần JDBC driver khi kết nối cơ sở dữ liệu?
3. Trình bày các bước truy cập cơ sở dữ liệu bằng JDBC.
4. `Connection`, `Statement` và `ResultSet` có vai trò gì?
5. Phân biệt `executeQuery()` và `executeUpdate()`.
6. JDBC-ODBC Bridge hoạt động như thế nào?
7. Vì sao cần đóng kết nối sau khi xử lý dữ liệu?
