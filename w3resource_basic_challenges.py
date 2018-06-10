import _datetime

def print_today():
    print("Utc Datetime:")
    print(_datetime.datetime.utcnow())
    print("Local Datetime")
    print(_datetime.datetime.now())

def circle_area(radius):
    area = radius * 3.142
    area = round(area,2)
    print("The area of your circle is " + str(area) + " units squared.")

#circle_area(4)

def convert_commasep_list(anylist):
    new_list = anylist.split(",")
    print(new_list)

#convert_commasep_list("2,3,5,1,2,6,1,2,45")

def first_and_last_of_list(anylist):
    length_of_list = len(anylist)
    if length_of_list > 0:
        print("The first item of your list is: ")
        print(anylist[0])
        print("The last item of your list is: ")
        print(anylist[length_of_list - 1])
    else:
        print("You have no items in your list!")

#first_and_last_of_list([1,2,54,1,233])
#first_and_last_of_list([])

def concat_list_to_string(anylist):
    string = ""
    for str in anylist:
        string = string + str
    print(string)

#concat_list_to_string(["This","is","daniels","spaghetti","do","not","touch","."])

def list_contains_value(value, anylist):
    for item in anylist:
        if item == value:
            return True
            break
    return False

#print(list_contains_value("tasdsa",["this","is","good","drink","spoon"]))

def print_name_age_address(name = "no name specified", age = "no age specified", address = "no address specified"):
    print("Name: " + str(name))
    print("Age: " + str(age))
    print("Address: " + str(address))

#print_name_age_address("Daniel", 25, "25 Goober Lane")

def add_both_if_integer(number_1):
    if number_1.isdigit():
        print("WOOOOO")
    else:
        print("NOOOOO")