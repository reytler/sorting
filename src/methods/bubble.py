def bubbleSort(list):
    x=0
    for item in list:
        y=0
        for item in list:
            if list[x] < list[y]:
                temp = list[x]
                list[x] = list[y]
                list[y] = temp
            y += 1
        x+=1