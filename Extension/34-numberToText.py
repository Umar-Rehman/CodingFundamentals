# Convert number to text

def num_to_text(num):
    num_dict = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    
    thousands = 1000
    millions = thousands * 1000
    billions = millions * 1000
    trillions = billions * 1000
    try:
        int(num)
    except:
        error_msg = 'Not and integer value: %s' % str(num)
        return error_msg
    
    if "-" in str(num):
        pos_neg = "negative "
        num = int(str(num)[1:])
    else:
        pos_neg = ""

    if (num < 20):
        num_text = num_dict[num]
        return pos_neg + num_text

    if (num < 100):
        if num % 10 == 0:
            num_text = num_dict[num]
            return pos_neg + num_text
        else:
            num_text = num_dict[num // 10 * 10] + '-' + num_dict[num % 10]
            return pos_neg + num_text

    if (num < thousands):
        if num % 100 == 0:
            num_text = num_dict[num // 100] + ' hundred'
            return pos_neg + num_text
        else:
            num_text = num_dict[num // 100] + ' hundred and ' + num_to_text(num % 100)
            return pos_neg + num_text

    if (num < millions):
        if num % thousands == 0:
            num_text = num_to_text(num // thousands) + ' thousand'
            return pos_neg + num_text
        else:
            num_text = num_to_text(num // thousands) + ' thousand ' + num_to_text(num % thousands)
            return pos_neg + num_text

    if (num < billions):
        if (num % millions) == 0:
            num_text = num_to_text(num // millions) + ' million'
            return pos_neg + num_text
        else:
            num_text = num_to_text(num // millions) + ' million, ' + num_to_text(num % millions)
            return pos_neg + num_text

    if (num < trillions):
        if (num % billions) == 0:
            num_text = num_to_text(num // billions) + ' billion'
            return pos_neg + num_text
        else:
            num_text = num_to_text(num // billions) + ' billion, ' + num_to_text(num % billions)
            return pos_neg + num_text
    
    if (num > trillions):
        if (num % trillions == 0):
            num_text = num_to_text(num // trillions) + ' trillion'
            return pos_neg + num_text
        else:
            num_text = num_to_text(num // trillions) + ' trillion, ' + num_to_text(num % trillions)
            return pos_neg + num_text

print(num_to_text(-198342197))