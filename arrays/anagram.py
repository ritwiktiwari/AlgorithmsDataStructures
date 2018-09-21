def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    counter = {}
    for i in s1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for i in s2:
        if i in counter:
            counter[i] -= 1
        else:
            return False
    for k in counter:
        if counter[k] != 0:
            return False
    return True


print(anagram('dog', 'god'))
print(anagram('clint eastwood', 'old west action'))
print(anagram('aa', 'bb'))
