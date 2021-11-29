"""Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def number_to_word(n):
    if n == 1000:
        return "onethousand"
    ones = n % 10
    n = n // 10
    tens = n % 10
    n = n // 10
    hundreds = n % 10
    ones_to_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tens_to_words = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    special_tens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

    word = ""
    if hundreds:
        word += ones_to_words[hundreds] + "hundred"
        if tens or ones:
            word += "and"
    if tens:
        if tens * 10 + ones in special_tens:
            word += special_tens[tens * 10 + ones]
            return word
        else:
            word += tens_to_words[tens]
    if ones:
        word += ones_to_words[ones]
    return word

words = [number_to_word(n) for n in range(1, 1001)]
count = 0
for w in words:
    count += len(w)
print(count)