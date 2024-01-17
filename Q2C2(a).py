def separate_and_convert(input_string):
    number_string = ''.join(char for char in input_string if char.isdigit())
    letter_string = ''.join(char for char in input_string if char.isalpha())

    even_numbers_ascii = [str(ord(char)) for char in number_string if int(char) % 2 == 0]
    
    uppercase_letters_ascii = [str(ord(char)) for char in letter_string if char.isupper()]

    return ''.join(even_numbers_ascii), ''.join(uppercase_letters_ascii)

input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
number_result, letter_result = separate_and_convert(input_string)

print("Number String:", number_result)
print("Letter String:", letter_result)
