"""
Write a function based on the following specification. Only put the code of the function in the answer box. Do NOT put
any test code that do not belong to the function.

Function name:	    remove_odd

Input arguments:	1 input argument
                    sentence: a string

Returned values:	The function returns a new string constructed from the sentence by removing all the occurrences of
                    the character "$" at the odd indices exactly like the following examples.

Examples:	        If sentence is a$bc$df$gh$i then the function returns abc$dfgh$i (this is because the character $
                    appears at indices 1, 4, 7, 10, so we remove the characters at the odd indices 1 and 7 only)

For example:
Test	                                            Result
result = remove_odd(sentence="a$bc$df$gh$i")        abc$dfgh$i
print(result)
result = remove_odd(sentence="$A$B$C")              $A$B$C
print(result)
result = remove_odd(sentence="A$B$C$")              ABC
print(result)
"""


def remove_odd(sentence):
    string = sentence
    string = list(string)
    for i in range(0, len(string)):
        if i % 2 == 0:
            pass
        else:
            string[i] = string[i].replace("$", "")

    new_string = ""
    for ele in string:
        new_string += ele
    return new_string
