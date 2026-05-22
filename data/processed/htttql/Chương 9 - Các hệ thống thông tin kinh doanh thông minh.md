# Chương 9 - Các hệ thống thông tin kinh doanh thông minh



<!-- page 1 -->

# HỆ THỐNG THÔNG TIN QUẢN LÝ

GLOBAL EDITION

Using MIS
TENTH EDITION
David M. Kroenke • Randall J. Boyle
Pearson

## Chương 9
## Các hệ thống Kinh doanh thông minh


<!-- page 2 -->

# “Data Analysis, Where You Don’t Know the Second Question to Ask Until You See the Answer to the First One.”

- Having great success with employers interested in tracking exercise data.
- Wants to match users to personal trainers in same locale.
- Earn referral fee.
- How to track them? Mailing address? IP address?
- Got data and Excel to start.
- Serious data mining needs a data mart.


<!-- page 3 -->

# Study Questions

Q9-1 How do organizations use business intelligence (BI) systems?
Q9-2 What are the three primary activities in the BI process?
Q9-3 How do organizations use data warehouses and data marts to acquire data?
Q9-4 How do organizations use reporting applications?
Q9-5 How do organizations use data mining applications?
Q9-6 How do organizations use Big Data applications?
Q9-7 What is the role of knowledge management systems?
Q9-8 What are the alternatives for publishing BI?
Q9-9 2027?


<!-- page 4 -->

# Components of Business Intelligence (BI) Systems

Q9-1 How do organizations use business intelligence (BI) systems?

- Operational DBs
- Social Data
- Purchased Data
- Employee Knowledge
- **Business Intelligence Application**
    - Analyze Data:
        - Reporting
        - Data mining
        - BigData
        - Knowledge management
- Business Intelligence
- Knowledge Workers

Figure 9-1 Components of a Business Intelligence System


<!-- page 5 -->

# How Do Organizations Use BI?

Q9-1 How do organizations use business intelligence (BI) systems?

| **Task** | **ARES Example** | **Falcon Security Example** |
| :--- | :--- | :--- |
| Project Management | Create partnership programs between ARES users and local health clubs. | Expand geographically. |
| Problem Solving | How can we increase revenue from health clubs? | How can we save money by rerouting drone flights? |
| Deciding | Which health club is closest to each user? Refer users to local trainers. | Which drones and related equipment are in need of maintenance? |
| Informing | In what ways are clients using the new system? | How do sales compare to our sales forecast? |

Figure 9-2 Example Uses of Business Intelligence


<!-- page 6 -->

# What Are Typical Uses for BI?

Q9-1 How do organizations use business intelligence (BI) systems?

- Identifying changes in purchasing patterns
  - Important life events change what customers buy.
- Entertainment
  - Netflix has data on watching, listening, and rental habits.
  - Classify customers by viewing patterns.
- **Predictive policing**
  - Analyze data on past crimes - location, date, time, day of week, type of crime, and related data.


<!-- page 7 -->

# Just-in-Time Medical Reporting

Q9-1 How do organizations use business intelligence (BI) systems?

- Example of real time data mining and reporting.
- Injection notification services
    - Software analyzes patient's records; if injections needed, recommends as exam progresses.
- Blurry edge of medical ethics.


<!-- page 8 -->

# Three Primary Activities in the BI Process

Q9-2 What are the three primary activities in the BI process?

**Feedback Results** (vòng lặp từ Publish Results quay lại Data Sources)

**Data Sources**
- Operational databases
- Social data
- Purchased data
- Employee knowledge

**Acquire Data**
- Obtain
- Cleanse
- Organize & relate
- Catalog

**Perform Analysis**
- Reporting
- Data mining
- BigData
- Knowledge management

**Publish Results**
- Print
- Web servers
- Report servers
- Automation

**Knowledge Workers**
- Push
- Pull

Figure 9-3 Three Primary Activities in the BI Process


<!-- page 9 -->

# Using Business Intelligence to Find Candidate Parts at Falcon Security

Q9-2 What are the three primary activities in the BI process?

- Identify parts that might qualify.
    - Provided by vendors who make part design files available for sale.
    - Purchased by larger customers.
    - Frequently ordered parts.
    - Ordered in small quantities.
- Used part weight and price surrogates for simplicity.


<!-- page 10 -->

# Acquire Data: Extracted Order Data

Q9-2 What are the three primary activities in the BI process?

## Query

Sales (CustomerName, Contact, Title, Bill Year, Number Orders, Units, Revenue, Source, PartNumber)

Part (PartNumber, Shipping Weight, Vendor)

| CustomerName | Contact | Title | Bill Year | Number Orders | Units | Revenue | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Island Biking | John Steel | Marketing Manager | 2017 | 10 | 39 | $195.22 | AWS |
| Island Biking | John Steel | Marketing Manager | 2016 | 14 | 59 | $438.81 | Internet |
| Island Biking | John Steel | Marketing Manager | 2016 | 21 | 55 | $255.96 | AWS |
| Island Biking | John Steel | Marketing Manager | 2017 | 4 | 11 | $85.55 | Internet |
| Kona Riders | Renate Messne | Sales Representative | 2014 | 43 | 54 | $349.27 | Internet |
| Kona Riders | Renate Messne | Sales Representative | 2015 | 30 | 53 | $362.45 | Internet |
| Kona Riders | Renate Messne | Sales Representative | 2016 | 1 | 2 | $14.34 | Internet |
| Lone Pine Crafters | Jaime Yorres | Owner | 2017 | 4 | 14 | $108.89 | Internet |
| Lone Pine Crafters | Jaime Yorres | Owner | 2017 | 2 | 2 | $15.56 | Internet |
| Lone Pine Crafters | Jaime Yorres | Owner | 2018 | 2 | 2 | $15.56 | Internet |
| Moab Mauraders | Carlos Gonzále | Accounting Manager | 2017 | 2 | 4 | $4,106.69 | Internet |
| Moab Mauraders | Carlos Gonzále | Accounting Manager | 2017 | 3 | 7 | $7,404.18 | Internet |
| Moab Mauraders | Carlos Gonzále | Accounting Manager | 2017 | 2 | 6 | $6,346.44 | Internet |
| Sedona Mountain Trails | Felipe Izquierc | Owner | 2017 | 6 | 7 | $73.46 | Internet |

