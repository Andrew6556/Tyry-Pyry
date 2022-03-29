num = []



for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        num.append("тыры-пыры")
    elif i % 3 == 0:
        num.append("тыры")
    elif i % 5 == 0:
        num.append("пыры")
    else:
        num.append(i)

for n in num:
    print(n)