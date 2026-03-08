# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}
#"Bellatrix"{"RA": "05h 25m 07.8s", "Dec": "+06° 20' 59″", "Spectral Type": "B2III B2V"}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

#dictionaries are different from lists, so 
def each_name(targets):
    for n in targets.keys(): #obtaining the name of the dictionary in order to retrieve the info
        print(n)

#2:Write a function that uses a loop to print the name of each star with its spectral type.
def star_and_type(targets):
    for n in targets.keys(): #retrieves the name of the dictionary and of each star
        stardict=targets[n] #- so this gives me the dictionary of that star
        for i in stardict: #so stardict retrieves the dictionary under the name of the star
            #where i then retrieves the names of the keys
            if i=="Spectral Type":
                type=stardict["Spectral Type"]
                print(type, n)


#3: Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def mag_greaterthan(targets):
    for n in targets.keys(): #retrieves the name of the dictionary and of each star
        stardict=targets[n] #- so this gives me the dictionary of that star
        for i in stardict: #so stardict retrieves the dictionary under the name of the star
            #where i then retrieves the names of the keys
            if i=="Magnitude": #now this is looking at the magnitude of each star
                magnitude=stardict["Magnitude"]# this retrives the value of the magnitude
                if magnitude>0.1:
                    return(n) #if this star has a magnitude greater than 0.1, it will be printed

# 4) Look up another target, add all the necessary information to the targets list. 
Bellatrix={"Bellatrix":{"RA": "05h 25m 07.8s", "Dec": "+06° 20' 59″", "Spectral Type": "B2III B2V"}}
targets.update(Bellatrix)

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def brightest_star(targets):
    degrees=""
    remainders=[]
    closest_to_20=""
    for n in targets.keys(): #retrieves the name of the dictionary and of each star
        stardict=targets[n] #- so this gives me the dictionary of that star
        for i in stardict: #so stardict retrieves the dictionary under the name of the star
            #where i then retrieves the names of the keys
            if i=="Dec": #now this is looking at the declination of each star
                declination=stardict["Dec"]# this retrives the declination of each star
                #unfortunately declination is a string, so i gotta accomodate for that. 
                #so i hope to retrieve the first 3 letters in the sting
                for j in range(1,2):
                    degrees+=declination[j]+declination[j+1] #now this takes the degrees of each star
                    remainders.append(int(degrees))
                    degrees="" #Now I've recived a list of my degrees, so finally, I'll check for whose is closest to 20 degrees:
    closest=0          
    for k in range(len(remainders)): #ill create a loop for it to return the closest to 20, so ill compare using subtraction for each one
        if abs(remainders[k]-20) < abs(remainders[closest]-20):
            closest=k
    #okay i got it to return the closest index, now to return simply the star, so i first create a list of the outer keys
    outerkeys=list(targets.keys())
    closest_to_20=outerkeys[closest] #finally, I take the index of the list that corresponds to the star closest to 20 degrees
    return(closest_to_20)

# 6) What is your favorite constellation?
#My favorite is the Gemini constellation

each_name(targets)
star_and_type(targets)
print(mag_greaterthan(targets))
print(brightest_star(targets))