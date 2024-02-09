# Place code below to do the munging part of this assignment.
def convert_to_fahrenheit(celsius):
    return format((celsius * 1.8) + 32, '.1f')

def clean_and_convert_data(lines):
    cleaned_data = []
    for line in lines:
        if not line.strip():
            continue

        parts = line.split()
        converted_temps = [parts[0]] 
        for temp in parts[1:-1]: 
            if temp == '***': 
                converted_temps.append('None')
            else:
                converted_temps = (
                [parts[0]]
                + [convert_to_fahrenheit(float(temp)) if temp.isdigit() else temp for temp in parts[1:-1]]
                + [parts[-1]]
                )

    return cleaned_data

def main():
    with open('data/Workshop1_Dataset.txt', 'r') as file:
        lines = file.readlines()
      
    data_lines = lines[7:-6]
    column_headers = data_lines[0]
    data_lines = data_lines[1:]
    cleaned_data = clean_and_convert_data(data_lines)
    
    with open('data/clean_data.csv', 'w') as file:
        file.write(column_headers)
        for line in cleaned_data:
            file.write(line + '\n')

if __name__ == '__main__':
    main()
