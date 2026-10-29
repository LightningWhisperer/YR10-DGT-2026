# 30/10/2026
# Jean de Klerk
# Fence cost calculator
# Version 3

# Error Checking
def num_check(question):

    # Error checking that a number is more than 0
    error_0 = "Please enter a number that is more than 0\n"
    # Error checking that a number is valid (not a word or roman numerals)
    error_message = "Please enter a valid number\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error_0)

        except ValueError:
            print(error_message)

# Main Routine
keep_going = ""
while keep_going == "":
    # Credits
    print("Coding and formatting by JDK, with the use of Visual Studio code. This project was last updated 30/10/2026")

    # Title
    print("________________________________________")
    print("| W𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖊 𝕱𝖊𝖓𝖈𝖊 𝕮𝖔𝖘𝖙 𝕮𝖆𝖑𝖈𝖚𝖑𝖆𝖙𝖔𝖗 |")
    print("<--------------------------------------->")
    print()

    # Introduction
    print("This programme is designed to calculate the cost of your fence based on its price per meter. \n simply answer the questions below, and the program will calculate the price.")
    print()

    # Ask user for length of the fence
    print("***************************************************")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ʟᴇɴɢᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)? ")
    print("***************************************************")
    length = num_check ("Answer: ")
    print()

    # Ask user for width of the fence
    print("*************************************************")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ᴡɪᴅᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)?")
    print("*************************************************")
    width = num_check ("Answer: ")

    # Work out perimeter
    perimeter = 2 * (width + length)
    print()

    # Ask user for $/m of fence
    print("************************************************************")
    print("     ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʀɪᴄᴇ ᴘᴇʀ ᴍᴇᴛᴇʀ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ ($) ")
    print("************************************************************")
    cost = num_check ("Answer: ")
    print()

    # Work out cost of the perimeter of the fence
    cost_of_fence = perimeter * cost

    # Display cost of the fence
    print("******************************************************")
    print(f"ᴛʜᴇ ᴄᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ ɪꜱ ${cost_of_fence}")
    print("******************************************************")
    print()

    # Ask if the User wants to keep going
    print("Do you want to keep going?")
    print("--")
    keep_going = input("Press enter to keep going or any key to quit  ")
    print()

    
    print("Thank you for using the fence cost calculator!")
