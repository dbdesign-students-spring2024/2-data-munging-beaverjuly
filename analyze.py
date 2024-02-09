# Place code below to do the analysis part of the assignment.
import csv

def calculate_decade_average(file_path):
    decade_data = {}

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 

        for row in reader:
            try:
                year = int(row[0]) 
                decade = (year // 10) * 10 
                
                for anomaly_str in row[1:]:
                    if anomaly_str == 'NA':
                        continue
                    anomaly = float(anomaly_str)
                    
                    if decade not in decade_data:
                        decade_data[decade] = {'sum': 0, 'count': 0}
                    
                    decade_data[decade]['sum'] += anomaly
                    decade_data[decade]['count'] += 1
            
            except ValueError:
                continue

    for decade in sorted(decade_data.keys()):
        avg_anomaly = decade_data[decade]['sum'] / decade_data[decade]['count']
        print(f"{decade}s: {avg_anomaly:.2f}°F")

if __name__ == "__main__":
    calculate_decade_average('data/clean_data.csv')
