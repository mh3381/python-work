#chained conditions are adding multiple conditions in one line
#(and or not)
x = 2 
y = 3

#if x == y and x + y == 5: it will not run on print
#    print('ran')
if y == x or x + y == 5: #it will run on print because at least one condition is true
   print('ran')
if not (y == x or x + y == 6): # it will print because 'not' reverse the result of brackets True to False and reverse
    print('ran')
else:
    print(':(')   

if x == 2:
    if y == 3:
        print('x = 2, y = 3' )
    else:
        print('x = 2, y != 3')         
else:
    print('x != 2')