import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect
from createTable import createTables


def getTables(engine):
    inspector = inspect(engine)
    all_tables = [tbl for tbl in inspector.get_table_names(schema=db)]
    return all_tables, inspector


df = pd.read_csv('../data/Customers_20210813185020.txt', sep="|", header=None)

is_header = df.iloc[0, 0]
is_trailer = df.iloc[df.shape[0] - 1, 0]

if is_header == 'H':
    df.drop(df.head(1).index, inplace=True)

df.columns = ["D", "customerName", "customerID",
              "customerOpenDate", "lastConsultedDate",
              "vaccinationType", "doctorConsulted",
              "state", "country", "postCode", "dateofBirth", "activeCustomer"]

if is_trailer == 'T':
    df.drop(df.tail(1).index, inplace=True)
del df['D']

df['customerID'] = df['customerID'].apply(np.int64)
df.set_index('customerID')

try:
    df['customerOpenDate'] = pd.to_datetime(
        df['customerOpenDate'], format='%Y%m%d')
    df['lastConsultedDate'] = pd.to_datetime(
        df['lastConsultedDate'], format='%Y%m%d')
    df['dateofBirth'] = pd.to_datetime(
        df['dateofBirth'], format='%d%m%Y')
except Exception as e:
    print(e)

df['country'] = df['country'].str.lower()
distinct_countries = df['country'].drop_duplicates()

db = "incubyte"
try:
    engine = create_engine(
        "mysql+mysqlconnector://root:password@localhost/" + db)
    engine.connect()
    print("Database Connected")
except Exception as e:
    print(e)

existing_tables, inspector = getTables(engine)
createTables(engine, inspector, db, distinct_countries, existing_tables)
existing_tables, inspector = getTables(engine)

for country in distinct_countries:
    my_filt = (df['country'] == country)
    try:
        print("Inserting Records in " + country)
        if country in existing_tables:
            df[my_filt].to_sql(
                name=country, con=engine,
                if_exists='replace', index=False)
    except Exception as e:
        print(e)
