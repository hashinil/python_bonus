import json

with open("files/data.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternative_text"]):
        print(index+1, '-', alternative)
    user_choice = int(input("what is the answer? "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["correct_answer"] == question["user_choice"]:
        score = score+1
        result = "Correct"
    else:
        result = "Wrong"
    message = f"{index} - {result} Your answer: {question['user_choice']}, " \
                f"Correct answer: {question['correct_answer']}"
    print(message)
print(f"Your score is {score}/{len(data)}")