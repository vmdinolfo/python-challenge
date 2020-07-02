#import modules to create directories and read csv files
import os
import pandas as pd

#read csv file from pybank > resources
file = 'Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'

#open and read csv file
budget_df = pd.read_csv(file)
output_file = os.path.join("analysis","budget_summary.txt")
opened_file = open(output_file, 'w')
#print(budget_df.head())

#Begin Financial Analysis
print("Financial Analysis")
print("--------------------------------------------------------")
#count number of months [column 0, 'Date'], and print the count
print(f"Total Months: {budget_df['Date'].count()}")

#calculate net value(sum) of Profit/Losses [column 1], and print the sum
print(f"Total Net Value: ${budget_df['Profit/Losses'].sum()}")

#calculate average of Profit/Losses [column 1], and print the sum
print(f"Average Change: ${round(budget_df['Profit/Losses'].mean(),2)}")

#find the max increase 
max_inc = budget_df['Profit/Losses'].max()
#print(max_inc)

#print the month of the max increase and the max increase
maxinc_month_df = budget_df.loc[budget_df["Profit/Losses"] == max_inc, :]
print(f"Greatest Increase in Profits: {maxinc_month_df.iloc[0]['Date']} (${maxinc_month_df.iloc[0]['Profit/Losses']})")

#find the min decrease 
max_dec = budget_df['Profit/Losses'].min()
#print(min_inc)

#print the month of the max decrease and the max decrease
maxdec_month_df = budget_df.loc[budget_df["Profit/Losses"] == max_dec, :]
print(f"Greatest Decrease in Profits: {maxdec_month_df.iloc[0]['Date']} (${maxdec_month_df.iloc[0]['Profit/Losses']})")

#write to txt file
opened_file.write("Financial Analysis\n")
opened_file.write("--------------------------------------------------------\n")
opened_file.write(f"Total Months: {budget_df['Date'].count()}\n")
opened_file.write(f"Total Net Value: ${budget_df['Profit/Losses'].sum()}\n")
opened_file.write(f"Average Change: ${round(budget_df['Profit/Losses'].mean(),2)}\n")
opened_file.write(f"Greatest Increase in Profits: {maxinc_month_df.iloc[0]['Date']} (${maxinc_month_df.iloc[0]['Profit/Losses']})\n")
opened_file.write(f"Greatest Decrease in Profits: {maxdec_month_df.iloc[0]['Date']} (${maxdec_month_df.iloc[0]['Profit/Losses']})\n")

#close file
opened_file.close()