# ----- All important import statements -----
from bakery import assert_equal
from dataclasses import dataclass, field
from PIL import Image as PIL_Image
from drafter import *
import io

set_site_information(
    author="dtanuj@udel.edu",
    description="""A brief description of what your website does.
    Use a triple quoted string if you want to span multiple lines.""",
    sources=["N/A Right now but will add when I do"],
    planning=["Project_planning.pdf"],
    links=["https://github.com/UD-F25-CS1/cs1-website-f25-TanujDontaraju, Youtubelink""]
)
hide_debug_information()
set_website_title("Your Website Title")
set_website_framed(False)

hide_debug_information()
set_website_title("Your Drafter Website")
set_website_framed(False)


# ----- Start of decoding code ----- 
def even_or_odd_bit(number: int) -> str:
    """
    Function determines if number is even or odd
     
    Argument:
            number (int): Integer to check
     
    Return:
            str: If number is odd, then "1" outputs, othwerise if number is even, then "0" outputs
    """
    if number % 2 != 0:
        return "1"
    else:
        return "0"

assert_equal(even_or_odd_bit(1), "1")
assert_equal(even_or_odd_bit(2), "0")
assert_equal(even_or_odd_bit(67), "1")
assert_equal(even_or_odd_bit(88), "0")

def decode_single_char(eight_numbers: list[int]) -> str:
    """
    Decodes a list of 8 number values into a ASCII characters
     
    Args:
            eight_numbers (list[int]): List of 8 number values
        
    Returns:
            str: Decoded ASCII character. Returns empty if list is empty or isn't 8 values inside the list
    """
    binary_string = ""
    if not eight_numbers or len(eight_numbers) != 8:
        return ""
    for number in eight_numbers:
        value = even_or_odd_bit(number)
        binary_string += value
        
    ascii_value = int(binary_string, 2)
    final_character = chr(ascii_value)
    return final_character

assert_equal(decode_single_char([46, 47, 46, 46, 47, 44, 46, 44]), "H")
assert_equal(decode_single_char([46, 46, 47, 46, 46, 46, 46, 47]), "!")
assert_equal(decode_single_char([46, 47, 46, 46, 47, 44, 46, ]), "")
assert_equal(decode_single_char([]), "")

def decode_chars(color_intensity_values: list[int], values_to_decode: int) -> str:
    """
    Decodes sequence of color intensity values into a string of ASCII characters.
     
    Args: 
        color_intensity_values (list[int]): List of color integer values numbers in int format
        values_to_decode (int): Number of characters to decode
     
    Returns:
        str: Decoded string of characters
        None: When length isn't 8 * values_to_decode
    """
    if len(color_intensity_values) != 8 * values_to_decode:
        return None
    
    decoded_message = ""
    
    for i in range(values_to_decode):
        first = i * 8
        last = first + 8
        full = color_intensity_values[first:last]
        decoded_message += decode_single_char(full)
        
    return decoded_message

assert_equal(decode_chars([46, 47, 46, 46, 47, 44, 46, 44
                            , 46, 47, 47, 46, 46, 44, 44, 46], 2), "H`")

assert_equal(decode_chars([46, 47, 46, 46, 47, 44, 46, 44], 1), "H")

assert_equal(decode_chars([46, 47, 46, 46, 47, 44, 46, 44
                            , 46, 47, 47, 46, 46, 44, 44, 46], 1), None)

assert_equal(decode_chars([], 1), None)

def get_message_length(color_intensity_values: list[int], length: int) -> int:
    """
    Determines numeric length of message econded within list of color intensity values
     
    Args:
        color_intensity_values (list[int]): List of integer color intenstiy  values representing encoded character data
        length (int): Expected number of characters in decoded message
    """
    if len(color_intensity_values) != 8 * length:
        return 0
    
    total = 8 * length
    decode = decode_chars(color_intensity_values[0: total], length)
    
    if decode == None: 
        return 0
    
    for d in decode:
        if d < "0" or d > "9":
            return 0
    
    int_decode = int(decode)
    return int_decode

assert_equal(get_message_length([20, 254, 45, 95, 40, 90, 20, 40, 200, 254, 45,
                           95, 40, 95, 20, 45,220, 250, 45, 95, 48, 95, 24, 44], 3), 54)

assert_equal(get_message_length([20, 254, 45, 95, 40, 90, 20, 40, 200, 254, 45,
                           95, 40, 95, 20, 45,220, 250, 45, 95, 48, 95, 24], 3), 0)

assert_equal(get_message_length([100, 150, 200, 250, 50, 75, 125, 175, 
                                100, 150, 200, 250, 50, 75, 125, 175,
                                100, 150, 200, 250, 50, 75, 125, 175], 3), 0)

def get_encoded_message(color_intensity_values: list[int]) -> str:
    """
    Decodes hidden message from list of color intensity values.
     
    Args: 
        color_intensity_values (list[int]): List of integer color intensity values containing
                                            header and encoded message
                                  
    Returns: 
        str: Decoded message as a string
    """
    header_values = color_intensity_values[: 24]
    
    message_length = get_message_length(header_values, 3)
    
    if message_length == 0:
        return ""
    
    start = 24
    end = start + (message_length * 8)
    message_values = color_intensity_values[start: end]
    message = decode_chars(message_values, message_length)
    return message

assert_equal(get_encoded_message([254, 254, 255, 255, 254, 254, 254, 254, 
                           254, 254, 255, 255, 254, 254, 254, 254, 
                           254, 254, 255, 255, 254, 254, 255, 254, 
                           254, 255, 254, 254, 255, 254, 254, 254, 
                           254, 255, 255, 254, 255, 254, 254, 255, 
                           254, 254, 254, 254, 254, 254, 254, 254, 
                           254, 254, 254, 254, 254, 254, 254, 254, 
                           254, 254, 254, 254, 254, 254, 254, 254, 
                           254, 254, 254, 254, 254, 254, 254, 254, 
                           254, 254, 254, 254, 254, 254, 254, 254, 
                           252]), "Hi" )


# Can't unit test function because grading system won't have all images I have locally
def get_color_values(image: PIL_Image.Image, channel_index: int) -> list[int]:
    """
    Gets all pixel values from once color channel in an image. Goes through each pixel to figure out the RGB values
    
    Args:
        image (PIL_Image.Image): Image to read from
        channel_index (int): Which color channel to use.
        
    Return:
        list[int]: List of pixel values from chosen channel
    """
    color_values = []
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x,y))
            color_values.append(pixel[channel_index])
    
    return color_values

