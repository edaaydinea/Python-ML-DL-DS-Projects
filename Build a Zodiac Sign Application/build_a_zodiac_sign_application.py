from datetime import date

year = input("What is your year of birth? (Example: 1995)\n")
month = input("What is your month of birth? (Example: 9)\n")
day = input("What is your day of birth? (Example: 19)\n")

print("Date of Your Birth is: ", (day + "/" + month + "/" + year))

today_day = date.today()

age = today_day.year - int(year)
print("You are ", age, " years old.")

y = int(year)
m = int(month)
d = int(day)

if (m == 12 and d >= 22) or (m == 1 and d <= 19):
    sign = "\nCapricorn"
elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
    sign = "\nAquarius"
elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
    sign = "\nPisces"
elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
    sign = "\nAries"
elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
    sign = "\nTaurus"
elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
    sign = "\nGemini"
elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
    sign = "\nCancer"
elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
    sign = "\nLeo"
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
    sign = "\nVirgo"
elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
    sign = "\nLibra"
elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
    sign = "\nScorpio"
elif (m == 11 and d >= 22) or (m == 12 and d <= 21):
    sign = "\nSagittarius"

print(sign)
