from convert14 import convert
import parse14

feet_inches = input("Enter your height: ")

parsed = parse14.parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} meters.")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
