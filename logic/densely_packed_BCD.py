def normalize_number(number, exponent, rounding):
    padded_number = ''  # Initialize padded_number at the beginning
    adjust_exponent = 0
    is_negative = False
    number_str = str(number)
    if number_str.startswith("-"):
        is_negative = True
        number_str = number_str[1:]  # Remove the negative sign
    
    if '.' in number_str:  # Check if there's a fractional part
        integer_part, float_part = number_str.split('.')
    else:  # If there's no fractional part, set float_part to an empty string
        integer_part = number_str
        float_part = ''

    num_decimal_digits = len(integer_part) + len(float_part)

    if num_decimal_digits <= 16:
        adjust_exponent += 16 - num_decimal_digits
        padded_number = integer_part + float_part
        padded_number = padded_number.zfill(16)
    elif num_decimal_digits > 16:
        padded_number = integer_part + float_part
        padded_number = padded_number.zfill(16)
        if is_negative:
            if rounding == "truncate":
                padded_number = padded_number[:16]
            elif rounding == "round_up":
                padded_number = padded_number[:16]
                padded_number = str(int(padded_number) + 1)
            elif rounding == "round_down":
                padded_number = padded_number[:16]
                padded_number = str(int(padded_number) - 1)
            elif rounding == "nearest_even":
                if int(padded_number[:16]) % 2 == 0: 
                    if int(padded_number) % 10 <= 5: 
                        padded_number = padded_number[:16] 
                    else: 
                        padded_number = padded_number[:16] 
                        padded_number = str(int(padded_number) + 1) 
                else:
                    if int(padded_number) % 10 <= 4:
                        padded_number = padded_number[:16]
                    else:
                        padded_number = padded_number[:16]
                        padded_number = str(int(padded_number) + 1)
            elif rounding == "nearest_zero":
                if int(padded_number) % 10 <= 4:
                    padded_number = padded_number[:16]
                else:
                    padded_number = padded_number[:16]
                    padded_number = str(int(padded_number) + 1)
        else:
            if rounding == "truncate":
                padded_number = padded_number[:16]
            elif rounding == "round_up":
                padded_number = padded_number[:16]
                padded_number = str(int(padded_number) + 1)
            elif rounding == "round_down":
                padded_number = padded_number[:16]
            elif rounding == "nearest_even":
                if int(padded_number[:16]) % 2 == 0: 
                    if int(padded_number) % 10 <= 5: 
                        padded_number = padded_number[:16] 
                    else: 
                        padded_number = padded_number[:16] 
                        padded_number = str(int(padded_number) + 1) 
                else:
                    if int(padded_number) % 10 <= 4:
                        padded_number = padded_number[:16]
                    else:
                        padded_number = padded_number[:16]
                        padded_number = str(int(padded_number) + 1)
            elif rounding == "nearest_zero":
                if int(padded_number) % 10 <= 4:
                    padded_number = padded_number[:16]
                else:
                    padded_number = padded_number[:16]
                    padded_number = str(int(padded_number) + 1)
    if is_negative:
        padded_number = "-" + padded_number

    # Calculate the result
    result = exponent - len(float_part)

    return padded_number, result

def extract_components(number, exponent):
    # Get the sign bit
    comparison = float(number)
    sign_bit = '0' if comparison >= 0 else '1'  # Convert to binary string

    # Get the combi and exponent bits
    biased_exponent = exponent + 398
    if biased_exponent > 767:
        combi = "11110"
        exponent = "00000000"
        coefficient = "0" * 50
    elif biased_exponent < 0:
        combi = "11111"
        exponent = "11111111"
        coefficient = "1" * 50
    else:
        binary_exponent = bin(biased_exponent)[2:].zfill(10)
        combi = extract_combi(number, binary_exponent[:2])
        exponent = binary_exponent[-8:]
        coefficient = ''.join(decode_coefficient(number[2:])) if number[0] == '-' else ''.join(decode_coefficient(number[1:]))

    return sign_bit, combi, exponent, coefficient

def extract_combi(floating_point, exponent_string):
    first_digit = int(floating_point[1]) if floating_point[0] == '-' else int(floating_point[0])
    string_binary_fdigit = bin(first_digit)[2:].zfill(3)
    string_exponent = exponent_string[:2]

    if(first_digit < 8):
        combi = string_exponent.zfill(2) + string_binary_fdigit
    else:
        combi = "11" + string_exponent.zfill(2) + string_binary_fdigit[-1:]
    
    return combi

def decode_coefficient(coefficient):
    result = ''
    for i in range(0, len(coefficient), 3):
        # Extract three digits from the original number
        num = coefficient[i:i+3]
        
        # Pass the three digits through the densely_packed function
        processed_digits = densely_packed(str(num))
        
        # Add the processed digits to the result
        result += ''.join(processed_digits)

    return result


