ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# GIỚI THIỆU HỆ QUẢN TRỊ CƠ SỞ DỮ LIỆU ORACLE

ORACLE DATABASE


<!-- page 2 -->

ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# Nội dung chính

- Cơ sở dữ liệu quan hệ
- Hệ quản trị CSDL
- Giới thiệu về Oracle
- Các sản phẩm của Oracle
- Cài đặt Oracle
- Sử dụng dịch vụ Database Configuration Assistant
    - Tạo mới cơ sở dữ liệu
    - Xóa cơ sở dữ liệu

ORACLE


<!-- page 3 -->

# CSDL quan hệ (Relational Databases)

## Dữ liệu?

## Cơ sở dữ liệu
- CSDL là một tập hợp thông tin có tổ chức được lưu trữ như một đơn vị. Mục đích của CSDL là thu thập, lưu trữ và truy xuất thông tin có liên quan cho các ứng dụng CSDL

## Cơ sở dữ liệu quan hệ
- Là CSDL lưu trữ dữ liệu trong các quan hệ (bảng)
- Một quan hệ (bảng) là một tập hợp các bộ giá trị (hàng). Bộ giá trị là một tập hợp các giá trị thuộc tính (cột) không quan trọng thứ tự.


<!-- page 4 -->

ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# DBMS

- Hệ quản trị cơ sở dữ liệu (DBMS)
- Chức năng chính của DBMS
- Nhóm người dùng chính trong một DBMS
- Hệ quản trị CSDL quan hệ (RDBMS)

ORACLE


<!-- page 5 -->

# DBMS..

Hệ quản trị CSDL (database management system – DBMS) là phần mềm giúp tạo CSDL và cung cấp cơ chế lưu trữ, truy cập theo các mô hình CSDL.

## Chức năng chính:
- Quản lý cơ sở dữ liệu
- Quản lý file
- Quản lý ổ đĩa

## Có 3 loại người dùng chính:
- Người quản trị CSDL (Database Administrator);
- Người lập trình ứng dụng (Application Programmer);
- Người dùng cuối (End user)


<!-- page 6 -->

ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# DBMS..

## Các DBMS phổ biến

- Microsoft Access
- Microsoft SQL Server
- ORACLE
- PostgreSQL
- IBM DB2
- MySQL
- InterSystems CACHE

ORACLE


<!-- page 7 -->

# DBMS..

Mô hình quan hệ là cơ sở cho hệ quản trị cơ sở dữ liệu quan hệ (relational database management system – RDBMS)

Oracle đảm bảo được các đặc tính chính của một CSDL quan hệ:

- **Cấu trúc**: dữ liệu được lưu trữ và truy cập bởi các đối tượng như bảng, khung nhìn, chỉ mục..
- **Hoạt động**: xác định hoặc thao tác dữ liệu từ các cấu trúc bảng những câu lệnh như CREATE, SELECT..
- **Toàn vẹn**: các quy tắc bảo vệ dữ liệu và cấu trúc của CSDL như khóa chính, khóa ngoại..

ORACLE


<!-- page 8 -->

ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# DBMS...

## A desktop DBMS
- Microsoft Access, Filemaker Pro, Paradox, Lotus Approach, and Fox Pro.

## A server DBMS
- Apache Derby, Microsoft SQL Server, Oracle, IBM DB2, Sybase ASE, Informix, MySQL, and ProgreSQL.

ORACLE


<!-- page 9 -->

# Hệ thống xử lý theo mô hình Clien/Server

## Các thành phần của một ứng dụng truy xuất CSDL

- Display control: tổ chức giao tiếp người – máy
- Application process: phân tích các kết quả giao tiếp; thực hiện các tính toán
- Data access: truy xuất CSDL, lọc và cập nhật dữ liệu

Display Control $\leftrightarrow$ Application Process $\leftrightarrow$ Data Access $\leftrightarrow$ Data Base

ORACLE


<!-- page 10 -->

# Hệ thống xử lý theo mô hình Client/Server

Oracle server có thể chạy trên một hay nhiều máy tính với các mô hình khác nhau:

- **Client – Application Server – Server**: đây là mô hình 3 lớp, người dùng truy cập từ Client vào Server thông qua trạm trung gian là Application Server.
- **Client – Server**: thông qua hệ thống mạng, người dùng từ Client truy xuất dữ liệu trên Server – mô hình 2 lớp
- **Host – Base**: người dung truy xuất dữ liệu ngay tại máy tính dùng làm Server lưu trữ CSDL


<!-- page 11 -->

# Giới thiệu về Oracle

- Được thành lập năm 1977, do Larry Ellison
- Giai đoạn đầu thành lập, sản phẩm chủ yếu của Oracle là về hệ quản trị CSDL
- Từ năm 1989 bắt đầu phát triển các ứng dụng lớn dùng trong doanh nghiệp


<!-- page 12 -->

ITDE
INFORMATION TECHNOLOGY & DIGITAL ECONOMICS
BANKING ACADEMY OF VIETNAM

# Các sản phẩm và dịch vụ của Oracle

- Oracle Application
- **Oracle Database**
- Engineered System
- Enterprise magement
- Middleware
- Hệ điều hành
- Server và storage systems
- Ảo hóa

ORACLE


