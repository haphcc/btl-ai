# CHƯƠNG 3
# GIỚI THIỆU HỆ QUẢN TRỊ CƠ SỞ DỮ LIỆU MS SQL SERVER

# NỘI DUNG CHÍNH

1 Các phiên bản MS SQL Server
2 Cài đặt SQL Server và Quản lý cơ sở dữ liệu
3. Các kiểu dữ liệu trong SQL
4. Làm việc với bảng dữ liệu
5. Import, Export cơ sở dữ liệu

# 1. Các phiên bản MS SQL Server

- Phiên bản đầu tiên của MS SQL Server ra đời vào năm 1989 cho các hệ điều hành chạy 16 bit với SQL Server version 1.0
- Được thị trường chấp nhận rộng rãi kể từ version 6.5 (phát hành năm 1996)
- Các phiên bản sau đó:

- SQL Server 7.0
- SQL Server 2000
- SQL Server 2005
- SQL Server 2008
- SQL Server 2008 R2
- SQL Server 2012
- SQL Server 2014
- SQL Server 2016 (hỗ trợ vi xử lý 64 bít)
- SQL Server 2017
- SQL Server 2019
- SQL Server 2022 (phát hành 11/2022)

Tùy từng phiên bản, SQL Server có các ấn bản sau:

- **Enterprise** - bản cao cấp nhất với đầy đủ tính năng.
- **Standard** - ít tính năng hơn Enterprise, sử dụng khi không cần dùng tới các tính năng nâng cao.
- **Workgroup** - phù hợp cho các công ty lớn với nhiều văn phòng làm việc từ xa.
- **Web** - thiết kế riêng cho các ứng dụng web.
- **Developer** - tương tự như Enterprise nhưng chỉ cấp quyền cho một người dùng duy nhất để phát triển, thử nghiệm, demo. Có thể dễ dàng nâng cấp lên bản Enterprise mà không cần cài lại.
- **Express** - bản này chỉ dùng ở mức độ đơn giản, tối đa 1 CPU và bộ nhớ 1GB, kích thước tối đa của cơ sở dữ liệu là 10GB.

- **Compact** - nhúng miễn phí vào các môi trường phát triển ứng dụng web. Kích thước tối đa của cơ sở dữ liệu là 4GB.
- **Datacenter** - thay đổi lớn trên SQL Server 2008 R2 chính là bản Datacenter Edition. Không giới hạn bộ nhớ và hỗ trợ hơn 25 bản cài.
- **Business Intelligence** - được giới thiệu trên SQL Server 2012. Phiên bản này có các tính năng của bản Standard và hỗ trợ một số tính năng nâng cao về BI như Power View và PowerPivot nhưng không hỗ trợ những tính năng nâng cao về mức độ sẵn sàng như AlwaysOn Availability Groups...
- **Enterprise Evaluation** - SQL Server Evaluation Edition là lựa chọn tuyệt vời để dùng được mọi tính năng và được miễn phí của SQL Server để học tập và phát triển. Phiên bản này có thời gian hết hạn là 6 tháng từ ngày cài.

| | 2005 | 2008 | 2008 R2 | 2012 | 2014 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Enterprise | | Yes | Yes | Yes | Yes |
| Standard | | Yes | Yes | Yes | Yes |
| Developer | | Yes | Yes | Yes | Yes |
| Workgroup | | Yes | Yes | No | No |
| Win Compact Edition - Mobile | | Yes | Yes | Yes | Yes |
| Enterprise Evaluation | | Yes | Yes | Yes | Yes |
| Express | | Yes | Yes | Yes | Yes |
| Web | | Yes | Yes | Yes | |
| Datacenter | | No | No | | |
| Business Intelligence | | Yes | | | |

# 2. Cài đặt MS SQL Server và quản lý CSDL

- **Cài đặt SQL Server Express từ phiên bản 2012 trở về đây**
- **Cửa sổ đăng nhập:**

| Connect to Server | |
| :--- | :--- |
| **Server type:** | Database Engine |
| **Server name:** | TRANGNTT\SQLEXPRESS |
| **Authentication:** | Windows Authentication |
| **User name:** | |
| **Password:** | |
| | ☐ Remember password |
| | [ Connect ] [ Cancel ] [ Help ] [ Options >> ] |

