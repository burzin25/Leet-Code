class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        #Importing libraries
        import string
        
        #Replacing the empty spaces from text assigned to the key variable
        key = key.replace(" ","")

        #Crating an empty list to store individual letters in the key string
        l=[]
        
        #Running a loop through the "key" variabble to append each letter into the list "l"
        for i in key:
            if i not in l:
                l.append(i)

        #Creating a list of alphabets using the string module in python
        a = list(string.ascii_lowercase)
        
        # Initializing an empty dictionary to store key and alphabets in a pair 
        d={}
        
        #Combine or zip each element from list 'l' to each element from list 'a' and form              tuples for creating a dictionary with i as key and j as the alphabet
        for i,j in zip(l,a):
            d[i] = j
        
        #Create a empty key to accomodate our answer
        d[' ']=' '
        #Using the join function to loop through the value for the assigned key in the                dictionary and joing them together as a string
        return ''.join(d[x] for x in message)
    
    