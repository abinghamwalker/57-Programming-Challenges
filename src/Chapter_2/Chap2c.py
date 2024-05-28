"""
Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.
Example Output
       What is the quote? These aren't the droids you're looking for.
       Who said it? Obi-Wan Kenobi
       Obi-Wan Kenobi says, "These aren't the droids
       you're looking for."
Constraints
• Use a single output statement to produce this output, using appropriate string-escaping techniques for quotes.
• If your language supports string interpolation or string substitution, don't use it for this exercise. Use string
concatenation instead.

"""

def what_is_your_quote():
    return input("What is the quote?")

def who_said_it():
    return input("Who said it?")

def add_it_together(what,who):
    output = who + " says, " + what
    return output

what = what_is_your_quote()
who = who_said_it()
print(add_it_together(what,who))