- Sau khi cài đặt xong SQL Server, người sử dụng được cung cấp một số công cụ:
- **SQL Server configuration manager** là công cụ quản lý cài đặt và cấu hình liên quan đến các dịch vụ Microsoft SQL Server:
    - **Quản lý dịch vụ SQL Server**: kiểm tra trạng thái của các dịch vụ SQL Server (như SQL Server Database Engine, SQL Server Agent, SQL Server Reporting Services, và nhiều dịch vụ khác), khởi động, tắt, khởi động lại, hoặc thay đổi tài khoản dịch vụ.
    - **Cấu hình mạng**: cho phép cấu hình cách các dịch vụ SQL Server lắng nghe kết nối từ mạng, có thể chỉ định các cổng, giao thức (ví dụ, TCP/IP hoặc Named Pipes), và giao diện mạng để một SQL Server cụ thể sử dụng.

- **Xác thực**: Cấu hình xác thực Windows hoặc xác thực SQL Server (mixed mode) cho SQL Server, cũng như quyết định nếu SQL Server nên sử dụng chế độ kiểm tra xác thực.

- **Cấu hình hiệu suất**: Cung cấp quyền truy cập đến các tùy chọn cấu hình hiệu suất của SQL Server, cho phép điều chỉnh các thông số như bộ đệm, CPU, bộ nhớ, và cách SQL Server sử dụng tài nguyên hệ thống.

- **Quản lý thẻ hệ thống và khung thời gian**: Có thể xác định các thẻ hệ thống cho các dịch vụ SQL Server và cấu hình các khung thời gian cho chúng, giúp quản lý tài nguyên hệ thống và đảm bảo rằng SQL Server hoạt động một cách hiệu quả.

- **SQL Server management studio (SSMS)** là một công cụ quan trọng và mạnh mẽ được phát triển bởi Microsoft để quản lý và tương tác với các cơ sở dữ liệu SQL Server:

- **Quản lý cơ sở dữ liệu**: Cho phép tạo, xóa, sao lưu, phục hồi, và thay đổi cơ sở dữ liệu SQL Server. Bạn cũng có thể cấu hình tùy chọn và thiết lập cho cơ sở dữ liệu.
- **Thực hiện truy vấn**: Viết và thực thi các truy vấn SQL, lập trình SQL, và xem kết quả truy vấn. SSMS cung cấp môi trường tương tác để làm việc với dữ liệu trong cơ sở dữ liệu.
- **Quản lý bảo mật**: Quản lý người dùng, vai trò, quyền truy cập, và chính sách bảo mật trong SQL Server bằng cách sử dụng SSMS.

- **Quản lý dịch vụ SQL Server**: Cho phép kiểm tra trạng thái của các dịch vụ SQL Server, khởi động, tắt, và khởi động lại chúng.
- **Quản lý báo cáo và tích hợp dữ liệu**: Cung cấp các công cụ để tạo và quản lý báo cáo, lên lịch cho chúng, tích hợp dữ liệu từ nhiều nguồn khác nhau vào SQL Server.
- **Xem và quản lý lịch làm việc (SQL Server Agent)**: Là một dịch vụ quản lý và lên lịch nhiệm vụ tự động trong SQL Server.
- **Quản lý dự án và tệp script**: Cho phép lưu trữ các truy vấn SQL, biểu đồ CSDL, và tệp script khác trong các dự án và quản lý chúng.
- **Tối ưu hóa cơ sở dữ liệu**: Bạn có thể sử dụng SSMS để tối ưu hóa CSDL, xem và phân tích kế hoạch thực thi truy vấn, và giám sát hoạt động CSDL để cải thiện hiệu suất.

- Trong SQL Server có 3 loại tập tin, một cơ sở dữ liệu được lưu trữ theo hai hay nhiều tập tin (tối thiểu là 2 tập tin .mdf và .ldf):

- **Primary data file (.mdf ):** **bắt buộc** có dùng để lưu trữ thông tin liên quan đến cấu trúc và đặc điểm của chính database đó.
- **Secondary data file (.ndf):** dùng để lưu trữ các đối tượng dữ liệu không nằm trong tập tin dữ liệu chính. Loại tập tin này **không bắt buộc** phải có khi tạo mới CSDL.
- **Transaction log file (.ldf):** dùng để lưu vết các giao tác, là những hành động dung cập nhật dữ liệu (thêm, sửa, xóa) vào các bảng do người tác động trên CSDL

