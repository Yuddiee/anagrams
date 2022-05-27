# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Type in your first word: ")
    anagram = input("Type in your second word: ")
    str1 = word.lower()
    str2 = anagram.lower()
    if len(str1) == len(str2) :
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)

    if sort_str1 == sort_str2 :

        return True
    else:
        return False
    
print(find_anagram('', ''))