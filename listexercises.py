def vowelchecker(x):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for character in x.lower():
        if character in vowels:
            count += 1
    return count

def analyse_numbers(numbers):
    if numbers == []:
        return None
    highest = numbers[0]
    lowest = numbers[0]
    total = 0
    count = 0
    for number in numbers:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
        total += number
        count += 1
    average = total / count
    return highest, lowest, average

def remove_odds(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 != 0:
            numbers.pop(index)
        else:
            index += 1
    return numbers
