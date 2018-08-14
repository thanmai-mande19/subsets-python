

class players:
    shirt_num=0
    goals=0
    def __init__(self,shirt,goals):
        self.goals=goals
        self.shirt_num=shirt
    def shirt(self):
        return self.shirt_num
    def goals_r(self):
        return self.goals
    def scored(self):
        self.goals+=1


def rec_sets(arr,size,index,final):

    if(index==-1):
        empty=[]
        final.append(empty)
        rec_sets(arr,size,0,final)

    elif(index<size):
        element=arr[index]
        v=0
        z=len(final)
        while(v<z):
            x=final[v]
            x_y=[]
            for t in x:
                x_y.append(t)
            x_y.append(element)
            final.append(x_y)
            v+=1

        rec_sets(arr,size,index+1,final)


def sub_sets():

    array=[]
    final=[]

    numbers=(input("Enter the numbers: "))

    tokens=numbers.split(",")

    for i in tokens:
        array.append(int(i))

    rec_sets(array,array.__len__(),-1,final)

    print(final)



def main():
    #sub_sets()
    hazard=players(10,70)

    print(hazard.goals_r())
    hazard.scored()
    print(hazard.goals_r())

if __name__ == '__main__':
    main()