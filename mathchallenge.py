import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    xpr = str(left) + " " + operator + " " + str(right)
    answer = eval(xpr)
    return xpr, answer

correct = 0
guesses = 0
input("Press enter to begin!")
print("----------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " " + "= ")
        if guess == str(answer):
            correct += 1
            guesses += 1
            break
        else:
            guesses += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
accuracy = round(correct / guesses * 100, 2)
print("----------------------")
print("Great job! You finished in " + str(total_time) + " seconds " +
      "with an accuracy score of " + str(accuracy) + "%.")