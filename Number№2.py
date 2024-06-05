import sys
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
 

if len(sys.argv) < 2:
    Width = 8
    Heiht = 5
elif len(sys.argv) < 3: 
    Width = sys.argv[1]
    Heiht = 5
else: 
    Width = sys.argv[1]
    Heiht = sys.argv[2]
    
a = [Width,Heiht]



tree = ET.parse('results/results.xml')
root = tree.getroot()
x = []
y = []
for i in range(len(root)):
    for j in range(len(root[i])):
        if i == 0:
            x.append(float(root[i][j].text))
        if i == 1:
            y.append(float(root[i][j].text))
            
print(x)
print(y)
 
plt.rcParams ['figure.figsize'] = a
plt.plot(x, y)
plt.title("График функции y = 100 * sqrt(abs(A-0.01*x*x))+0.01*abs(x+10)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
