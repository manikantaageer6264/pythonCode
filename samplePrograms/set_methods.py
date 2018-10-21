##set methods
##1) add( ) - to add single element to a set
set1 ={1,2,3}
set1.add( 4 )
print (set1)
###update method can take (list,tuple,string and set as an arugument)
##2) update [ ] - to add mutiple elements
set1.update( [ 5,6])  #elements are list
print (set1)
set1.add(9,10) #elements are tuple
print (set1)
set1.update ("hai","hello") #element are strings
print (set1)
set1.update({11,12})
print (set1)

##to list all the built in functions and methods supported by a set
#print (dir(set1))

#discard( ) - to emove a particular item from the set
set.discard ( 11 ) #arugument is the element of a set
print("after remove in element::",set1)

#remove () - to remov a particular item from te set
set1.remove()
print("after remove in element::",set1) # If item in set Exception arises

#pop #arbitaly an element and print the remaining
print ("before pop", set1)
set1.pop ( )
print ("after pop",set1)

#write a program to get a string from a given string where all occurrences of it's fitsr char have been changed to
#except the first char itself. Go to the editor
#simple string : 'restart'
#excpected result : 'resta$t