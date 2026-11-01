# 31/11/2026
# Jean de Klerk
# Fence cost calculator
# Version 5

# Error Checking
def num_check(question):

    # Error checking that a number is more than 0
    error_0 = "<<ERROR>> PLEASE ENTER A NUMBER LARGER THAN 0 \n"
    # Error checking that a number is valid (not a word or roman numerals)
    error_message = "<<ERROR>> PLEASE ENTER A VALID NUMBER\n"
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
    print()
    print("Coding and formatting by JDK, with the use of Visual Studio code. This project was last updated 1/11/2026")
    print()

    # Title
    print(" <--______________________________________-->")
    print("   |                                      |")
    print("   | W𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖊 𝕱𝖊𝖓𝖈𝖊 𝕮𝖔𝖘𝖙 𝕮𝖆𝖑𝖈𝖚𝖑𝖆𝖙𝖔𝖗 |")
    print("   |                                      |")
    print("<<<----------------------------------------->>>")
    print()

    # Introduction
    print("This programme is designed to calculate the cost of your fence based on its price per meter. \nSimply answer the questions below, and the program will calculate the cost of your fencing.")
    print()

    # Ask user for length of the fence
    print(".~~~~-------------------------------------------~~~~,")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ʟᴇɴɢᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)? ")
    print(".~~~~-------------------------------------------~~~~,")
    print()
    length = num_check ("Answer: ")
    print()

    # Ask user for width of the fence
    print(".~~~~-------------------------------------------~~~~,")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ᴡɪᴅᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)?")
    print(".~~~~-------------------------------------------~~~~,")
    print()
    width = num_check ("Answer: ")
    print()

    # Ask user what type of fence they are pricing
    print(".~~~~-------------------------------------------~~~~,")
    print("         ᴡʜᴀᴛ ᴛʏᴘᴇ ᴏꜰ ꜰᴇɴᴄᴇ ᴀʀᴇ ʏᴏᴜ ʙᴜɪʟᴅɪɴɢ? ")
    print(".~~~~-------------------------------------------~~~~,")
    print()
    fence_type = input("Answer: ")
    print()
    print(f"That's Great! {fence_type} is such a lovely choice ♡!")

    # Work out perimeter
    perimeter = 2 * (width + length)
    print()

    # Ask user for $/m of fence
    print(".~~~~----------------------------------------------------~~~~,")
    print("     ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʀɪᴄᴇ ᴘᴇʀ ᴍᴇᴛᴇʀ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ ($) ")
    print(".~~~~----------------------------------------------------~~~~,")
    print()
    cost = num_check ("Answer: ")
    print()

    # Work out cost of the perimeter of the fence
    cost_of_fence = perimeter * cost

    # Work out the price with added GST (gst15 represents 15%)
    gst15 = cost_of_fence * 1.15

    # Loading Animation

    import time
    for _ in range(3):
        for i in range (1,4):
            # "______" clears out any previous 'dots'
            print("Loading" + "." * i + "    ", end="\r", flush=True)
            time.sleep(0.5)
    print()
    print("ALL DONE!")

    # Display cost of the fence without GST
    print(".~~~~----------------------------------------------------~~~~,")
    print(f"    ᴛʜᴇ ᴄᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (Excluding GST) ɪꜱ ${cost_of_fence:.2f}") # ".2f" means that the number is formatted with two decimal points
    print(".~~~~----------------------------------------------------~~~~,")
    print()

    # Display cost of the fence with GST
    print("******************************************************")
    print(f"ᴛʜᴇ ᴄᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (Including GST) ɪꜱ ${gst15:.2f}")
    print("******************************************************")
    print()

    # SUmmay of information entered and outputs
    print("========== FENCE SUMMARY ==========")
    print(f"Length: {length} meters")
    print(f"Width: {width} meters")
    print(f"Perimeter: {perimeter} meters")
    print(f"Type of fence evaluated: {fence_type}")
    print(f"Price per metre: ${cost:.2f}")
    print(f"Cost (ex GST): ${cost_of_fence:.2f}")
    print(f"Cost (inc GST): ${gst15:.2f}")
    print("===================================")
    print()

    # Ask if the User wants to keep going
    print("Do you want to keep going?")
    print("--")
    keep_going = input("Press <enter> to keep going or any key to quit  ")
    print()

    print("_________________________________________________")
    print("| Thank you for using the fence cost calculator! |")
    print("_________________________________________________")
    print()
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("     𝕀𝕗 𝕪𝕠𝕦 𝕖𝕟𝕛𝕠𝕪𝕖𝕕 𝕥𝕙𝕚𝕤 𝕡𝕣𝕠𝕕𝕦𝕔𝕥, 𝕡𝕝𝕖𝕒𝕤𝕖 𝕔𝕠𝕟𝕤𝕚𝕕𝕖𝕣 𝕤𝕡𝕠𝕟𝕤𝕠𝕣𝕚𝕟𝕘 𝕒 \n        𝕔𝕠𝕗𝕗𝕖𝕖 𝕥𝕠 𝕙𝕖𝕝𝕡 𝕞𝕒𝕚𝕟𝕥𝕒𝕚𝕟 𝕤𝕚𝕥𝕖 𝕔𝕠𝕤𝕥𝕤.☕︎")
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print(" This site has 4 star review on google. Please consider leaving a review!")
    print(" ★ ★ ★ ★ ☆")
    print()
    print(".~~~~----------------------------------------------------~~~~,")
    print("                  𝒫𝓁𝑒𝒶𝓈𝑒 𝓁𝑒𝒶𝓋𝑒 𝒶 𝓇𝑒𝓋𝒾𝑒𝓌               ")
    print(".~~~~----------------------------------------------------~~~~,")
    leave_a_review = ("Review: ")
    print()
    print("Unknown_User8:       {leave_a_review}")
