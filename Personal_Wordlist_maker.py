from itertools import permutations, combinations
import os

# Questions and prompts
questions = [
    "What is your date of birth? (Day/Month/Year)",
    "What is the name of your first pet?",
    "What was your college mascot?",
    "Who is your favorite musician?",
    "What is your favorite color?",
    "What was your last vacation spot?",
    "What is the name of the first company you worked for?",
    "What high school did you attend?"
]

# Collect answers
answers = []
for q in questions:
    a = input(q + " ").strip().replace(" ", "").lower()
    answers.append(a)

# Generate combinations for long passwords
print("\nGenerating wordlist...")
wordlist = set()

# Combine 3-5 answers in all orders
for r in range(3, 6):
    for combo in combinations(answers, r):
        for perm in permutations(combo):
            wordlist.add("".join(perm))
            wordlist.add("-".join(perm))
            wordlist.add("_".join(perm))
            wordlist.add(".".join(perm))

# Write to file
with open("custom_wordlist.txt", "w") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")

print(f"✅ Wordlist created: {os.path.abspath('custom_wordlist.txt')} ({len(wordlist)} entries)")
