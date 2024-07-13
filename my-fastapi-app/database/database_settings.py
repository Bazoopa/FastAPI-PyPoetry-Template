import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The default values are required for the tests to work, might need to change this later.
# Database Configuration
DATABASE = {
    "hostname": os.getenv("DB_HOST", "localhost"),
    "username": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database_name": os.getenv("DB_NAME", "test"),
    "ssl_ca": os.getenv("DB_SSL_CA", ""),
    "port": int(os.getenv("DB_PORT", 3306)),  # Provide default port 3306 for MySQL
    "ssl_disabled": os.getenv("DB_SSL_DISABLED", "False") == "True"  # Convert string to boolean
}

# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{DATABASE['username']}:{DATABASE['password']}"
    f"@{DATABASE['hostname']}:{DATABASE['port']}/{DATABASE['database_name']}?"
    f"ssl_ca={DATABASE['ssl_ca']}&ssl_disabled={DATABASE['ssl_disabled']}"
)

# Logging Configuration
logging.basicConfig(level=logging.DEBUG)
