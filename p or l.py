"""
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
"""
X = float(input())
Y = float(input())
total_selling_price = 12 * Y
profit_or_loss = total_selling_price - X
if profit_or_loss > 0:
    print(f"Profit : Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss : Rs.{abs(profit_or_loss):.2f}")
else:
    print("No Profit No Loss")
