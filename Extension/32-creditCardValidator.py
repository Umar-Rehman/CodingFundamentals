# Credit card number validator

def validate_card():
    card_num = input("Enter card number: ")
    card_num_list = list(card_num)
    
    input_invalid = False
    
    while input_invalid == False:
        try:
            if len(card_num_list) == 16 and bool(card_num.isdecimal() == True):
                input_invalid = True 
            else:
                raise Exception
        except:
            card_num = input("Please check your card number and re-enter: ")
            card_num_list = list(card_num)
    
    doubled_li = []

    sum_of_undoubled = 0

    sum_doubled = 0

    for i in range(15, -1, -1):
        if i%2 == 0:
            doubled_li.append(int(card_num_list[i])*2)
        else:
            sum_of_undoubled+=int(card_num_list[i])

    for i in doubled_li:
        if i > 9:
            sum_doubled+=int(str(i)[:1])+int(str(i)[1:2])
        else:
            sum_doubled+=i

    sum_total = sum_doubled + sum_of_undoubled

    if int(str(sum_total)[1:]) == 0:
        validated_message = "Valid"
        print(validated_message)
        return validated_message
    else:
        validated_message = "Invalid"
        print(validated_message)
        return validated_message

validate_card()