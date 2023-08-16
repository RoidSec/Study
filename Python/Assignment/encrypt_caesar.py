def shift(num, sentence):
    encryptedText = ""

    # Softcoded shift:
    shift = num

    # Iterate and shift.
    for ch in sentence:
        # shift uppercase characters
        if ch.isupper():
            # find the position in 0-25
            c_unicode = ord(ch)
            c_index = ord(ch) - ord("A")

            # shift characters
            newIndex = (int(c_index) + int(shift)) % 26
            newUnicode = newIndex + ord("A")

            # captures
            newChar = chr(newUnicode)
            encryptedText = encryptedText + newChar

    return encryptedText