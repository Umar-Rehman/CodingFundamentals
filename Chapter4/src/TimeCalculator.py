# Part 3 - Time calculator

from numpy import subtract

class TimeCalculator:
    def __init__(self, time_list=[]):
        self.first = time_list
    
    def sort_time(self, unsorted_time):
        sorted_time = unsorted_time
        
        if sorted_time[2] > 59 or sorted_time[2] < 0:
            sorted_time[1]+= sorted_time[2]//60
            sorted_time[2] = sorted_time[2]%60
        if sorted_time[1] > 23 or sorted_time[1] < 0:
            sorted_time[0]+= sorted_time[1]//24
            sorted_time[1] = sorted_time[1]%24
        return sorted_time

    def add(self):
        time_sum = [sum(x) for x in zip(*self.first)]
        time_sum = self.sort_time(time_sum)
        output_time = f"{time_sum[0]:02d}:{time_sum[1]:02d}:{time_sum[2]:02d}"
        return output_time

    def difference(self):
        time_dif = subtract(*self.first).tolist()
        time_dif = self.sort_time(time_dif)
        output_time = f"{time_dif[0]:02d}:{time_dif[1]:02d}:{time_dif[2]:02d}"
        return output_time

    def convert_to_hours(self):
        hours = self.first[0][1]
        hours += self.first[0][0]*24
        hours += round(self.first[0][2]/60, 2)
        return(hours)

    def convert_to_mins(self):
        mins = self.first[0][2]
        mins += self.first[0][0]*1440
        mins += self.first[0][1]*60
        return(mins)

    def convert_mins_to_time(self):
        new_time = []
        mins = input("Enter a number of minutes: ")
        while type(mins) != int:
            try:
                mins = int(mins)
            except:
                mins = input("Please enter an integer value for the number of minutes: ")
        
        days = mins//1440
        mins = mins%1440
        hours = mins//60
        mins = mins%60

        
        new_time.append(days)
        new_time.append(hours)
        new_time.append(mins)
        output_time = f"{new_time[0]:02d}:{new_time[1]:02d}:{new_time[2]:02d}"
        return(output_time)

    def convert_hours_to_time(self):
        new_time = []
        hours = input("Enter a number of hours: ")
        while type(hours) != float:
            try:
                hours = float(hours)
            except:
                hours = input("Please enter an integer/float value for the number of hours: ")
        
        days = round(hours//24)
        hours = hours - days*24
        mins = round((hours%1)*60)
        hours -= hours%1

        new_time.append(round(days))
        new_time.append(round(hours))
        new_time.append(round(mins))
        output_time = f"{new_time[0]:02d}:{new_time[1]:02d}:{new_time[2]:02d}"
        return(output_time)

    def convert_days_to_time(self):
        new_time = []
        days = input("Enter a number of days: ")
        while type(days) != float:
            try:
                days = float(days)
            except:
                days = input("Please enter an integer value for the number of days: ")
        hours = days%1*24
        days -= days%1
        mins = (hours%1)*60
        hours -= hours%1
        new_time.append(round(days))
        new_time.append(round(hours))
        new_time.append(round(mins))
        output_time = f"{new_time[0]:02d}:{new_time[1]:02d}:{new_time[2]:02d}"
        return(output_time)

def get_times(quantity=1):
    time_list = []
    count = 1
    while count <= quantity:
        times = input("Enter a time (in format DD:HH:MM): ")

        good_input = False
        while good_input == False:
            try:
                newtimes = times.split(":")
                newtimes = list(map(int, newtimes))
                TC = TimeCalculator()
                TC.sort_time(newtimes)
                time_list.append(newtimes)
                count+=1
                good_input = True
    
            except:
                times = input("Enter a time (in format DD:HH:MM): ")
    
        
    return(time_list)

def calculate_time():
    do = True
    while do:
        option = input("Select an operation:\n1. Add 2 times\n2. Find the difference between 2 times\n3. Convert to Hours\n4. Convert to Minutes\n5. Convert Minutes to Time\n6. Convert Hours to Time\n7. Convert Days to Time\n8. Exit\n\n")
        while type(option) != int:
            try:
                option = int(option)
                if int(option) < 1 or int(option) > 8:
                    raise Exception
                else:
                    continue
            except:
                option = input("Please enter an option between 1-8: ")

        if option == 1:
            li = get_times(2)
            TC = TimeCalculator(li)
            ans = TC.add()
            print(ans)

        elif option == 2:
            li = get_times(2)
            TC = TimeCalculator(li)
            ans = TC.difference()
            print(ans)

        elif option == 3:
            li = get_times(1)
            TC = TimeCalculator(li)
            ans = TC.convert_to_hours()
            print(ans)

        elif option == 4:
            li = get_times(1)
            TC = TimeCalculator(li)
            ans = TC.convert_to_mins()
            print(ans)

        elif option == 5:
            TC = TimeCalculator()
            ans = TC.convert_mins_to_time()
            print(ans)

        elif option == 6:
            TC = TimeCalculator()
            ans = TC.convert_hours_to_time()
            print(ans)

        elif option == 7:
            TC = TimeCalculator()
            ans = TC.convert_days_to_time()
            print(ans)
        else:
            do = False

# To try the function yourself, uncomment the following lines:
# calculate_time()
