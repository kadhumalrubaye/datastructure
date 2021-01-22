def sortit(lst):
    length=len(lst)
    isSorted=True;

    for i in range(length):
        for j in range(0,length-i-1): #cuz if it was (length-i) we get out of index erro ;and if it was (length-1) it will not be effecient cuz it will repeat it self in const times althoug i has been detected the pervoius number
            if(lst[j]>lst[j+1]):
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
                isSorted=False
        if(isSorted==True):
            break
    print(lst)

if __name__ == '__main__':
    lst=[5,9,4,8,3,7,2,6,1,0]
    sortit(lst)
