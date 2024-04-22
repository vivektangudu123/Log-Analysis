import signal
import subprocess
import re
import time
from collections import deque
import logging 

# A deque to strore the past 100 keywords
my_deque = deque() 

# logging to write to logs of the warnings
logging.basicConfig(level=logging.DEBUG, filename='warnings.log') 

# Keywords to search in the logs generated 
keywords = ["ERROR", "INFO","CRITICAL","FATAL","DEBUG"]

# A dictionary to store the count of the keywords in the past 100 logs 
keyword_100 = {keyword: 0 for keyword in keywords}


# We can modify the threshold for the keywords.
threshold = { 
    "INFO": 101, 
    "DEBUG": 50, 
    "ERROR": 40,
    "CRITICAL": 10,
    "FATAL": 5
    }

# functiont to stop the stop the code
def signal_handler(sig, frame):
    print("\nStopping log monitoring...")
    global running
    running = False

# check the threshold for updated keyword only
def check_threshold(keyword):
    if keyword_100[keyword] > threshold[keyword]:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logging.warning(f"{current_time} {keyword} count exceeds the threshold!!!")
        keyword_100[keyword]=0


# check for the keyword in the last 100 lines, Give the warning if the keyword crosses the threshold 
def past_100(keyword):
    my_deque.append(keyword)
    keyword_100[keyword]+=1
    check_threshold(keyword)
    if(len(my_deque)>100):
        last_keyword=my_deque.pop()
        if(keyword_100[last_keyword]>0):
            keyword_100[last_keyword]-=1

#update the count of each keyword in the keyword_count.txt file
def write_counts_to_file(keyword_counts):
    existing_counts = {}
    try:
        with open("keyword_counts.txt", "r") as file:
            for line in file:
                keyword, count = line.strip().split(": ")
                existing_counts[keyword] = int(count)
    except FileNotFoundError:
        pass  

    for keyword, count in keyword_counts.items():
        existing_counts[keyword] = existing_counts.get(keyword, 0) + count
        keyword_counts[keyword]=0
    with open("keyword_counts.txt", "w") as file:
        for keyword, count in existing_counts.items():
            file.write(f"{keyword}: {count}\n")

def monitor_log(log_file, keywords):
    print("Starting log monitoring...")
    print("Press Ctrl+C to stop.")
    print("Analyzing log file:", log_file)
    print("Keywords to analyze:", keywords)

    #To search the keywords in the last line of log file.
    patterns = {keyword: re.compile(keyword) for keyword in keywords}
    keyword_counts = {keyword: 0 for keyword in keywords}
    tail_process = subprocess.Popen(["tail", "-n", "0", "-f", log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #to update the file every 60 seconds
    last_write_time = time.time()
    write_interval = 60 
    try:
        while running:
            line = tail_process.stdout.readline().decode().strip()
            if line:
                print("New log entry:", line)
                 # Check if the new log entry matches any keyword pattern
                for keyword, pattern in patterns.items():
                    if pattern.search(line):
                        keyword_counts[keyword] += 1
                        past_100(keyword)

                print("Keyword counts:")
                for keyword, count in keyword_counts.items():
                    print(f"{keyword}: {count}")
                current_time = time.time()

                # Write keyword counts to file at regular intervals
                if current_time - last_write_time >= write_interval:
                    write_counts_to_file(keyword_counts)
                    last_write_time = current_time
    except KeyboardInterrupt:
        pass
    finally:
        tail_process.terminate()
        tail_process.wait()

if __name__ == "__main__":

    log_file = "logs.log"
    running = True
    signal.signal(signal.SIGINT, signal_handler)
    monitor_log(log_file, keywords)