from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Azure MySQL database connection parameters
hostname = "bru.mysql.database.azure.com"
username = "bruce"
password = "hnCXcNhyMvU8*jwmtsqi"
database_name = "your_database_name"  # Replace with your actual database name
ssl_mode = "require"

# SQLAlchemy URL for MySQL with SSL mode enabled
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}/{database_name}?ssl={ssl_mode}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
