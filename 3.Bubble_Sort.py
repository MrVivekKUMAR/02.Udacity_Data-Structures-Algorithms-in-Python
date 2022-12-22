
def bubble_sort(lst):
    upperCount = 1
    while upperCount <= len(lst) - 1:
        count = 1
        while count <= len(lst) - 1:
            print(f"Count is : {count} and UpperCount is {upperCount}")
            if lst[count-1] > lst [count]:
                temp = lst[count-1]
                lst[count - 1] = lst [count]
                lst[count] = temp
            count += 1
            print(lst)
        upperCount +=1
    return lst


lst = [8,5,3,1,6,7,4]
bubble_sort(lst)
