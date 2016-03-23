count = 1

i = int(raw_input("Vnesi stevilko med 1 in 100:"))

for x in range(1, i + 1):
    
    if (count % 5) == 0 and (count % 3) == 0:
        print "fizzbuzz"
        count = count +1
    elif (count % 3) == 0:
        print "fizz"
        count = count + 1
    elif (count % 5) == 0:
        print "buzz"
        count = count +1
    else:
        print count
        count = count + 1