def number_of_bottles():
    for i in range(99,1,-1):
        print(str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk.")
        print("Take one down and pass it around, "+ str(i-1) + " bottles of milk on the wall.\n")
    print("1 bottle of milk on the wall, 1 bottle of milk.")
    print("Take one down and pass it around, no more bottles of milk on the wall.\n")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.\n")

number_of_bottles()