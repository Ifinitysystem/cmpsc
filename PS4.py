"""
Course     : CMPSC 131, Summer 2025
File       : PS4.py 

Name       : Jonathan Reese
GitHub User:  ifinitysystem
Collaboration Statement: N/A
"""


#-YOUR CODE STARTS HERE  (TODO) 
def is_consonant(char):
    vowels = "aeiouAEIOU"
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        if char not in vowels:
            return True
    return False

def count_consonants(s):
    count = 0
    for ch in s:
        if is_consonant(ch):
            count += 1
    return count

def get_even_sum(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

def get_second(s):
    parts = s.split(",")
    second = parts[1]
    start = 0
    end = len(second) - 1

    while start <= end and second[start] == ' ':
        start += 1
    while end >= start and second[end] == ' ':
        end -= 1

    cleaned = ''
    i = start
    while i <= end:
        cleaned += second[i]
        i += 1

    return cleaned

def is_vowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'

def replace_vowels_in_list(lst):
    for i in range(len(lst)):
        word = lst[i]
        new_word = ''
        for j in range(len(word)):
            if is_vowel(word[j]):
                new_word += 'q'
            else:
                new_word += word[j]
        lst[i] = new_word

def is_rotation(txt_1, txt_2):
    if len(txt_1) != len(txt_2):
        return False

    for i in range(len(txt_1)):
        rotated = txt_2[i:] + txt_2[:i]
        if rotated == txt_1:
            return True
    return False

def is_vowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'

def words_with_vowels(text):
    result = []
    word = ''
    for i in range(len(text)):
        ch = text[i]
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            word += ch
        else:
            if word != '':
                has_vowel = False
                for j in range(len(word)):
                    if is_vowel(word[j]):
                        has_vowel = True
                        break
                if has_vowel:
                    result.append(word)
                word = ''
    if word != '':
        has_vowel = False
        for j in range(len(word)):
            if is_vowel(word[j]):
                has_vowel = True
                break
        if has_vowel:
            result.append(word)

    return result

def most_vowels_word(text):
    words = words_with_vowels(text)
    max_vowels = 0
    result_word = ''
    
    for i in range(len(words)):
        word = words[i]
        count = 0
        for j in range(len(word)):
            if is_vowel(word[j]):
                count += 1
        if count > max_vowels:
            max_vowels = count
            result_word = word

    return result_word

def normalize_list(lst):
    if len(lst) == 0:
        return []

    min_val = lst[0]
    max_val = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
        if lst[i] > max_val:
            max_val = lst[i]

    result = []
    if min_val == max_val:
        for i in range(len(lst)):
            result.append(0.5)
    else:
        for i in range(len(lst)):
            normalized = (lst[i] - min_val) / (max_val - min_val)
            result.append(normalized)

    return result

def get_top_student(data):
    top_name = ""
    top_avg = 0.0

    for i in range(len(data)):
        name = data[i][0]
        scores = data[i][1]
        total = 0
        for j in range(len(scores)):
            total += scores[j]
        avg = total / len(scores)
        if avg > top_avg:
            top_avg = avg
            top_name = name

    return top_name


def get_avg_increase(temp_readings):
    total_increase = 0.0
    increase_count = 0

    for i in range(1, len(temp_readings)):
        prev_temp = temp_readings[i - 1][1]
        curr_temp = temp_readings[i][1]

        if curr_temp > prev_temp:
            total_increase += (curr_temp - prev_temp)
            increase_count += 1

    if increase_count == 0:
        return 0.0
    else:
        return total_increase / increase_count





################################################################################

def main():
    #-YOUR ASSERTION TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)

    assert count_consonants("ApPLeS!!!") == 4
    assert count_consonants("a-131") == 0

    assert get_even_sum([-1, 0, 1, 2, -2]) == 0
    assert get_even_sum([1, 2, 3, 4, 5, 6]) == 12

    assert get_second('mouse, cat, dog, pig, lion') == 'cat'
    assert get_second('apple,       pear   , banana') == 'pear'

    test_list = ['hello', 'world']
    replace_vowels_in_list(test_list)
    assert test_list == ['hqllq', 'wqrld']

    assert is_rotation("waterbottle", "erbottlewat") == True
    assert is_rotation("hello", "lohel") == True
    assert is_rotation("hello", "ohlle") == False

    assert words_with_vowels("Hello, World! Are you okay Ms.?") == ["Hello", "World", "Are", "you", "okay"]
    assert words_with_vowels("Try my crypt") == []

    assert most_vowels_word("This is the ultimate example string") == "ultimate"

    assert normalize_list([10, 20, 30, 40, 50]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert normalize_list([5, 5, 5, 5]) == [0.5, 0.5, 0.5, 0.5]

    student_data = [
        ("Joseph", [98, 56, 0, 99]),
        ("Elijah", [89, 78, 100, 81]),
        ("Jeremiah", [89, 78, 89])
    ]
    assert get_top_student(student_data) == "Elijah"

    temp_readings = (
        ("08:00", 15.0),
        ("10:00", 16.5),
        ("12:00", 17.2),
        ("14:00", 16.8),
        ("16:00", 18.3),
        ("18:00", 18.0)
    )
    assert abs(get_avg_increase(temp_readings) - 1.2333333333333334) < 0.0001


if __name__ == "__main__":
    main()
