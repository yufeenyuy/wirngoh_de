import re

"""
Regular expressions: This offers a means to match characters based on a special expression.
Regular expression offer special characters that are used in expressions
Some of these characters and their meaning as well functions include:
re.search('regular expression', string to be search from): this function returns boolean values
re.findall('regular expression', string to be search from): this function returns a list.
A dot i.e . means match any characted e.g &$§,numbers, alphabets
A * means match 0...many characters and matche the longest possible part of the string.
A *? means match 0...many characters and matche the shortest possible part of the string.
A + means match 1...many characters and matche the longest possible part of the string.
A +? means match 1...many and match the shortest possible part of the string.
A \S means match non-blank character i.e white spaces are not matched.
A ^ means start matching at the beginning of a string
A [] matches what is defined in the bracket as a single character. e.g [adb] matches strings containing a d or b
A [^] matches everything except what is defined in the bracket. e.g [^adb] matches strings that don't contain a d or b. 
A () extracts exactly the characters defined in the paranthesis. ( for beginning of extraction and ) for end of extraction.
\ helps to take special characters like $ e.g \$ takes the $ sign.
"""

sample_dt = open(file='regex_sum_42.txt', mode='r')
sample_dt = sample_dt.readlines()

actual_dt = open(file='regex_sum_1982230.txt', mode='r')
actual_dt = actual_dt.readlines()

def getnum(txt):
    sm = 0
    for line in txt:
        nums = re.findall('[0-9]+',line)
        if len(nums) == 0:
            pass
        for num in nums:
            print(num)
            sm = sm + int(num)
            print(sm)
    return sm
print(f'The sum of all numbers in the sample data is: {getnum(sample_dt)}\n')
#print(f'The sum of all numbers in the actual data is: {getnum(actual_dt)}')