Figure 9-4a Sample Extracted Data: Order Extract Table
Source: Microsoft Corporation


<!-- page 11 -->

# Sample Extracted Data: Part Data Table

Q9-2 What are the three primary activities in the BI process?

### Part Data
| ID | PartNumber | Shipping Weight | Vendor | Click to Add |
| :--- | :--- | :--- | :--- | :--- |
| 9 | 200-219 | 7.28 | DePARTures, Inc. | |
| 22 | 200-225 | 3.61 | DePARTures, Inc. | |
| 23 | 200-227 | 5.14 | DePARTures, Inc. | |
| 11 | 200-207 | 9.23 | DePARTures, Inc. | |
| 28 | 200-205 | 4.11 | DePARTures, Inc. | |
| 29 | 200-211 | 4.57 | DePARTures, Inc. | |
| 10 | 200-213 | 1.09 | DePARTures, Inc. | |
| 37 | 200-223 | 3.61 | DePARTures, Inc. | |
| 45 | 200-217 | 1.98 | DePARTures, Inc. | |
| 2 | 200-209 | 10.41 | DePARTures, Inc. | |
| 3 | 200-215 | 1.55 | DePARTures, Inc. | |
| 47 | 200-221 | 10.85 | DePARTures, Inc. | |
| 42 | 200-203 | 3.20 | DePARTures, Inc. | |
| 17 | 300-1007 | 2.77 | Desert Gear Supply | |

Figure 9-4b Sample Extracted Data: Part Data Table
Source: Microsoft Corporation


<!-- page 12 -->

# Analyze Data

Q9-2 What are the three primary activities in the BI process?

**Orders and Parts View**

| Order Extract | Part Data |
| :--- | :--- |
| 🔑 ID | 🔑 ID |
| CustomerName | PartNumber |
| Contact | Shipping Weight |
| Title | Vendor |
| Bill Year | |
| Number Orders | |
| Units | |
| Revenue | |
| Source | |
| PartNumber | |

| Field | Table | Sort | Show | Criteria | or |
| :--- | :--- | :---: | :---: | :--- | :--- |
| Title | Order Extract | | ☑ | | |
| Bill Year | Order Extract | | ☑ | | |
| Number Orders | Order Extract | | ☑ | | |
| Units | Order Extract | | ☑ | | |
| Revenue | Order Extract | | ☑ | | |
| Source | Order Extract | | ☑ | | |
| PartNumber | Part Data | | ☑ | | |
| Shipping Weight | Part Data | | ☑ | | |
| Vendor | Part Data | | ☑ | 'DePARTures, Inc.' Or 'Desert Gear' | |

Figure 9-5 Joining Orders Extract and Filtered *Parts* Tables
Source: Microsoft Corporation


<!-- page 13 -->

# Sample Orders and Parts View Data

Q9-2 What are the three primary activities in the BI process?

### Orders and Parts View

| CustomerName | Contact | Title | Bill Year | Number Orders | Units | Revenue | Source | PartNumber | Shipping Weight | Vendor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gordos Dirt Bikes | Sergio Gutiérrez | Sales Represe | 2011 | 43 | 107 | $26,234.12 | Internet | 100-108 | 3.32 | Riley Manufacturing |
| Island Biking | | | 2012 | 59 | 135 | $25,890.62 | Phone | 500-2035 | 9.66 | ExtremeGear |
| Big Bikes | | | 2010 | 29 | 77 | $25,696.00 | AWS | 700-1680 | 6.06 | HyperTech Manufacturing |
| Lazy B Bikes | | | 2009 | 19 | 30 | $25,576.50 | Internet | 700-2280 | 2.70 | HyperTech Manufacturing |
| Lone Pine Crafters | Carlos Hernández | Sales Represe | 2012 | 1 | 0 | $25,171.56 | Internet | 500-2030 | 4.71 | ExtremeGear |
| Seven Lakes Riding | Peter Franken | Marketing M | 2009 | 15 | 50 | $25,075.00 | Internet | 500-2020 | 10.07 | ExtremeGear |
| Big Bikes | | | 2012 | 10 | 40 | $24,888.00 | Internet | 500-2025 | 10.49 | ExtremeGear |
| B' Bikes | Georg Pipps | Sales Manage | 2012 | 14 | 23 | $24,328.02 | Internet | 700-1680 | 6.06 | HyperTech Manufacturing |
| Eastern Connection | Isabel de Castro | Sales Represe | 2012 | 48 | 173 | $24,296.17 | AWS | 100-105 | 10.73 | Riley Manufacturing |
| Big Bikes | Carine Schmitt | Marketing M | 2009 | 22 | 71 | $23,877.48 | AWS | 500-2035 | 9.66 | ExtremeGear |
| Island Biking | Manuel Pereira | Owner | 2011 | 26 | 45 | $23,588.86 | Internet | 500-2045 | 3.22 | ExtremeGear |
| Mississippi Delta Riding | Rene Phillips | Sales Represe | 2012 | 9 | 33 | $23,550.25 | Internet | 700-2180 | 4.45 | HyperTech Manufacturing |
| Uncle's Upgrades | | | 2012 | 9 | 21 | $22,212.54 | Internet | 700-1680 | 6.06 | HyperTech Manufacturing |
| Big Bikes | | | 2010 | 73 | 80 | $22,063.92 | Phone | 700-1680 | 6.06 | HyperTech Manufacturing |
| Island Biking | | | 2012 | 18 | 59 | $22,025.88 | Internet | 100-108 | 3.32 | Riley Manufacturing |
| Uncle's Upgrades | | | 2011 | 16 | 38 | $21,802.50 | Internet | 500-2035 | 9.66 | ExtremeGear |