# ----- Start of encoding code -----
def get_message(max_characters: int) -> str:
    """
    Asks user to enter secret message and if message is > max_characters, the the user has to reinput unitl the message's characters match the max_characters value
    
    Args:
        max_characters(int): Max length of characters in message
        
    Return: 
        str: Message by user that isn't longer than max_characters value
    """
    message = input("Enter secret message: ")
    while len(message) > max_characters:
        print("Your message is to long with" + str(len(message)) + " characters")
        message = input("Enter secret message: ")
    
    return message

# These unit tests commented out because they need manual
# user input in console, which stops drafter from working
# automatically without user interference, but these unit
# tests 100% do work
# assert_equal(get_message(5), "hello")
# assert_equal(get_message(0), "")
# assert_equal(get_message(1), "T")

def prepend_header(hidden_message: str) -> str:
    """
    Put the length of the hidden message right before the message
     
    Args:
        hidden_message(str): Message that will have length prepended to the front
        
    Return:
        str: New string with the length of the hidden_message, and the hidden_message text
    """
    length = (len(hidden_message))
    
    if length < 10: 
        string_length = "00" + str(length)
    elif length < 100:
        string_length = "0" + str(length)
    else:
        string_length = str(length)
    return string_length + hidden_message

assert_equal(prepend_header("Hi!"), "003Hi!")
assert_equal(prepend_header("S o S"), "005S o S")
assert_equal(prepend_header("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "026ABCDEFGHIJKLMNOPQRSTUVWXYZ")
assert_equal(prepend_header(""), "000")
assert_equal(prepend_header
             ("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"),
             "110BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")


def message_to_binary(ascii_characters: str) -> str:
    """
    Converts string of ASCII characters into binary digit representation (0 and 1)
     
    Args:
        ascii_characters (str): Sting containing ASCII characters to convert.
        
    Return:
        str: String of 0 and 1 reprsenting binary equivalence of the ASCII character string. 
    """
    binary = ""
    for ascii in ascii_characters:
        binary += format(ord(ascii), "08b")
    
    return binary

assert_equal(message_to_binary("Hi"), "0100100001101001")
assert_equal(message_to_binary("058"),"001100000011010100111000")
assert_equal(message_to_binary("Bye"),"010000100111100101100101")
assert_equal(message_to_binary(""),"")

def new_color_value(color_intensity_value: int, single_bit: str) -> int:
    """
    Adjusts color intesnity value to single bit 
     
    Rules:
    If we are hiding a ‘1’ bit, we want the color intensity value to be an odd Base 10 number:
        - If the color intensity value is even, we will add 1 to it so that it is odd. (By adding a 1 we are not changing the color intensity value that much.)
        - If the color intensity value is already odd, we do not change it.
    If we are hiding a ‘0’ bit, we want the color intensity value to be an even Base 10 number.
        - If the color intensity value is already even, we do not change it.
        - If the color intensity value is odd, we will subtract 1 from it so that it is even. (By subtracting 1 we are not changing the color intensity value that much.)
        
   Args:
       color_intensity_values(int): Original Base 10 color intensity value.
       single_bit (str): Bit to hide which is 0 or 1.
       
   Return:
       int: Adjusted Base 10 color with hidden bit value.
    """
    if single_bit == "1":
        if color_intensity_value % 2 == 0:
            return color_intensity_value + 1
        else:
            return color_intensity_value
    elif single_bit == "0":
        if color_intensity_value % 2 == 0:
            return color_intensity_value
        else:
            return color_intensity_value - 1

assert_equal(new_color_value(1, "0"), 0)
assert_equal(new_color_value(2, "1"), 3)
assert_equal(new_color_value(0, "0"), 0)
assert_equal(new_color_value(1, "1"), 1)

def hide_bits(image: PIL_Image, binary_string: str) -> PIL_Image:
    """
    Hides binary string inside image by modifying least significant bit of red channel of each pixel as it doens't make too much of a difference
    in color picture
     
    Args:
        image (PIL_Image): Pillow image in RGB mode where message whill be hidden
        binary_string (str): String of 0 and 1 representing the bits
        
    Return:
        PIL_Image: New Pillow Image object with hidden message.
    """
    new_img = image.copy()
    width, height = new_img.size
    index = 0
    
    for y in range(height):
        for x in range(width):
            
            if index >= len(binary_string):
                return new_img
            
            r, g, b = new_img.getpixel((x, y))
            
            if index < len(binary_string):
                r = new_color_value(r, binary_string[index])
                index +=1
            
            new_img.putpixel((x, y), (r, g, b))
    
    return new_img

test_img_hide = PIL_Image.new("RGB", (2, 1), "black")
test_img_hide.putpixel((0, 0), (10, 0, 0))
test_img_hide.putpixel((1, 0), (10, 0, 0))
binary_to_hide = "10"
result_img = hide_bits(test_img_hide, binary_to_hide)
assert_equal(result_img.getpixel((0, 0))[0], 11)
assert_equal(result_img.getpixel((1, 0))[0], 10)

