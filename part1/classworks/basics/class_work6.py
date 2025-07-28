# HACKERRANK SUALI: `ginortS`

# You are given a string S.
# S contains alphanumeric characters only.

# Your task is to sort the string S in the following manner:
#     All sorted lowercase letters are ahead of uppercase letters.
#     All sorted uppercase letters are ahead of digits.
#     All sorted odd digits are ahead of sorted even digits.


# Input Format
# A single line of input contains the string S.

# Constraints
# 0 < len(S) <= 1000

# Output Format
# Output the sorted string S.


# Sample Input
# Sorting1234

# Sample Output
# ginortS1324


# Sample Input
# Sorting1234

# Sample Output
# ginortS1324


# sorted(), isupper(), islower(), isdigit() -> % 2 == 0, int(), for loop

s = input()

lower_result = [] # Kicik
upper_result = [] # Boyuk
odd_result = [] # Tek
even_result = [] # Cut

for i in s:
    if i.islower():
        lower_result.append(i)
    elif i.isupper():
        upper_result.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            even_result.append(i)
        else:
            odd_result.append(i)


lower_result = sorted(lower_result)
upper_result = sorted(upper_result)
odd_result = sorted(odd_result)
even_result = sorted(even_result)


result = lower_result + upper_result + odd_result + even_result

sorted_str = ''.join(result)

print(sorted_str)
