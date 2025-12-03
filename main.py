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
        return []
    
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

teacher_img = PIL_Image.open("hidden_message.png").convert('RGB')

def get_color_values(image: PIL_Image.Image, channel_index: int) -> list[int]:
    color_values = []
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x,y))
            color_values.append(pixel[channel_index])
    
    return color_values
    
@dataclass
class State: 
    image: PIL_Image
    message: str
    
@route
def index(state: State) -> Page:
    return Page(state, [
        "Upload a PNG image to decrypt",       
        FileUpload("img", accept="image/png"),
        Button("Next", display_image)
        ])

@route
def display_image(state : State, new_image: bytes) -> Page:
    state.image = PIL_Image.open(io.BytesIO(new_image)).convert('RGB')

    return Page(state, [
        Image(state.image),
        Button("Decrypt", decrypt),
        Button("Back", index)
        ])

@route
def decrypt(state: State) -> Page:
    if state.image == None:
        return Page(state, ["No image uploaded.", Button("Back", index)])
    green_vals = get_color_values(state.image, 1)
    state.message = get_encoded_message(green_vals)
    return Page(state, ["Decrypted message:",
                        state.message,
                        Button("Back", index)])

start_server(State(None, "")) 
