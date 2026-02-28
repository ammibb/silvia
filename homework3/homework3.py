def say_goodbye(message):
    print(message)
say_goodbye("Goodbye!")

def circle_area(radius):
    print(radius**2*3.14) 
circle_area(20)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

def weather_today(temps):
    return(min(temps), max(temps))

def is_weekend(day_number):
    if day_number==6 or day_number==7: 
        return True
    else:
        return False
    
def fuel_efficiency(distance, fuel_used):
    return(distance/fuel_used)

def encrypt(password):
    s=str(password)
    size=len(s)-1 #so the size of the password is recorded, this is to understand how many decimal points it occupies
    ending=password%10
    remaining=password//10 #in these 2 lines i got both the ending of the password and what remains after the ending is ignored
    decimal_place=10**size #i figured that I should simply add the ending, but since we removed it, I have to see where it places, so I exponentiated
    #by the size in order to get the respective order it should take. so if i originally had 123, then this allows me to do 10^2, which gives me 100, 
    #this way I can then do the following:
    add_by=ending*decimal_place #here i mulitpled the ending by the previous line. this then gives me the place it should take.
    new_password=add_by+remaining #i added to the remaining I had, so it took the place and kept the magnitude the same
    return(new_password)

def exponential(x,y):
    counter=1
    for n in range(y): #the range allowed me to loop for however long y was. so if y was 3, then it would start at 1 and keep going until 3.
        counter=counter*x #the range then allows me to multiply x with itself for y times. 
    return(counter)

def max_val(values):
    max=values[0] #so i took the value in the zeroeth index. this allowed me to compare and also establish which numbers I should compare
    for n in values:
        if n>=max: 
            max=n #because max was designated as the first value, we simply replace it with the nth index in values. since this for loops takes and comparees the values
            #, not the indexes.
    return(max)

def min_val(values): #this one uses the same idea as the previous, only replacing min if it finds a value smaller than it.
    min=values[0]
    for n in values:
        if n<=min:
            min=n
    return(min)

def max(values):
    max=values[0] #since a while loop can't really take and loook at the values I assume, 
    #, I made it so that we designate a value first, then I took how long the list of values was, 
    #where I then created an n to be able to use as reference for when to stop.
    n=len(values)
    m=0
    while m<n: #next, m was defined and so since m starts at zero, it'll count the first value in the zeroeth index of the list
        #this also helps as a natural stopping point since the total amount of indexes will always be 1 less than the length of the list.
        if values[m]>=max:
            max=values[m]
        m+=1 #after each one, it adds up in order to stop.
    return(max)

def min(values):#this one also shares the same idea, it also has to keep checking every value, so the only difference is designating a minimum
    min=values[0]
    n=len(values)
    m=0
    while m<n:
        if values[m]<=min:
            min=values[m]
        m+=1
    return(min)

#for this one, I first needed to know how many spaces the digits took. so if i had 123, it would take up 3 spaces.
def digits_sum(digits):
    s=str(digits)
    n=len(s)
    #knowing the amount of spaces/length, I created n to record it. This gave me a reference on how long the for loop should go
    #Because the range allows me to continue on for as many digits in the integer, this allows me to account for each number and lets
    #me add them indivially up.
    leftover=digits
    total=0
    for n in range(n):
        total+=leftover%10 #here, I obtained the last digit and I used this as my starting point.
        leftover=leftover//10 #after obtaining the last digit, I could change the value of the integer, which is why I named it leftover as those
        #had not yet been added. 
        #Afterwards, my total then keeps on being added to the next digit to the left of it. so if I started with 123, the first iteration
        #desigantes total as =3. then the remaining amount would be 12. the second iteration then adds 2 to 3 (total) and so on
        #until I account all the digits. 
    return(total)


#for the variables that were only inteded for the loops or a length, I named them short as I didn't need to keep track of them.

list=[1,3,6,12,.0222,0.3,1,300]
print(min(list))
print(max(list))

def counting_vowels_and_consonants(input):
    vowels=["a","e","i","o","u","y", "A", "E", "I", "I", "O", "U"] #ill use this to more easily differentiate from a vowel and consonant
    #if a letter is not a vowel, then itll be made a consoannt
    vowelsnum=0 #tracking the number of vowels and consonants
    consnum=0
    for char in input: #checks each letter in the string
        if char.isalpha():
            if char in vowels:
                vowelsnum+=1
            else:
                consnum+=1
    return (vowelsnum,consnum)

def average_vowels_and_consonants(phrase):
    #avg vowels per sentence would take in the num of vowels and divide by amount of letters in the sentence
    endsentence=["!",".","?"]
    sentences=[] #can use .append() to add the sentences to my list 
    beginsent=0
    for s in range(len(phrase)): #for each index in the length of the string, ill run it through the if statemtn
        #this statement then checks the letter of the given index. where phrase[s] picks the letter in the phrase
        #i can then use s to slice the string and add it into my sentences list. 
        if phrase[s] in endsentence:
            sentences.append(phrase[beginsent:s+1]) #slicing my phrase and using the beginsent variable in order to mark the 
            #beginning of a sentence, where s+1 marks the end of the sentence, allowing the inclusion of the last character.
            #Here, i can then begin a new "loop" where the beginning of a sentence is s+1. 
            beginsent=s+1 #
    #now I have split the different sentences apart. I'll then create a for loop that stores
    #the amount of consonants and vowels per sentence. (for this i'll add the amount of cons and vowels in each and divide by amnt of sentences)
    amntofsents=len(sentences) #amount of sentences 
    #making a list to store each sentences' vowels and consts:
    totalvowels=0
    totalcons=0 #i will simply use the for loop to add onto the total vowels and consonants
    #add counting_vowels_and_consonants[0] to 
    for i in sentences:
        storing=counting_vowels_and_consonants(i) #it will loop for each index in sentence, so for the first,
        #itll use the function on the first index, and so on. So i represents the first sentence, and itll loop until done.
        totalvowels+=storing[0]
        totalcons+=storing[1]
    #This added all out vowels and consonants into the variables
    #now ill just group them up
    avgcons=totalcons/amntofsents
    avgvowels=totalvowels/amntofsents
    return(amntofsents,avgvowels,avgcons)

#first sentence:
def describing(phrase):
    endsentence=["!",".","?"]
    sentences=[] #can use .append() to add the sentences to my list 
    beginsent=0
    for s in range(len(phrase)): #for each index in the length of the string, ill run it through the if statemtn
        #this statement then checks the letter of the given index. where phrase[s] picks the letter in the phrase
        #i can then use s to slice the string and add it into my sentences list. 
        if phrase[s] in endsentence:
            sentences.append(phrase[beginsent:s+1]) #slicing my phrase and using the beginsent variable in order to mark the 
            #beginning of a sentence, where s+1 marks the end of the sentence, allowing the inclusion of the last character.
            #Here, i can then begin a new "loop" where the beginning of a sentence is s+1. 
            beginsent=s+1 
    for i in sentences:
        observe=average_vowels_and_consonants(i) 
        print(f"The '{i}' sentence,  has {observe[1]} average vowels and {observe[2]} average consonants")

describing("Fall in love with some activity, and do it! Nobody ever figures out what life is all about, and it doesn't matter. Explore the world. Nearly everything is really interesting if you go into it deeply enough. Work as hard and as much as you want to on the things you like to do the best. Don't think about what you want to be, but what you want to do. Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all.")