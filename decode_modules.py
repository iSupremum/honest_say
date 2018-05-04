dec_table = [{"oe": '0', "oK": '1', "ow": '2', "oi": '3', "7e": '4', "7K": '5', "7w": '6', "7i": '7', "Ne": '8', "NK": '9'},
{"4": '5', "6": '1', "n": '0', "-": '2', "o": '3', "v": '4', "C": '6', "S": '7', "c": '8', "E": '9'},
{"5": '1', "z": '0', "A": '2', "i": '3', "P": '4', "k": '5', "s": '6', "l": '7', "F": '8', "q": '9'},
{"on": '0', "ov": '1', "oc": '2', "oz": '3', "7n": '4', "7v": '5', "7c": '6', "7z": '7', "Nn": '8', "Nv": '9'}
]


def decode(json_string):
    qq_number = ""
    temp_list = []
    for i in range(len(json_string)):
        if(i % 4 == 1):
            tempChr = temp_list.pop()
            temp_list.append(tempChr + json_string[i])
        else:
            temp_list.append(json_string[i])
    for i in range(len(temp_list)):
        if((len(temp_list) % 3 == 1) and i == len(temp_list) - 1):
            if temp_list[i] in dec_table[3]:
                qq_number += dec_table[3][temp_list[i]]
            else:
                qq_number += "*"
        else:
            if temp_list[i] in dec_table[i % 3]:
                qq_number += dec_table[i % 3][temp_list[i]]
            else:
                qq_number += "*"
    return qq_number