<!-- page 13 -->

# Oracle database

- Phiên bản hệ quản trị CSDL quan hệ đầu tiên ra mắt vào năm 1979
- Thực sự mạnh từ Oracle 7.0 (1992)
- 1999: ra mắt Oracle 8i, có hỗ trợ Internet
- 2001: ra mắt Oracle 9i, có hỗ trợ RAC (Real Application Clusters)
- 2003: ra mắt Oracle 10g, hỗ trợ tính toán lưới (grid)
- 2007: ra mắt Oracle 11g,
- **2013: ra mắt Oracle 12c (c trong 12c là viết tắt của cloud)**
- 2018: ra mắt Oracle 18c
- **2019: ra mắt phiên bản Oracle 19c**
- Cuối năm 2020: ra mắt phiên bản Oracle 21c


<!-- page 14 -->

# Oracle database

- Phiên bản “i” là viết tắt của “internet”
- Đưa ra Oracle RAC, viết tắt của Oracle Real Application Clusters: cung cấp phần mềm để phân cụm và có tính sẵn sàng cao trong môi trường CSDL Oracle.
- Phân cụm: cho phép nhiều máy tính chạy Oracle RDBMS đồng thời khi truy cập vào một CSDL.
- Thuật toán phân tích dữ liệu và khai thác dữ liệu trong bản phát hành 9.2.0.8 vào năm 2007.


<!-- page 15 -->

# Oracle database

- Phiên bản “g” viết tắt của “grid”
- Điện toán lưới cung cấp cơ sở hạ tầng phần mềm sử dụng lưu trữ theo modul và máy chủ, rủi ro thấp.
- Giúp cân bằng khối lượng công việc tổng thể và cung cấp nguồn lực theo yêu cầu.
- **Các tính năng mới như**: hệ thống quản lý cơ sở dữ liệu tự động, cơ sở hạ tầng lưới, Oracle ASM (Automatic Storage Management), bảo vệ dữ liệu hoạt động, **Oracle Database Appliance**.


<!-- page 16 -->

# Oracle database

- **Các phiên bản có hậu tố là “c” viết tắt của “cloud”**
- **Giúp doanh nghiệp đưa CSDL Oracle có sẵn của họ lên cloud.**
- **Tự động hóa cơ chế tối ưu hóa dữ liệu để quản lý hệ thống thiết bị lưu trữ**
    - Dữ liệu ít khi truy cập được chuyển vào lưu trữ trên thiết bị có chi phí rẻ hơn, dữ liệu thường xuyên truy cập được lưu trữ trên thiết bị lưu trữ có tốc độ cao và chi phí đắt hơn


<!-- page 17 -->

# Oracle database

Có thể hợp nhất các CSDL thành phần vào một CSDL cha (root container)

- Tối ưu hóa tài nguyên điện toán, giảm chi phí hạ tầng
- Có tính năng biên tập (Redaction)
    - Có tác dụng che giấu dữ liệu nhạy cảm khi cung cấp dữ liệu cho người sử dụng cuối.
- Giúp doanh nghiệp tìm thêm cơ hội kinh doanh từ dữ liệu lớn (Big Data) gồm cả dữ liệu phi cấu trúc (dữ liệu từ mạng xã hội) và các dữ liệu có cấu trúc thông thường.


<!-- page 18 -->

# Oracle 19c...

## Đặc điểm mới của Oracle 19c:

- *Kiểm định truy vấn* (Query Quarantine): giải quyết vấn đề quá tải tài nguyên hệ thống, đảm bảo các truy vấn không chạy lặp đi lặp lại.
- *Hỗ trợ JSON* (JSON Support): Đơn giản cú pháp cho các hàm JSON, cung cấp API SODA cho Node.js, C, Python và Java.
    - JSON (JavaScript Object Notation), định dạng dữ liệu tuân theo một quy luật nhất định mà hầu hết các ngôn ngữ lập trình hiện nay đều có thể đọc được


<!-- page 19 -->

# Oracle 19c...

- **Lập chỉ mục tự động** (Automatic Indexing): Chỉ mục được tự động điều chỉnh trong thời gian ngắn, giúp nâng cao hiệu suất & tiết kiệm chi phí nhờ học máy (machine learning).
- **Bảng phân vùng kết hợp** (Hybrid Partitioned Tables): người quản trị CSDL quản lý các bảng cả bên trong và bên ngoài CSDL một cách dễ dàng.
- **Bảo vệ dữ liệu hoạt động** (Active Data Guard): ngăn chặn thời gian chết và mất dữ liệu trong quá trình sửa chữa và nâng cấp cơ sở dữ liệu.


<!-- page 20 -->

# Những lưu ý khi cài đặt

Trước khi cài:
- Dọn dẹp ổ cứng cho đủ dung lượng cài đặt
- Stop các chương trình diệt virus

Nếu quá trình cài bị lỗi:
- **Gỡ bỏ phiên bản cũ**, sau đó mới cài phiên bản mới

Trong quá trình dùng bị lỗi:
- **Tìm mọi cách để sửa** (không thể sửa được thì mới cài lại)


<!-- page 21 -->

# Cài đặt

