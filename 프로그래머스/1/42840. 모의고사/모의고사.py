def solution(answers):
    ans = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answers_length = len(answers)
    student1 = full_marking_list(student1, answers_length)
    student2 = full_marking_list(student2, answers_length)
    student3 = full_marking_list(student3, answers_length)
    
    score_student1 = count_matching_elements(answers, student1)
    score_student2 = count_matching_elements(answers, student2)
    score_student3 = count_matching_elements(answers, student3)
    
    max_score = max([score_student1, score_student2, score_student3])
    
    score_student_map = {1: score_student1, 2: score_student2, 3: score_student3}
    
    for student, score in score_student_map.items():
        if score == max_score:
            ans.append(student)

    return ans


def count_matching_elements(list1, list2):
    ans = sum(1 for x, y in zip(list1, list2) if x == y)
    return ans

def full_marking_list(marking_list, answers_length):
    full_marking_list = (marking_list * (answers_length // len(marking_list) + 1))[:answers_length]
    return full_marking_list