Figure 9-6 Sample Orders and Parts View Data
Source: Microsoft Corporation


<!-- page 14 -->

# Creating Customer Summary Query

Q9-2 What are the three primary activities in the BI process?

**Customer Summary**

**Orders and Parts View**
- CustomerName
- Contact
- Title
- Bill Year
- Number Orders
- Units
- Revenue
- Source
- PartNumber
- Shipping Weight
- Vendor

| Field: | CustomerName | Revenue | Units | Average Price: (Sum(Revenue)/Sum(Units)) |
| :--- | :--- | :--- | :--- | :--- |
| Table: | Orders and Parts View | Orders and Parts View | Orders and Parts View | |
| Total: | Group By | Sum | Sum | Expression |
| Sort: | | | | |
| Show: | [x] | [x] | [x] | [x] |
| Criteria: | | | | |
| or: | | | | |

Figure 9-7 Creating the Customer Summary Query
Source: Microsoft Corporation


<!-- page 15 -->

# Customer Summary

Q9-2 What are the three primary activities in the BI process?

| CustomerName | SumOfRevenue | SumOfUnits | Average Price |
| :--- | :--- | :--- | :--- |
| Great Lakes Machines | $1,760.47 | 142 | 12.3976535211268 |
| Seven Lakes Riding | $288,570.71 | 5848 | 49.3451963919289 |
| Around the Horn | $16,669.48 | 273 | 61.0603611721612 |
| Dewey Riding | $36,467.90 | 424 | 86.0092018867925 |
| Moab Mauraders | $143,409.27 | 1344 | 106.7033234375 |
| Gordos Dirt Bikes | $113,526.88 | 653 | 173.854335068913 |
| Mountain Traders | $687,710.99 | 3332 | 206.395855432173 |
| Hungry Rider Off-road | $108,602.32 | 492 | 220.736416056911 |
| Eastern Connection | $275,092.28 | 1241 | 221.669848186946 |
| Mississippi Delta Riding | $469,932.11 | 1898 | 247.593315542676 |
| Island Biking | $612,072.64 | 2341 | 261.457770098249 |

Figure 9-8 Customer Summary
Source: Microsoft Corporation


<!-- page 16 -->

# Qualifying Parts Query Design

Q9-2 What are the three primary activities in the BI process?

**Qualifying Parts**
- **Big Customers**
    - CustomerName
- **Orders and Parts View**
    - CustomerName
    - Contact
    - Title
    - Bill Year
    - Number Orders
    - Units
    - Revenue
    - Source
    - PartNumber
    - Shipping Weight
    - Vendor

| Field | Number Orders | Average Order Size: [Units]/[Number Orders] | Unit Price: [Revenue]/[Units] | Shipping Weight | PartNumber |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Table | Orders and Parts View | | | Orders and Parts View | Orders and Parts View |
| Sort | | | | | |
| Show | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Criteria | >50 | <2.5 | <100 | <5 | |

Figure 9-9 Qualifying Parts Query Design
Source: Microsoft Corporation


<!-- page 17 -->

# Publish Results: Qualifying Parts Query Results

Q9-2 What are the three primary activities in the BI process?

### Qualifying Parts

| Number Orders | Average Order Size | Unit Price | Shipping Weight | PartNumber |
| :--- | :--- | :--- | :--- | :--- |
| 275 | 1 | 9.14173854545455 | 4.14 | 300-1016 |
| 258 | 1.87596899224806 | 7.41284524793388 | 4.14 | 300-1016 |
| 110 | 1.18181818181818 | 6.46796923076923 | 4.11 | 200-205 |
| 176 | 1.66477272727273 | 12.5887211604096 | 4.14 | 300-1016 |
| 139 | 1.0431654676259 | 6.28248965517241 | 1.98 | 200-217 |
| 56 | 1.83928571428571 | 6.71141553398058 | 1.98 | 200-217 |
| 99 | 1.02020202020202 | 7.7775 | 3.20 | 200-203 |
| 76 | 2.17105263157895 | 12.0252206060606 | 2.66 | 300-1013 |

Figure 9-10 Qualifying Parts Query Results
Source: Microsoft Corporation


<!-- page 18 -->

# Publish Results: Sales History for Selected Parts

Q9-2 What are the three primary activities in the BI process?

### Revenue Potential
| Total Orders | Total Revenue | PartNumber |
| :--- | :--- | :--- |
| 3987 | $84,672.73 | 300-1016 |
| 2158 | $30,912.19 | 200-211 |
| 1074 | $23,773.53 | 200-217 |
| 548 | $7,271.31 | 300-1007 |
| 375 | $5,051.62 | 200-203 |
| 111 | $3,160.86 | 300-1013 |
| 139 | $1,204.50 | 200-205 |

Figure 9-11 Sales History for Selected Parts
Source: Microsoft Corporation


<!-- page 19 -->

# MIS-Diagnosis
Ethics Guide

- Doctors are relying more and more on artificial intelligence (AI)-driven expert systems to select the most appropriate medications and treatments.
- Ordered to improve the system’s “perception” of the company’s drugs.
- Minor modifications to the drug’s profile made a big difference.
    - But some of the numbers he used to modify the profile were *not* accurate.
    - The changes would warrant a *regulatory review*.


<!-- page 20 -->

# MIS-Diagnosis (cont'd)

Ethics Guide

- Suppose the company alters the drug profile.
- Would the company be liable if something happened to a patient who took the drug based on *altered* information?
- Do you think that manipulating the recommendation of an AI system even though the new recommendation may be for the better drug is ethical according to the categorical imperative, and utilitarian perspective?


<!-- page 21 -->

# Using Data Warehouses and Data Marts to Acquire Data

