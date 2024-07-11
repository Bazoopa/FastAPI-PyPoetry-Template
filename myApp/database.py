import logging

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import SQLALCHEMY_DATABASE_URL, DATABASE

# Establish MySQL connection using mysql.connector with SSL
try:
    cnx = mysql.connector.connect(
        user=DATABASE["username"],
        password=DATABASE["password"],
        host=DATABASE["hostname"],
        port=DATABASE["port"],
        database=DATABASE["database_name"],
        ssl_ca=DATABASE["ssl_ca"],
        ssl_disabled=DATABASE["ssl_disabled"]
    )
    print("Successfully connected to MySQL database using mysql.connector.")
    cnx.close()
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL database: {err}")

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for ORM models


# Dependency to provide a database session
def get_db():
    logging.debug("Attempting to establish database connection...")
    db = SessionLocal()
    try:
        yield db
        logging.debug("Successfully connected to the database!")
    finally:
        db.close()
        logging.debug("Database connection closed.")
