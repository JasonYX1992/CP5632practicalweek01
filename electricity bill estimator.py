price = float(input('enter cents per kWh:'))

daily_use = float(input('enter daily use in kWh:'))

number_of_billing_days = float(input('enter number of billing days:'))

estimated_bill = price * 10 ** -2 * daily_use * number_of_billing_days

print('estimated bill', estimated_bill)

