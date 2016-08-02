price=float(input('enter cents per kWh:'))
dailyuse=float(input('enter daily use in kWh:'))
numberofbillingda
ys=float(input('enter number of billing days:'))
estimatedbill=price * 10 ** -2 * dailyuse * numberofbillingdays
print('estimated bill',estimatedbill)