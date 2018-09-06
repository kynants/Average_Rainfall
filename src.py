# Design a program that uses nested loops to collect data and calculate the
# average rainfall over a period of years. The program should first ask for
# the number of years. The outer loop will iterate once for each year. The
# inner loop will iterate twelve times, once for each month. Each iteration of
# the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the
# total inches of rainfall, and the average rainfall per month for the entire
# period.

# Prompt User Input
year = int(input('Enter the number of years: '))

# Initialized Variables
count_year = 1
count_month = 1
num_of_month = 12 * year
inch_amt = 0

# Outer while loop increments year
while count_year <= year:
    # Inner while loops increments month
    while count_month <= num_of_month:
        inch = int(input('Enter the number of inches of rainfall for '
                         'month {}'.format(count_month)))
        inch_amt += inch
        count_month += 1
    count_year += 1

print('Number of months:', count_month)
print('Total inches of rainfall:', inch_amt)
print('Average rainfall per month:', inch_amt / count_month)