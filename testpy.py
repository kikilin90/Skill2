
def check_anagrams(first_words, second_words):
    # Write your code here
    sortedList1 = []
    sortedList2 = []

    for word in first_words:
        temp = word.split()
        temp2 = temp.sort()
        print temp2
        sortedWord = temp2.join(',')
        print sortedWord
        sortedList1.append(sortedWord)
    
    for word in second_words:
        temp = word.split()
        temp2 = temp.sort()
        sortedWord = temp2.join(',')
        sortedList2.append(sortedWord)
    
    for i in sortedList1:
        if i in sortedList2:
            print 1
        else:
            print 0


check_anagrams(["cinema","host","aba","train"], ["iceman","shot","bab","rain"])