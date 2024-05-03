# CODIO SOLUTION BEGIN
# Prompt for initial balance
principal = float(input("Enter the initial balance: $"))

# Prompt for interest rate
interest_rate = float(input("Enter the interest rate as a percent: "))

# Prompt for time period
time_period = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * interest_rate * time_period) / 100

print(f"Ending Balance: ${(simple_interest + principal):.2f}")
# CODIO SOLUTION END