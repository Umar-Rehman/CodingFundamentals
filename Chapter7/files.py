#  File I / O

import csv

def read_file():
    companies = []
    sales = []

    with open("Chapter7//carSale.csv", "r") as f:
        for i, line in enumerate(f):
            if i % 2 == 0:
                companies.append(line.strip())
            if i % 2 != 0:
                sales.append(list(map(int, line.split(","))))
    f.close()
    return companies, sales

def calculate_sales():
    companies, sales = read_file()
    monthly_sales = [sum(i) for i in zip(*sales)]
    months = ["January", "Febraury", "March", "April", "May", "June", "July", "August"]
    count = 0
    for i in monthly_sales:
        print(f"Cars sold in {months[count]}: {i}")
        count+=1

    for i in range(0, len(sales)):
        print(f"Yearly sales by {companies[i]}: {sum(sales[i])}")

calculate_sales()