# 1.

# with open('data.txt', 'r') as file:
#     data = file.read()
#
# odd_numbers = eval(data)
#
# filtered_numbers = [num for num in odd_numbers if num % 3 == 0]
#
# n = sum(filtered_numbers) / len(filtered_numbers) if filtered_numbers else 0
# print(n)


# 3.
# def filter_odd_values(input_dict):
#
#     result_dict = {}
#
#     for key, value_list in input_dict.items():
#         odd_numbers = []
#
#         for num in value_list:
#             if num % 2 != 0:
#                 odd_numbers.append(num)
#
#         result_dict[key] = odd_numbers
#
#     return result_dict
#
#
# input_data = {
#     'a': [1, 8, 3, 7, 2],
#     'b': [12, 4, 8, 4],
#     'c': [9, 9, 2, 8, 5]
# }
#
# result = filter_odd_values(input_data)
# print(result)