Mỗi tập tin trong CSDL (.MDF, .NDF, .LDF) đều có 5 thuộc tính:

- **NAME**: Tên logic của tập tin
- **FILENAME**: Đường dẫn đầy đủ
- **SIZE**: Kích thước ban đầu của tập tin (KB, MB, GB, TB)
- **MAXSIZE**: Kích thước tối đa cho phép của tập tin (KB, MB, GB, TB)
- **FILEGROWTH**: Tốc độ gia tăng kích thước của tập tin (KB, MB, GB, TB).

## Tạo mới cơ sở dữ liệu

**Object Explorer**
- Connect
    - TRANGNTT\SQLEXPRESS (SQL Server 11.0)
        - Databases
            - New Database...
            - Attach...
            - Restore Database...
            - Restore Files and Filegroups...
            - Deploy Data-tier Application...
            - Import Data-tier Application...
            - Start PowerShell
            - Reports
            - Refresh
        - Security
        - Server
        - Replication
        - Management

**New Database**

**Select a page**
- General
- Options
- Filegroups

**Database name:**
**Owner:** <default>
[ ] Use full-text indexing

**Database files:**

| Logical Na... | File Type | Filegroup | Initial Size (M... | Autogrowth / Maxsize | Path |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Rows ... | PRIMARY | 3 | By 1 MB, Unlimited | C:\Program Files\Microsoft SQL |
| _log | Log | Not Applicable | 1 | By 10 percent, Unlimited | C:\Program Files\Microsoft SQL |

**Connection**
Server: TRANGNTT\SQLEXPRESS
Connection: TRANGNTT\admin
[View connection]

**Progress**
[Ready]

[Add] [Remove]
[OK] [Cancel]

## Sửa cơ sở dữ liệu

### Object Explorer
- Connect
- **TRANGNTT\SQLEXPRESS (SQL Server 11.0)**
    - Databases
        - System Databases
        - Bank
        - BikeStore
        - **QL_SinhVien**
            - New Database...
            - New Query
            - Script Database as
            - Tasks
            - Policies
            - Facets
            - Start PowerShell
            - Reports
            - Rename
            - Delete
            - Refresh
            - **Properties**
    - QLy_
    - Quar
    - Repo
    - Repo
    - Security
    - Server
    - Replica
    - Manag

### Database Properties - QL_SinhVien

| Select a page | |
| :--- | :--- |
| General | **Backup** |
| Files | Last Database Backup | None |
| Filegroups | Last Database Log Backup | None |
| Options | **Database** |
| Change Tracking | Name | QL_SinhVien |
| Permissions | Status | Normal, Autoclosed |
| Extended Properties | Owner | TRANGNTT\admin |
| | Date Created | 21/09/2021 10:22:28 SA |
| | Size | 10.00 MB |
| | Space Available | 2.76 MB |
| | Number of Users | 4 |
| **Connection** | **Maintenance** |
| Server: TRANGNTT\SQLEXPRESS | Collation | SQL_Latin1_General_CP1_CI_AS |
| Connection: TRANGNTT\admin | |
| View connection | |
| **Progress** | **Name** |
| Ready | The name of the database. |

- Script
- Help
- OK
- Cancel

## Xóa cơ sở dữ liệu

| Object Explorer | Delete Object |
| :--- | :--- |
| Connect | **Select a page** |
| TRANGNTT\SQLEXPRESS (SQL Server 11.0) | General |
| Databases | **Obiect to be deleted** |
| System Databases | Object Name | Object Type | O... | Status | Message |
| Bank | QL_SinhVien | Database | T... | | |
| BikeStore | | | | | |
| QL_... | | | | | |
| Qly | **Connection** | | | | |
| Qua | Server: TRANGNTT\SQLEXPRESS | | | | |
| Rep | Connection: TRANGNTT\admin | | | | |
| Rep | View connection | | | | |
| Securit | | | | | |
| Server | **Progress** | | | | |
| Replica | Ready | | | | |
| Manag | | [x] Delete backup and restore history information for databases |
| | | [ ] Close existing connections |
| | | **OK** **Cancel** |

- New Database...
- New Query
- Script Database as
- Tasks
- Policies
- Facets
- Start PowerShell
- Reports
- Rename
- **Delete**
- Refresh
- Properties

## **Tạo file dữ liệu (Tạo script SQL):**

- Sử dụng SSMS hoặc các công cụ tương tự, tạo một script SQL cho cơ sở dữ liệu hiện tại. Điều này bao gồm cấu trúc cơ sở dữ liệu, bảng, chỉ mục, quyền truy cập, và dữ liệu.
- Chia sẻ script SQL này với người khác.
- Người khác có thể chạy script SQL trên SQL Server của họ để tạo một bản sao chính xác của cơ sở dữ liệu.

## Object Explorer
- Connect
- TRANGNTT\SQLEXPRESS (SQL Server 11.0.
    - Databases
        - System Databases
        - Bank
        - BikeStore
        - QU
            - New Database...
            - New Query
            - Script Database as
            - **Tasks**
                - Detach...
                - Take Offline
                - Bring Online
                - Shrink
                - Back Up...
                - Restore
                - **Generate Scripts...**
                - Extract Data-tier Application...
                - Deploy Database to SQL Azure...
                - Export Data-tier Application...
                - Register as Data-tier Application...
                - Upgrade Data-tier Application...
                - Delete Data-tier Application...
                - Import Data...
                - Export Data...
            - Policies
            - Facets
            - Start PowerShell
            - Reports
            - Rename
            - Delete
            - Refresh
            - Properties
        - QU
        - QU
        - Re
        - Re
    - Security
    - Server Objects
    - Replication
    - Management

## Generate and Publish Scripts
**Introduction**

- Introduction
- Choose Objects
- Set Scripting Options
- Summary
- Save or Publish Scripts

**Generate scripts for database objects.**

This wizard generates a script of selected database objects. The scripts can be saved for later use in creating databases in an instance of the Database Engine, or to publish a database to a Database Publishing Web Service.

There are four steps to complete this wizard:
1. Select database objects.
2. Specify scripting or publishing options.
3. Review your selections.
4. Generate scripts, then save or publish them.

To begin the script generation process, click Next.

[ ] Do not show this page again.

< Previous | Next > | Finish | Cancel

---

### Generate and Publish Scripts

**Choose Objects**

- Introduction
- **Choose Objects**
- Set Scripting Options
- Summary
- Save or Publish Scripts

**Select the database objects to script.**

- (•) Script entire database and all database objects
- ( ) Select specific database objects
    - [+] Tables
    - [+] Stored Procedures

[Select All] [Deselect All]

[< Previous] [Next >] [Finish] [Cancel]

---

### Generate and Publish Scripts

**Set Scripting Options**

- Introduction
- Choose Objects
- **Set Scripting Options**
- Summary
- Save or Publish Scripts

**Specify how scripts should be saved or published.**

**Output Type**
- (•) Save scripts to a specific location
- ( ) Publish to Web service

- (•) Save to file
    - Files to generate:
        - (•) Single file
        - ( ) Single file per object
    - File name: C:\Users\admin\Documents\script.sql [...]
    - [x] Overwrite existing file
    - Save as:
        - (•) Unicode text
        - ( ) ANSI text
- ( ) Save to Clipboard
- ( ) Save to new query window

[Advanced]

[< Previous] [Next >] [Finish] [Cancel]

Quan tâm đến các thông tin sau:

## Advanced Scripting Options (Hình trái)

| Option | Value |
| :--- | :--- |
| Continue scripting on Error | False |
| Convert UDDTs to Base Types | False |
| Check for object existence | False |
| Generate Script for Dependent Objects | True |
| Include Descriptive Headers | True |
| Include system constraint names | False |
| Include unsupported statements | False |
| Script Bindings | False |
| Script Collation | False |
| Script Defaults | True |
| Script DROP and CREATE | Script CREATE |
| Script Extended Properties | True |
| **Script for Server Version** | **SQL Server 2012** |

- **Script for Server Version**: SQL Server 2012
- Script only features compatible with the specified version of SQL Server.

## Advanced Scripting Options (Hình phải)

| Option | Value |
| :--- | :--- |
| Script for Server Version | SQL Server 2012 |
| Script for the database engine type | Stand-alone instance |
| Script Logins | False |
| Script Object-Level Permissions | False |
| Script Owner | False |
| Script Statistics | Do not script statistics |
| Script USE DATABASE | True |
| Schema qualify object names | True |
| **Types of data to script** | **Schema only** |
| Table/View Options | |
| Script Change Tracking | Schema and data |
| Script Check Constraints | Schema only |
| Script Data Compression Options | False |
| Script Foreign Keys | True |
| Script Full-Text Indexes | False |
| Script Indexes | True |

- **Types of data to script**: Schema only
- Generates script that contains schema only or schema and data.

## **Biên dịch file script đã có:**

- Mở file dữ liệu đã tạo (script) trên SQL Server Management Studio
- Chỉnh sửa (nếu cần)
- Chạy chương trình bằng nút **Execute** hoặc ấn **F5**

## Tạo file dữ liệu (Sao lưu và phục hồi):

- Sử dụng SQL Server Management Studio (SSMS) hoặc các công cụ tương tự, sao lưu cơ sở dữ liệu hiện tại bằng cách chọn "Tasks" > "Backup" và tạo một tệp sao lưu (backup file). Chọn tùy chọn sao lưu toàn bộ cơ sở dữ liệu.
- Chuyển tệp sao lưu đến người khác.
- Người khác có thể phục hồi cơ sở dữ liệu từ tệp sao lưu bằng cách sử dụng SSMS hoặc lệnh RESTORE DATABASE với tên cơ sở dữ liệu mới.

# 3. Các kiểu dữ liệu trong SQL (kiểu kí tự)

| Data type | Description | Max size | Storage |
| :--- | :--- | :--- | :--- |
| char(n) | Fixed width character string | 8,000 characters | Defined width |
| varchar(n) | Variable width character string | 8,000 characters | 2 bytes + number of chars |
| varchar(max) | Variable width character string | 1,073,741,824 characters | 2 bytes + number of chars |
| text | Variable width character string | 2GB of text data | 4 bytes + number of chars |
| nchar | Fixed width Unicode string | 4,000 characters | Defined width x 2 |
| nvarchar | Variable width Unicode string | 4,000 characters | |
| nvarchar(max) | Variable width Unicode string | 536,870,912 characters | |
| ntext | Variable width Unicode string | 2GB of text data | |
| binary(n) | Fixed width binary string | 8,000 bytes | |
| varbinary | Variable width binary string | 8,000 bytes | |
| varbinary(max) | Variable width binary string | 2GB | |

# 3. Các kiểu dữ liệu trong SQL (kiểu số)

| Data type | Description | Storage |
| :--- | :--- | :--- |
| bit | Integer that can be 0, 1, or NULL | |
| tinyint | Allows whole numbers from 0 to 255 | 1 byte |
| smallint | Allows whole numbers between -32,768 and 32,767 | 2 bytes |
| int | Allows whole numbers between -2,147,483,648 and 2,147,483,647 | 4 bytes |
| bigint | Allows whole numbers between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807 | 8 bytes |
| decimal(p,s) | Fixed precision and scale numbers. Allows numbers from $-10^{38} +1$ to $10^{38} -1$. The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0 | 5-17 bytes |

# 3. Các kiểu dữ liệu trong SQL (kiểu số)

| Data type | Description | Storage |
| :--- | :--- | :--- |
| **numeric(p,s)** | Fixed precision and scale numbers. Allows numbers from $-10^{38} + 1$ to $10^{38} - 1$. The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0 | 5-17 bytes |
| **smallmoney** | Monetary data from -214,748.3648 to 214,748.3647 | 4 bytes |
| **money** | Monetary data from -922,337,203,685,477.5808 to 922,337,203,685,477.5807 | 8 bytes |
| **float(n)** | Floating precision number data from $-1.79E + 308$ to $1.79E + 308$. The n parameter indicates whether the field should hold 4 or 8 bytes. float(24) holds a 4-byte field and float(53) holds an 8-byte field. Default value of n is 53. | 4 or 8 bytes |
| **real** | Floating precision number data from $-3.40E + 38$ to $3.40E + 38$ | 4 bytes |

# 3. Các kiểu dữ liệu trong SQL (kiểu ngày)

| Data type | Description | Storage |
| :--- | :--- | :--- |
| datetime | From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds | 8 bytes |
| datetime2 | From January 1, 0001 to December 31, 9999 with an accuracy of 100 nanoseconds | 6-8 bytes |
| smalldatetime | From January 1, 1900 to June 6, 2079 with an accuracy of 1 minute | 4 bytes |
| date | Store a date only. From January 1, 0001 to December 31, 9999 | 3 bytes |
| time | Store a time only to an accuracy of 100 nanoseconds | 3-5 bytes |
| datetimeoffset | The same as datetime2 with the addition of a time zone offset | 8-10 bytes |
| timestamp | Stores a unique number that gets updated every time a row gets created or modified. The timestamp value is based upon an internal clock and does not correspond to real time. Each table may have only one timestamp variable | |

# 3. Các kiểu dữ liệu trong SQL (kiểu khác)

| Data type | Description |
| :--- | :--- |
| sql_variant | Stores up to 8,000 bytes of data of various data types, except text, ntext, and timestamp |
| uniqueidentifier | Stores a globally unique identifier (GUID) |
| xml | Stores XML formatted data. Maximum 2GB |
| cursor | Stores a reference to a cursor used for database operations |
| table | Stores a result-set for later processing |

# 4. Làm việc với bảng dữ liệu

## **Thêm bảng**

| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| | | ☐ |

### Column Properties

**Object Explorer**
- Connect
- TRANGNTT\SQLEXPRESS (SQL Server 1)
    - Databases
        - System Databases
        - Bank
        - BikeStore
        - QL_SinhVien
            - Database Diagrams
            - Tables
                - New Table...
                - New FileTable...
                - Filter
                - Start PowerShell
                - Reports
                - Refresh
            - Views
            - Synonyms
            - Programmability
            - Service Broker
            - Storage
            - Security
        - QLy_SinhVien
        - QuanLy_SinhVien
        - ReportServer$SQLEXPRESS
        - ReportServer$SQLEXPRESSTempDB
    - Security
    - Server Objects

## **Sửa, xóa bảng**

| |
| :--- |
| New Table... |
| **Design** |
| Select Top 1000 Rows |
| Edit Top 200 Rows |
| Script Table as |
| View Dependencies |
| Full-Text index |
| Policies |
| Facets |
| Start PowerShell |
| Reports |
| Rename |
| **Delete** |
| Refresh |
| Properties |

## Thuộc tính:

- **Tên cột (Name)**: Đặt tên cột
- **Cho phép giá trị Null (Allow Nulls)**: Đặt ràng buộc NOT NULL cho cột
- **Kiểu dữ liệu (Data Type)**: Đặt kiểu dữ liệu của cột
- **Giá trị mặc định (Default Value or Binding)**: Đặt ràng buộc mặc định cho cột. Tùy chọn này được bỏ trống nếu không có ràng buộc mặc định.
- **Chiều dài (Length)**: Biểu thị số lượng ký tự hoặc byte tối đa cho dữ liệu của cột, chẳng hạn nvarchar (50) có chiều dài là 50

## Xem thuộc tính:

| Object Explorer | Column Properties - MaMH |
| :--- | :--- |
| Connect | Select a page |
| TRANGNTT\SQLEXPRESS (SQL Server 1) | General |
| Databases | Extended Properties |
| System Databases | |
| Bank | |
| BikeStore | |
| QL_SinhVien | |
| Database Diagrams | |
| Tables | |
| System Tables | |
| FileTables | |
| dbo.Ket_Qua | |
| Columns | |
| MaMH (PK, FK, char(10)) | |
| MaSV (PK, FK, i | |
| Diem (float, nu | |
| KyThi (PK, tinyi | |
| Keys | |
| Constraints | |
| Triggers | |
| Indexes | |
| Statistics | |
| dbo.Khoa | |
| dbo.Lop | |
| dbo.M_Hoc | |
| dbo.Sinh_Vien | |
| Views | |
| Synonyms | |

| Name | MaMH |
| :--- | :--- |
| Data Type | char |
| System Type | char |
| Primary Key | True |
| Allow Nulls | False |
| Is Computed | False |
| Computed text | |
| Identity | False |
| Identity Seed | 0 |
| Identity Increment | 0 |
| Default Binding | |
| Default Schema | |
| Rule | |
| Rule Schema | |
| Length | 10 |
| Collation | SQL_Latin1_General_CP1_CI_ |
| Numeric Precision | 0 |

**Connection**
- Server: TRANGNTT\SQLEXPRESS
- Connection: TRANGNTT\admin
- View connection

**Progress**
- Ready

**Name**
The column's name.

## Tạo các loại ràng buộc

| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaMH | char(10) | □ |
| MasV | int | □ |
| Diem | float | ☑ |
| KyThi | tinyint | □ |

### Column Properties

| (General) | |
| :--- | :--- |
| (Name) | MaMH |
| Allow Nulls | No |
| Data Type | char |
| Default Value or Binding | |
| Length | 10 |

### Table Designer
- (General)

## **Thêm/ sửa/ xóa dữ liệu**

| Object Explorer | | MaMH | MaSV | Diem | KyThi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Connect | | CSDL1 | 1 | 9 | 3 |
| ⊞ BikeStore | | CSDL1 | 2 | 9 | 3 |
| ⊟ QL_SinhVien | | CSDL1 | 3 | 4 | 3 |
| ⊞ Database Diagrams | | CSDL1 | 6 | 7 | 3 |
| ⊟ Tables | | TA1 | 1 | 9 | 1 |
| ⊞ System Tables | | TA1 | 2 | 7 | 1 |
| ⊞ FileTables | | TA2 | 4 | 9 | 3 |
| ⊟ **dbo.Ket_Qua** | New Table... | TDC | 1 | 8 | 1 |
| ⊞ dbo.Kho | Design | TDC | 2 | 4 | 1 |
| ⊞ dbo.Lop | **Select Top 1000 Rows** | TDC | 2 | 8 | 3 |
| ⊞ dbo.M_H | Edit Top 200 Rows | TDC | 3 | 8 | 1 |
| ⊞ dbo.Sinh | Script Table as | TDC | 6 | 0 | 1 |
| ⊞ Views | View Dependencies | TDC | 6 | 0 | 2 |
| ⊞ Synonyms | Full-Text index | TDNH1 | 2 | 6 | 4 |
| ⊞ Programma | Policies | *NULL* | *NULL* | *NULL* | *NULL* |
| ⊞ Service Bro | Facets | | | | |
| ⊞ Storage | Start PowerShell | | | | |
| ⊞ Security | Reports | | | | |
| ⊞ Qly_SinhVien | Rename | | | | |
| ⊞ QuanLy_Sinh | Delete | | | | |
| ⊞ ReportServer | Refresh | | | | |
| ⊞ ReportServer | Properties | | | | |
| ⊞ Security | | | | | |
| ⊞ Server Objects | | | | | |
| ⊞ Replication | | | | | |
| ⊞ Management | | | | | |

# 5. Import và Export dữ liệu

- **Import và Export** trong **SQL Server Management Studio (SSMS)** hỗ trợ người dùng sao chép dữ liệu từ vị trí này sang vị trí khác.
- **Export** cho phép xuất dữ liệu sang cơ sở dữ liệu khác, Excel, tệp văn bản, v.v.
- **Import** cho phép tải dữ liệu từ cơ sở dữ liệu hoặc nguồn khác như Excel, tệp văn bản, v.v.

# 5. Import và Export dữ liệu

- In SQL Server Management Studio, connect to an instance of the SQL Server Database Engine.
- Expand **Databases**.
- Right-click a database.
- Point to **Tasks**.
- Click one of the following options.
    - **Import Data**
    - **Export Data**

# 5. Import và Export dữ liệu

**Object Explorer**

- Connect
- TRANGNTT\SQLEXPRESS (SQL Server 11.0.2218 -
    - Databases
        - System Databases
        - Bank
        - BikeStore
        - QL_SinhVien
        - Qly_Si
            - New Database...
            - New Query
            - Script Database as
            - **Tasks**
                - Detach...
                - Take Offline
                - Bring Online
                - Shrink
                - Back Up...
                - Restore
                - Generate Scripts...
                - Extract Data-tier Application...
                - Deploy Database to SQL Azure...
                - Export Data-tier Application...
                - Register as Data-tier Application...
                - Upgrade Data-tier Application...
                - Delete Data-tier Application...
                - **Import Data...**
                - **Export Data...**
            - Policies
            - Facets
            - Start PowerShell
            - Reports
            - Rename
            - Delete
            - Refresh
            - Properties
        - QuanL
        - Report
        - Report
    - Security
    - Server Ol
    - Replicatio
    - Manager

Mô hình cơ sở dữ liệu quan hệ

# THANK YOU FOR WATCHING

**Học viện Ngân hàng**
12 P. Chùa Bộc, P. Kim Liên, TP. Hà Nội

**T:** 1900 561 595 **F:** 1900 561 595 **E:** truyenthong@hvnh.edu.vn **W:** www.hvnh.edu.vn
