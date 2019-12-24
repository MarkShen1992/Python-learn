# if 
# x = int(input("Please enter an integer: "))
x = 12
if x > 10:
    print(str(x) + ' > 10')
else:
    print(str(x) + ' <= 10')

score = 60
if score >= 80:
    print('优')
elif score < 80 and score >= 70:
    print('良')
elif score < 70 and score >= 60:
    print('及格')
else:
    print('不及格')