Q9-3 How do organizations use data warehouses and data marts to acquire data?

## Functions of a data warehouse
- Obtain data from operational, internal and external databases.
- Cleanse data.
- Organize and relate data.
- Catalog data using metadata.


<!-- page 22 -->

# Components of a Data Warehouse

Q9-3 How do organizations use data warehouses and data marts to acquire data?

- Operational Databases
- Other Internal Data
- External Data
- Data Extraction/ Cleaning/ Preparation Programs
- Data Warehouse Metadata
- Data Warehouse Database
- Data Warehouse DBMS
- Business Intelligence Tools
- Business Intelligence Users

Figure 9-12 Components of a Data Warehouse


<!-- page 23 -->

# Examples of Consumer Data That Can Be Purchased

Q9-3 How do organizations use data warehouses and data marts to acquire data?

- Name, address, phone
- Age
- Gender
- Ethnicity
- Religion
- Income
- Education
- Voter registration
- Home ownership
- Vehicles
- Magazine subscriptions
- Hobbies
- Catalog orders
- Marital status, life stage
- Height, weight, hair and eye color
- Spouse name, birth date
- Children's names and birth dates

Figure 9-13 Examples of Consumer Data That Can Be Purchased


<!-- page 24 -->

# Possible Problems with Source Data

Q9-3 How do organizations use data warehouses and data marts to acquire data?

- Dirty data
- Missing values
- Inconsistent data
- Data not integrated
- Wrong granularity
    - Too fine
    - Not fine enough
- Too much data
    - Too many attributes
    - Too many data points

Figure 9-14 Possible Problems with Source Data


<!-- page 25 -->

# Data Warehouses Versus Data Marts

Q9-3 How do organizations use data warehouses and data marts to acquire data?

**Diagram Components:**

- **Data Producers** $\rightarrow$ Data Warehouse DBMS
- **Data Warehouse Metadata** $\rightarrow$ Data Warehouse DBMS
- **Data Warehouse Database** $\rightarrow$ Data Warehouse DBMS
- **Data Warehouse DBMS** $\rightarrow$
    - **Web Sales Data Mart**: Web Log Data $\leftrightarrow$ BI tools for Web clickstream analysis $\rightarrow$ Web page design features
    - **Store Sales Data Mart**: Store Sales Data $\leftrightarrow$ BI tools for store management $\rightarrow$ Market-basket analysis for sales training
    - **Inventory Data Mart**: Inventory History Data $\leftrightarrow$ BI tools for inventory management $\rightarrow$ Inventory layout for optimal item picking

Figure 9-15 Data Mart Examples


<!-- page 26 -->

# Reporting Applications

Q9-4 How do organizations use reporting applications?

- Create meaningful information from disparate data sources.
- Deliver information to user on time.
- Basic operations:
    1. Sorting
    2. Filtering
    3. Grouping
    4. Calculating
    5. Formatting


<!-- page 27 -->

# RFM Analysis: Example RFM Scores

Q9-4 How do organizations use reporting applications?

- How **recently** (R) a customer has ordered
- How **frequently** (F) a customer ordered
- How much **money** (M) the customer has spent

| Customer | RFM Score |
| :--- | :--- |
| Big 7 Sports | 1 1 3 |
| St. Louis Soccer Club | 5 1 1 |
| Miami Municipal | 5 4 5 |
| Central Colorado State | 3 3 3 |

Figure 9-16 Example RFM Scores


<!-- page 28 -->

# RFM Analysis Classification Scheme

Q9-4 How do organizations use reporting applications?

- To produce an RFM score:
    - Sort customer purchase records by date of most recent (R) purchase.
    - Divide sorts into quintiles.
    - Give customers a score of 1 to 5.
- Process is repeated for Frequently and Money.

(Pyramid Diagram)
- Top 20%: 5
- 4
- Middle 20%: 3
- 2
- Bottom 20%: 1


<!-- page 29 -->

# Example of Grocery Sales OLAP Report

Q9-4 How do organizations use reporting applications?

- OLAP Product Family by Store Type
- http://www.tableausoftware.com

| Store Sales Net / Store Type | Deluxe Supermarket | Gourmet Supermarket | Mid-Size Grocery | Small Grocery | Supermarket | Grand Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Product Family** | | | | | | |
| Drink | $8,119.05 | $2,392.83 | $1,409.50 | $685.89 | $16,751.71 | $29,358.98 |
| Food | $70,276.11 | $20,026.18 | $10,392.19 | $6,109.72 | $138,960.67 | $245,764.87 |
| Non-Consumable | $18,884.24 | $5,064.79 | $2,813.73 | $1,534.90 | $36,189.40 | $64,487.05 |
| **Grand Total** | $97,279.40 | $27,483.80 | $14,615.42 | $8,330.51 | $191,901.77 | $339,610.90 |

Figure 9-17 Example Grocery Sales OLAP Report
Source: Microsoft Corporation


<!-- page 30 -->

# Example of Expanded Grocery Sales OLAP Report

Q9-4 How do organizations use reporting applications?

- **Drilling down**