def densely_packed(number):
    bcd = []
    dpbcd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checker = []

    for digit in number:
        digit_int = int(digit)
        binary_digit = bin(int(digit_int))[2:].zfill(4)  # Convert each digit to 4-bit binary
        bcd.extend(binary_digit)  # Append each bit of the binary representation to the BCD list

    # Check if 'bcd' has less than 12 elements
    while len(bcd) < 12:
        bcd.insert(0, '0')  # Append zeros to the left until 'bcd' has 12 elements

    checker = [bcd[0], bcd[4], bcd[8]]
    # dpbcd = 012 345 6789
    # bcd = -0 1 2 3- -4 5 6 7- -8 9 10 11-
    print("bcd: "+str(bcd))
    dpbcd[2] = bcd[3]
    dpbcd[5] = bcd[7]
    dpbcd[9] = bcd[11]
    print("dpbcd before ifs: "+ str(dpbcd))
    print("checker: "+ str(checker)+'\n')
    if checker == ['0', '0', '0']:
        print("In 000")

        dpbcd[0] = bcd[1]
        dpbcd[1] = bcd[2]

        dpbcd[3] = bcd[5]
        dpbcd[4] = bcd[6]

        dpbcd[6] = '0'
        dpbcd[7] = bcd[9]
        dpbcd[8] = bcd[10]

    elif checker == ['0', '0', '1']:
        print("In 001")
        
        dpbcd[0] = bcd[1]
        dpbcd[1] = bcd[2]

        dpbcd[3] = bcd[5]
        dpbcd[4] = bcd[6]

        dpbcd[6] = '1'
        dpbcd[7] = '0'
        dpbcd[8] = '0'

    elif checker == ['0', '1', '0']:
        print("In 010")
        
        dpbcd[0] = bcd[1]
        dpbcd[1] = bcd[2]

        dpbcd[3] = bcd[9]
        dpbcd[4] = bcd[10]

        dpbcd[6] = '1'
        dpbcd[7] = '0'
        dpbcd[8] = '1'

    elif checker == ['1', '0', '0']:
        print("In 100")
        dpbcd[0] = bcd[9]
        dpbcd[1] = bcd[10]

        dpbcd[3] = bcd[5]
        dpbcd[4] = bcd[6]

        dpbcd[6] = '1'
        dpbcd[7] = '1'
        dpbcd[8] = '0'

    elif checker == ['0', '1', '1']:
        print("In 011")
        dpbcd[0] = bcd[1]
        dpbcd[1] = bcd[2]

        dpbcd[3] = '1'
        dpbcd[4] = '0'

        dpbcd[6] = '1'
        dpbcd[7] = '1'
        dpbcd[8] = '1'

    elif checker == ['1', '0', '1']:
        print("In 101")
        dpbcd[0] = bcd[5]
        dpbcd[1] = bcd[6]

        dpbcd[3] = '0'
        dpbcd[4] = '1'

        dpbcd[6] = '1'
        dpbcd[7] = '1'
        dpbcd[8] = '1'

    elif checker == ['1', '1', '0']:
        print("In 110")
        dpbcd[0] = bcd[9]
        dpbcd[1] = bcd[10]

        dpbcd[3] = '0'
        dpbcd[4] = '0'

        dpbcd[6] = '1'
        dpbcd[7] = '1'
        dpbcd[8] = '1'

    elif checker == ['1', '1', '1']:
        print("In 111")
        dpbcd[0] = '0'
        dpbcd[1] = '0'

        dpbcd[3] = '1'
        dpbcd[4] = '1'

        dpbcd[6] = '1'
        dpbcd[7] = '1'
        dpbcd[8] = '1'
    
    print("dpbcd after ifs: "+ str(dpbcd))
    print("checker: "+ str(checker)+'\n')
    
    return dpbcd


def convert_to_dpd(floating_point, power, round):
    normalized_float, normalized_exponent = normalize_number(floating_point, power, round)
    sign, combi, exponent, coefficient = extract_components(normalized_float, normalized_exponent)
    binary_answer = str(sign) + ' ' + str(combi) + ' ' + str(exponent) + ' ' + str(coefficient)
    
    # Convert binary strings to integers
    sign_int = int(sign, 2)
    combi_int = int(combi, 2)
    exponent_int = int(exponent, 2)
    coefficient_int = int(coefficient, 2)
    
    # Perform bitwise operations
    binary = bin(sign_int)[2:].zfill(1) + bin(combi_int)[2:].zfill(5) + bin(exponent_int)[2:].zfill(8) + bin(coefficient_int)[2:].zfill(50)
    hexadecimal_answer = hex(int(binary, 2))[2:].zfill(16)

    return binary_answer, hexadecimal_answer

def write_to_file(binary, hexadecimal):
    try:
        with open("dpd_results.txt", "w") as file:
            file.write(f"Binary: {binary}\nHexadecimal: {hexadecimal}")
        print("Results written to 'dpd_results.txt'")
    except Exception as e:
        print(f"An error occurred while writing to file: {str(e)}")