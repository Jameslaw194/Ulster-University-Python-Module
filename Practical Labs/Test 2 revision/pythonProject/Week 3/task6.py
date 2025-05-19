# This program determines whether a bank customer
# qualifies for a loan. A customer is eligible for
# a loan if s/he satisifes at least one of the following:
# 1)earns at least £30,000/year
# 2)has been in full time emplyment for at least 2 years

min_salary = 30000.0  # The minimum annual salary
min_years = 2  # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary or years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')

# end of if-else structure
