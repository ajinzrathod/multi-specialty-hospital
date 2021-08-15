import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect


df = pd.read_csv('data/Customers_20210813185020.txt', sep="|", header=None)

# header may or may not exist, so using `skiprows = 1` is not good idea
is_header = df.iloc[0, 0]
is_trailer = df.iloc[df.shape[0] - 1, 0]

# checking if Header Records exists
if is_header == 'H':
    df.drop(df.head(1).index, inplace=True)

# Naming the Columns
df.columns = ["D",
              "customerName", "customerID",
              "customerOpenDate", "lastConsultedDate",
              "vaccinationType", "doctorConsulted",
              "state", "country", "postCode",
              "dateofBirth", "activeCustomer"]

# Checking if Trailer record exists
if is_trailer == 'T':
    df.drop(df.tail(1).index, inplace=True)

# Dropping D columns as it of no use
del df['D']

# customerID is considered as float by pandas, so casting to int
df['customerID'] = df['customerID'].apply(np.int64)

# Setting customerID as index for faster operations
df.set_index('customerID')

# here date is treated as string
print(df.info(), end="\n\n")

# Converting String to Dates
try:
    df['customerOpenDate'] = pd.to_datetime(df['customerOpenDate'], format='%Y%m%d')
    df['lastConsultedDate'] = pd.to_datetime(df['lastConsultedDate'], format='%Y%m%d')
    df['dateofBirth'] = pd.to_datetime(df['dateofBirth'], format='%d%m%Y')
except Exception as e:
    print(e)

# here date is treated as date
print(df.info(), end="\n\n")
print(df)


# lower is applied here and not in `distinct_countries` coz we need to fetch rows also
df['country'] = df['country'].str.lower()

# Getting Distinct Countries
distinct_countries = df['country'].drop_duplicates()

print("\nDistinct Countries:\n", distinct_countries)

# Connecting to Database
print()
db = "incubyte"
try:
    my_eng = create_engine("mysql+mysqlconnector://root:password@localhost/" + db)
    my_eng.connect()
    print("Database Connected")
except Exception as e:
    print(e)

# Performing database inspection
inspector = inspect(my_eng)

# Loading all schemas
schemas = inspector.get_schema_names()

# Printing all schemas
for schema in schemas:
    print("schema: %s" % schema)

for table_name in inspector.get_table_names(schema=db):
    print()
    print(table_name)

    # printing all coulmns
    for column in inspector.get_columns(table_name, schema=db):
        print("Column: %s" % column)
