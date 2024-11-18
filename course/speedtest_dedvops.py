import speedtest
import datetime
import csv
import time
import os

# Function to measure download and upload speeds
def measure_speed():
    st = speedtest.Speedtest()
    
    print("Measuring download speed...")
    download = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download:.2f} Mbps")
    
    print("Measuring upload speed...")
    upload = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload:.2f} Mbps")
    
    # Get the current timestamp
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp: {today}")
    
    return today, download, upload

# Function to record results in a CSV file
def file_record():
    # Check if the CSV file exists and create it with headers if not
    file_exists = os.path.exists("internet_speed.csv")
    
    with open("internet_speed.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write headers if the file is new
            writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])
        today, download, upload = measure_speed()
        writer.writerow([today, f"{download:.2f}", f"{upload:.2f}"])
    
    print("Results recorded in 'internet_speed.csv'.")

# Main loop to record speed every 5 minutes
while True:
    file_record()
    print("Sleeping for 5 minutes...")
    time.sleep(5)  # Sleep for 300 seconds (5 minutes)

