`Calculator`

1. Defines five functions for basic arithmetic operations: `add`, `subtract`, `multiply`, `divide`, and `floordivision`.

2. Prints a menu to select an operation: Add, Subtract, Multiply, Divide, or Floordivision.
3. Enters an infinite loop to repeatedly prompt the user for input.
4. Asks the user to enter a choice (1-5) and two numbers.
5. Based on the user's choice, calls the corresponding function with the two input numbers and prints the result.
6. Handles division by zero by returning an error message.
7. Asks the user if they want to perform another calculation.
8. If the user responds with "yes", the program loops back to the beginning. If they respond with "no", the program exits.

`OUTPUT`
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Floordivison

Enter choice (1/2/3/4/5): 1

Enter first number: 5

Enter second number: 3

Result: 8.0

Do you want to perform another calculation? (yes/no): yes

Enter choice (1/2/3/4/5): 2

Enter first number: 10

Enter second number: 4

Result: 6.0

Do you want to perform another calculation? (yes/no): yes

Enter choice (1/2/3/4/5): 4

Enter first number: 10

Enter second number: 0

Result: Error: Cannot divide by zero!

Do you want to perform another calculation? (yes/no): no