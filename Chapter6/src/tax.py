# User-defined Functions

def getIncomeTax(salary):
    taxDict = {0: 0.2, 34501: 0.4, 150000: 0.45}
    for i in range(0,3):
        if int(salary) == 0:
            tax_rate = 0.0
        elif int(salary) > list(taxDict)[i] and (i == 2 or int(salary) < list(taxDict)[i+1]):
            tax_rate = list(taxDict.values())[i]
        else:
            continue
    tax_amount = round(tax_rate*salary, 2)
    salary_after = round(salary-tax_amount, 2)
    print(f"A salary of £{salary:.2f} is taxed at {tax_rate*100:.2f}%\nTax amount: £{tax_amount:.2f}\nFinal salary: £{salary_after:.2f}\n")
    return tax_rate, tax_amount, salary_after

# To try the function yourself, uncomment the following lines:
# getIncomeTax(200000)