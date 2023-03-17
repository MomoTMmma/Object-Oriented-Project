# Step 1. 
# INCOME
# Rental = $2,000
# laundry, storage, misc = $0
# total = $ 2,000

# Step 2.
# Expenses
# Tax = $150
# Insurance = $100
# Utilities = $ 0
# HOA = $0
# Lawn / Snow = $ 0
# Vacancy = $ 100
# Repairs = $ 100
# CopEx = $ 100
# Property Manage = $ 200
# Morgage = $ 860
# Total Monthly Expenses = $ 1,610

# Step 3.
# Cash Flow 
# Income Expenses = $2,000 - $1,610 
# Total Cash Flow = $390

# Step 4.
# Cash on Cash ROI
# Down Payment = $40,000
# Closing cost = $3,000 
# Rehab budget = $7,000
# Misc other = $0
# Total Investment = $ 50,000

# monthly cash flow * 12 months will equal annual cash flow
# Annual cash flow = 4,680
# annual cash flow divided by total investment will equal cash ROI
# Cash on Cash ROI = 9.36%

# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 

# Our client's name is Brandon from a company called "Bigger Pockets".

# Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.

# income = {'rental': input(), 'misc': input()}
# # print(income['rental'])

# expenses = {'tax': input(), 'insur': input(), 'utili': input(), 'hoa': input(), 'lawn': input(), 'vacancy': input(), 'repairs': input(), 'capex': input(), 'prop_mang': input(), 'morgage': input()}
# # print(expenses['hoa'])

# cash_flow = {'income_expense': input()}
# # print(cash_flow['income_expense'])

# cash_roi = {'down_pay': input(), 'close_cost': input(), 'repair_budg': input()}
# # print(cash_roi['repair_budg'])

# print(income.items())
# print(expenses.items())
# print(cash_flow.items())
# print(cash_roi.items())

# # class income:
# #     def __dict__(rental, misc):
# #         rental = 2000
# #         misc = 0

class income:
    def __init__(self, rental, misc):
        self.rental = int(input('rental'))
        self.misc = int(input('misc'))

    def add_income(self):
        monthly_income = self.rental + self.misc
        annual_income = monthly_income * 12
        return monthly_income, annual_income


class expenses:
    def __init__(self, tax, insur, utili, hoa, lawn, vacancy, repairs, capex, prop_mang, morgage):
        self.tax = int(input('tax'))
        self.insur = int(input('insururance'))
        self.utili = int(input('utility')) 
        self.hoa = int(input('HOA')) 
        self.lawn = int(input('lawn/snow')) 
        self.vacancy = int(input('vacancy'))
        self.repairs = int(input('repairs')) 
        self.capex = int(input('capex'))
        self.prop_mang = int(input('property management'))
        self.mortgage = int(input('mortgage'))

    def add_expenses(self):
        monthly_expenses = self.tax + self.insur + self.utili + self.hoa + self.lawn + self.vacancy + self.repairs + self.capex + self.prop_mang + self.mortgage
        annual_expenses = monthly_expenses * 12
        return monthly_expenses, annual_expenses

    

class cash_flow:
    def __init__(self, income_expense):
        self.income_expense = income - expenses

    def calculate_cash_flow(self):
        monthly_cash_flow = self.income - self.expenses
        annual_cash_flow = monthly_cash_flow * 12
        return monthly_cash_flow, annual_cash_flow
# annual cash flow divided by total investment will equal cash ROI

class cash_roi:
    def __init__(self, down_pay, close_cost, repair_budg):
        self.down_pay = int(input('down payment'))
        self.close_cost = int(input('closing cost'))
        self.repair_budg = int(input('repair budget'))
        self.misc2 = int(input('misc'))

    def calculate_cash_roi(self):
        monthly_cash_roi = cash_flow - total_investment
        annual_cash_flow = cash_flow // 12
        
        return monthly_cash_roi, annual_cash_flow



