# coffee shop lab cis 129
# made by Josue Monreal for PCC 

print("*******************\n*******************")
value1 = input( "Number of coffee's bought?")

value2 = input("Number of muffins bought?")

# the statements above grab user input for number of items bought for each menu item

print('*******************\n*******************')

coffee = 5.00 
muffins = 4.00
scones = 3.00
chai = 6.00
# above gives a dollar amount to each menu item

print('My Coffee and Muffin Shop Reciept')
print ('--------------------')

coffeeprice = int(value1) * coffee
muffinprice = int(value2) * muffins
sconeprice = int(value3) * scones
chaiprice = int(value4) * chai
sub_total = coffeeprice + muffinprice + sconeprice + chaiprice
tax = 0.06 * sub_total 
Total = coffeeprice + muffinprice + sconeprice + chaiprice + tax

# above gives equations for all things displayed

print (value1,"coffee at 5$ each:")
print ("$",coffeeprice)
\
print (value2,"muffins at 4$ each:") 
print ("$",muffinprice)

print(value3,"Scones at 3$ each:")
print("$",sconeprice)

print(value4,"Chai at 6$ each:")
print("$",chaiprice)

print ("6% tax:")
print ("$",'%.2f' %tax)

print ("---------")
print ("TOTAL","$",'%.2f' %Total)
print ("*******************")

# above displays the number values for the reciept based on equations above
# i did have to lookup how to round tax value so i didnt have a million decimals for it on the reciept

print ("Have a Nice Day, See You Soon!!")

# above gives a nice message to come back, tehe, thanks!!
