#Write code to remove the duplicate characters in a string.

# create two loops.  The first loop will go to the character in the string, the second will scan to make sure there is no duplicate of that character in a second string. If there is then it will remove the character.

    
string1='jakeeeeeell'
string2=''

for ele in string1:
    if ele not in string2:
        string2=string2+ele

print(string2)
