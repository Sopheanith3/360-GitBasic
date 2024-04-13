def main():
    swap()
    strings = ['I','feel','like','a','Gucci','ad-lib','burr',]
    print(strings)
    print(get_list(strings[:3]))
    print(strings)
    print(get_list(['It','go','right','foot','up','left','foot','slide',][:3]))

def swap():
    list1 = [10,20,30,40]
    print(list1)
    list1[0],list1[2] = list1[2], list1[0],
    # Either one works first one is in one line
    #list1[0] = 30
    #list1[2] = 10
    print(list1)

    
    list2 = [5,8,15,12,18]
    print(list2)
    list2[2], list2[3] = list2[3], list2[2]
    #list2[2] = 12
    #list2[3] = 15
    print(list2)

def get_list(list_length):
    list_short = []
    for words in list_length:
        list_short = list_length
    return list_short
main()
