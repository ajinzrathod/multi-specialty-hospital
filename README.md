# Multi Specialty Hospital

I own a multi-specialty hospital chain with locations all across the world. My hospital is famous for
vaccinations. Patients who come to my hospital (across the globe) will be given a user card with
which they can access any of my hospitals in any location.

## The Problem

We maintain all customers in one database. There are heaps of customers who have user cards. So, I
decided to split up the customers based on the country and load them into corresponding country
tables.

To pull customers by country, my developers should know where all the Customer Data is available.
So, the data extracting will be done by our Source System. They will pull all the relevant customer
data and will give us a pipe delimited data file.

In design documents, you will have:

| File Position | Column Name         | Field Length | Data Type | Mandatory | Key Column |
|---------------|---------------------|--------------|-----------|-----------|------------|
| 1             | Customer Name       | 255          | VARCHAR   | Y         | N          |
| 2             | Customer ID         | 18           | VARCHAR   | Y         | Y          |
| 3             | Customer Open Date  |              | DATE      | Y         | N          |
| 4             | Last Consulted Date |              | DATE      | N         | N          |
| 5             | Vaccination Type    | 5            | VARCHAR   | N         | N          |
| 6             | Doctor Consulted    | 255          | VARCHAR   | N         | N          |
| 7             | State               | 5            | VARCHAR   | N         | N          |
| 8             | Country             | 5            | VARCHAR   | N         | N          |
| 9             | Post Code           | 5            | INTEGER   | N         | N          |
| 10            | Date of Birth       |              | DATE      | N         | N          |
| 11            | Active Customer     | 1            | CHAR      | N         | N          |


**The sample file format will be:**

H|Customer_Name|CustomerID|CustomerOpenDate|LastConsultedDate|VaccinationType|Doctor|State|Country|PostCode|DateofBirth|ActiveCustomer
D|Yael|1|20101012|20121013|sput5|Piper Sheppard|Lange|Peru|75532|06031987|A
D|Xaviera|2|20101112|20210329|sput5|Savannah Keith|Sint|Peru|3604|26011999|A
D|Matthew|3|20100323|20160202|sput5|Justin Leblanc|Marlb|Peru|18518|17121996|A
D|Alec|4|20210101|20220305|sput5|Colin Hodge|Eindh|Nepal|19167|15031966|A
D|Ethan|5|20200505|20210814|sput5|Charlotte Campbell|Keumi|Nepal|Z4730|27061959|A
D|Macey|6|20150518|20190808|mvd|Garrison Mosley|Salci|Peru|87049|17081971|A
D|Angelica|7|20171214|20171214|covix|TaShya Mendez|Perth|india|61188|11082000|A
D|April|8|20190126|20201231|covix|Amal Gray|Burin|India|96896|24071999|A
D|Nissim|9|20181130|20181201|mvd|Chelsea Farmer|Masca|Nepal|09666|03101928|A
T|9|


**Output:**

Any script or program which reads the data from files which will load the data into tables, one table per country.

## How to use it?

1. Clone the repository
    ```
    git clone https://github.com/ajinzrathod/multi-specialty-hospital.git
    ```
2. Go to cloned directory and Install virtual Environment
    
    ```
    python3 -m venv venv
    ```
3. Activate Virtual Environment

    **For Linux and Mac:**
    ```
    source venv/bin/activate
    ```
    
    **For Windows:**
    ```
    source .\venv\Scripts\activate
    ```

4. Install Requirements
* If you want to use it with jupyter-notebook, use this command:
    
    ```
    pip install -r requirements.txt
    ```
    
    **OR**
* If you want to use it just using terminal, use this command:
    
    ```
    pip install -r requirements-before-jupyterLab.txt
    ```

### Things to know before you create database

There are 2 folders:
1. **Database-independent**
  * Scripts in this folder will create Tables in **Any Database**. You just have to change the connection string which is also  given below:
2. **For-mysql**
  * Script is this folder is solely made for **MySql** as it was asked in question to make "**Create table queries**". So we have created a procedure named `createCountryTable` inside `create-table-stored-procedure.sql` file which can also be found in same directory. 
    
    **Connection String:**
    ```
    engine = create_engine("mysql+mysqlconnector://root:password@localhost/" + db)
    ```
    Here, `root` is the **username** and `password` is the **password**.
    *Edit the connection String according to your database configuration.*

### After updating connection String

* You need to create a Database named `incubyte`
* Now open your **Terminal** or **Command Line**
* Go to **database-independent** directory or **for-mysql** directory as per your need.
* Now run the code using this command: `python index.py`


### Screenshots

![Tree](https://github.com/ajinzrathod/multi-specialty-hospital/blob/main/screenshots/after-loading-in-database.png?raw=true)
<p align="center"> Database after loading tables from txt file </p>

----

![Tree](https://github.com/ajinzrathod/multi-specialty-hospital/blob/main/screenshots/when-table-does-not-exists.png?raw=true)
<p align="center"> When country table does NOT exists already </p>

----

![Tree](https://github.com/ajinzrathod/multi-specialty-hospital/blob/main/screenshots/when-table-exists.png?raw=true)
<p align="center"> When country table already exists </p>

## Other Details
**Python Version:** 3.8.10

**NOTE**: We could remove `country` column from each country table. But considering a scenario when we want to merge all the data in one table. This would be a easy approach.
