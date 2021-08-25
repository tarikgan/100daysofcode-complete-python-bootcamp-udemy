# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining = 90 - int(age)
day = years_remaining * 365
week = years_remaining * 52
month = years_remaining * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")