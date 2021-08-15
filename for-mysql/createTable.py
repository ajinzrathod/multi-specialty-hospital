from sqlalchemy import Column, Integer, String, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def createTable(tablename):
    pass


def createTables(engine, inspector, db, distinct_countries):
    # Getting list of tables from "incubyte" database
    existing_tables = [tbl for tbl in inspector.get_table_names(schema=db)]
    print("Existing Tables:", existing_tables)

    for tbl in distinct_countries:
        if not tbl in existing_tables:
            print("trying to create " + tbl)
            try:
                createTable(tbl).__table__.create(bind=engine)
                print("Created")
            except Exception as e:
                print(e)
        else:
            print(tbl + " already exists")
