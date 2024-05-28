"""
Create a program that prompts for an input string and dis- plays output that shows the input string and the number of characters the string contains.
Example Output
       What is the input string? Homer
       Homer has 5 characters.
Constraints
• Be sure the output contains the original string.
• Use a single output statement to construct the output.
• Use a built-in function of the programming language to
determine the length of the string.
"""

def string_counter() -> str:
    input_string = input("Please input a string to this program:")
    length = len(input_string)
    if length == 0:
        print("Please enter a valid string")
        return string_counter()
    else:
        return (f' {input_string} has {length} characters')

if __name__ == "__main__":
    string_counter()