def solution(answers):
    answer = []
    
    score_count = [0, 0, 0]
    first_person = [1, 2, 3, 4, 5]
    second_person = [2, 1, 2, 3, 2, 4, 2, 5]
    third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first_index = 0
    second_index = 0
    third_index = 0 
    
    for i in range(len(answers)):
        if answers[i] == first_person[first_index]: 
            score_count[0] += 1 
        if answers[i] == second_person[second_index]:
            score_count[1] += 1 
        if answers[i] == third_person[third_index]:
            score_count[2] += 1 
        
        first_index += 1 
        second_index += 1 
        third_index += 1 
        
        if first_index > 4: 
            first_index = 0 
        if second_index > 7:
            second_index = 0 
        if third_index > 9:
            third_index = 0 
    
    max_score = max(score_count)
    
    for i in range(3): 
        if score_count[i] == max_score: 
            answer.append(i+1)
            
    return answer 