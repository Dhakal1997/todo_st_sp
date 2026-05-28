from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]

# CREATE ONLY ONCE
supabase: Client = create_client(url, key)

def get_supabase() -> Client:
    return supabase




