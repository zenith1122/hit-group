def separate_and_convert(input_string):
    # Separateing numbers and letters
    number_string = ''.join(char for char in input_string if char.isdigit())
    letter_string = ''.join(char for char in input_string if char.isalpha())

    # Converting even numbers to ASCII code Decimal values
    even_numbers_ascii = [str(ord(char)) for char in number_string if int(char) % 2 == 0]

    # Converting uppercase letters to ASCII code Decimal values
    uppercase_letters_ascii = [str(ord(char)) for char in letter_string if char.isupper()]

    return ''.join(even_numbers_ascii), ''.join(uppercase_letters_ascii)

# Example scenario
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
number_result, letter_result = separate_and_convert(input_string)

# Display all results
print("Number String:", number_result)
print("Letter String:", letter_result)
