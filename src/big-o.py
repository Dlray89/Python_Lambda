
count = 0

def my_print_counter(thing_to_print):
    global count
    count += 1
    print(thing_to_print)

my_items = [1,2,3,4,5,6,7,8,9,20]


'''
0(1) - Constant time (1) is input
'''
#(items) = input/ No matter how big items get the number of op occur stays the same
# def print_first_item(items):
#     my_print_counter(items[0])
    
# print_first_item(my_items)

'''
Constant time has only one operation y = 12 is one op
in the example is  items[0]. We are calling a specific index in a list just onces.
'''

'''
================================================================================
'''

'''
0(n) = linear Time
'''
# this will print out every item in the list. (items) will be a collection that will be looped through and print
def print_all_items(items):
    for item in items:
        my_print_counter(items)

print_all_items(my_items)


'''
===============================================
'''

'''
0(n ^ 2) - Quadratic Time
'''

def print_all_possible_ordered_pairs(items):
    for first_item in items: # outer loop/ this will run 10 times
        for second_item in items: # inner loop/ this will run 10 times n = items ^ 2 = 100(10*10)
            my_print_counter((first_item, second_item)) #print a tuple with both 1st and 2nd item
print_all_possible_ordered_pairs(my_items)


'''
N  could be the actual N or the size of the input
'''
# Linear run Time
def say_hi_n_times(n): # not a list but an integer
    for item in range(n): # looping thorugh item up to n
        my_print_counter('Hi')
say_hi_n_times(10) # loop through 10 times  



def print_all_items(items): # looping through list of items
    for item in items:
        my_print_counter(item)

print_all_items(my_items)


'''
drop the onstant
'''
# o(2n) is simplified to what?
def print_all_items_twices(items): # looping through and print twice because my_print_counter is counting 2 per loop
    for item in items:
        my_print_counter(item)

    #one more loop
        for item in items:
            my_print_counter(item)

print_all_items_twices(my_items)

'''
0(1 + n/2 + 100) is simplified to what?
0(n)

'''

def print_all_items_then_first_half_then_say_hi(items): # pass in items
    my_print_counter(items[0]) # run this 0(1)

    middleindex = len(items) / 2 #go up to half way the size of the list
    index = 0 # start the index at 0
    while index < middleindex: # 0(n/2)
        my_print_counter(items[index]) #Each time print something out
        index += 1

        for time in range(100): # 0(100)
            my_print_counter('Hi')

print_all_items_then_first_half_then_say_hi(my_items)


'''
Drop the less significant terms
'''
#(0(n + n^2)) = 
def print_all_numbers_then_all_pair_sums(numbers):
    print('these are numbers')
    for number in numbers: #0(n)
        my_print_counter(number)


    print('the sre there sums')
    for first_number in numbers: # 0(n^)
        for second_number in numbers:
            my_print_counter(first_number, second_number)
print_all_numbers_then_all_pair_sums(my_items)




'''
We are usually talking about the worst case
'''

#Linear time 0(2)
my_haystack = [1,2,3,4,5,6,7,8,9,10]
def contains(haystack, needle):

    for item in haystack:
        if item == needle:
            return True

    return False

contains(my_haystack, 1)

'''
sometimes constant do matter
beware of premature optimzation
'''

'''
desmo graph
www.desmo.com
'''