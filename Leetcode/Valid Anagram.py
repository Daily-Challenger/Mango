def isAnagram( s: str, t: str) -> bool:
    for i in s:
        if i in t:
            pass
        else:
            return False
    return True



print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))