# declaration of function get_multiplied_digits
def get_multiplied_digits(n):
    str_number = f"{n}"  # number ==> string
    if len(str_number) == 1:
        return int(str_number)
    else:
        first = int(str_number[0])
        # the last character is 0
        if int(str_number[1:]) == 0:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)
# the last digit is 0
result2 = get_multiplied_digits(402030)
print(result2)
# one more check
result3 = get_multiplied_digits(4020305)
print(result3)

# consol
# 24
# 24
# 120
