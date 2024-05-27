
"""Create a simple mad-lib program that prompts for a noun, a verb, an adverb, and an adjective and injects those into a story that you create.
Example Output
       Enter a noun: dog
       Enter a verb: walk
       Enter an adjective: blue
       Enter an adverb: quickly
       Do you walk your blue dog quickly? That's hilarious!
Constraints
• Use a single output statement for this program.
• If your language supports string interpolation or string
substitution, use it to build up the output."""

def gimmie_the_noun():
    return input("Please enter a noun:")
def gimmie_the_verb():
    return input("Please enter a verb:")
def gimmie_the_adjective():
    return input("Please enter a adjective:")
def gimmie_the_adverb():
    return input("Please enter a adverb:")

def construct_the_madlib(noun,verb,adj,adv):
    return f'Do you {verb} your {adj} {noun} {adv}? That\'s hilarious!'

noun = gimmie_the_noun()
verb = gimmie_the_verb()
adj = gimmie_the_adjective()
adv = gimmie_the_adverb()

print(construct_the_madlib(noun,verb,adj,adv))