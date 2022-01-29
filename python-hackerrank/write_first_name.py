'''
What's Your Name?
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.

Input Format
The first line contains the first name, and the second line contains the last name.

Constraints
The length of the first and last name ≤ 10.

Output Format
Print the output as mentioned above.
'''

def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + ' ' + last +"!" + " You just delved into python.")

print_full_name("Md Yasen", "rafe")