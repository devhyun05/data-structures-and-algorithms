def solution(s):
    answer = ""
    char_map = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    cur = 0 
    end = len(s)
    
    while cur != end: 
        temp = ""
        if s[cur].isalpha():                     
            while cur != end and temp not in char_map: 
                temp += s[cur]
                cur += 1 
            answer += str(char_map[temp]) 
        else: 
            answer += s[cur]
            cur += 1 
 
    return int(answer) 