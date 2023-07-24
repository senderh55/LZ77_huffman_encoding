
import adaptiveHuffman
import utils


def lz77_compress(input_string, search_buffer_size=1024, lookahead_buffer_size=1024):
    input_size = len(input_string)
    cursor = 0
    encoded_data = []
    

    while cursor < input_size:
        search_buffer_start = max(0, cursor - search_buffer_size)
        search_buffer = input_string[search_buffer_start:cursor]
        lookahead_buffer = input_string[cursor:cursor + lookahead_buffer_size]

        longest_match_length = 0
        longest_match_index = -1
        buffer_len = min(lookahead_buffer_size, input_size - cursor)

        for length in range(1, buffer_len + 1):
            substring = lookahead_buffer[:length]
            position = search_buffer.rfind(substring)

            if position != -1 and length > longest_match_length:
                longest_match_length = length
                longest_match_index = len(search_buffer) - position

        if longest_match_length == 0:
            encoded_data.append((0, lookahead_buffer[0]))      
            cursor += 1
        else:
            encoded_data.append((longest_match_index, longest_match_length)) 
            cursor += longest_match_length
            
    return encoded_data

def lz77_decompress(encoded_data):
    output_string = ""

    for item in encoded_data:
        if item[0] == 0:
            # No match, just append the character
            output_string += item[1]
        else:
            # Match found in the search buffer
            match_distance, match_length = item
            # The position in the output string where the match starts
            start_pos = len(output_string) - match_distance
            # Add the matched string to the output
            for i in range(match_length):
                output_string += output_string[start_pos + i]

    return output_string


if __name__ == "__main__":
    my_id = 313314315        
    initial_sentence = utils.process_number(my_id)
    utils.write_to_text_file(initial_sentence,"Initial_sentence.txt")
    lz77_compressed = lz77_compress(initial_sentence)
    lz77_compressed_str = ''.join(['{}{}'.format(item[0], item[1]) for item in lz77_compressed])
    lz77_decompressed = lz77_decompress(lz77_compressed)
    assert initial_sentence == lz77_decompressed
    tree = adaptiveHuffman.AdaptiveHuffmanTree()
    adaptive_huffman_encoded_sentence = tree.encode(lz77_compressed_str, 10) 
    lz77_str_format = ', '.join('<{},{}>'.format(x, y) for x, y in lz77_compressed)
    utils.write_to_text_file(lz77_str_format,"LZ77_results.txt")
    utils.write_to_text_file(adaptive_huffman_encoded_sentence,"adaptive_huffman_encoded_sentence.txt")
    utils.write_bit_code_to_file(adaptive_huffman_encoded_sentence)

    
    
