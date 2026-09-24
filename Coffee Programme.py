# Creating a hot chocolate programme that a user will be able to interact with.
# Jean de Klerk
# 23/9/26
# Version 1

# TODO: record an input (store the answer)
#       check for valid answer (input checker)
#       Ask questions and respond

# Ask the user whether they like hot chocolate or not
like_hot_chocolate = input("Do you like hot chocolate? ")
print(like_hot_chocolate) #checking input is stored
print(f"Your answer was '{like_hot_chocolate}'.")

# Check the input and respond
if like_hot_chocolate == "Yes" or "y" or "yea" or "yeah" or "Y" or "Yea" or "Yeah" or "Of course" or "of course" or "yes":
    print("That is great! I like hot chocolate too.")
else:
    print("You are missing out! Why not give it a try?")