| | Product Family | Store Country | Store State | Deluxe Superma | Gourmet Supermar | Supermar | Mid-Size Groce | Small Grocery | Supermarket | Grand Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | **Store Sales Net** | | | **Store Type** | | | | | | |
| 4 | Product Family | Store Country | Store State | Deluxe Superma | Gourmet Supermar | Supermar | Mid-Size Groce | Small Grocery | Supermarket | Grand Total |
| 5 | Drink | USA | CA | | | $2,392.83 | | $227.38 | $5,920.76 | $8,540.97 |
| 6 | | | OR | $4,438.49 | | | | | $2,862.45 | $7,300.94 |
| 7 | | | WA | $3,680.56 | | | $1,409.50 | $458.51 | $7,968.50 | $13,517.07 |
| 8 | | USA Total | | $8,119.05 | | $2,392.83 | $1,409.50 | $685.89 | $16,751.71 | $29,358.98 |
| 9 | Drink Total | | | $8,119.05 | | $2,392.83 | $1,409.50 | $685.89 | $16,751.71 | $29,358.98 |
| 10 | Food | USA | CA | | | $20,026.18 | | $1,960.53 | $47,226.11 | $69,212.82 |
| 11 | | | OR | $37,778.35 | | | | | $23,818.87 | $61,597.22 |
| 12 | | | WA | $32,497.76 | | | $10,392.19 | $4,149.19 | $67,915.69 | $114,954.83 |
| 13 | | USA Total | | $70,276.11 | | $20,026.18 | $10,392.19 | $6,109.72 | $138,960.67 | $245,764.87 |
| 14 | Food Total | | | $70,276.11 | | $20,026.18 | $10,392.19 | $6,109.72 | $138,960.67 | $245,764.87 |
| 15 | Non-Consumable | USA | CA | | | $5,064.79 | | $474.35 | $12,344.49 | $17,883.63 |
| 16 | | | OR | $10,177.89 | | | | | $8,428.53 | $16,606.41 |
| 17 | | | WA | $8,706.36 | | | $2,813.73 | $1,060.54 | $17,416.38 | $29,997.01 |
| 18 | | USA Total | | $18,884.24 | | $5,064.79 | $2,813.73 | $1,534.90 | $36,189.40 | $64,487.05 |
| 19 | Non-Consumable Total | | | $18,884.24 | | $5,064.79 | $2,813.73 | $1,534.90 | $36,189.40 | $64,487.05 |
| 20 | Grand Total | | | $97,279.40 | | $27,483.80 | $14,615.42 | $8,330.51 | $191,901.77 | $339,610.90 |

Figure 9-18 Example of Expanded Grocery Sales OLAP Report
Source: Microsoft Corporation


<!-- page 31 -->

# Example of Drilling Down into Expanded Grocery Sales OLAP Report

Q9-4 How do organizations use reporting applications?

| Store Country | Store Sta | Store City | Product Family | Deluxe Super | Gourmet Supermarket | Mid-Size Grocery | Small Grocery | Supermarket | Grand Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| USA | CA | Beverly Hills | Drink | | $2,392.83 | | | | $2,392.83 |
| | | | Food | | $20,026.18 | | | | $20,026.18 |
| | | | Non-Consumable | | $5,064.79 | | | | $5,064.79 |
| | | Beverly Hills Total | | | $27,483.80 | | | | $27,483.80 |
| | | Los Angeles | Drink | | | | | $2,870.33 | $2,870.33 |
| | | | Food | | | | | $23,598.28 | $23,598.28 |
| | | | Non-Consumable | | | | | $6,305.14 | $6,305.14 |
| | | Los Angeles Total | | | | | | $32,773.74 | $32,773.74 |
| | | San Diego | Drink | | | | | $3,050.43 | $3,050.43 |
| | | | Food | | | | | $23,627.83 | $23,627.83 |
| | | | Non-Consumable | | | | | $6,039.34 | $6,039.34 |
| | | San Diego Total | | | | | | $32,717.61 | $32,717.61 |
| | | San Francisco | Drink | | | | $227.38 | | $227.38 |
| | | | Food | | | | $1,960.53 | | $1,960.53 |
| | | | Non-Consumable | | | | $474.35 | | $474.35 |
| | | San Francisco Total | | | | | $2,662.26 | | $2,662.26 |
| | CA Total | | | | $27,483.80 | | $2,662.26 | $65,491.35 | $95,637.41 |
| | OR | | Drink | $4,438.49 | | | | $2,862.45 | $7,300.94 |
| | | | Food | $37,778.35 | | | | $23,818.87 | $61,597.22 |
| | | | Non-Consumable | $10,177.89 | | | | $6,428.53 | $16,606.41 |
| | OR Total | | | $52,394.72 | | | | $33,109.85 | $85,504.57 |
| | WA | Drink | $3,680.56 | | $1,409.50 | $458.51 | $7,968.50 | $13,517.07 |
| | | Food | $32,497.76 | | $10,392.19 | $4,149.19 | $67,915.69 | $114,954.83 |
| | | Non-Consumable | $8,706.36 | | $2,813.73 | $1,060.54 | $17,416.38 | $29,997.01 |
| | WA Total | | | $44,884.68 | | $14,615.42 | $5,668.24 | $93,300.57 | $158,468.91 |
| USA Total | | | | $97,279.40 | $27,483.80 | $14,615.42 | $8,330.51 | $191,901.77 | $339,610.90 |
| Grand Total | | | | $97,279.40 | $27,483.80 | $14,615.42 | $8,330.51 | $191,901.77 | $339,610.90 |

Figure 9-19 Example of Drilling Down into Expanded Grocery Sales OLAP Report
Source: Microsoft Corporation


<!-- page 32 -->

# Convergence of Disciplines

Q9-5 How do organizations use data mining applications?

- Statistics/ Mathematics $\rightarrow$ **Data Mining**
- Artificial Intelligence Machine Learning $\rightarrow$ **Data Mining**
- Huge Databases $\rightarrow$ **Data Mining**
- Cheap Computer Processing and Storage $\rightarrow$ **Data Mining**
- Sophisticated Marketing, Finance, and Other Business Professionals $\rightarrow$ **Data Mining**
- Data Management Technology $\rightarrow$ **Data Mining**

Figure 9-20 Source Disciplines of Data Mining


<!-- page 33 -->

# Unsupervised Data Mining

Q9-5 How do organizations use data mining applications?

- No a priori hypothesis or model.
- Findings obtained solely by data analysis.
- Hypothesized model created to explain patterns found.
- Example: Cluster analysis.


<!-- page 34 -->

# Supervised Data Mining

Q9-5 How do organizations use data mining applications?

