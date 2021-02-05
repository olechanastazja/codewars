'''
    Task 1: Encode function

    Implement the encode function, using the following steps:

        convert every letter of the text to its ASCII value;
        convert ASCII values to 8-bit binary;
        triple every bit;
        concatenate the result;

    For example:

    input: "hey"
    --> 104, 101, 121                  // ASCII values
    --> 01101000, 01100101, 01111001   // binary
    --> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
    --> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated

    Task 2: Decode function:

    Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:

        111 --> 101 : this can and will happen
        111 --> 11 : this cannot happen

    Note: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

    Steps:

        Split the input into groups of three characters;
        Check if an error occurred: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1, etc;
        Take each group of 8 characters and convert that binary number;
        Convert the binary values to decimal (ASCII);
        Convert the ASCII values to characters and concatenate the result

    For example:

    input: "100111111000111001000010000111111000000111001111000111110110111000010111"
    --> 100, 111, 111, 000, 111, 001, ...  // triples
    -->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
    --> 01101000, 01100101, 01111001       // bytes
    --> 104, 101, 121                      // ASCII values
    --> "hey"
'''


def encode(string):
    bits = "".join([bin(ord(i))[2:].zfill(8) for i in string])
    return "".join([str(i)*3 for i in bits])


print(encode("hey"))


def decode(bits):
    triples = [str(bits)[i:i+3] for i in range(0, len(str(bits)), 3)]
    bytes = [max(set(i), key=i.count) if len(set(i)) > 1 else next(iter(set(i))) for i in triples]
    return ''.join([chr(int(''.join(bytes[i:i+8]), 2)) for i in range(0, len(bytes), 8)])


print(decode(100111111000111001000010000111111000000111001111000111110110111000010111))
