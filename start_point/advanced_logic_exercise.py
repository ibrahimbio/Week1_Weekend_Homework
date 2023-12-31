# # For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# # 1. Print out a list of the even integers:
even_integers = []
def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            even_integers.append(number)
    return even_integers
print(even_numbers(numbers))


# # 2. Print the difference between the largest and smallest value:
largest_number = max(numbers)
smallest_number = min(numbers)
print(largest_number - smallest_number)

# # 3. Print True if the list contains a 2 next to a 2 somewhere.


if numbers.index(2) == 2  and numbers.index(2) == 2:
    print(True)
else:
    print(False)


# # 4. Print the sum of the numbers, 
# #    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
# #    
# #    So [11, 6, 4, 99, 7, 11] would have sum of 22

integers = [11, 6, 4, 99, 7, 11]

print(sum(integers[::5]))


# # 5. HARD! Print the sum of the numbers. 
# #    Except the number 13 is very unlucky, so it does not count.
# #    And numbers that come immediately after a 13 also do not count.
# #    HINT - You will need to track the index throughout the loop.
# #
# #    So [5, 13, 2] would have sum of 5. 

integer = [5, 13, 2]

allowed_to_sum = []

for index, elem in enumerate(integer):
    if elem == 13:
        continue

    if index != 0 and integer[index-1] == 13:
        continue

    allowed_to_sum.append(elem)

print(allowed_to_sum)
print(sum(allowed_to_sum))





