from supabase_client import get_supabase
from datetime import datetime
import csv
import os

# Get all todos
supabase = get_supabase()
todo_list = supabase.table("todolist").select("*").execute().data

# total_progress = [(sum for value in item['is_completed'])if "is_completed"== False]
progress_count = 0
for item in todo_list:
    if not item["is_completed"]:
        progress_count += 1
# print(f"Total inprogress is {count}")
    
# Current date and time
now = datetime.now()
date = now.strftime("%m-%d")
time = now.strftime("%H:%M")


file_name = "daily_todo_log.csv"

# check if file exists
file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)
    
# write header if file does not exist
    if not file_exists:
        writer.writerow(["Date", "Time", "Totaltodo","In-Progress", "Completed"])    

    writer.writerow([date, time, len(todo_list), progress_count, len(todo_list)-progress_count])

   
# print("Daily log updated successfully")
 