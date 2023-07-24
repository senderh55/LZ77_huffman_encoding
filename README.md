# LZ77_huffman_encoding
As part of my data compression course, I implement the LZ77 compression and decompression algorithms and encode them using Adaptive Huffman encoding.

LZ77 compression
```sh
•	The function takes three parameters: input_string, search_buffer_size, and lookahead_buffer_size. The input_string is the data to be compressed, while search_buffer_size and lookahead_buffer_size are optional parameters that determine the sizes of the search buffer and lookahead buffer, respectively. If not provided, they default to 1024.

•	The function begins by initializing several variables: input_size is the length of the input string, cursor is a pointer to the current position in the input string, encoded_data is an empty list that will hold the compressed data

•	then enters a while loop that continues until the cursor has moved past the end of the input_string.

•	In each iteration of the loop, the function first determines the start of the search buffer and then slices the input_string to get the search buffer and lookahead buffer.

•	Then enters a for loop that iterates over each possible length of a substring in the lookahead buffer. For each length, it checks if the substring is in the search buffer. If it is, and its length is greater than the current longest match length, it updates the longest match length and index.

•	After checking all possible lengths, the function checks if it found a match. If it didn't (i.e., longest_match_length is 0), it appends a tuple of (0, first character of lookahead buffer) to encoded_data, and moves the cursor one step forward.

•	If it did find a match, it appends a tuple of (longest match index, longest match length) to encoded_data, and moves the cursor forward by the length of the match.

•	After the while loop finishes (i.e., the entire input_string has been processed), the function returns the encoded_data, which is a list of tuples representing the compressed data.

```
Adaptive Huffman encoding
```sh
•	The string to be encoded is fed into the `encode` method. The method starts with an empty result string that will gradually be filled with the binary Huffman codes.

•	For each character in the input string, the method first checks if this character has been seen before by looking it up in the `seen` array. 

•	If the character has been seen before, it already has a Huffman code in the tree. The method retrieves this code using `get_code`, adds it to the result string, and updates the tree with the `insert` method.

•	If the character is new (i.e., it has not been seen before), the method retrieves the Huffman code for NYT (Not Yet Transmitted), which serves as an indicator that a new character is being transmitted.

•	After the NYT code, the method needs to transmit the identity of the new character. This is done by converting the character into an integer `k` and calculating its binary representation in a specific way:
a.	First, the variables `e` and `r` are calculated based on `m`, the total number of possible characters.
b.	If `k` is within the range from 1 to `2*r`, the binary representation of `k-1` is calculated with `e+1` bits and appended to the result.
c.	Otherwise, the binary representation of `k-r-1` is calculated with `e` bits and appended to the result.

•	The new character is then inserted into the Huffman tree with the `insert` method. This involves adding new nodes and adjusting the positions of existing nodes to maintain the correct Huffman property.

•	This process is repeated for all characters in the input string. At the end, the `encode` method returns the result string, which is the Huffman-encoded version of the input.
```
