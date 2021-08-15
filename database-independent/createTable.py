from sqlalchemy import Column, Integer, String, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def createTable(tablename):
    class CountryName(Base):
        __tablename__ = tablename
        customerName = Column(String(255), nullable=False)
        id = Column(BigInteger, primary_key=True, autoincrement=True)
        customerOpenDate = Column(Date, nullable=False)
        lastConsultedDate = Column (Date)
        vaccinationType =Column(String(5))
        doctorConsulted =Column(String(255))
        state = Column(String(5))
        country = Column(String(5))
        postCode = Column(String(5))
        dateOfBirth = Column(Date)
        activeCustomer = Column(String(1))
    return CountryName


def createTables(engine, inspector, db, distinct_countries, existing_tables):
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
