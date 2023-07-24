# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:31:38 2023

@author: sende
"""

# creating sentence 
def process_number(number):
    result = ''
    for i in range(1, 10):
        result += str(number * i)
    result *= 1000

    return result

def write_bit_code_to_file(bit_code, file_name="lz77_adaptive_huffman.bin"):
    # Convert bit code to bytes
    byte_code = bytes(int(bit_code[i:i+8], 2) for i in range(0, len(bit_code), 8))
    
    # Write bytes to binary file
    with open(file_name, 'wb') as binary_file:
        binary_file.write(byte_code)
        
def write_to_text_file(string,file_name):
    with open(file_name, "w") as file:
        file.write(string)