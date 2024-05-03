

## Write a program that calculates simple interest

|||info

<font size="3"><center>$interest = principal \times interest\_rate \times time\_period$</center></font>
<font size="3"><center>$ending\_balance = principal + interest$</center></font>

|||

- Prompt the user for the following values 
  - **principal**
  - **interest_rate**
  - **time_period**


- Print the resulting **ending_balance** at the end of the specified time period. 


|||warning
Note the formatting in the examples, ending balance should be preceded by a dollar sign and display two decimal places. 

**You must use an f-string to format the output.**
|||




<div style="background-color:rgba(3, 30, 60, 0.05); padding:20px; margin: 20px auto; max-width: 800px;">

<strong><center><h3>Test your code using the <span style = "color: #24439A">Try it</span> button</h3></center></strong>
<hr>

<h3>Examples:</h3>

  - principal = 1000
  - interest_rate = 5.3 %
  - time_period = 1

  Ending Balance = $1053.00

<hr>

  - principal = 5000
  - interest_rate = 4.9 %
  - time_period = 5

  Ending Balance = $6225.00



<details>
  <summary>
     Solution for demo purposes
  </summary>

```python
# Prompt for initial balance
principal = float(input("Enter the initial balance: $"))

# Prompt for interest rate
interest_rate = float(input("Enter the interest rate as a percent: "))

# Prompt for time period
time_period = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * interest_rate * time_period) / 100

print(f"Ending Balance: ${(simple_interest + principal):.2f}")

```

</details>

{Try It | terminal}(python3 simple_interest.py)




</div>
