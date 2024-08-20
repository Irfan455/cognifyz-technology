def count_word_occurrences(word):
    count = 0
    with open("file.txt") as file:
        for line in file:
            words = line.split()
            for w in words:
                if w == word:
                    count += 1
    return count
  
word_to_count = input("enter a word:")   
occurrences = count_word_occurrences(word_to_count)
print(f"The word '{word_to_count}' appears {occurrences} times in the file.")
