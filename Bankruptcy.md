`Bankruptcy`

1. Load data: Reads a CSV file named 'data.csv' into a Pandas DataFrame. Output: Missing values in the dataset.

2. Preprocess data: Drops the 'Bankrupt?' column as the target variable and stores the rest as features.
3. Oversample using RandomOverSampler: Balances the class distribution by oversampling the minority class using the RandomOverSampler. Output: Original and resampled class distribution.
4. Split data: Divides the resampled dataset into training and testing sets with a test size of 0.2.
5. Train the model: Initializes and trains a Random ForestClassifier using the training set.
6. Predict on the test set: Generates predictions on the test set using the trained classifier.
7. Calculate metrics: Computes Mean Square Error (MSE) and accuracy to evaluate the model's performance. Output: Mean Square Error and Accuracy.

`OUTPUT`

Mean Square Error: 0.003409090909090909

Accuracy: 0.9965909090909091
