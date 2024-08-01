def count_no_of_times(line,word):
    words=line.split()
    count=words.count(word)
    return count
line="This is a test haha sample test for python coding test"
word="test"
no_of_times=count_no_of_times(line,word)
print(f"The word {word} occurs {no_of_times} times in the line.")
