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
                try:
                    converted_temps = [parts[0]] + [convert_to_fahrenheit(float(temp)) for temp in parts[1:-1]] + [parts[-1]]
                    cleaned_line = ' '.join(converted_temps)
                    cleaned_data.append(cleaned_line)
                except ValueError:
                    continue

    return cleaned_data

def main():
    with open('data/raw_data.txt', 'r') as file:
        lines = file.readlines()
      
    data_lines = lines[7:-6]

    # Assuming the first data line after skipped lines is the column header
    column_headers = data_lines[0]
    data_lines = data_lines[1:]  # Remove header from data lines

    # Further clean, convert, and format data
    cleaned_data = clean_and_convert_data(data_lines)

    # Write cleaned and converted data to a new CSV file
    with open('data/clean_data.csv', 'w') as file:
        file.write(column_headers)
        for line in cleaned_data:
            # Optionally standardize space as a separator if desired
            standardized_line = ' '.join(line.split())
            file.write(standardized_line + '\n')

if __name__ == '__main__':
    main()
