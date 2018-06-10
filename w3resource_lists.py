def p(x):
    print(x)

#7. Write a Python program to remove duplicates from a list.

my_list = [1,2,3,4,1,2,3,2,3,4,5,1,2,2,3,4,5,1,2,3,1,2,3,4,4,5,5,5,3,4,2,3,1,1]

def remove_list_duplicates(l):
    unused = []
    used = []

    for number in l:
        if number not in unused:
            unused.append(number)
        else:
            used.append(number)
    p(used)
    p(unused)

#remove_list_duplicates(my_list)

#10. Write a Python program to find the list of words that are longer than n from a given list of words.

word_list = ['table','program','silver','program','as','it','apple','table','white','red','computer','quote','line','reverse','orange']

def words_longer_than_n(l):

    n = int(input("words longer than?"))

    for word in l:
        if len(word) > n:
            p("True: " + word + " is longer than n: " + str(n))
        else:
            p("False: " + word + " is shorter than n: " + str(n))

#words_longer_than_n(word_list)s

#22. Write a Python program to find the index of an item in a specified list.

def find_index_of_value(my_list):

    index_list = []
    list_length = len(my_list)
    input_ = input("type a word")

    for n in range(list_length):
        x = my_list[n]
        if x == input_:
            index_list.append(n)

    p("item : " + input_ + " was found at indices " + str(index_list))

#find_index_of_value(word_list)

#37. Write a Python program to find common items from two lists.

test1 = [1,2,3,4,5,6]
test2 = [5,6,7,8,9]

def find_common_items(l1,l2):
    common = []
    for item in l1:
        if item in l2 and item not in common:
            common.append(item)

    for item in l2:
        if item in l1 and item not in common:
            common.append(item)

    print(common,l1,l2)

    l1p = len(common) / len(l1)
    l2p = len(common) / len(l2)

    print(str(round(l1p*100,2)) + "% match")
    print(str(round(l2p*100,2)) + "% match")

#find_common_items(test1,test2)

#68. Write a Python program to extend a list without append.

def append_without_append(l1,l2):
    for n in range(len(l2)):
        l1.insert(len(l1),l2[n])
    print(l1)

append_without_append(test1,test2)

#Remove last or first n items from list

def remove_n_items_headtail(my_list):

    my_list.sort()

    first_or_last = input("enter f or l (first or last)").lower().strip()

    while first_or_last != 'f' or first_or_last == 'l':
        if first_or_last == 'f' or first_or_last == 'l':
            break
        else:
            first_or_last = input("enter f or l (first or last)")

    n = int(input("enter number of items to remove..."))

    p("You have chosen to remove the " +str(n)+ " items from the " + first_or_last + " position.")

    if first_or_last == 'f':
        for i in range(0,n):
            my_list.pop(0)

    elif first_or_last == 'l':
        for i in range(0,n):
            my_list.pop(len(my_list)-1)

    p(my_list)

#remove_n_items_headtail(word_list)

#Remove unlimited amount of items from list based on value

rem_list = ['program', 'as', 'white']

def rem_unlimited_values(rem_list,my_list):
    for word in rem_list:
        my_list.remove(word)
    p(my_list)
    p(rem_list)

#rem_unlimited_values(rem_list, word_list)

