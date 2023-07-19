password = input("Enter strong password: ")

result = []
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
upper = False
for l in password:
    if l.isdigit():
        digit = True
    if l.isupper():
        upper = True

result.append(digit)
result.append(upper)

if all(result):
    print("Your Password is Strong!")
else:
    print("Your Password is Weak!")

