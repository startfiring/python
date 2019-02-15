
def raise_to_power1(base_num, pow_num):

    if (base_num == 0) and (pow_num <= 0):
        return ("Math ERROR")
    
    count = 1
    result = base_num
    while count < pow_num:
        result = result * base_num
        count += 1
    return result


def raise_to_power2(base_num, pow_num):

    if (base_num == 0) and (pow_num <= 0):
        return ("Math ERROR")

    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result
print(raise_to_power1(3, 5))
print(raise_to_power2(3, 15))



