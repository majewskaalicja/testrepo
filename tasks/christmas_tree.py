'''
using python functions and loops create half christmas tree
*
**
***
****

where first parameter of function would be height number (lines)
and second parameter would be symbol of christams tree (*, &, # or else)

#
##
###
####

'''
def tree(hight, symbol):
    
    for x in range(1, hight + 1):
        print(symbol * x)

tree(3, '*')
tree(4, '#')
tree(5, '%')