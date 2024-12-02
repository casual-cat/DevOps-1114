# - Uses the speedtest-cli library to measure download and upload speeds.
import speedtest
import datetime
def measure_speed():
    st = speedtest.Speedtest()
    print("measuring download speed...")
    download = st.download() / 1_000_000
    print(f"download speed: {download:.2f} Mbps")  
    print("measuring upload speed...")
    upload = st.upload() / 1_000_000
    print(f"upload speed: {upload:.2f} Mbps.")
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(today)
    return (today, download, upload)

# - Records the results in a CSV file named internet_speed.csv.
# Adds a new entry with a timestamp, download speed, and upload speed every 5 minutes.
import os
import csv
def file_record():
    with open("internet_speed.csv", "a", newline="") as file:
        file.write(str(measure_speed()))
    if os.path.exists("internet_speed.csv"):
        print("results recorded in 'internet_speed.csv.'")
    else:
        print("file does not exist. creating file...")
    with open("internet_speed.csv", "w") as file:
        file.write(str(measure_speed()))

import os
import datetime
import speedtest
import time
import csv

while True:
    file_record()
    print("sleeping for 60 seconds...")
    time.sleep(60)
    
    
        
# - Runs the speedtest and records the results.