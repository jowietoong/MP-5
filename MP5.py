from matplotlib import pyplot as plt
import numpy as np

n = np.linspace(0,199,200)  

print('In entering a function use np. to math syntax. Ex: np.sin')     
    
def x(n): 
    e = eval(func)  
    return e 

func = (input("Enter a Function: ")) 

def y(n):
    
    for i in range(0,200):
    
        if n == 0:
            return -1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
        elif 0 < n and n <= 198:
            return 0.5*x(n+1) - 0.5*x(n-1)
        else:
            return 1.5*x(n) - 2*x(n-1) + 0.5*x(n-2)


x1 = [x(n) for n in n] 
y1 = [y(n) for n in n]
    
plt.plot(n, x1, color = 'm', label = 'Value of x(n)')
plt.plot(n, y1, color = 'c', label = 'Value of y(n)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show
