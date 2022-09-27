def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    return longest_word


txt = input()

word_list = txt.split()  
print(find_longest_word(word_list)) 