import numpy as np
import matplotlib.pyplot as plt 
import sys
import json


file = sys.argv[1]

f = open(file)

data = json.load(f)

imp_dict = data.items()
imp_list = list(data.items())[1][1]

mait_list = list(data.items())[0][1]

Importance = np.array(list(imp_list.values()))

Maitrise = np.array(list(mait_list.values()))

# multiplying the arrays "importance" and "maitrise" to get the final scores
result = np.multiply(Importance,Maitrise)

print(result)
# Opening JSON file
#f = open('data.json')
# creating the dataset
courses = list(data["Importance"].keys())
values = list(result)
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='green', 
        width = 0.4)
 
plt.xlabel("Aspects environmentaux")
plt.ylabel("Indice d'impact")
plt.title("Students enrolled in different courses")
plt.savefig('test.png')