def chickandrabbit():
 head = int(input("count of heads: "))

 legs = int(input("count of legs: "))

 rabbit = 4

 chicken = 2
 
 y = (legs - 2 * head) / 2
 x = head - y

 if y > 0 and x > 0 and x.is_integer() and y.is_integer() :
    print( "chickens : " + str(x),"rabbit : " + str(y))
 else:
    print("Error")

chickandrabbit()