list = [5,2,7,-1,-10,5,-20,-64,12,-34]

n = len(list)
i=0
while(i<n):
    if(list[i]<0):
        print(list[i],",", end="")
    i += 1