Yêu cầu hệ thống
- RAM: tối thiểu 2GB
- Dung lượng ổ đĩa trống: 12G
    - Swap: 2GB
    - Thư mục /tmp: 595MB
    - Oracle home: 6.5 GB
    - Data file: 4.4GB
    - ...

ORACLE


<!-- page 22 -->

# Cài đặt

- Download Oracle Database 19c
- Giải nén file .zip vừa tải về & tạo đường dẫn như sau rồi copy các file vừa giải nén vào

> This PC > D (:) > app > oracle > product > 19c > db_home1


<!-- page 23 -->

# Cài đặt

Nhấp chuột phải vào **setup.exe** (1) > **Run as administrator** (2)

| Name | Date modified | Type | Size |
| :--- | :--- | :--- | :--- |
| ord | 02/05/2020 6:34 AM | File folder | |
| ords | 02/05/2020 6:34 AM | File folder | |
| oui | 02/05/2020 6:34 AM | File folder | |
| owm | | File folder | |
| perl | | File folder | |
| plsql | | File folder | |
| precomp | | File folder | |
| QOpatch | | File folder | |
| R | | File folder | |
| racg | | File folder | |
| rdbms | | File folder | |
| relnotes | | File folder | |
| slax | | File folder | |
| sqldeveloper | | File folder | |
| sqlj | | File folder | |
| sqlpatch | | File folder | |
| sqlplus | | File folder | |
| srvm | | File folder | |
| suptools | | File folder | |
| ucp | | File folder | |
| usm | | File folder | |
| utl | | File folder | |
| wwg | | File folder | |
| xdk | | File folder | |
| env.ora | | File | 1 KB |
| schagent.conf | | File | 3 KB |
| setup.bat | | Windows Batch File | 2 KB |
| setup.exe | 14/11/2018 10:42 PM | Application | 282 KB |


<!-- page 24 -->

# Oracle Database 19c Installer - Step 1 of 16

## Select Configuration Option

Select any of the following install options.

- **Create and configure a single instance database.**
  This option creates a starter database. (1)
- Set Up Software Only

Note 1: For RAC install, do 'Set Up Software Only' and then execute DBCA (Database Configuration Assistant) from the oracle home.
Note 2: To upgrade an Oracle Database, do 'Set Up Software Only' and then execute DBUA (Database Upgrade Assistant) from the oracle home.

Help
Back
Next > (2)
Install
Cancel


<!-- page 25 -->

# Oracle Database 19c Installer - Step 2 of 15

## Select System Class

- Configuration Option
- **System Class**
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

(1)
- Desktop class
  Choose this option if you are installing on a laptop or desktop class system. This option includes a starter database and allows minimal configuration.
- **Server class**
  Choose this option if you are installing on a server class system, which Oracle defines as a system used in a production data center. This option allows for more advanced configuration options.

(2)
Help | < Back | **Next >** | Install | Cancel


<!-- page 26 -->

# Oracle Database 19c Installer - Step 3 of 16

## Select Install Type

- Typical install
  Perform full Oracle Database installation with basic configuration.

- **Advanced install**
  Allows advanced selections such as different passwords for the SYS, SYSMAN, SYSTEM and DBSNMP accounts, database character set, product languages, automated backups, custom installation, and alternative storage options such as Oracle Automatic Storage Management.

(1)

(2)

- Help
- < Back
- Next >
- Install
- Cancel


<!-- page 27 -->

# Oracle Database 19c Installer - Step 4 of 17

## Select Database Edition

Which database edition do you want to install?

(1)

- **Enterprise Edition**
  Oracle Database 19c **Enterprise Edition** is a self-managing database that has the scalability, performance, high availability, and security features required to run the most demanding, mission-critical applications.

- Standard Edition 2
  Oracle Database 19c Standard Edition 2 is a full-featured data management solution ideally suited to the needs of medium-sized businesses.

---

### Navigation Menu

- Configuration Option
- System Class
- Install Type
- **Database Edition**
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

(2)

[Help] [< Back] [Next >] [Install] [Cancel]


<!-- page 28 -->

# Oracle Database 19c Installer - Step 5 of 17

## Specify Oracle Home User

For enhanced security, you may choose to run Windows Services from this Oracle home with a non-administrator account. Oracle recommends that you choose a Virtual Account or specify a standard Windows User Account for this purpose.

- (1) **Use Virtual Account**
- Use Existing Windows User
    - User Name:
    - Password:
- Create New Windows User
    - User Name:
    - Password:
    - Confirm Password:
    - The newly created user is denied Windows logon privileges.
- Use Windows Built-in Account

---

### Navigation Menu

- Configuration Option
- System Class
- Install Type
- Database Edition
- **Oracle Home User**
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

Help | < Back | (2) Next > | Install | Cancel


<!-- page 29 -->

# Oracle Database 19c Installer - Step 6 of 17

## Specify Installation Location

Specify a path to place all Oracle software and configuration-related files installed by this installation owner. This location is the Oracle base directory for the installation owner.

**Oracle base**: D:\app\oracle\ (1)

This software directory is the Oracle Database home directory.
Software location: D:\app\oracle\product\19c\db_home1

---

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- **Installation Location**
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

Help | < Back | Next > (2) | Install | Cancel


<!-- page 30 -->

# Oracle Database 19c Installer - Step 7 of 17

## Select Configuration Type