- Uses a priori model.
- Prediction, such as regression analysis.
- Ex: CellPhoneWeekendMinutes
  $= (12 + (17.5 * \text{CustomerAge}) + (23.7 * \text{NumberMonthsOfAccount}))$
  $= 12 + 17.5 * 21 + 23.7 * 6 = \mathbf{521.7 \text{ minutes}}$


<!-- page 35 -->

# Market-Basket Analysis

Q9-5 How do organizations use data mining applications?

- **Market-basket analysis**
    - Identify sales patterns in large volumes of data.
    - Identify what products customers tend to buy together.
    - Computes probabilities of purchases.
    - Identify cross-selling opportunities.
        - Customers who bought fins also bought a mask.


<!-- page 36 -->

# Market-Basket Example: Dive Shop
## Transactions = 400

Q9-5 How do organizations use data mining applications?

| | Mask | Tank | Fins | Weights | Dive Computer |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mask** | | 270 | 10 | 250 | 10, 90 |
| **Tank** | 10 | 200 | 40 | 130 | 30 |
| **Fins** | 250 | 40 | 280 | 20 | 20 |
| **Weights** | 10 | 130 | 130 | 10 | 10 |
| **Dive Computer** | 90 | 30 | 20 | 10 | 120 |

**Support**
| | Mask | Tank | Fins | Weights | Dive Computer |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mask** | | 0.675 | 0.025 | 0.625 | 0.025, 0.225 |
| **Tank** | | 0.5 | 0.1 | | 0.325, 0.075 |
| **Fins** | 0.625 | 0.1 | 0.7 | 0.05 | 0.05 |
| **Weights** | 0.025 | 0.325 | | 0.325 | 0.025 |
| **Dive Computer** | 0.225 | 0.075 | 0.05 | 0.025 | 0.3 |

**Confidence**
| | Mask | Tank | Fins | Weights | Dive Computer |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mask** | | 1 | 0.05 | 0.892857143 | 0.076923077, 0.75 |
| **Tank** | 0.037037037 | 1 | 0.142857143 | 1 | 0.25 |
| **Fins** | 0.925925926 | 0.2 | 1 | 0.153846154 | 0.166666667 |
| **Weights** | 0.037037037 | 0.65 | 0.071428571 | 1 | 0.083333333 |
| **Dive Computer** | 0.333333333 | 0.15 | 0.071428571 | 0.076923077 | 1 |

**Lift (Improvement)**
| | Mask | Tank | Fins | Weights | Dive Computer |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mask** | | 0.074074074 | 1.322751323 | 0.113960114 | 1.111111111 |
| **Tank** | 0.074074074 | 2 | | 2 | 0.5 |
| **Fins** | 1.322751323 | 0.285714286 | | 0.21978022 | 0.238095238 |
| **Weights** | 0.113960114 | 2 | 0.21978022 | | 0.256410256 |
| **Dive Computer** | 1.111111111 | 0.5 | 0.238095238 | 0.256410256 | |

Figure 9-21 Market-Basket Analysis at a Dive Shop
Source: Microsoft Corporation


<!-- page 37 -->

# Decision Trees

Q9-5 How do organizations use data mining applications?

- Unsupervised data mining technique.
- Hierarchical arrangement of criteria to predict a value or classification.
- Basic idea
    - Select attributes most useful for classifying “pure groups.”
    - Creates decision rules.


<!-- page 38 -->

# Credit Score Decision Tree

Q9-5 How do organizations use data mining applications?

**Classification Tree (2) - Status**
File Tree Dendrogram Help

- root 3485 [0.72 0.28 ]
    - PeroPastDue < 0.50 2574 [0.94 0.06 ]
        - CreditScore >= 654.42 2244 [0.98 0.02 ]
        - CreditScore < 654.42 330 [0.67 0.33 ]
            - MonthsPastDue < 0.50 253 [0.81 0.19 ]
            - MonthsPastDue >= 0.50 77 [0.22 0.78 ]
    - PeroPastDue >= 0.50 911 [0.11 0.89 ]
        - CreditScore >= 572.60 135 [0.42 0.58 ]
            - CurrentLTV < 0.94 89 [0.58 0.42 ]
            - CurrentLTV >= 0.94 46 [0.11 0.89 ]
        - CreditScore < 572.60 776 [0.05 0.95 ]
            - CreditScore >= 470.17 222 [0.14 0.86 ]
                - MonthsPastDue < 0.50 103 [0.24 0.76 ]
                - MonthsPastDue >= 0.50 119 [0.04 0.96 ]
            - CreditScore < 470.17 554 [0.02 0.98 ]

**Classes:**
- No Default
- Default

**Show Text:**
- [x] Split Decision
- [ ] Score
- [ ] Number Records
- [ ] Misclassifications
- [ ] Entropy
- [x] Probabilities

**CLASSIFICATION TREE MODEL: "Status" (1 tree)**
**NUMBER OBSERVATIONS: 3485**
**CURRENT TREE: 1**

View Level: < >

Figure 9-22 Credit Score Decision Tree
Source: Used with permission of TIBCO Software Inc. Copyright © 1999-2005 TIBCO Software Inc. All rights reserved.


<!-- page 39 -->

# Decision Rules for Accepting or Rejecting Offer to Purchase Loans

Q9-5 How do organizations use data mining applications?

- If percent past due is less than 50 percent, then accept loan.
    - If percent past due is greater than 50 percent **and**
    - If *CreditScore* is greater than 572.6 **and**
    - If *CurrentLTV* is less than .94, then accept loan.
- Otherwise, reject loan.


<!-- page 40 -->

# BI for Securities Trading?

So What?

- Quantitative applications using Big Data and BI.
    - Analyze immense amounts of data over a broad spectrum of sources.
    - Build and evaluate investment strategies.
- Two Sigma (www.twosigma.com)
    - Analyzes financial statements, developing news, Twitter activity, weather reports, other sources.
    - Develops and tests investment strategies.


<!-- page 41 -->

# Two Sigma's Five-Step Process

