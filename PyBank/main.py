import csv
# define_variables
months = 0
total_profit = 0
profit_change = 0
prev_profit = 0
profit_change_list = []
date_of_greatest_increase = ""
date_of_greatest_decrease = ""
greatest_increase = 0
greatest_decrease = float("inf")

#open and read the csv file
with open("/Users/elenavinyukova/Desktop/AssignmentsUoT/PyBank/Resources/budget_data.csv", "r") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    # skip the header row
    next(budget_data)
    # iterate through rows
    for row in budget_data:
        # increment the number of months
        months += 1
        # add to the total profit
        total_profit += int(row[1])
        # calculate the profit change
        profit_change = int(row[1]) - prev_profit
        profit_change_list.append(profit_change)
        prev_profit = int(row[1])
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            date_of_greatest_increase = row[0]
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            date_of_greatest_decrease = row[0]
    # calculate the average profit change
    average_profit_change = sum(profit_change_list[1:]) / (months - 1)
    # print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_profit_change:.2f}")
    print(f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})")

    #export results as text file
with open("budget_analysis.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Total: ${total_profit}\n")
    text_file.write(f"Average Change: ${average_profit_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})\n")
