import re
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def analyze_logs(self):
        try:
            f = open(self.log_file, 'r')
            logs = f.readlines()
            f.close()
        except FileNotFoundError:
            f = open(self.log_file, 'w')
            logs = []
            f.close()

        total_entries = len(logs)
        error_count = 0
        warning_count = 0
        info_count = 0
        errors = []

        # More basic regex pattern
        pattern = r'\[(\w+)\] (.*?): (.*)'

        for l in logs:
            match = re.match(pattern, l)
            if match:
                level, title, message = match.groups()

                if level == 'ERROR':
                    error_count += 1
                    errors.append(message)
                elif level == 'WARNING':
                    warning_count += 1
                elif level == 'INFO':
                    info_count += 1

        summary = {
            'total_entries': total_entries,
            'error_count': error_count,
            'warning_count': warning_count,
            'info_count': info_count,
            'errors': errors
        }

        if logs:
            first = logs[0]
            last = logs[-1]
            summary['time_range'] = f"{first[:19]} to {last[:19]}"

        return summary

ana = LogAnalyzer('log.txt')
summary = ana.analyze_logs()
print(summary)
