import xml.etree.ElementTree as ET
 
tree = ET.parse('results.xml')
root = tree.getroot()
x = []
y = []
for i in range(len(root)):
    for j in range(len(root[i])):
        if i == 0:
            x.append(int(root[i][j].text))
        if i == 1:
            y.append(int(root[i][j].text))
            
plt.plot(x, y)
plt.title("График функции y = 100 * sqrt(abs(A-0.01*x*x))+0.01*abs(x+10)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(x)
print(y)
