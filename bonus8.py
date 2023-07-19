date = input("What is the date?")
rate = input("Rate the date:")
thoughts = input("Share your thoughts:")

with open(f"files/{date}.txt", 'w') as file_w:
    file_w.write(rate + 2 * '\n')
    file_w.write(thoughts)
