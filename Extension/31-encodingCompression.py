# Run length encoding compression

def encode_string(string):
    string_list = []
    count = 1
    char = string[0]
    for i in range(1,len(string)):
        if string[i] == char:
            count = count + 1
        else:
            string_list.append([char,count])
            char = string[i]
            count = 1
    
    string_list.append([char,count])
    encoded_string = ''
 
    for i in range(0,len(string_list)):
        for j in string_list[i]:
            encoded_string += str(j)
    
    print(encoded_string)
    return encoded_string

def decode_string(encoded_string):
    string = ''
    for i in range(0,len(encoded_string)):
        if encoded_string[i].isalpha() == True:
            for j in range(int(encoded_string[i+1])):
                string += encoded_string[i]
    print(string)
    return(string)

string = input("Enter a string: ")

encoded_string = encode_string(string)

decode_string(encoded_string)