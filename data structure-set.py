# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 22:21:01 2016

@author: YI
"""

#detect the duplication in the list
duplist = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#method 1
duplicates = []
for i in duplist:
    if duplist.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
            
print duplicates

#method 2
duplicates = set([x for x in duplist if duplist.count(x)>1])
        
print duplicates

#intersection
color1 = set(['yellow', 'red', 'blue', 'green', 'black'])
color2 = set(['red', 'brown'])

print color1.intersection(color2)

#difference
print color1.difference(color2) #return elements that color1 has but color2 doesn't  have







