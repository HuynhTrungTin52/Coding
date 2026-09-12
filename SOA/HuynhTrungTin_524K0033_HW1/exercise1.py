def calculate_final_score(assignment_score:float, midterm_score:float, final_score:float,) -> float:
    score:float =assignment_score*20/100+midterm_score*30/100+final_score*50/100
    return final_score

def get_result(score:float) -> str:
    if(score >=5.0):
        return "Pass"
    else:
        return "Fail"