Q9-5 How do organizations use data mining applications?

1. Acquire data
2. Create models
3. Evaluate models
4. Analyze risks
5. Place trades

- Does it work? Two Sigma and other firms claim it does.


<!-- page 42 -->

# Using Big Data Applications

Q9-6 How do organizations use Big Data applications?

- Huge volume – petabyte and larger.
- Rapid velocity – generated rapidly.
- Great variety
  - Structured data, free-form text, log files, graphics, audio, and video.


<!-- page 43 -->

# MapReduce Processing Summary

Q9-6 How do organizations use Big Data applications?

- **Map Phase: Google search log broken into thousands of pieces**

| Search log: | Log segments: | Map Phase | Reduce Phase |
| :--- | :--- | :--- | :--- |
| Halon; Wolverine;<br>Abacus; Poodle; Fence;<br>Acura; Healthcare;<br>Cassandra; Belltown;<br>Hadoop; Geranium;<br>Stonework; Healthcare;<br>Honda; Hadoop;<br>Congress; Healthcare;<br>Frigate; Metric; Clamp;<br>Dell; Salmon; Hadoop;<br>Picasso; Abba; | $\rightarrow$ Processor 1 $\rightarrow$ | | |
| | $\rightarrow$ Processor 2 $\rightarrow$ | | |
| | $\rightarrow$ Processor 9,555 (+ or -) $\rightarrow$ | | |

**Intermediate Results (Map Phase Output):**

| Processor 1 | | Processor 2 | | Processor 9,555 | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Hadoop | 14 | Hadoop | 3 | Halon | 11 |
| Healthcare | 85 | Healthcare | 2 | Hotel | 175 |
| Hiccup | 17 | Honda | 1 | Honda | 87 |
| Hurricane | 8 | | | Hurricane | 53 |

**Keyword: Total Count (Reduce Phase Output):**

| Keyword | Total Count |
| :--- | :--- |
| Hadoop | 10,418 |
| Halon | 4,788 |
| Healthcare | 12,487,318 |
| Hiccup | 7,435 |
| Honda | 127,489 |
| Hotel | 237,654 |
| Hurricane | 2,799 |

Figure 9-23 MapReduce Processing Summary


<!-- page 44 -->

# Google Trends on the Term Web 2.0

Q9-6 How do organizations use Big Data applications?

Compare Search terms
- hadoop Search term
- web 2.0 Search term
- + Add term

Interest over time
- News headlines
- Forecast
- Average
- 2005
- 2007
- 2009
- 2011
- 2013
- 2015

Figure 9-24 Google Trends on the Terms Web 2.0 and Hadoop
Source: Google and the Google logo are registered trademarks of Google Inc., Used with permission.


<!-- page 45 -->

# Hadoop

Q9-6 How do organizations use Big Data applications?

- Open-source program supported by Apache Foundation2.
- Manages thousands of computers.
- Implements MapReduce.
    - Written in Java.
- Amazon.com supports Hadoop as part of EC3 cloud.
- Query language entitled Pig (platform for large dataset analysis).
    - Easy to master.
    - Extensible.
    - Automatically optimizes queries on map-reduce level.


<!-- page 46 -->

# Knowledge Management Systems

Q9-7 What is the role of knowledge management systems?

- Knowledge Management (KM)
    - Creating value from intellectual capital and sharing knowledge with those who need that capital.
- Preserving organizational memory
    - Capturing and storing lessons learned and best practices of key employees.
- Scope of KM same as SM in hyper-social organizations.


<!-- page 47 -->

# Benefits of Knowledge Management

Q9-7 What is the role of knowledge management systems?

- Improve process quality.
- Increase team strength.
- Goal:
    - Enable employees to use organization's collective knowledge.


<!-- page 48 -->

# What Are Expert Systems?

Q9-7 What is the role of knowledge management systems?

- **Expert systems**
    - Rule-based IF/THEN
    - Encode human knowledge
- **Expert systems shells**
    - Process IF side of rules
    - Report values of all variables
    - Knowledge gathered from human experts


<!-- page 49 -->

# Example of IF/THEN Rules

Q9-7 What is the role of knowledge management systems?

Other rules here...

IF CardiacRiskFactor = 'Null' THEN Set CardiacRiskFactor = 0
IF PatientSex = 'Male' THEN Add 3 to CardiacRiskFactor
IF PatientAge >55 THEN Add 2 to CardiacRiskFactor
IF FamilyHeartHistory = 'True' THEN Add 5 to CardiacRiskFactor
IF CholesterolScore = 'Problematic' THEN Add 4 to CardiacRiskFactor
IF BloodPressure = 'Problematic' THEN Add 3 to CardiacRiskFactor
IF CardiacRiskFactor >15 THEN Set EchoCardiagramTest = 'Schedule'
...
Other rules here...

Figure 9-25 Example of If/Then Rules


<!-- page 50 -->

# Drawbacks of Expert Systems

Q9-7 What is the role of knowledge management systems?

1. Difficult and expensive to develop.
    - Labor intensive.
    - Ties up domain experts.
2. Difficult to maintain.
    - Changes cause unpredictable outcomes.
    - Constantly need expensive changes.
3. Don’t live up to expectations.
    - Can’t duplicate diagnostic abilities of humans.


<!-- page 51 -->

# What Are Content Management Systems (CMS)?

Q9-7 What is the role of knowledge management systems?

- Support management and delivery of documents, other expressions of employee knowledge.
- Challenges of Content Management
    - Huge databases.
    - Dynamic content.
    - Documents refer to one another.
    - Perishable contents.
    - In many languages.


<!-- page 52 -->

# What are CMS Application Alternatives?

Q9-7 What is the role of knowledge management systems?

- In-house custom development
    - Customer support develops in-house database applications to track customer problems.
- Off-the-shelf
    - Horizontal market products (SharePoint).
    - Vertical market applications.
