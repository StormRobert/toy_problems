def solve(word):
    vowels = "aeiou"

    def get_letter_value(char):
        return ord(char) - ord('a') + 1 if char.isalpha() else 0

    max_consonant_sum = 0
    current_consonant_sum = 0
    current_consonant_substring = ""

    for char in word:
        if char.isalpha() and char not in vowels:
            current_consonant_sum += get_letter_value(char)
            current_consonant_substring += char
        else:
            if current_consonant_sum > 0:
                print(f"Consonant Substring: {current_consonant_substring} | Value: {current_consonant_sum}")
            max_consonant_sum = max(max_consonant_sum, current_consonant_sum)
            current_consonant_sum = 0
            current_consonant_substring = ""

    if current_consonant_sum > 0:
        print(f"Consonant Substring: {current_consonant_substring} | Value: {current_consonant_sum}")

    return max(max_consonant_sum, current_consonant_sum)


print(solve("zodiacs"))  
print(solve("strength"))

