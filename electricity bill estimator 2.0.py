price = float(input('enter cents per kWh:'))
daily_use = float(input('enter daily use:'))
number_of_billing_days = float(input('number of billing days:'))
estimated_bill = price * 10 ** -2 * daily_use * number_of_billing_days

traiff = float(input('enter traiff 11 or 31:'))

if traiff == 11:
    estimated_bill = estimated_bill * 0.244618
elif traiff == 31:
    estimated_bill = estimated_bill * 0.136928

print('estimated_bill', estimated_bill)
