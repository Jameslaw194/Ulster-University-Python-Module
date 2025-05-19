# This program determines whether a bank customer
# qualifies for a loan. A customer is eligible for
# a loan if s/he satisifes at least one of the following:
# 1)earns at least £30,000/year
# 2)has been in full time emplyment for at least 2 years

min_salary = 30000.0  # The minimum annual salary          #WRONG AMOUNT
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = float(input('Enter the number of ' +           #needs float
                         'years employed: '))                  #should be years

# Determine whether the cumtomer qualifies.
if salary >= min_salary or years_on_job >= min_years:  #SHOULD BE min_years #SHOULD BE OR #NO COLON
    print('You qualify for the loan.')                      #NO INDENT
else:                                                   #NO COLON
    print('You do not qualify for this loan.')              #NO INDENT
    
#end of if-else structure    
