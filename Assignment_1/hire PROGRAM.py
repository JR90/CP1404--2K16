#-----------------------LIST ALL ITEMS ----------------------/*



# Pseudo CODE--------------------------
"""
def movieList()
    print(("All items on file (* indicates item is currently out):")
    open file in read mode
    make list of items
    n=0
    for i in movie:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]
    print items in table format

    if movie is out
    pirnt *
    close file


"""
def movieList():
    print("All items on file (* indicates item is currently out):")
    f= open("items.csv",'r')
    movie= f.readlines()
    n=0
    for i in movie:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]

        print(str(n)+" - "+"%-45s"%(movieName+"("+discp+")")+"= $"+"%7.2f"%(price),sep=" ",end="")
        n+=1
        if status == "out":
            print(" *")

        else:
            print()
    f.close()



#-----------------------HIRE ITEMS--------------------------------------------\\
"""
def hireMovies()
    open file in read mode
    make list of items
    n=0
    for i in item:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]
    print items in table format

    if hireMovies is in
    pirnt ()
    close file

    movieChoice = Enter the number of an item to hire
    open file in read mode
    m = item.index(hList[movieChoice])
    movie = item[m]
    movieName = movie.strip().split(',')[0]
    discp = movie.strip().split(',')[1]
    price = float(movie.strip().split(',')[2])
    print (movieName+ " hired for $"+ "%.2f" %(price) )
    item[m] = movieName+","+discp+","+str(price)+","+"out\n"
    file=""
    for i in item:
        file = file + i
    f.write(file)

"""

def hireMovies():
    f= open("items.csv",'r')
    item= f.readlines()
    n=0
    hList=[]
    for i in item:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]

        if status == "in":
            print(str(n)+" - "+"%-45s"%(movieName+"("+discp+")")+"= $"+"%7.2f"%(price),sep=" ")
            n+=1
            hList.append(i)

    f.close()
    movieChoice = int(input("Enter the number of an item to hire "))
    f= open("items.csv",'w')

    m = item.index(hList[movieChoice])


    movie = item[m]
    movieName = movie.strip().split(',')[0]
    discp = movie.strip().split(',')[1]
    price = float(movie.strip().split(',')[2])
    print (movieName+ " hired for $"+ "%.2f" %(price) )
    item[m] = movieName+","+discp+","+str(price)+","+"out\n"
    file=""
    for i in item:
        file = file + i
    f.write(file)


#\\---------------------------------RETURN ITEM------------------------\\

"""
def returnMovies()
    open file in read mode
    make list of items
    n=0
    for i in item:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]
    print items in table format

    if hireMovies is in
    pirnt ()
    close file

    movieChoice = Enter the number of an item to return
    open file in read mode
    m = item.index(hList[movieChoice])
    movie = item[m]
    movieName = movie.strip().split(',')[0]
    discp = movie.strip().split(',')[1]
    price = float(movie.strip().split(',')[2])
    print (movieName+ " returned")
    item[m] = movieName+","+discp+","+str(price)+","+"in\n"
    file=""
    for i in item:
        file = file + i
    f.write(file)
"""
def returnMovies():
    f= open("items.csv",'r')
    item= f.readlines()
    n=0
    hList=[]
    for i in item:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        status = i.strip().split(',')[-1]

        if status == "out":
            print(str(n)+" - "+"%-45s"%(movieName+"("+discp+")")+"= $"+"%7.2f"%(price),sep=" ")
            n+=1
            hList.append(i)

    f.close()
    movieChoice = int(input("Enter the number of an item to return "))
    f= open("items.csv",'w')

    m = item.index(hList[movieChoice])


    movie = item[m]
    movieName = movie.strip().split(',')[0]
    discp = movie.strip().split(',')[1]
    price = float(movie.strip().split(',')[2])
    print (movieName+ " returned")
    item[m] = movieName+","+discp+","+str(price)+","+"in\n"
    file=""
    for i in item:
        file = file + i
    f.write(file)



#\\-----------------------------ADD ITEMS-------------------------------\\

"""
def addItems()
    movieName = Enter item name
    discp = Enter description
    prince = Enter price per day

    print("now available for hire")

    open file in read mode
    new = movieName+","+discp+","+str(price)+","+"in\n"
    f.write(new)

"""

def addItems():
    movieName = input("Item Name: ")
    discp = input("Description: ")
    price = float(input("Price per day: $"))

    print(movieName+" ("+discp+"), $"+str("%-0.2f" %(price))+ " now available for hire")
    f = open("Items.csv", 'a')
    new = movieName+","+discp+","+str(price)+","+"in\n"
    f.write(new)


#\\----------------LENGTH LIST------------------------------------------\\
"""
def numItems()
    open file in read mode
    make list of items
    numItem= len(items)
    return numItem

"""
def numItems():
    f= open("Items.csv",'r')
    items = f.readlines()
    numItem= len(items)
    return numItem



#\\----------------------MAIN FUNCTION-----------------------------------\\
"""
function main()
    display welcome message
    display menu
    get choice
    while true
        if  choice in ['l' 'L']
            call movieList()
        else if choice in ['h''H']
            call hireMovies()
        else if choice is ['r''R']
            call returnMovies()
        else if choice is ['a''A']
            call addItems()
        else if  choice in ['q''Q']
            numItem = numItems()
            print(str(numItem)+"items saved to items.csv - Have a nice day:)
        else
            print("Invalid menu choice")
"""

def main():
    print ("WELCOME \nCP1404 Assessment 1 - Let's test item for Hire in Python 3.5 style!\nItems for Hire - by Jiwan Rai - April 2016")
    numItem= numItems()
    print (str(numItem)+" items loaded from items.csv")

    while True:
        choice=input("Menu:\n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock\n(Q)uit \n\n")
        if choice in ['l','L']:
            movieList()

        elif choice in ['H','h']:
            hireMovies()

        elif choice in ['R','r']:
            returnMovies()

        elif choice in ['A','a']:
            addItems()

        elif choice in ['q','Q']:
            numItem = numItems()
            print(str(numItem)+" items saved to items.csv \n Have a nice day :)")
            break

        else:
            print ("Invalid menu choice")



main()
            
