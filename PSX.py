"""
Course     : CMPSC 131, Summer 2025
File       : PSX.py 

Name       : Jonathan Reese
GitHub User:   ifinitysystem
Collaboration Statement: YOUR_STATEMENT_HERE
"""



#-YOUR CODE STARTS HERE  (TODO) 

#Part 1.1
def move_vowels(s):
    assert isinstance(s, str) and len(s) > 0

    vowels = "aeiouAEIOU"
    chars = []
    for ch in s:
        chars.append(ch)

    vowel_indices = []
    for i in range(len(chars)):
        if chars[i] in vowels:
            vowel_indices.append(i)

    i = 0
    j = len(vowel_indices) - 1
    while i < j:
        temp = chars[vowel_indices[i]]
        chars[vowel_indices[i]] = chars[vowel_indices[j]]
        chars[vowel_indices[j]] = temp
        i += 1
        j -= 1

    result = ""
    for ch in chars:
        result += ch
    
    return result

#Part 1.2
def is_snaky(num):
    assert isinstance(num, int) and num > 0

    def transform(n):
        if n < 10:
            return n
        result = 0
        while n >= 10:
            a = n % 10
            b = (n // 10) % 10
            result += a * b
            n = n // 10
        return result

    slow = num
    fast = transform(num)

    while fast != 5 and slow != fast:
        slow = transform(slow)
        fast = transform(transform(fast))

    return fast == 5

#Part 1.3
def water_meter(water, target):
    assert isinstance(water, list) and all(isinstance(x, int) and x > 0 for x in water)
    assert isinstance(target, int) and target > 0

    n = len(water)
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += water[end]

        while current_sum >= target:
            window_length = end - start + 1
            if window_length < min_length:
                min_length = window_length
            current_sum -= water[start]
            start += 1

    if min_length == n + 1:
        return -1
    return min_length






################################################################################

def main():
    #-YOUR ASSERTION TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print(move_vowels("Hello, Sami!"))     
    print(move_vowels("CMPSC131 at PSU"))  
    print(is_snaky(532))   
    print(is_snaky(1171))  
    print(water_meter([4, 6, 2, 8, 1, 7], 13)) 
    print(water_meter([1, 1, 4, 1], 16))       



if __name__ == "__main__":
    main()
