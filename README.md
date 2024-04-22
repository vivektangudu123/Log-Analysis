# Log analysis

By Vivek Tangudu

[GitHub - vivektangudu123/Log-Analysis](https://github.com/vivektangudu123/Log-Analysis)

[generate.py](http://generate.py/) generates the logs and writes them into a file named logs.log.

[logs.py](http://logs.py/) performs an analysis based on the logs generated by the previous code.

The file named keywords_count.txt contains the count of each log listed in [generate.py](http://generate.py/).

The file named warning.log contains the logs whose occurrences exceed a specified threshold.

1. **Imports and Setup**:
    - It initializes a deque named **`my_deque`** to keep track of the last 100 occurrences of each keyword. This deque allows efficient addition and removal of elements from both ends.
    - **`logging.basicConfig()`** is used to configure logging, setting the logging level to **`DEBUG`** and directing log messages to a file named **`warnings.log`**.
    - **`keywords`** is a list containing the keywords to be monitored in the log file.
    - **`keyword_100`** is a dictionary that will store the count of each keyword within the last 100 log entries.
    - **`threshold`** is a dictionary specifying the threshold for each keyword type, beyond which a warning message will be logged.
2. **Signal Handling**:
    - Defines a signal handler function **`signal_handler`** to catch the interrupt signal (**`SIGINT`**, generated by Ctrl+C) and gracefully stop the log monitoring process.
3. **Threshold Checking**:
    - **`check_threshold()`** function is defined to check if the count of a keyword exceeds its threshold. If it does, a warning message is logged.
4. **Deque Management**:
    - **`past_100()`** function is defined to manage the deque **`my_deque`**. It adds the current keyword to the deque, increments the count of the keyword, checks the threshold, and removes the oldest keyword if the deque length exceeds 100.
5. **Writing Counts to File**:
    - **`write_counts_to_file()`** function is defined to write the keyword counts to a file named **`keyword_counts.txt`**. It reads existing counts from the file, updates them with the current counts, and writes them back to the file.
6. **Log Monitoring**:
    - **`monitor_log()`** function is defined to monitor the log file in real-time.
    - It sets up regex patterns for each keyword and initializes a dictionary **`keyword_counts`** to track the occurrence count of each keyword.
    - It starts a subprocess to tail the log file, continuously reads new log entries, matches them against keyword patterns, updates counts, and prints the counts periodically.
    - Counts are written to the file every 60 seconds or when the script is stopped.
    
    [https://drive.google.com/file/d/1gATYbPiR1fEuOw77wdH_nuVlmsWGePLy/view?usp=share_link](https://drive.google.com/file/d/1gATYbPiR1fEuOw77wdH_nuVlmsWGePLy/view?usp=share_link)
    
    Vivek Tangudu
    
    International Institute of Information Technology, Bangalore
    
    9441354555
    
    [vivektangudu@outlook.com](mailto:vivektangudu@outlook.com)
