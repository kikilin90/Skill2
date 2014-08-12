# import operator


"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	word_string = string1.split(" ")
	word_dict = {}
	for i in word_string:
		if i in word_dict:
			word_dict[i] += 1
		else:
			word_dict[i] = 1
	return word_dict


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	result = list(set(list1).intersection(list2))
	return result


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	num_dict = {}
	result = []

	for i in list1:	
		num_dict[i] = True
	print num_dict

	for i in list2: # you have the num_dict that contains list 1 already
		if i in num_dict: # so this one compares list 2 to num_dict, if it's there, it means a duplicate already
			result.append(i)

	return result


"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    num_dict = {}
    zero = []
    
    for i in list1:
    	num_dict[i] = True
    return num_dict

    for i in num_dict.keys():
    	if num_dict.get(i*-1):
    		zero.append([i,i*-1])
    return zero[:len(zero)/2]


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	result = []
	word_dict = {}
	i = 0
	while i < len(words):
		for i in words:		
			if i in word_dict:
				word_dict[i] += 1
			else:
				word_dict[i] = 1
	print word_dict

	for i in word_dict:
		if word_dict[i] > 1:
			result.append(i)
	return result


# # JavaScript
# function duplicate(argv) {
#     var result = []
#     var dict = {};
#     for (var i = 0; i < argv.length; i++) {
#         if (argv[i] in dict) {
#             if (typeof(argv[i]) === 'string') {
#                 dict[argv[i]]++;
#             }
#             else if (typeof(argv[i]) === 'boolean') {
#                 dict[argv[i]]++;
#             }
#         }
#         else {
#             dict[argv[i]] = 1; 
#         }
#     }
#     console.log(dict); 
#     for (var k in dict) {
#         if (dict[k] > 1) {
#             result.push(i);
#         }
#     }
#     console.log(result);
# }

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
	word_dict = {}
	for i in words:
		if word_dict.get(len(i)):
			word_dict[len(i)] += [i] #.append(i) works, too.
		else:
			word_dict[len(i)] = [i]
	return word_dict


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
def translate_to_pirate():

	pirate_dict = {
		"sir" : "matey",
		"hotel" : "fleabag inn",
		"student" : "swabbie",
		"boy" : "matey",
		"madam" : "proud beauty",
		"professor" : "foul blaggart",
		"restaurant" : "galley",
		"your" : "yer",
		"excuse" : "arr",
		"students" : "swabbies",
		"are" : "be",
		"lawyer" : "foul blaggart",
		"the" : "th'",
		"restroom":"head",
		"my" : "me",
		"hello" : "avast",
		"is" : "be",
		"man" : "matey"
	}

	user_input = raw_input("Tell me about yourself.")

	input_list = user_input.split()

	for i in range(len(input_list)):
		if pirate_dict.get(input_list[i]):
			input_list[i] = pirate_dict.get(input_list[i])

	new_translation = " ".join(input_list)

	return new_translation


# Callbacks on functions with test lists and strings

string1 = "I do not like green eggs and ham, but I do love eggs benedict."
list1 = [2, 5, 12, 6, -100, 1, -5, 8, 5, -6, -2, 2, 27, -27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am", "benedict"]

print count_unique(string1)

print common_items(list1,list2)

print common_items2(list1, list2)

print sum_zero(list1)

print find_duplicates(words)

print word_length(words)

print translate_to_pirate()


