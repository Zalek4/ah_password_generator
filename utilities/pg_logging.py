import os
import sys
import logging
import datetime
today = datetime.date.today()

class PG_Logging():
        # ===================================================
    # Function Name: pg_log
    # Description: Takes a log level and a message for the logger. Logs to a file.
    # Input values: log_level(int), log_message(string)
    # ===================================================
    def pg_log(log_level, log_message):
        now = datetime.datetime.now()
        log_file = now.strftime('speed_beans_%Y-%m-%d.log')
        log_format = '%(asctime)s - %(levelname)s | %(message)s'
        logging.basicConfig(filename=log_file, filemode='w', format=log_format, level=logging.INFO)

        # Figure out which level of logging to use
        if log_level == 0:
            print(f"{log_message}")
            logging.debug(log_message)
        elif log_level == 1:
            print(f"INFO: {log_message}")
            logging.info(log_message)
        elif log_level == 2:
            print(f"WARNING: {log_message}")
            logging.warning(log_message)
        elif log_level == 3:
            print(f"ERROR: {log_message}")
            logging.error(log_message)
        elif log_level == 4:
            print(f"CRITICAL: {log_message}")
            logging.critical(log_message)
        else:
            print(f"ERROR: UNABLE TO LOG ACTION")
            logging.error("UNABLE TO LOG ACTION")

    # ===================================================
    # Function Name: pg_log_delete_old
    # Description: Deletes any logs that are more than 3 days old
    # Input values: N/A
    # ===================================================
    def sb_log_delete_old():
        sub_results = []
        list_of_files = []
        oldest_file = []
        log = PG_Logging.sb_log

        try:
            log(1, f"{'Checking for old log files':=^80}")
            log_scan = os.listdir()
            for i in log_scan:
                if ".log" in i:
                    list_of_files.append(i)

            for i in range(len(list_of_files)):
                list_of_files[i] = f"{os.getcwd()}\{list_of_files[i]}"

            full_path = ["{0}".format(x) for x in list_of_files]
            log(1, f">\tLog files: {list_of_files}")

            if len(list_of_files) > 3:
                oldest_file.append(min(full_path, key=os.path.getctime))
                log(2, f">\tDeleting old log file: {oldest_file}")
                os.remove(oldest_file[0])

                sub_results = ["sb_log_delete_old", "Success", oldest_file]
                log(1, f">\tSuccess")
                return(True, sub_results)
            else:
                log(1, f">\tNo old log files detected")
                sub_results = ["sb_log_delete_old", "Passed", oldest_file]
                return(True, sub_results)
        except:
            sub_results = ["sb_log_delete_old", "Failed", oldest_file]
            log(4, f">\t{sys.exc_info()[1]}")
            return(True, sub_results)