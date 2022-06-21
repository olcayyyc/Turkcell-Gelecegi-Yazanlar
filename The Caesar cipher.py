import string

alphabet =' ' + string.ascii_lowercase

#What is the value of the key n in the positions dictionary?
positions = {}
index = 0
for char in alphabet:
    positions[char] = index
    index += 1
    
print(positions['n'])

#Use positions to create an encoded message based on message where each character in message has been shifted-
#forward by 1 position, as defined by positions.
#Note that you can ensure the result remains within 0-26 using result % 27.
#İf you change encoded_position = (position +3) % 27, results will be same.
message = "hi my name is caesar"
encoding_list = []
for char in message:
    position = positions[char]
    encoded_position = (position + 1) % 27
    encoding_list.append(alphabet[encoded_position])
encoded_message = "".join(encoding_list)

print(encoded_message)

#Define a function encoding that takes a message as input as well as an int encryption key,
#key to encode a message with the Caesar cipher by shifting each letter in message by key positions.
def encoding(message, key = 0):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string
    
encoded_message = encoding(message, 3)
print(encoded_message)

#İt returns encoded_message to decoded_message
decoded_message = encoding(encoded_message, -3)
print(decoded_message)


#Also you can get input from user
"""message2 = input("Your message is: ")"""

