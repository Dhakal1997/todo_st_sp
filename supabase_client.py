from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]
def get_supabase() -> Client:
    return create_client(url, key)
supabase: Client = create_client(url, key)

# name = str(input("Enter todo"))

response = supabase.table("todolist").select("*").execute().data

print(response)



