import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

df = pandas.read_excel(r"C:\Users\Uzair\Documents\warzonedropdata.xlsx",engine='openpyxl')
dfsheet = pandas.read_excel(r"C:\Users\Uzair\Documents\warzonedropdata.xlsx", sheet_name = [1],engine='openpyxl')

Flight = ["Security area","living quarters","factory","headquarters","control center","shore ","prison block","harbour","chemical engineering","decon zone","bioweapon labs"]
Circle = ["Security area in circle","living quarters in circle","factory in circle","headquarters in circle","control center in circle","shore in circle","prison block in circle","harbour in circle","chemical engineering in circle","decon zone in circle","bioweapon labs in circle"]
Land = ["Die on Landing?","Outcome"]



###data####

FlightPath = df[["Security area","living quarters","factory","headquarters","control center","shore ","prison block","harbour","chemical engineering","decon zone","bioweapon labs"]]
InCircle = df[["Security area in circle","living quarters in circle","factory in circle","headquarters in circle","control center in circle","shore in circle","prison block in circle","harbour in circle","chemical engineering in circle","decon zone in circle","bioweapon labs in circle"]]
Landing = df[["Die on Landing?","Land in Circle?","where did you land?","Outcome"]]

dfs = [FlightPath,InCircle,Landing]
dataframe = dfs[0].join(dfs[1:])

###mapping####

labels = {"Security area":1,"living quarters":2,"factory":3,"headquarters":4,"control center":5,"shore ":6,"prison block":7,"harbour":8,"chemical engineering":9,"decon zone":10,"bioweapon labs":11}
dataframe["where did you land?"] = dataframe["where did you land?"].map(labels)

###Features###
features = Flight + Circle + Land
X =  dataframe[features]
y = dataframe['where did you land?']


##Plot Decision Tree##
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png(r"C:\Users\Uzair\Documents\mydecisiontree.png")

img=pltimg.imread(r'C:\Users\Uzair\Documents\mydecisiontree.png')
imgplot = plt.imshow(img)

######to show decision tree uncomment below##########
#plt.show()

##Prediction##

d = dfsheet[1]
input = list(d[features].iloc[0])
output = dtree.predict([input])

# function to return key for any value
def get_key(val):
    for key, value in labels.items():
        if val == value:
            return key

print(get_key(int(output)))

print(input)




