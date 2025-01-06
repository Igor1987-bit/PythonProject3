# print_params function declaration
def print_params(a=1, b='string', c=True):
    print(a, b, c)
# Calling the print_params function with different parameters, including empty
print("----------------1----------------")
print_params(2, 'column', False & True)  # Checking operand entry &
print_params(3, '"c" is underlined? - ', 3)
print_params(a=1, b='two')
print_params(a='one', c="three")
print_params(c=' - in reverse order', b='B', a='A')  #
print_params()  # Call without arguments
print("----------------2----------------")
print_params(b=25)
print_params(c=[1, 2, 3])
print("----------------3----------------")
values_list = [1, '2', True]
print_params(*values_list)
print("----------------4----------------")
values_list_2 = [54.32, 'string']
print_params(*values_list_2, 42)
print("----------------5----------------")
values_dict = {}
print(type(values_dict))
keys_for_values_dict = ['a', 'b', 'c']
i = 1
while i <= 3:
    values_dict.update({keys_for_values_dict[i - 1]: values_list[i - 1]})
    i += 1
print(values_dict)
# consol
# ----------------1----------------
# 2 column False
# 3 "c" is underlined? -  3
# 1 two True
# one string three
# A B  - in reverse order
# 1 string True
# ----------------2----------------
# 1 25 True
# 1 string [1, 2, 3]
# ----------------3----------------
# 1 2 True
# ----------------4----------------
# 54.32 string 42
# ----------------5----------------
# <class 'dict'>
# {'a': 1, 'b': '2', 'c': True}
