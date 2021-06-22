import time
def selection_sort(data, drawData, timeTick):
    n = len(data)
    k = n - 1
    for j in range(0,k-1):
        min = 1000
        i2 = -1
        for i in range(j,n):
            if(min>data[i]):
                min=data[i]
                i2=i


        data[j],data[i2]=data[i2],data[j]
        drawData(data, ['green' if x == j or x == i2 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])