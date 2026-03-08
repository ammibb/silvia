favfoods=["Khao Soi", "Fried Chicken", "Tortas","Rice", "Mole"]
print(favfoods[-1])
favfoods.append("French Fries")
favfoods.insert(0, "apple")
favfoods.remove("Fried Chicken") #1st error: I got an error since I tried to remove by index, but .remove() deletes by value, but .pop() deletes by index.
#So I changed it to a string.
print(len(favfoods))

for i in favfoods:
    print(i.upper())
new_favfoods=[favfoods[0],favfoods[-1]]
print(new_favfoods)
for i in favfoods:
    if i=="potato":
        print("A potato!")
    else:
        print("No potato!")


def get_first_15():
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    first15=numbers[0:15]
    return(first15)
def get_every_5th(first15):
    every5th=first15[0::4] #start, stop, step
    return(every5th)
def reverse_and_stride(every5th):
    reversed_5th=every5th[::-1] #steps by -1 each time so the whole list is reversed
    return(reversed_5th[::2])
step1=get_first_15()
step2=get_every_5th(step1)
step3=reverse_and_stride(step2)

#NESTED LISTS
list_1=[1,2,3]
list_2=[4,5,6]
list_3=[7,8,9]
nested_numbers=[[1,2,3],[4,5,6],[7,8,9]]

print(nested_numbers[2])
#2nd error: on the first attempt, I used nested_numbers[2,] since I wasnt sure how to print the row 
#by itself, and I got an error since that wasn't valid, in which I change to simply nested_number[2] which
#gave me what I needed
print(nested_numbers[1][1])
nested_numbers.append([10,11,12])

def sum_nested(nested_list):
    rows_sum=0
    for n in nested_list: #goes through each row, so our row is now n
        for i in n: #this goes through a specific row,n and keeps going
            rows_sum+=i
    return(rows_sum)


def create_list():
    nested5x5=[]
    storing=[]
    for i in range(1,26): #this lets me begin at 1 and end at 25
        storing.append(i)
        if len(storing)==5:
            nested5x5.append(storing.copy()) #i have to make a copy, since I tried to clear it, but it still clears whatever is inside the 
            #5x5, so they end up coming out blank.
            #therefore, using storing.copy() does not end up being affected by the clear afterwards.
            storing.clear()
    return(nested5x5)

nested5x5=create_list()

def replace_mult3():
    multiplesof3=nested5x5.copy()
    for n in multiplesof3: #for this row n, 
        for i in range(len(n)): #since range starts at 0 and length ends at the last index+1, this line accounts for all the indexes 
            if n[i]%3==0: #if the ith index in the nth row has a remainder of 0
                n[i]="?"  #using n[i] allows me to access the value at the ith index and replace it
    return(multiplesof3) #if I tried using "i" instead of n[i], it wouldn't change, it'll only modify the variable, not the list
#3rd error: I am attempting to access the list from the previous function, but it doesn't work since it's only defined in there
#so, instead i designated a variable as the list given from create_list

result2=replace_mult3()

def not_equal_to():
    test=result2.copy() #so i've accessed the list from the previous function
    sum=0
    #ill go through each row first, and then through each element in said row to acces them
    for n in test:
        for i in n:
            if i!="?": #so if this index is not equal (!=) to "?", we will add it to our sum
                sum+=i
    return(sum)

#DICTIONARIES
ages={"Katie":30,"Mariam":42, "Safia": 25, "Mira": 48} #defined by curly brackets
print(ages["Katie"])
ages.update({"Mira":100})
ages.update({"Milana":52})
del ages["Mariam"]
#using only for a in ages, only prints out the keys, so in order to get both, I'll use .item(), as it accesses both the keys and values
for key, value in ages.items():
    print(key,value)


print(not_equal_to())