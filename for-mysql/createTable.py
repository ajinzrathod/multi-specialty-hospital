from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def createTable(engine, tablename):
    try:
        with engine.connect() as con:
            con.execute("call createCountryTable(\"" + tablename + "\")")
    except Exception as e:
        print(e)


def createTables(engine, inspector, db, distinct_countries, existing_tables):
    for tbl in distinct_countries:
        if tbl not in existing_tables:
            print("trying to create " + tbl)
            try:
                createTable(engine, tbl)
                print("Created")
            except Exception as e:
                print(e)
        else:
            print(tbl + " already exists")
