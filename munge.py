# Place code below to do the munging part of this assignment.
def convert_to_fahrenheit(celsius):
    return format(celsius/100 * 1.8, '.1f')

def clean_and_convert_data(lines):
    cleaned_data = []
    for line in lines:
        if not line.strip(): 
            continue
        
        parts = line.split()
        converted_temps = [parts[0]]  
        
        for temp in parts[1:-1]:
            if temp == "***" or temp == "****": 
                 converted_temps.append('None')
            else:
                try:
                    converted_value = convert_to_fahrenheit(float(temp))
                    converted_temps.append(converted_value)
                except ValueError:
                    continue


        cleaned_line = ','.join(converted_temps)
        cleaned_data.append(cleaned_line)

    return cleaned_data

def main():
    with open('data/Workshop1_Dataset.txt', 'r') as file:
        lines = file.readlines()
      
    everything = lines[7:-7]
    column_headers = ",".join(everything[0].split()[:-1])
    data_lines = everything[1:]
    cleaned_data = clean_and_convert_data(data_lines)
    cleaned_data = [
    line for line in cleaned_data if not line.startswith("Year")
    ]   
    
    with open('data/clean_data.csv', 'w') as file:
        file.write(column_headers + '\n')
        for line in cleaned_data:
            file.write(line + '\n')

if __name__ == '__main__':
    main()

