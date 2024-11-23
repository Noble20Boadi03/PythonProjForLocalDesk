with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# check if word exist and save to a set
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
        
        
answers = {}

# put word in dictionary, use input as value
for word in words:
    answer = input("Enter a word in place of " + word + " : ")
    answers[word] = answer
# replace th word with answer
for word in words:
    story = story.replace(word, answers[word])

print(story)
