`Line Regression`

1. The code reads a CSV file named "HousingData.csv" into a Pandas DataFrame.

2. It checks for missing values and replaces them with the mean of the respective column.
3. It performs outlier detection and replacement using the Interquartile Range (IQR) method for each column.
4. It creates box plots for each column to visualize the data distribution.
5. It splits the data into training and testing sets using 'train_test_split`.
6. It trains a Linear Regression model on the training data and evaluates its performance using Mean Squared Error (MSE) on the testing data.

`OUTPUT`

Mean Squared Error: 21.4321