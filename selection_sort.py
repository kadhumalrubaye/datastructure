#min
#compare
#swap
#[6,1,8,3,10,5]
# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#[9,1,8,2,7,3]
def selection_sor(lst):
    length=len(lst)
    # min=min(lst)
    #[9,1,8,2,7,3]
    #[9,1,8,2,7,3]
    #[1,8,2,7,3,9] pass1 here we need min
    #--------------------
   #i #[9,1,8,2,7,3] min =9
   #j #[9,1,8,2,7,3]
    #[

    for i in range(length):
        minnum=i #
        for j in range (length):
            if lst[j]<lst[minnum]:
                temp=lst[j]
                lst[j]=lst[minnum]
                lst[minnum]=temp

    print(lst)







if __name__ == '__main__':
    lst=[9,1,8,2,7,3,5]
    selection_sor(lst)
