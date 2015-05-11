word = input("Enter a word: ")
vowel = ["a", "e", "i", "o", "u"]
chars = []
  
for letter in word:
  if letter.lower() not in vowel:
      chars.append(letter)
      
print("".join(chars))
