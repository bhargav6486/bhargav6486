# 1)  FIRST IT READS DATA FROM THE DATASET

# 2)  THEN WE HAVE MADE A MODEL THAT IS TRAINED TO PREDICT THAT THE TRANSACTION IS FRAUD OR NOT

# 3)  BUT THIS MODEL JUST ASSUMES THAT ALL TRANSACTION ARE FRAUD FOR DEMONSTRATION

# 4)  THEN BY COMPARING THE PREDICTED LABEL WITH THE ACTUAL TABLE WE GET THE ACCURACY

# 5)  AND THE LAST WE PRINT THE ACCURACY IN TERMS OF ACCURACY SCORE THAT IS 0.99%

import pandas as pd
from sklearn.metrics import accuracy_score

# Load the CSV file
data = pd.read_csv("E:/bhargav.internship/myyyyyy/Fraud Detection/creditcard.csv")

# Assuming the last column contains labels (fraud or not fraud)
# Adjust this if your dataset structure is different
X = data.iloc[:, :-1]  # Features
y_true = data.iloc[:, -1]  # True labels

# Assuming you have a model that predicts the labels
# Replace `predicted_labels` with your actual predicted labels
# Here, it's just assumed to be all zeros for demonstration
y_pred = pd.Series([0] * len(data))

# Calculate accuracy
accuracy = accuracy_score(y_true, y_pred)

print("Accuracy:", accuracy)