- Public search engine
    - Google, Bing.


<!-- page 53 -->

# How Do Hyper-Social Organizations Manage Knowledge?

Q9-7 What is the role of knowledge management systems?

- **Hyper-social knowledge management**
    - Social media, and related applications, for management and delivery of organizational knowledge resources.
- **Hyper-organization theory**
    - Framework for understanding KM.
    - Focus shifts from knowledge and content to fostering authentic relationships among knowledge creators and users.


<!-- page 54 -->

# Hyper-Social KM Media

Q9-7 What is the role of knowledge management systems?

| Media | Public or Private | Best for: |
| :--- | :--- | :--- |
| Blogs | Either | Defender of belief |
| Discussion groups (including FAQ) | Either | Problem solving |
| Wikis | Either | Either |
| Surveys | Either | Problem solving |
| Rich directories (e.g. Active Directory) | Private | Problem solving |
| Standard SM (Facebook, Twitter, etc.) | Public | Defender of belief |
| YouTube | Public | Either |

Figure 9-27 Hyper-Social KM Media


<!-- page 55 -->

# Resistance to Knowledge Sharing

Q9-7 What is the role of knowledge management systems?

- Employees reluctant to exhibit their ignorance.
- Employee competition.
- Remedy
    - Strong management endorsement.
    - Strong positive feedback.
    - “Nothing wrong with praise or cash . . . especially cash.”


<!-- page 56 -->




<!-- page 57 -->

# What Are the Two Functions of a BI Server?

Q9-8 What are the alternatives for publishing BI?

- **Management and delivery**

**BI System**
- **BI Application**
    - **BI Data Source**
        - Operational data
        - Data warehouse
        - Data mart
        - Content material
        - Human interviews
    - **BI Application**
        - RFM
        - OLAP
        - Other reports
        - Market basket
        - Decision tree
        - Other data mining
        - Content indexing
        - RSS feed
        - Expert system
    - **BI Application Result**
- **Metadata** (connected to BI Server)
- **BI Server** (Push/Pull)
- **"Any" Device**
    - Computer
    - Mobile devices
    - Office and other applications
    - Cloud services to anything...
- **BI users**

Figure 9-29 Elements of a BI System


<!-- page 58 -->

# Business Intelligence Systems in 2027

Q9-9 2027?

- Exponentially more information about customers, better data mining techniques.
- Companies buy and sell your purchasing habits and psyche.
- **Singularity**
    - Computer systems adapt and create their own software without human assistance.
    - Machines will possess and create information for themselves.
    - Will we know what the machines will know?


<!-- page 59 -->

# Semantic Security
Security Guide

1. Unauthorized access to protected data and information.
    - Physical security
        - Passwords and permissions.
        - Delivery system must be secure.
2. Unintended release of protected information through reports and documents.
3. What, if anything, can be done to prevent what Megan did?


<!-- page 60 -->

# Manager, Data and Analytics
Career Guide

## Lindsey Tsuya at American Express Company

**Q. What attracted you to this field?**
A. “As a college student, I worked in the service industry. When I was selecting my degree, I knew I wanted two things. First, I wanted a degree that made money. Second, I wanted a job that did not involve direct provision of service to the public. By choosing information systems, I knew I would be doing more of a behind-the-scenes job.”

**Q. What advice would you give to someone who is considering working in your field?**
A. “No matter what field you choose, make sure it is something you are passionate about because if you are not passionate about it, work will feel like... work.”


<!-- page 61 -->

# Active Review

Q9-1 How do organizations use business intelligence (BI) systems?
Q9-2 What are the three primary activities in the BI process?
Q9-3 How do organizations use data warehouses and data marts to acquire data?
Q9-4 How do organizations use reporting applications?
Q9-5 How do organizations use data mining applications?
Q9-6 How do organizations use Big Data applications?
Q9-7 What is the role of knowledge management systems?
Q9-8 What are the alternatives for publishing BI?
Q9-9 2027?


<!-- page 62 -->

# Hadoop the Cookie Cutter

Case Study 9

- **Third-party cookie** created by site other than one you visited.
- Most commonly occurs when a Web page includes content from multiple sources.
- **DoubleClick**
    - IP address where content was delivered.
        - DoubleClick instructs your browser to store a DoubleClick cookie.
    - Records data in cookie log on DoubleClick’s server.


<!-- page 63 -->

# Hadoop the Cookie Cutter (cont’d)

Case Study 9

- Third-party cookie owner has history of what was shown, what ads you clicked, and intervals between interactions.
- Cookie log shows how you respond to ads and your pattern of visiting various Web sites where ads placed.
- **Firefox Lightbeam** tracks and graphs cookies on your computer.


<!-- page 64 -->

# FireFox Lightbeam: Display on Start Up

Case Study 9

- **No cookies on startup.**

![Hình ảnh minh họa giao diện Lightbeam]

**Figure 9-30a Third-Party Cookie Growth**
Source: © Mozilla Corporation


<!-- page 65 -->

# After Visiting MSN.com

Case Study 9

- After MSN.com and Gmail.

[Hình ảnh hiển thị giao diện phần mềm Lightbeam for Firefox]

**Figure 9-30b Third-Party Cookie Growth**
Source: © Mozilla Corporation


<!-- page 66 -->

# 5 Sites Visited Yields 27 Third Parties

Case Study 9

- **Five sites visited yield 27 third parties.**

[Hình ảnh minh họa giao diện phần mềm Lightbeam for Firefox]

Figure 9-30c Third-Party Cookie Growth
Source: © Mozilla Corporation


<!-- page 67 -->

# Sites Connected to DoubleClick

Case Study 9

- **Sites connected to DoubleClick.**

![Hình ảnh minh họa: Giao diện phần mềm Lightbeam cho Firefox hiển thị biểu đồ các trang web kết nối với doubleclick.net]

**Figure 9-30d Third-Party Cookie Growth**
Source: © Mozilla Corporation
