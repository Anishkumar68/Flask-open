import os
from dotenv import load_dotenv

load_dotenv()

app = os.getenv("secret_key")
print(app)
