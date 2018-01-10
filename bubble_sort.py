def bubble_sort(lst):
    l=len(lst)
    for i in range(l-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
print("Enter list of numbers to sort")             
lst = [int(x) for x in input().split()]
bubble_sort(lst)
print(lst)
