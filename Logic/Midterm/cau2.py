import csv #To turn the csv Data into Dictionary items 
import time #To measure runtime
import pandas as pd #To extract the data in a vectorized method
import matplotlib.pyplot as plt #To draw the runtime differenece 
#Predicates
def is_passing(student):
    return float(student['Math']) >= 5 and float(student['CS']) >= 5 and float(student['Eng']) >= 5

def is_high_math(student):
    return float(student['Math']) >= 9

def is_struggling(student):
    return float(student['Math']) < 6 and float(student['CS']) < 6

def improved_in_cs(student):
    return float(student['CS']) > float(student['Math'])
#Statments
#Uni1
def AllStudentsPassed(dataset):
    return all(is_passing(student) for student in dataset)
#NotUni1
def exists_not_passing(data):
    return any(not is_passing(student) for student in data)

#auxiliary function
def math_gt_3(student):
    return float(student['Math']) > 3
#Uni2
def AllMathHigherThan3(dataset):
    return all(math_gt_3(student) for student in dataset)
#NotUni2
def exists_math_3_or_less(data):
    return any(not math_gt_3(student) for student in data)

#Exi1
def exists_student_math_above_9(dataset):
    return any(is_high_math(student) for student in dataset)
#NotExi1
def all_math_9_or_less(data):
    return all(not is_high_math(student) for student in data)
#Exi2
def exists_improved_in_cs(dataset):
    return any(improved_in_cs(student) for student in dataset)
#NotExi2
def none_improved_in_cs(data):
    return all(not improved_in_cs(student) for student in data)

#Combined1
def all_have_one_subject_above_6(dataset):
    def has_high_subject(student):
        for subject in ['Math', 'CS', 'Eng']:
            if float(student[subject]) > 6:
                return True
        return False

    return all(has_high_subject(student) for student in dataset)
#NotCombined1
def exists_student_all_subjects_6_or_less(data):
    def no_high_subject(student):
        for subject in ['Math', 'CS', 'Eng']:
            if float(student[subject]) > 6:
                return False
        return True

    return any(no_high_subject(student) for student in data)
#Combined2
def all_low_math_have_other_high_subject(data):
    def condition_met(student):
        if float(student['Math']) < 6:
            for subject in ['Math', 'CS', 'Eng']:
                if float(student[subject]) > 6:
                    return True
            return False
        return True

    return all(condition_met(student) for student in data)
#NotCombined2
def exists_struggling_math_no_high_subject(data):
    def negated_condition(student):
        if float(student['Math']) < 6:
            for subject in ['Math', 'CS', 'Eng']:
                if float(student[subject]) > 6:
                    return False
            return True
        return False

    return any(negated_condition(student) for student in data)

l_start = time.perf_counter()
raw_dataset=[]
try:
    #If the file is not found even if it's there, paste in the absolute path
    with open('students.csv', 'r') as f:
     reader = csv.DictReader(f) #Turn data(row) into a dict, like mentioned before
     raw_dataset=list(reader)
        
except FileNotFoundError:
    print("Can't find the student.csv")
    exit
   
dataset=[]
for row in raw_dataset:
    try:
        m = float(row['Math'])
        c= float(row['CS'])
        e= float(row['Eng'])
        if 0 <= m <= 10 and 0 <= c <= 10 and 0 <= e <= 10:
            row['Math'] = m
            row['CS'] = c
            row['Eng'] = e
            
            dataset.append(row) #Cleaning the data and inserting it into a new array
    except (ValueError,TypeError):
        continue

#Calling and storing these functions to keep the terminal clean
r_univ_1 = AllStudentsPassed(dataset)
r_univ_2 = AllMathHigherThan3(dataset)
r_exis_1 = exists_student_math_above_9(dataset)
r_exis_2 = exists_improved_in_cs(dataset)
r_comb_1 = all_have_one_subject_above_6(dataset)
r_comb_2 = all_low_math_have_other_high_subject(dataset)
r_n_univ_1 = exists_not_passing(dataset)
r_n_univ_2 = exists_math_3_or_less(dataset)
r_n_exis_1 = all_math_9_or_less(dataset)
r_n_exis_2 = none_improved_in_cs(dataset)
r_n_comb_1 = exists_student_all_subjects_6_or_less(dataset)
r_n_comb_2 = exists_struggling_math_no_high_subject(dataset)
l_end=time.perf_counter()
l_time=l_end - l_start
print(f"Loop approach's Runtime: {l_time:.6f} seconds")

pd_start = time.perf_counter() #Starting panda/vectorized approach

try:
    df = pd.read_csv("students.csv")
    
    cols = ['Math', 'CS', 'Eng']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce') #Convert the column into a numeric type, otherwise convert to NaN
    
    df = df.dropna(subset=cols)#Drop said NaN
    
    df = df[(df['Math'] >= 0) & (df['Math'] <= 10) & 
            (df['CS'] >= 0)   & (df['CS'] <= 10)   & 
            (df['Eng'] >= 0)  & (df['Eng'] <= 10)] #Drop the numbers outside of our accepted range
    # print(f"Reading {len(df)} records")
    is_passing= (df['Math'] >= 5) & (df['CS'] >= 5) & (df['Eng'] >= 5)
    is_high_math= (df['Math'] >= 9)
    improved_in_cs= (df['CS'] > df['Math'])
    is_struggling_math= (df['Math'] < 6)
    #Predicates
    
    
    pd_univ_1 = is_passing.all()    
    pd_univ_2 = (df['Math'] > 3).all()
    # print(pd_univ_2)
    pd_exis_1 = is_high_math.any()
    pd_exis_2 = improved_in_cs.any()
    # print(pd_exis_2)
    
    #Auxiliary variables for the combined statements
    has_high_subj = (df['Math'] > 6) | (df['CS'] > 6) | (df['Eng'] > 6)
    pd_comb_1 = has_high_subj.all()
    pd_comb_2 = (~is_struggling_math | has_high_subj).all() 
    # print(pd_comb_2)
    pd_n_univ_1 = ~((df['Math'] >= 5) & (df['CS'] >= 5) & (df['Eng'] >= 5)).all()
    pd_n_univ_2 = ~(df['Math'] > 3).all()
    pd_n_exis_1 = ~(df['Math'] >= 9).any()
    pd_n_exis_2 = ~(df['CS'] > df['Math']).any()
    pd_n_comb_1 = ~(has_high_subj).all()
    pd_n_comb_2 = (is_struggling_math & ~has_high_subj).any() 
    # print(pd_n_comb_2)


except FileNotFoundError:
    print(f"Can't find students.csv")

pd_end = time.perf_counter()
pd_time = pd_end - pd_start
print(f"Vectorized Approach Finished. Runtime: {pd_time:.6f} seconds\n")


plt.figure(figsize=(8, 6))
labels = ['Loop-based (Python Lists)', 'Vectorized (Pandas)']
times = [l_time, pd_time]
colors = ['#FF6B6B', '#4ECDC4']

bars = plt.bar(labels, times, color=colors)
plt.ylabel('Runtime (seconds)')
plt.title(f'Runtime Comparison on {len(dataset)} Records(after removing invalid data)')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.6f}s", ha='center', va='bottom')

plt.show()