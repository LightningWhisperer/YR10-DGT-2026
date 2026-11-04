# 4/11/2026
# Jean de Klerk
# Fence cost calculator
# Version 7

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
    print("Coding and formatting by JDK, with the use of Visual Studio code. This project was last updated 4/11/2026")
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
    section = "=" * 50
    subsection = "-" * 50
    print(f"{section}")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ʟᴇɴɢᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)? ")
    print(f"{section}")
    print()
    length = num_check ("Answer: ")
    print()

    # Ask user for width of the fence
    print(f"{section}")
    print("     ᴡʜᴀᴛ ɪꜱ ᴛʜᴇ ᴡɪᴅᴛʜ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (ᴍᴇᴛᴇʀꜱ)?")
    print(f"{section}")
    print()
    width = num_check ("Answer: ")
    print()

    # Ask user what type of fence they are pricing
    print(f"{subsection}")
    print("        ᴡʜᴀᴛ ᴛʏᴘᴇ ᴏꜰ ꜰᴇɴᴄᴇ ᴀʀᴇ ʏᴏᴜ ʙᴜɪʟᴅɪɴɢ? ")
    print(f"{subsection}")
    print()
    fence_type = input("Answer: ").title() # Makes the input capatilised (if not already)
    print()
    print(f"♡ That's Great! {fence_type} is such a lovely choice! ♡")

    # Work out perimeter
    perimeter = 2 * (width + length)
    print()

    # Ask user for $/m of fence
    print(f"{section}")
    print("ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʀɪᴄᴇ ᴘᴇʀ ᴍᴇᴛᴇʀ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ ($) ")
    print(f"{section}")
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
        for i in range (0,4):
            # "______" clears out any previous 'dots'
            print("Processing" + "." * i + "    ", end="\r", flush=True) # \r resets the line to the start, flush=true removes the previous line before rewriting it
            time.sleep(0.5)

    # Display cost of the fence without GST
    print()
    time.sleep(1)
    print()
    print(f"{section}")
    print(f"   ᴛʜᴇ ᴄᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (Excluding GST) ɪꜱ ${cost_of_fence:.2f}") # ".2f" means that the number is formatted with two decimal points (like money)
    print(f"{section}")
    print()

    # Display cost of the fence with GST
    import time
    for _ in range(3):
         for i in range (0,4):
            print("Calculating cost with GST" + "." * i + "    ", end="\r", flush=True)
            time.sleep(0.5)
    print()
    time.sleep(1)
    print("******************************************************")
    print(f"ᴛʜᴇ ᴄᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ꜰᴇɴᴄᴇ (Including GST 15%) ɪꜱ ${gst15:.2f}")
    print("******************************************************")
    print()
    time.sleep(2)

    # SUmmay of information entered and outputs
    import time
    for _ in range(2):
             for i in range (0,4):
                print("Printing Summary" + "." * i + "    ", end="\r", flush=True)
                time.sleep(0.5)

    print()
    print("========== FENCE SUMMARY ==========")
    print(f"       Length: {length} meters")
    print(f"       Width: {width} meters")
    print(f"       Perimeter: {perimeter} meters")
    print(f"       Type of fence evaluated: {fence_type}")
    print(f"       Price per metre: ${cost:.2f}")
    print(f"       Cost (ex GST): ${cost_of_fence:.2f}")
    print(f"       Cost (inc GST): ${gst15:.2f}")
    print("===================================")
    print()

    # Ask if the User wants to keep going
    print("Do you want to keep going?")
    print("--")
    keep_going = input("Press <enter> to keep going or any key to quit  ")
    print()

    # End proramme after asking for a review
    if keep_going != "":  # The exclamation means it is 'not equal' to an empty string (meaning the user didn"t just press <enter>)
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
        print(" This site has a 4 star review on google. Please consider leaving a review!")
        print(" ★ ★ ★ ★ ☆")
        print()

        # Leave a review!
        print(".~~~~----------------------------------------------------~~~~,")
        print("                  𝒫𝓁𝑒𝒶𝓈𝑒 𝓁𝑒𝒶𝓋𝑒 𝒶 𝓇𝑒𝓋𝒾𝑒𝓌               ")
        print(".~~~~----------------------------------------------------~~~~,")
        leave_a_review = input("Review: ")
        print()
        print()
        print(f"(YOUR REVIEW) Unknown_User8:       {leave_a_review}")
        print()
        print("Bah.bah.blacksheep:      This program is so useful. I really appreciate the throughtful work that has gone into this.\n                          This site perfectly calculated the cost of my fence, thus helping me to prepare accordingingly.")
        print()
        print("twinkle-little-star:     Although I appreciate this website, it is not the most aesthetically pleasing and therefore \n                          I am still on the hunt for a better program.")
        print()
        print()
        print()

        if leave_a_review != "":
            print("✓ Review submitted successfully!")
        print("Thank you for your contribution!")
