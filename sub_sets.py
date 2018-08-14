


def rec_sets(set,size,index,final_subset):

    if(index==-1):
        empty=[]
        final_subset.append(empty)
        rec_sets(set,size,0,final_subset)

    elif(index<size):
        element=set[index]  #new element to add
        inital=0
        len_set=len(final_subset)
        while(inital<len_set):
            sub=final_subset[inital]   #subset already in the final_subset
            copy_sub=[] #copy the subset
            for num in sub:
                copy_sub.append(num)    #copy the elements
            copy_sub.append(element)
            final_subset.append(copy_sub)
            inital+=1

        rec_sets(set,size,index+1,final_subset)


def sub_sets():

    set=[]
    final_subset=[]

    numbers=(input("Enter the numbers: "))

    tokens=numbers.split(",")

    for i in tokens:
        if "[" in i:
            sub_tokens=i.split("[")
            i=sub_tokens[1]
        elif "]" in i:
            sub_tokens=i.split("]")
            i=sub_tokens[0]
        set.append(int(i))



    rec_sets(set,set.__len__(),-1,final_subset)

    print(final_subset)



def main():
    sub_sets()

if __name__ == '__main__':
    main()