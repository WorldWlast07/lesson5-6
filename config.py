import os

from dotenv import load_dotenv

load_dotenv()

db_config = {
    'datbase': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
}