Select the type of database that you want to create.

- **General Purpose / Transaction Processing**
  A starter database designed for general purpose use, or for transaction-heavy applications.
- Data Warehousing
  A starter database optimized for data warehousing applications.

(1)

(2)

Help | < Back | Next > | Install | Cancel


<!-- page 31 -->

# Oracle Database 19c Installer - Step 8 of 17

## Specify Database Identifiers

Provide the identifier information required to access the database uniquely. An Oracle database is uniquely identified by a **Global database name**, typically of the form "name.domain". A database is referenced by at least one Oracle instance which is uniquely identified from any other instance on this computer by an Oracle system identifier (SID).

- **Global database name:** [ orcl ] (1)
- **Oracle system identifier (SID):** [ orcl ] (1)

[ ] **Create as Container database**
Creates a database container for consolidating multiple databases into a single database and enables database virtualization.
- Pluggable database name: [ orclpdb ]

---

### Navigation Menu
- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- **Database Identifiers**
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

[ Help ] [ < Back ] [ Next > ] (2) [ Install ] [ Cancel ]


<!-- page 32 -->

# Oracle Database 19c Installer - Step 9 of 17

## Specify Configuration Options

(1) **Memory** | Character sets | Sample schemas

Enabling Automatic Memory Management allows the database to distribute memory automatically between the system global area (SGA) and the program global area (PGA), based on user-specified overall database memory target size. If automatic memory management is not enabled, then the SGA and PGA must be sized manually.

[ ] **Enable Automatic Memory Management**

Allocate memory:
256 | 2000 | 8073
(2) [ 2,000 ] 25 %

SGA target: 1500 MB
PGA aggregate target: 500 MB
Target database memory: 2000 MB

---

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- **Configuration Options**
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

[ Help ] [ < Back ] [ Next > ] [ Install ] [ Cancel ]


<!-- page 33 -->

# Oracle Database 19c Installer - Step 9 of 17

## Specify Configuration Options

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- **Configuration Options**
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

### (1) Character sets

Memory | **Character sets** | Sample schemas

The database character set determines how character data is stored in the database.

- (2) **Use Unicode (AL32UTF8)**
  Setting character set to Unicode (AL32UTF8) enables you to store multiple language groups.
- Use OS character set (WE8MSWIN1252)
  Character set is based on the language setting of this operating system: WE8MSWIN1252.
- Choose from the following list of character sets
  Select Database character set:
  AL32UTF8 - Unicode UTF-8 Universal character set

---

Help | < Back | Next > | Install | Cancel


<!-- page 34 -->

# Oracle Database 19c Installer - Step 9 of 17

## Specify Configuration Options

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- **Configuration Options**
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

### (1) Sample schemas

Memory | Character sets | **Sample schemas**

You can choose to install sample schema in the starter database. If you choose this option, **Human Resources schema** will be installed in the starter database,in the SYSAUX tablespace.

(2) [x] **Install sample schemas in the database**

---

Help | < Back | (3) **Next >** | Install | Cancel


<!-- page 35 -->

# Oracle Database 19c Installer - Step 10 of 17

## Specify Database Storage Options

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- **Database Storage**
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

(1) **File system**
Use a file system for database storage. For optimal database organization and performance, Oracle recommends that you install data files and the Oracle database software on different disks.

(2) Specify database file location: D:\app\oracle\oradata [Browse...]

Oracle Automatic Storage Management
Oracle Automatic Storage Management (Oracle ASM) simplifies database administration, and places database files for optimal I/O performance. Select this option if you intend to use Oracle ASM.

(3) [< Back] [Next >] [Install] [Cancel]

[Help]


<!-- page 36 -->

# Oracle Database 19c Installer - Step 11 of 17

## Specify Management Options

Oracle Database 12c is managed by Oracle Database Express by default. You can use Oracle Enterprise Manager 12c Cloud Control to manage each Oracle Database 19c centrally. Specify the details of the Cloud Control configuration to manage your database.

- [ ] **Register with Enterprise Manager (EM) Cloud Control**

- **OMS Host:**
- **OMS Port:**
- **EM Admin User Name:**
- **EM Admin Password:**

---

### Các bước cài đặt:
- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- **Management Options**
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- Finish

---

[Help] [< Back] [Next >] [Install] [Cancel]


<!-- page 37 -->

# Oracle Database 19c Installer - Step 12 of 17

## Specify Recovery Options

Enable or disable recovery for your database. If you choose to enable recovery, then the location specified will be used as recovery area storage.

- **(1)** [x] **Enable Recovery**
- **(2)** (o) **File system**
- **(3)** Recovery area location: [ D:\app\oracle\recovery_area ] [Browse...]
- ( ) Oracle Automatic Storage Management

**(4)** [ Next > ]

[ Help ] [ < Back ] [ Next > ] [ Install ] [ Cancel ]


<!-- page 38 -->

# Oracle Database 19c Installer - Step 13 of 17

## Specify Schema Passwords

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- **Schema Passwords**
- Prerequisite Checks
- Summary
- Install Product
- Finish

The starter database contains pre-loaded schemas, most of which have passwords that are expired and locked at the end of installation. After installation is complete, you must unlock and set new passwords for those accounts you want to use. Schemas used for database management and postinstallation functions are left unlocked, and passwords for these accounts will not expire. Specify the passwords for these accounts.

