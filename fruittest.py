from sklearn import tree 

features = [[140,1] , [130,1] , [150,0] , [170,0]]                          # 0 for bumpy and 1 for smooth. 
labels = [0, 0, 1, 1] 

clf = tree.Decision.TreeClassifier() 
clf = clf.fit(features, labels) 

print clf.predict([[150, 0]])                                               # 150 grams and bumpy (Input parameters) 

# The output would be 0 if it's an apple and 1 if it's an orange 
# If we hit enter , our classifier will tell us that it is an orange based on the data we provided. 


