# Place code below to do the munging part of this assignment.
def convert_to_fahrenheit(celsius):
    return format(celsius/100 * 1.8, '.1f')

def clean_and_convert_data(lines):
    cleaned_data = []
    for line in lines:
        if not line.strip(): #exclude blank lines
            continue
        
        parts = line.split()
        converted_temps = [parts[0]]  #Leave out the first column in each line that represents year
        
        for temp in parts[1:-1]:
            if temp == "***" or temp == "****": 
                 converted_temps.append('NA') #fill in missing data with NA strings
            else:
                try:
                    converted_value = convert_to_fahrenheit(float(temp))
                    converted_temps.append(converted_value)
                except ValueError:
                    continue #If the string cannot be converted into float then skip the the string by leaving it intact


        cleaned_line = ','.join(converted_temps) #join everthing with commas
        cleaned_data.append(cleaned_line)

    return cleaned_data

def main():
    with open('data/Workshop1_Dataset.txt', 'r') as file:
        lines = file.readlines()
      
    everything = lines[7:-7] #exclude the note lines and blank lines at the beginning and the end
    column_headers = ",".join(everything[0].split()[:-1]) #make the headers comma separated; exclude the last string in the header which is a repeated year column
    data_lines = everything[1:] #these are all data
    cleaned_data = clean_and_convert_data(data_lines)
    cleaned_data = [
    line for line in cleaned_data if not line.startswith("Year")
    ]   #exclue repeated header lines that are among the data lines
    
    with open('data/clean_data.csv', 'w') as file:
        file.write(column_headers + '\n')
        for line in cleaned_data:
            file.write(line + '\n')

if __name__ == '__main__':
    main()

