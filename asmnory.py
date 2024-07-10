import re


# Enable to remove non BiNOry characters.
remove_comments = False

# All the simple numbers
simple_numbers = {
    "0": "111110010",
    "1": "1",
    "2": "1110",
    "3": "1111010",
    "4": "1110111010",
    "5": "1111110101010",
}


# Strip all non BiNOry characters.
def strip_non_binory(string: str):
    return re.sub("[^01]", "", string)


# Count the amount of BiNOry commands.
def count_binory(string: str):
    return len(strip_non_binory(string))


# For strings.
def control_chars(string: str):
    return string.replace("\\n", "\n").replace("\\s", " ").replace("\\0", "\0")


# Create the smallest BiNOry code to add a number to the stack.
def get_num(num: int):
    negetive = num < 0
    num = abs(negetive)
    
    if str(num) in simple_numbers:
        string = simple_numbers[str(num)]
        if negetive:
            string += " 11100"
    else:
        string1 = f"1{' 110'*(num-1)}"

        bits = str(bin(num))[2:]

        i = 0
        amount = 0
        string2 = f"1 "
        while i <= len(bits)-2:
            if bits[-(i+1)] == "1":
                string2 += f"{get_num(3)}0{get_num(3)}010 "
                amount += 1
            else:
                string2 += f"{get_num(3)}010 "
            i += 1

        string2 += "10"*amount

        if count_binory(string1) > count_binory(string2):
            string = string2
        else:
            string = string1

        if negetive:
            string += " 11100"

        return string


# Compile AsmNOry.
# file_name should not contain the extension.
def compile_asmnory(file_name: str):
    input_file_name = file_name + ".ano"
    output_file_name = file_name + ".bno"