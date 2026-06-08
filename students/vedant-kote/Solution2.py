#problem no1
d = {"Ram": 30, "Vijay": 40, "Radha": 60}
print(d["Vijay"])

#problem no2
d.update({"Tom":2,"Don": 10})
print(d)

#problem no3
s = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",  "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z"}

v = 0
c= 0

vowels = "aeiou"

for x in s:
    if x in vowels:
        v = v + 1  
    else:
        c = c+ 1  

print("Total Vowels:", v)
print("Total Consonants:", c)

