from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# Load from environment
API_KEY = os.getenv('API_KEY')