O Use different passwords for these accounts

| | Password | Confirm password |
| :--- | :--- | :--- |
| SYS | | |
| SYSTEM | | |

(1) O **Use the same password for all accounts**

(2) **Password:** ●●●●●●●● **Confirm password:** ●●●●●●●●

(3) < Back **Next >** Install Cancel

Help


<!-- page 39 -->

# Oracle Database 19c Installer - Step 14 of 17

## Perform Prerequisite Checks

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- **Prerequisite Checks**
- Summary
- Install Product
- Finish

Verifying that the target environment meets minimum installation and configuration requirements for products you have selected. This can take time. Please wait.

33%

Checking Swap Size ...

Help | < Back | Next > | Install | Cancel


<!-- page 40 -->

# Oracle Database 19c Installer - Step 15 of 17

## Summary

- **Oracle Database 19c Installer**
    - **Global settings**
        - Oracle Home User: Virtual Account [Edit]
        - Install method: Advanced installation [Edit]
        - Database edition: Enterprise Edition (Create and configure a database) [Edit]
        - Oracle base: D:\app\oracle\ [Edit]
        - Software location: D:\app\oracle\product\19c\db_home1
        - OraMTS Port Number: 49152
    - **Database information**
        - Configuration: General Purpose / Transaction Processing [Edit]
        - Global database name: orcl [Edit]
        - Oracle system identifier (SID): orcl [Edit]
        - Allocated memory: 2000 MB [Edit]
        - Automatic memory management option: FALSE [Edit]
        - Database character set : AL32UTF8 (Unicode UTF-8 Universal character set) [Edit]
        - Management method: Database express [Edit]
        - Database storage mechanism: File system [Edit]
        - Database file location: D:\app\oracle\oradata [Edit]
        - Recovery: Enabled [Edit]
        - Recovery Storage Type: File system [Edit]
        - Database Recovery file location: D:\app\oracle\oradata [Edit]

---

### Các bước thực hiện:
- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- **Summary**
- Install Product
- Finish

---

[Save Response File...] [Help] [< Back] [Next >] [Install] [Cancel]


<!-- page 41 -->

# Oracle Database 19c Installer - Step 16 of 17

## Install Product

**Progress**
7%
Starting Installations

**Status**
| Task | Status |
| :--- | :--- |
| Configure Local Node | Pending |
| • Prepare | Pending |
| • Setup | Pending |
| Setup Oracle Base | Pending |
| Oracle Database configuration | Pending |

Details | Revert All | Revert | Retry | Skip

19c ORACLE Database

Help | < Back | Next > | Install | Cancel


<!-- page 42 -->

# Hoàn thành

## Oracle Database 19c Installer - Step 17 of 17

**Finish**

- Configuration Option
- System Class
- Install Type
- Database Edition
- Oracle Home User
- Installation Location
- Configuration Type
- Database Identifiers
- Configuration Options
- Database Storage
- Management Options
- Recovery Options
- Schema Passwords
- Prerequisite Checks
- Summary
- Install Product
- **Finish**

**The configuration of Oracle Database was successful.**

**Note:**
Oracle Enterprise Manager Database Express URL: https://COM:5500/em

Help | < Back | Next > | Install | Close


<!-- page 43 -->

# Chắc chắn rằng **OracleOraDB19Home1TNSListener** và **OracleServiceORCL** đang **Running** (Start > Run > Services.msc > Enter) trước khi thực hiện các bước tiếp theo

