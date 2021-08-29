import csv
import math 

with open('masterData.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

# sorting data to get list
data = file_data

# finding mean
def mean(data):
    total = 0
    n = len(data)

    for x in data:
        total += int(x[1])

    mean = total / n
    return mean

# subtract mean from all values and squaring them
squared_list = []
for number in data:
    a= int(number[1]) - mean(data)
    a= a**2
    squared_list.append(a)

# sum of all values from squared list
sum = 0
for i in squared_list:
    sum = sum + i

# divide the sum by (n-1)
result = sum / (len(data)-1)

# square root  of result
std_deviation = math.sqrt(result)

print(std_deviation)