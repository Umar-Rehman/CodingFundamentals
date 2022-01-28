# Task: Inbuilt Functions

import statistics

def analyze_csv_list(csv_number_string):
    '''Requires string of comma seperated integer values.
       Returns statistics of inputted data.'''
    grades = list(map(int, csv_number_string.split(",")))
    low = min(grades)
    high = max(grades)
    avg = round(sum(grades)/len(grades), 2)
    mean = round(statistics.mean(grades),2)
    mdn = statistics.median(sorted(grades))
    print("Minimum Value: {}\nMaximum Value: {}\nAverage: {}\nMean: {}\nMedian: {}".format(low, high, avg, mean, mdn))
    return(low, high, avg, mean, mdn)

# To try the function yourself, uncomment the following lines:
# data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,1,4,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
# analyze_csv_list(data)