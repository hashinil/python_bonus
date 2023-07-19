password = input("Enter strong password: ")

result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
upper = False
for l in password:
    if l.isdigit():
        digit = True
    if l.isupper():
        upper = True

result["digit"] = digit
result["upper"] = upper

if all(result):
    print("Your Password is Strong!")
else:
    print("Your Password is Weak!")
