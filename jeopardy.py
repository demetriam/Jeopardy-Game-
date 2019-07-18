import requests

response = requests.get('http://jservice.io/api/clues?category=21').json()

question = response[21]["question"]
answer = response[21]["answer"]


print(question)
print(answer)


# Print out just the first item in the entire response.


# Print out just the question of the first item in the entire response.

# You might notice that each of the dictionary keys has the letter u in front of it - this just means the string that follows is represented in Unicode, and it won't affect your code in any way today. You can igore the u.

# Refactor your code so that it prints out a random question, not just the first one every time.

# Now, get some user input after the question. If what they type matches the answer, print a "congratulations!" message of some sort. If it doesn't match, print a "sorry" message of some sort.

# It's important to think about how specific Python's matching will be. If the user types "gorge" but the correct answer is "Gorge.", then the user will get the question wrong. Consider finding a way of making your program responsive to small variations in capitalization or punctuation.
# If you get it wrong, you probably still want to know the right answer - it can be so frustrating if you were sure you were right. If the user gets it wrong, print out a message that tells them what the correct answer really was.
# Collapse
