# defining how many letters to shift
shift = 3

# input of the unencrypted message
message = (input("What is your message?"))
# Force capitalization, remove spaces and replace . with X
message = message.upper()
message = message.replace(" ","")
message = message.replace(".","X")
encryption = ""

for everyLetter in message:

    # check if character is an uppercase letter
    if everyLetter.isupper():
        # find the position in 0-25
        c_unicode = ord(everyLetter)

        c_index = ord(everyLetter) - ord("A")

        # shift characters
        newIndex = (c_index + shift) % 26
        newUnicode = newIndex + ord("A")
        #captures
        newChar = chr(newUnicode)
        encryption = encryption + newChar

print("Encrypted text:",encryption)
