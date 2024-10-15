"""
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
Marks scored  Grade 
100           S
90 - 99       A
80 - 89       B
70 - 79       C
60 - 69       D
50 - 59       E
<50           F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C
"""
n=int(input())
if n==100:
  print("s")
elif n>=90 and n<=99:
  print("A")
elif n>=80 and n<=89:
  print("B")
elif n>=70 and n<=79:
  print("C")
elif n>=60 and n<=69:
  print("D")
elif n>=50 and n<=59:
  print("E")
elif  n<=50:
  print("F")
else:
  print("Invalid")
