import logging
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase  # Updated import
from settings import SQLALCHEMY_DATABASE_URL, DATABASE
from endpoints.base import Base

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    logger.info("Successfully connected to MySQL database using mysql.connector.")
    cnx.close()
except mysql.connector.Error as err:
    logger.error(f"Error connecting to MySQL database: {err}")

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Create a sessionmaker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Declare a base class for ORM models


# Dependency to provide a database session
def get_db():
    logger.debug("Attempting to establish database connection...")
    db = SessionLocal()
    try:
        yield db
        logger.debug("Successfully connected to the database!")
    finally:
        db.close()
        logger.debug("Database connection closed.")
