from matplotlib import pyplot as plt

print(1174063%3+2)

def plot():
    x = [1,3,5,7,9,11,13]
    y = [12,22,32,42,52,67,89]

    x1 = [10,7,13,4,5]
    y1 = [2,3,2,7,9]

    x2 = [20,50,60,10,40,20,90]
    y2 = [30,50,70,90,20,80,10]

    plt.subplot(221)
    plt.plot(x,y)
    plt.subplot(222)
    plt.plot(x1,y1)
    plt.subplot(223)
    plt.plot(x2,y2)
    plt.show()