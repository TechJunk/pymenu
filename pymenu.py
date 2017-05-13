def menu(p,d):
    a=0
    while not a:
        print()
        print(p)
        for x in p: print("=", end="")
        print("")
        c=1
        for x in d: print(str(c)+") "+x[0]);c+=1
        i=input(">")
        if(int(i)-1 in range(len(d))):
            a=1
            print()
            d[int(i)-1][1]()
        else:
            h=""
            for x in range(len(d)): h+=str(x+1)+" "
            print("Invalid choice "+i+", choose from "+h+"\n")
