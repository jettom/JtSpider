import matplotlib.pyplot as plt

def myplot(x):
    plt.plot(x, 'o-')
    plt.show()

if __name__ == '__main__':
    x = [i**2 for i in range(20)]
    myplot(x)

