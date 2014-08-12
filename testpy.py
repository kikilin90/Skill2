List1 = ["cinema","host","aba","train", "god"]
List2 = ["iceman","shot","bab","rain", "dog"]

def check_anagrams(first_words, second_words):
    # Write your code here
    sortedList1 = []
    sortedList2 = []

    for word in first_words:
        split = list(word)
        # print split
        split.sort()
        # print split
        sortedWord = split
        # print sortedWord
        new_word = "".join(sortedWord)
        # print new_word
        sortedList1.append(new_word)

    for word in second_words:
        split = list(word)
        # print split
        split.sort()
        # print split
        sortedWord = split
        # print sortedWord
        new_word = "".join(sortedWord)
        # print new_word
        sortedList2.append(new_word)

    print sortedList1
    print sortedList2
    
    for i in sortedList1:
        if i in sortedList2:
            print "1 - anagram"
        else:
            print "0 - not anagram"


check_anagrams(List1,List2)