price=float(input('enter cents per kWh:'))
dailyuse=float(input('enter daily use:'))
numberofbillingdays=float(input('number of billing days:'))
estimatedbill=price * 10 ** -2 * dailyuse * numberofbillingdays

traiff=float(input('enter traiff 11 or 31:'))
if traiff==11:
    estimatedbill=estimatedbill * 0.244618
elif traiff==31:
    estimatedbill=estimatedbill *0.136928

print('estimatedbill',estimatedbill)