"""
age = 20
print = 19.95
first_name = 'Laney'
is_online = True

#my code
patient_name = 'john smith'
age = 20
is_new = True
"""

'''
Write a function that reverses the words in a str.
Input: "Hello World! How are you doing today?"
'''

def reverse_words(str):
    words = str.split()
    reversed_words = words[::-1]
    reversed_str = ' '.join(reversed_words)
    return reversed_str
    

input_str = "Hello World! How are you doing today?"
reversed_str = reverse_words(input_str)
print(reversed_str)


# Bonus: Optimize your solution for the minimum number of loops
def reverse_words(string):
    # Initialize variables
    start = 0
    result = []

    # Traverse the string
    for end in range(len(string)):
        # Check for space or end of string
        if string[end] == " " or end == len(string) - 1:
            # Extract the word and add to result
            word = string[start:end + 1].strip()
            result.insert(0, word)  # Insert at the beginning for reverse order
            start = end + 1

    # Join the words back into a string
    reversed_str = ' '.join(result)

    return reversed_str

input_str = "Hello World! How are you doing today?"
reversed_str = reverse_words(input_str)
print(reversed_str)

