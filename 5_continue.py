# >>> 5.  What is the purpose continue statement in python?

# The primary purpose of the continue statement is to control the flow of the loop based on certain conditions without exiting the loop entirely. It allows you to skip specific parts of the loop's code block based on certain conditions being met.

# Example using continue statement

for i in range(1, 6):
    if i == 3:
        continue
    print(f"Current value of i is {i}")