| Name | Description | Status | Startup Type | Log On As |
| :--- | :--- | :--- | :--- | :--- |
| Optimize drives | Helps the co... | | Manual | Local System |
| OracleJobSchedulerORCL | | | Disabled | NT SERVICE... |
| OracleOraDB19Home1MTSRecoveryService | | Running | Automatic | NT SERVICE... |
| **OracleOraDB19Home1TNSListener** | | **Running** | **Automatic** | **NT SERVICE...** |
| OracleRemExecServiceV2 | | Running | Manual | Local System |
| **OracleServiceORCL** | | **Running** | **Automatic** | **NT SERVICE...** |
| OracleVssWriterORCL | | | Automatic | NT SERVICE... |
| Parental Controls | Enforces par... | | Manual | Local System |
| Payments and NFC/SE Manager | Manages pa... | Running | Manual (Trigg... | Local Service |
| Peer Name Resolution Protocol | Enables serv... | | Manual | Local Service |
| Peer Networking Grouping | Enables mul... | | Manual | Local Service |
| Peer Networking Identity Manager | Provides ide... | | Manual | Local Service |
| Performance Counter DLL Host | Enables rem... | | Manual | Local Service |
| Performance Logs & Alerts | Performance... | | Manual | Local Service |
| Phone Service | Manages th... | | Manual (Trigg... | Local Service |
| PimIndexMaintenanceSvc_52f80 | Indexes cont... | Running | Manual | Local System |
| Plug and Play | Enables a co... | Running | Manual | Local System |
| PNRP Machine Name Publication Service | This service... | | Manual | Local Service |
| Portable Device Enumerator Service | Enforces gro... | | Manual (Trigg... | Local Service |
| Power | Manages po... | Running | Automatic | Local System |
| Print Spooler | This service... | Running | Automatic | Local System |
| Printer Extensions and Notifications | This service... | | Manual | Local System |
| PrintWorkflowUserSvc_52f80 | Print Workfl... | | Manual | Local System |
| Problem Reports and Solutions Control Pan... | This service... | | Manual | Local System |
| Program Compatibility Assistant Service | This service... | Running | Manual | Local System |
| Quality Windows Audio Video Experience | Quality Win... | | Manual | Local Service |
| Radio Management Service | Radio Mana... | Running | Manual | Local Service |
| Realtek Audio Universal Service | Realtek Audi... | Running | Automatic | Local System |
| Recommended Troubleshooting Service | Enables aut... | | Manual | Local System |
| Remote Access Auto Connection Manager | Creates a co... | | Manual | Local System |
| Remote Access Connection Manager | Manages di... | Running | Automatic | Local System |
| Remote Desktop Configuration | Remote Des... | | Manual | Local System |
| Remote Desktop Services | Allows users... | | Manual | Network Se... |
| Remote Desktop Services UserMode Port R... | Allows the re... | | Manual | Local System |


<!-- page 44 -->

# Tạo mới cơ sở dữ liệu

**Tạo CSDL sử dụng DBCA**

- Oracle - OraDB19Home1
    - Database Configuration Assistant
    - Database Migration Assistant for Un...
    - Database Upgrade Assistant
    - Locale Builder
    - Net Configuration Assistant
    - Net Manager
    - Oracle Instance Manager
    - Oracle ODBC Help
    - Oracle Provider for OLE DB for OLA...
    - Oracle Provider for OLE DB Readme
    - SQL Plus


<!-- page 45 -->

# Database Configuration Assistant - Application - Step 1 of 14

**Select Database Operation**

- **Create a database**
- Configure an existing database
- Delete database
- Manage templates
- Manage Pluggable databases
- Oracle RAC database Instance management

**Database Operation**
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Database Options
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

Help | < Back | Next > | Finish | Cancel


<!-- page 46 -->

# Database Configuration Assistant - Create a database - Step 2 of 14

**Select Database Creation Mode**

- **Typical configuration**
    - Global database name: orcl
    - Storage type: File System
    - Database files location: {ORACLE_BASE}\oradata\{DB_UNIQUE_NAME}
    - Fast Recovery Area (FRA): {ORACLE_BASE}\fast_recovery_area\{DB_UNIQUE_NAME}
    - Database character set: AL32UTF8 - Unicode UTF-8 Universal character set
    - Administrative password:
    - Confirm password:
    - [x] Create as Container database
    - Pluggable database name:

- (o) **Advanced configuration**

---

- Database Operation
- **Creation Mode**
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Database Options
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

---

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 47 -->

# Database Configuration Assistant - Create a database - Step 3 of 14

**Select Database Deployment Type**

- Select the type of database you want to create.
- **Database type:** Oracle Single Instance database
- **Configuration type:** Admin Managed

Select a template for your database.

Templates that include datafiles contain pre-created databases. They allow you to create a new database quickly. Use templates without datafiles only when necessary, such as when you need to change attributes like block size that cannot be altered after database creation.

| Template name | Include datafiles | Details |
| :--- | :--- | :--- |
| Data Warehouse | Yes | View details |
| General Purpose or Transaction Processing | Yes | View details |
| Custom Database | No | View details |

**Template location:** D:\App\oracle\product\19c\db_home1\assistants\dbca\templates [Change...]

---

- Database Operation
- **Creation Mode**
- **Deployment Type**
- **Database Identification**
- Storage Option
- Fast Recovery Option
- Database Options
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 48 -->

# Database Configuration Assistant - Create a database - Step 4 of 14

**Specify Database Identification Details**

19c ORACLE Database

Provide a unique database identifier information. An Oracle database is uniquely identified by a Global database name, typically of the form "name.domain".

- **Global database name:** Manager
- **SID:** Manager
- Service name:

**Đặt tên CSDL**

[ ] **Create as Container database**

A Container database can be used for consolidating multiple databases into a single database, and it enables database virtualization. A Container database (CDB) can have zero or more pluggable databases (PDB).

- [x] Use **Local Undo tablespace for PDBs**
- ( ) Create an empty Container database
- ( ) Create a Container database with one or more PDBs

- Number of PDBs: 1
- PDB name: pdb

Help | < Back | **Next >** | Finish | Cancel


<!-- page 49 -->

# Database Configuration Assistant - Create 'Manager' database - Step 5 of 14

**Select Database Storage Option**

- Database Operation
- Creation Mode
- Deployment Type
- **Database Identification**
- **Storage Option**
- **Fast Recovery Option**
- Database Options
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

- (•) **Use template file for database storage attributes**
  Storage type and location for database files will be picked up from the specified template (General Purpose or Transaction Processing).

- ( ) **Use following for the database storage attributes**
  All the database files will be put at the specified location below. You can customize the name and location of each datafile in the subsequent screen.

  Database files storage type: [ File System ]
  Database files location: [ {ORACLE_BASE}\oradata\{DB_UNIQUE_NAME} ] [ Browse... ]

  Oracle Managed files option will enable Oracle to automatically generate the names of the datafiles for simplified database management.

  [ ] **Use Oracle-Managed Files (OMF)** [ Multiplex redo logs and control files... ]

[ File location variables... ]

[ Help ] [ < Back ] [ **Next >** ] [ Finish ] [ Cancel ]


<!-- page 50 -->

# Database Configuration Assistant - Create 'Manager' database - Step 6 of 14

## Select Fast Recovery Option

Choose the recovery options for the database.

- [x] Specify **Fast Recovery Area**
    - Recovery files **s**torage type: File System
    - Fast **R**ecovery Area: C:\Users\admin\Documents [Browse...]
    - Fast Recovery Area size: 8256 [MB]
- [x] **E**nable archiving [Edit **a**rchive mode parameters...]

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 51 -->

# Database Configuration Assistant - Create 'Manager' database - Step 7 of 14

**Specify Network Configuration Details**

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Fast Recovery Option
- **Network Configuration**
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

## Listener selection
Listeners from current Oracle home are listed below. Specify the listener name and port to create a new listener in current Oracle home.

| | Name | Port | Oracle home | Status |
| :--- | :--- | :--- | :--- | :--- |
| ☑ | LISTENER | 1521 | D:\App\oracle\product\19c\db_home1 | Up |

☐ **Create a new listener**
Listener name:
Listener port: 1521
Oracle home: D:\App\oracle\product\19c\db_home1

Help | < Back | Next > | Finish | Cancel


<!-- page 52 -->

# Database Configuration Assistant - Create 'Manager' database - Step 8 of 15

## Select Oracle Data Vault Config Option

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- **Data Vault Option**
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

---

- [ ] Configure Oracle Database **V**ault
    - Database Vault owner: __________________________________________________
    - Password: ______________________________ Confirm password: ______________________________
    - [ ] Create a separate account manager
        - Account manager: __________________________________________________
        - Password: ______________________________ Confirm password: ______________________________

- [ ] Configure Oracle **L**abel Security
    - [ ] Configure Oracle Label Security with O**I**D

---

< Help | < Back | Next > | Finish | Cancel >


<!-- page 53 -->

# Database Configuration Assistant - Create 'Manager' database - Step 9 of 15

## Specify Configuration Options

| Memory | Sizing | Character sets | Connection mode | Sample schemas |
| :--- | :--- | :--- | :--- | :--- |

- **Use Automatic Shared Memory Management**
    - **SGA size:** 1267 MB
    - **PGA Size:** 423 MB
- **Use Manual Shared Memory Management**
    - Shared pool size: 0 MB
    - Buffer cache size: 0 MB
    - Java pool size: 0 MB
    - Large pool size: 0 MB
    - PGA size: 0 MB
    - Total memory for database 0 MB
- **Use Automatic Memory Management**
    - Memory target: 502 MB

---

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- **Data Vault Option**
- **Configuration Options**
- **Management Options**
- User Credentials
- Creation Option
- Summary
- Progress Page
- Finish

---

Help | < Back | Next > | Finish | Cancel


<!-- page 54 -->

# Database Configuration Assistant - Create 'Manager' database - Step 9 of 15

**Specify Configuration Options**

- Memory
- Sizing
- Character sets
- Connection mode
- **Sample schemas**

Installing sample schema configures the Human Resources schema. The contents are stored under the SYSAUX tablespace.

- [x] **Add sample schemas to the database**

Help | < Back | Next > | Finish | Cancel


<!-- page 55 -->

# Database Configuration Assistant - Create 'Manager' database - Step 10 of 15

## Specify Management Options

Specify the management options for the database.

- [x] **Configure Enterprise Manager (EM) database express**
    - **EM database express port:** 5501

- [ ] **Register with Enterprise Manager (EM) cloud control**
    - **OMS host:**
    - **OMS port:**
    - **EM admin username:**
    - **EM admin password:**

---

| Help | < Back | Next > | Finish | Cancel |
| :--- | :--- | :--- | :--- | :--- |


<!-- page 56 -->

# Database Configuration Assistant - Create 'Manager' database - Step 11 of 15

**Specify Database User Credentials**

19c ORACLE Database

You must specify passwords for the following user accounts in the new database for security reasons.

- O Use different administrative passwords

| | Password | Confirm password |
| :--- | :--- | :--- |
| SYS | | |
| SYSTEM | | |

- ◉ **Use the same administrative password for all accounts**

**Password**: ●●●●●●●● **Confirm password**: ●●●●●●●●

---

### Danh sách các bước:
- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- Data Vault Option
- Configuration Options
- Management Options
- **User Credentials**
- Creation Option
- Summary
- Progress Page
- Finish

---

Help | < Back | Next > | Finish | Cancel


<!-- page 57 -->

# Database Configuration Assistant - Create 'Manager' database - Step 12 of 15

## Select Database Creation Option

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- Data Vault Option
- Configuration Options
- Management Options
- **User Credentials**
- **Creation Option**
- **Summary**
- Progress Page
- Finish

Select the database creation options.

[x] **Create database**
Specify the SQL scripts you want to run after the database is created. The scripts are run in the order listed below.
Post DB creation scripts: [                                                                    ] [Browse...]

[ ] **Save as a database template**
Template name: [dbca_template_2021-08-14_07-56-51PM                                ]
Template location: [D:\App\oracle\product\19c\db_home1\assistants\dbca\templates\    ] [Browse...]
Description: [                                                                    ]

[ ] **Generate database creation scripts**
Destination directory: [{ORACLE_BASE}\admin\{DB_UNIQUE_NAME}\scripts                ] [Browse...]

Following advanced configuration options can be used to configure initialization parameters and customize database storage locations.

[All Initialization Parameters...] [Customize Storage Locations...]

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 58 -->

# Database Configuration Assistant - Create 'Manager' database - Step 13 of 15

**Summary**

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- Data Vault Option
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- **Summary**
- Progress Page
- Finish

## Database Configuration Assistant

### Global Settings
- Global database name: Manager
- Configuration type: Oracle Single Instance database
- SID: Manager
- Create as Container database: No
- Memory Configuration Type: Automatic Shared Memory Management
- Template name: General Purpose

### Initialization Parameters
- audit_file_dest: {ORACLE_BASE}\admin\{DB_UNIQUE_NAME}\adump
- audit_trail: db
- compatible: 19.0.0
- control_files: ("{ORACLE_BASE}\oradata\{DB_UNIQUE_NAME}\control01.ctl", "{ORACLE_BASE}\oradata\{DB_UNIQUE_NAME}\control01.ctl")
- db_block_size: 8192 BYTES
- db_name: Manager
- diagnostic_dest: {ORACLE_BASE}
- dispatchers: (PROTOCOL=TCP) (SERVICE=ManagerXDB)
- local_listener: LISTENER_MANAGER
- nls_language: AMERICAN
- nls_territory: AMERICA
- open_cursors: 300
- pga_aggregate_target: 423 MB
- processes: 320
- remote_login_passwordfile: EXCLUSIVE

[Save Response File...]

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 59 -->

# Database Configuration Assistant - Create 'Manager' database - Step 14 of 15

## Progress Page

**Progress**
10%
Copying database files : In Progress

**Status**
| Task | Status |
| :--- | :--- |
| ➡ DB Creation | In Progress |
| ✔ Prepare for db operation | Succeeded |
| ➡ Copying database files | In Progress |
| • Creating and starting Oracle instance | Pending |
| • Completing Database Creation | Pending |
| • Executing Post Configuration Actions | Pending |

[Details] [Revert All] [Revert] [Retry] [Skip]

DBCA Log Location:
D:\App\oracle\cfgtoollogs\dbca\Manager\trace.log_2021-08-14_07-56-51PM

[Help] [< Back] [Next >] [Finish] [Cancel]


<!-- page 60 -->

# Database Configuration Assistant - Create 'Manager' database - Step 15 of 15

**Finish**

- Database Operation
- Creation Mode
- Deployment Type
- Database Identification
- Storage Option
- Fast Recovery Option
- Network Configuration
- Data Vault Option
- Configuration Options
- Management Options
- User Credentials
- Creation Option
- Summary
- Progress Page
- **Finish**

Database creation complete. For details check the logfiles at:
D:\App\oracle\cfgtoollogs\dbca\Manager.

Database Information:
Global Database Name: Manager
System Identifier(SID): Manager
Server Parameter File name: D:\APP\ORACLE\PRODUCT\19C\DB_HOME1\DATABASE\SPFILEMANAGER.ORA
EM Database Express URL: https://TrangNTT:5501/em

Note: All database accounts except SYS and SYSTEM are locked. Select the Password Management button to view a complete list of locked accounts or to manage the database accounts. From the Password Management window, unlock only the accounts you will use. Oracle strongly recommends changing the default passwords immediately after unlocking the account.

[Password Management...]

Help | < Back | Next > | Finish | Close


<!-- page 61 -->

# Xóa CSDL

**Database Configuration Assistant - Application - Step 1 of 14**

**Select Database Operation**

- Select the operation that you want to perform.
- Create a database
- Configure an existing database
- **Delete database**
- Manage templates
- Manage Pluggable databases
- Oracle RAC database Instance management

Help | < Back | Next > | Finish | Cancel


<!-- page 62 -->

# Thực hiện lần lượt các bước cho đến khi hoàn tất

## Database Configuration Assistant - Delete database - Step 2 of 7

**Select Source Database**

| Database | Local instance | Type |
| :--- | :--- | :--- |
| ORCL | ORCL | Single Instance |
| MANAGER | MANAGER | Single Instance |

Specify the SYSDBA user credentials.

**User name:** SYS
**Password:** •••••••••

- Database Operation
- **Select Database**
- Instance Details
- Creation Option
- Summary
- Progress Page
- Finish

Help | < Back | Next > | Finish | Cancel


<!-- page 63 -->

![ITDE](https://i.imgur.com/4y5y15S.png)

# Demo

![ORACLE](https://i.imgur.com/4y5y15S.png)


<!-- page 64 -->

![ITDE - INFORMATION TECHNOLOGY & DIGITAL ECONOMICS - BANKING ACADEMY OF VIETNAM](https://i.imgur.com/4y11111.png)

(Hình ảnh minh họa: Hai nhân vật màu xanh lá cây đang tương tác với một dấu chấm hỏi lớn màu đỏ)

ORACLE
