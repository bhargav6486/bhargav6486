# 1)  WE HAVE FILLED THE MISSING VALUES IN THE FILE.

# 2)  WE HAVE SET A CONDITION THAT THE BANK BALANCE SHOULD BE GREATER THAN 30,000 &
#     THE TRANSACTION AMOUNT SHOULD BE GREATER THAN 5,000.

# 3)  AS TO SET THE AGE LIMIT WE NEED TO USE THE CUSTOMER'S DATE OF BIRTH AND SO THAT
#     BUT THERE WAS A OBSTACLE DATE [1\1\1800] SO AS TO REMOVE IT WE USED [ROW DROP] TO SKIP THAT ROW
#     WITH OBSTACLE VALUE [1\1\1800].

# 4)  AFTER THAT WE STARTED WITH THE YEAR 1980 - 2005 TO SET THE AGE LIMIT FROM 18 - 40 YEARS.

# 5)  AND AT THE END AFTER APPLYING ALL THE CONDITIONS WE PRINTED THE NUMBER OF PEOPLE WHO MEET THE
#     CONDITION.

#     THEREFORE THE TOTAL NUMBER OF PEOPLE ARE :- 33724.



import pandas as pd

df = pd.read_csv("E:/bhargav.internship/myyyyyy/Data Analytics - BankData/bank_transactions.csv")

missing_values = df.isnull().sum()
print("Missing values in the dataset:")
print(missing_values)

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())


categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

missing_values_after_imputation = df.isnull().sum()
print("Missing values in the dataset after imputation:")
print(missing_values_after_imputation)

filtered_df = df[(df['CustAccountBalance'] > 30000) & (df['TransactionAmount (INR)'] > 5000)]

rows_to_drop = df[df['CustomerDOB'] == '1/1/1800'].index
df.drop(rows_to_drop, inplace=True)

total_customers = len(filtered_df)
filtered_df = filtered_df[(filtered_df['CustomerDOB'] >= '1980-11-02') & (filtered_df['CustomerDOB'] <= '2005-01-05')]
print("People with bank balance more than 30000 and transaction amount more than 5000:")
print(filtered_df)
print("\nTotal number of customers: ", total_customers)
