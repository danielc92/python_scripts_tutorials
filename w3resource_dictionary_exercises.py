def p(p):
    print(p)
'''
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {
    "tuesday" : 30,
    "monday" : 23,
    "thursday" : 13,
    "friday" : 5,
    "wednesday" : 50,
}

p(sorted(zip(my_dict.keys(),my_dict.values())))
p(sorted(zip(my_dict.values(),my_dict.keys())))
p(my_dict)

# 2. Write a Python script to add a key to a dictionary.
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

sample_dictionary = {0: 10, 1: 20}

sample_dictionary[2] = 30

p(sample_dictionary)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
#
# Sample Dictionary :
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

concatenated_dict = {}
concatenated_dict.update(dic1)
concatenated_dict.update(dic2)
concatenated_dict.update(dic3)
p(concatenated_dict)

# 4. Write a Python script to check if a given key already exists in a dictionary.

check_key = 5
if check_key in concatenated_dict.keys():
    p("success")
else:
    p("failure")

# 5. Write a Python program to iterate over dictionaries using for loops.

for each_item in concatenated_dict:
    p(str(each_item) + " : " + str(concatenated_dict[each_item]))

# 6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

cn = 5
elements = cn + 1
squared_dict = {}

for x in range(1, elements):
    squared_dict[x] = x*x
p(squared_dict)

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
upper = 15
n = upper + 1
d = {}

for x in range(1,n):
    d[x] = x**2

p(d)

# 8. Write a Python script to merge two Python dictionaries.

def merge_two_dicts(d1,d2):
    d3 = {}
    d3.update(d1)
    d3.update(d2)
    p(d3)

md1 = {1:2, 4:33}
md2 = {2:5}

# 10. Write a Python program to sum all the items in a dictionary.

sum = 0
for x in md1:
    sum = sum + x + md1[x]
p(sum)

# 11. Write a Python program to multiply all the items in a dictionary.



# 12. Write a Python program to remove a key from a dictionary.

del md1[1] #deletes item with key 1
p(md1)

md1[1] = 2 #adds item back in
p(md1)

# 13. Write a Python program to map two lists into a dictionary.

lst1 = [1,2,3,4,5]
lst2 = ["a","b","c","d","e"]

def map_two_lists_into_dict(l1,l2):
    d = {}
    for x in range(0, len(l1)):
        d[l1[x]] = l2[x]
    p(d)

map_two_lists_into_dict(lst1,lst2)

# 14. Write a Python program to sort a dictionary by key.

dict = {1:-23,3:55,2:20}
def sort_dict_by_values(dict):
    p(sorted(zip(dict.keys(),dict.values())))

# 15. Write a Python program to get the maximum and minimum value in a dictionary.

def min_max_of_dictionary(dict):
    list = []
    for value in dict.values():
        list.append(value)
    p("The maximum value in the dictionary is: " + str(max(list)) + " The minimum value in the dictionary is: " + str(min(list)))

min_max_of_dictionary(dict)

# 16.Write a Python program to get a dictionary from an object's fields.


# 17. Write a Python program to remove duplicates from Dictionary.

rem_dups = {1:2, 2:3, 3:3, 4:2, 5:23, 6:33, 7:33}

def remove_duplicates_from_dict(dict):
    orig_dict = dict
    p("Original dictionary: " + str(orig_dict))
    dlist = []
    klist = []

    for key in dict.keys():

        if dict[key] not in klist:
            klist.append(dict[key])
        else:
            dlist.append(key)
    for k in dlist:
        del dict[k]

    p("Removed keys: " + str(dlist))

    p("Cleaned dictionary: " +str(dict))

# 18. Write a Python program to check a dictionary is empty or not.

def check_dict_empty(dict):
    if len(dict) > 0:
        p("dictionary contains items")
    else:
        p("dictionary does not contain items")

# 19. Write a Python program to combine two dictionary adding values for common keys.
dc1 = {'a': 100, 'b': 200, 'c':300, 'g':205, 'r':120}
dc2 = {'a': 300, 'b': 200, 'd':400, 'e':150, 'g':145}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def combine_dict_if_dup_key(d1,d2):
    cd  = {}
    for k in d1.keys():
        if k in d1.keys() and k in d2.keys():
            cd[k] = d1[k] + d2[k]
        else:
            cd[k] = d1[k]

    for k in d2.keys():
        if k in d1.keys() and k in d2.keys():
            cd[k] = d1[k] + d2[k]
        else:
            cd[k] = d2[k]
    p(sorted(zip(cd.keys(),cd.values())))
    p(sorted(zip(cd.values(),cd.keys())))

# 20. Write a Python program to print all unique values in a dictionary.
sd = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

ord_list = []
dup_list = []
for x in sd.values():
    if x in ord_list:
        dup_list.append(x)
    else:
        ord_list.append(x)
p(sd.values())
p(ord_list)
p(dup_list)

# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

alpha1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha2 = alpha1
l = []

for char in alpha1:
    for char2 in alpha2:
      l.append(char + char2)
p(str(len(l)))
p(l)

# 22. Write a Python program to find the highest 3 values in a dictionary.

p("\n\n")
dv = {}
for i in range(10):
    dv[i] = i**3
p(dv)

vl = []
for v in dv.values():
    vl.append(v)

vl = sorted(vl)
p("maximum 3 numbers: " + str(vl[len(vl)-1]))
p("maximum 3 numbers: " + str(vl[len(vl)-2]))
p("maximum 3 numbers: " + str(vl[len(vl)-3]))

# 23. Write a Python program to combine values in python list of dictionaries.
com_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})



# 24. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
ss = 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

ss_dict = {}

for char in ss:
    if char in ss_dict.keys():
        ss_dict[char] = ss_dict[char] + 1
    else:
        ss_dict[char] = 1
p(ss_dict)

# 25. Write a Python program to print a dictionary in table format.


for x in sd:
    p(x + " | " + sd[x])

# 26. Write a Python program to count the values associated with key in a dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True



# 27. Write a Python program to convert a list into a nested dictionary of keys.

l = [0,1,2,3,4,5]
dl = {}

for num in l:
    dl[num] = "any"
p(dl)

# 28. Write a Python program to sort a list alphabetically in a dictionary.

l2 = ["asd", "aee", "dde", "aerd", "gred", "aerf", "aedf"]

def alpha_dict(l2):
    l2s_dict = {}
    l2s = sorted(l2)
    for i in l2s:
        l2s_dict[i] = "anything"
    p(l2s)
    p(l2s_dict)

alpha_dict(l2)

# 29. Write a Python program to remove spaces from dictionary keys.
trim_dict = {" d f fS ":3, "D add r":1}

for key in trim_dict.keys():
    key.replace(" ","")
    p(key)


# 30. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3



# 31. Write a Python program to get the key, value and item in a dictionary.

def print_keysvaluesitems(dc1):
    p(dc1.keys())
    p(dc1.values())
    p(dc1.items())

print_keysvaluesitems(dc1)

# 32. Write a Python program to print a dictionary line by line.

def print_line_by_line(dc1):
    for item in dc1.items():
        p(item)

print_line_by_line(dc1)

# 33. Write a Python program to check multiple keys exists in a dictionary.

def check_multiple_keys_in_dictionary(dc1):
    if len(dc1) > 1:
        p("this dictionary contains multiple values.")
    else:
        p("this dictionary has 1 or less values.")

check_multiple_keys_in_dictionary(dc1)

# 34. Write a Python program to count number of items in a dictionary value that is a list.
list_dict = {1: [1,2,3], 2: "ac", 3:[2,3,4,5]}

def find_lists_in_dict(list_dict):
    for x in list_dict.values():
        if isinstance(x, list) == True:
            p(str(x) + " \nis a list\n")
        else:
            p(str(x) + " \nis not a list\n")

find_lists_in_dict(list_dict)
'''
# 35. Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]



# 36. Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})



# 37. Write a Python program to replace dictionary values with their sum.
'''
sum_me_dict =  {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

for x in sum_me_dict:
    sum_me_dict[x] =  sum_me_dict[x] + 3

p(sum_me_dict)


# 38. Write a Python program to match key values in two dictionaries.

d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

key_list = []

for x in d1.keys():
    key_list.append(x)

for y in d2.keys():
    if y in key_list:
        print(str(y) + " is within d1 dictionary")
    else:
        print(str(y) + " is not within d1 dictionary")

'''