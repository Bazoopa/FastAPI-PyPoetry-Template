import logging
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Azure MySQL database connection parameters
hostname = "bru.mysql.database.azure.com"
username = "bruce"
password = ""  # Replace with your actual password
database_name = "testdatabase"  # Replace with your actual database name
ssl_ca = 'DigiCertGlobalRootCA.crt.pem'  # Replace with the path to DigiCertGlobalRootCA.crt.pem

# Establish MySQL connection using mysql.connector with SSL
try:
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=hostname,
        port=3306,
        database=database_name,
        ssl_ca=ssl_ca,
        ssl_disabled=False  # Ensure SSL is enabled
    )
    print("Successfully connected to MySQL database using mysql.connector.")
    cnx.close()
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL database: {err}")

# Create SQLAlchemy URL for MySQL with SSL mode enabled
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}?ssl_ca={ssl_ca}&ssl_disabled=False"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for ORM models
Base = declarative_base()


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
