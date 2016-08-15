score = float(input("Enter score:"))
if score < 0:
    print('Invalid score')
elif score >= 100:
    print('Invalid score')
elif 90 <= score < 100:
    print('Excellent')
elif 50 <= score < 0:
    print('Passable')
elif 0 <= score < 50:
    print('Bad')
