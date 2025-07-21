"""
Course     : CMPSC 131, Summer 2025
File       : PS5.py 

Name       : Jonathan Reese
GitHub User:   ifinitysystem
Collaboration Statement: N/A
"""

#-YOUR CODE STARTS HERE  (TODO) 
#Part 1.1
def invert_dict(d):
    result = {}
    keys = d.keys()
    for i in range(len(keys)):
        current_key_list = list(keys)
        key = current_key_list[i]
        value = d.get(key)

        if value in result:
            result.get(value).append(key)
        else:
            result[value] = [key]
    return result
#Part 1.2
def char_frequency(s):
    freq = {}
    for i in range(len(s)):
        ch = s[i]

        # Convert uppercase to lowercase manually
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        # Accept only lowercase letters
        if ch >= 'a' and ch <= 'z':
            if ch in freq:
                freq[ch] = freq.get(ch) + 1
            else:
                freq[ch] = 1

    return freq

#Part 1.3
def find_missing_pangram_chars(s):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    found = {}

    for i in range(len(s)):
        ch = s[i]

        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)

        if ch >= 'a' and ch <= 'z':
            if ch not in found:
                found[ch] = True

    missing = []
    for i in range(len(all_letters)):
        ch = all_letters[i]
        if ch not in found:
            missing.append(ch)

    return missing

#Part 1.4 
def are_anagrams(s1, s2):
    freq1 = {}
    freq2 = {}

    for i in range(len(s1)):
        ch = s1[i]
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if ch >= 'a' and ch <= 'z':
            if ch in freq1:
                freq1[ch] = freq1.get(ch) + 1
            else:
                freq1[ch] = 1

    for i in range(len(s2)):
        ch = s2[i]
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if ch >= 'a' and ch <= 'z':
            if ch in freq2:
                freq2[ch] = freq2.get(ch) + 1
            else:
                freq2[ch] = 1

    keys1 = list(freq1.keys())
    keys2 = list(freq2.keys())

    if len(keys1) != len(keys2):
        return False

    for i in range(len(keys1)):
        k = keys1[i]
        if k not in freq2:
            return False
        if freq1.get(k) != freq2.get(k):
            return False

    return True

#Part 1.5
def find_anagram_pairs(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                result.append((i, j))
    return result

#Part 1.6
def is_steady(s):
    s = s.lower()
    freq = {}

    for i in range(len(s)):
        ch = s[i]
        if ch >= 'a' and ch <= 'z':
            if ch in freq:
                freq[ch] = freq.get(ch) + 1
            else:
                freq[ch] = 1

    values = list(freq.values())
    first = values[0]

    for i in range(1, len(values)):
        if values[i] != first:
            return False

    return True

#Part 1.7
def nearly_equal(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    freq1 = {}
    freq2 = {}

    for i in range(len(s1)):
        ch = s1[i]
        if ch >= 'a' and ch <= 'z':
            if ch in freq1:
                freq1[ch] = freq1.get(ch) + 1
            else:
                freq1[ch] = 1

    for i in range(len(s2)):
        ch = s2[i]
        if ch >= 'a' and ch <= 'z':
            if ch in freq2:
                freq2[ch] = freq2.get(ch) + 1
            else:
                freq2[ch] = 1

    all_keys = {}

    keys1 = freq1.keys()
    for i in range(len(list(keys1))):
        key = list(keys1)[i]
        if key not in all_keys:
            all_keys[key] = True

    keys2 = freq2.keys()
    for i in range(len(list(keys2))):
        key = list(keys2)[i]
        if key not in all_keys:
            all_keys[key] = True

    all_keys_list = list(all_keys.keys())

    for i in range(len(all_keys_list)):
        key = all_keys_list[i]
        count1 = freq1.get(key)
        count2 = freq2.get(key)

        if count1 is None:
            count1 = 0
        if count2 is None:
            count2 = 0

        if abs(count1 - count2) > 2:
            return False

    return True

#Part 1.8
def get_term(code):
    term_map = {
        1: "Spring",
        5: "Summer",
        8: "Fall"
    }

    if code < 2000 or code > 2999:
        return False

    year = (code % 1000) // 10 + 2000
    term_digit = code % 10

    if term_digit not in term_map:
        return False

    term = term_map.get(term_digit)
    return term + " " + str(year)




################################################################################

def main():
    #-YOUR ASSERTIONS TO TEST FOR YOUR FUNCTIONS STARTS HERE (TODO)
    original = {
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 3
    }

    inverted = invert_dict(original)
    print(inverted)

   
    result = char_frequency("~ABC abc!!!!!!! !!!!!!! ")
    print(result)

        
    missing = find_missing_pangram_chars("The quick brown fox")
    print(missing)  

    print(are_anagrams("Lis ten", "Silent!"))  
    print(are_anagrams("Listen", "Google"))    

    anagram_list = ["Lis Ten", "silent", "enli st", "inlet s", "google"]
    pairs = find_anagram_pairs(anagram_list)
    print(pairs)  

    print(is_steady("ARE era"))   
    print(is_steady("ARE eras"))  

    print(nearly_equal("sesame", "SundrivE"))  
    print(nearly_equal("hello", "helloooooo")) 

    print(get_term(2255)) 
    print(get_term(2186)) 
    print(get_term(2241))  


if __name__ == "__main__":
    main()
