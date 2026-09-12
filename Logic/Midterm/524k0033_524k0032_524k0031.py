import csv #To turn the csv Data into Dictionary items 
import time #To measure runtime
import pandas as pd #To extract the data in a vectorized method
import matplotlib.pyplot as plt #To draw the runtime differenece 
import itertools #Combination using
import re
import rsa

# ==========================================
# TASK 1: 524k0031.py (Propositional Logic)
# ==========================================

#Operator precedence (higher = binds tighter)
PRECEDENCE = {
    '~': 5,    #Not  (unary, highest)
    '&': 4,    #And
    '^': 3,    #XOr
    '|': 2,    #Or
    '>': 1,    #Implies
    '=': 0,    #IFF  (lowest)
}
RIGHT_ASSOC = {'~', '>'}    #right-associative operators

#Tokenizer: split infix string into token list
def tokenize(infix: str) -> list:
    """
    Split an infix string into a list of tokens.
    Tokens can be multi-character variable names (ex: Var1, P2) or single-character operators.
    If an operator or parenthesis is encountered, immediately create a single-character token.
    """
    tokens = []
    i = 0
    while i < len(infix):
        ch = infix[i]
        if ch.isspace():
            i += 1
            continue
         #Start of a variable name (letter or digit following a letter)
        if ch.isalpha():
            j = i + 1
            while j < len(infix) and (infix[j].isalnum() or infix[j] == '_'):
                j += 1
            tokens.append(infix[i:j])
            i = j
        elif ch in ('(', ')', '~', '&', '|', '^', '>', '='):
            tokens.append(ch)
            i += 1
        else:
            raise ValueError(f"Unknown character: '{ch}'")
    return tokens

# 1. Infix-> Postfix  (Shunting-Yard Algorithm)
def Infix2Postfix(Infix: str)-> list:
    """
    - Traverse tokens from left to right
    - Use two structures: an output queue (postfix) and an operator stack
    - Operand (variable)-> add directly to output
    - '('-> push onto stack
    - ')'-> pop operators from stack to output until '(' is encountered
    - Operator-> pop operators with higher precedence (or equal precedence if left-associative) to output, then push the current operator onto the stack
    - Finally: pop all remaining operators from the stack to output
    """
    tokens = tokenize(Infix)
    output = []    #postfix output queue
    op_stack = []  #operator stack

    for token in tokens:
         #1.1
        if token == '(':
            #Push those onto the stack as a barrier 
            op_stack.append(token)

        elif token == ')':
             # 1.2
             #Pop until matching '('
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            if not op_stack:
                raise ValueError("Mismatched parentheses")
            op_stack.pop()   #remove '('

        elif token in PRECEDENCE:
             # 1.3
             #While the top of the stack has an operator with higher (or equal,
             #for left-associative) precedence, pop it to output.
            while (op_stack and
                   op_stack[-1] != '(' and
                   op_stack[-1] in PRECEDENCE and
                   (PRECEDENCE[op_stack[-1]] > PRECEDENCE[token] or
                    (PRECEDENCE[op_stack[-1]] == PRECEDENCE[token]
                     and token not in RIGHT_ASSOC))):
                output.append(op_stack.pop()) # higher priority
            op_stack.append(token)

        else:
             # 1.4
             # Variable / operand -> straight to output
            output.append(token)

     #Drain remaining operators
    while op_stack:
        top = op_stack.pop()
        if top == '(':
            raise ValueError("Mismatched parentheses")
        output.append(top)

    return output

# 1.1.1 Helper: extract variable names (in order of appearance)
def extract_variables(postfix: list)-> list:
    """
    - Traverse the postfix expression, collecting tokens that are neither operators nor parentheses.
    - Use a seen set to ensure each variable appears only once in the result.
    - Preserve the order of variables based on their first occurrence
    """
    seen = set() #set of variables that have been seen
    variables = [] #in appeared order
    for token in postfix:
        if token not in PRECEDENCE and token not in ('(', ')'):
            # If token is not operator or have not seen yet -> new variable
            if token not in seen:
                seen.add(token)
                variables.append(token)
    return variables

# 1.1.2 Helper: Evaluate a postfix expression for given variable values
def evaluate_postfix(postfix: list, assignment: dict)-> bool:
    stack = []
    for token in postfix:
        if token == '~':
            a = stack.pop()
            stack.append(not a)
        elif token == '&':
            b, a = stack.pop(), stack.pop()
            stack.append(a and b)
        elif token == '|':
            b, a = stack.pop(), stack.pop()
            stack.append(a or b)
        elif token == '^':
            b, a = stack.pop(), stack.pop()
            stack.append(a ^ b)
        elif token == '>':
            b, a = stack.pop(), stack.pop()
            stack.append((not a) or b)
        elif token == '=':
            b, a = stack.pop(), stack.pop()
            stack.append(a == b)
        else:
            stack.append(assignment[token])
    return stack[0]

# 2. Postfix -> Truth Table
def Postfix2Truthtable(Postfix: list)-> dict:
    """
    Generate the truth table for the expression given in Postfix form.
    """
    variables = extract_variables(Postfix)
    rows = []
    for combo in itertools.product([False, True], repeat=len(variables)):
        assignment = dict(zip(variables, combo))
        result = evaluate_postfix(Postfix, assignment)
        rows.append({'assignment': assignment, 'result': result})
    return {'variables': variables, 'rows': rows}

def print_truth_table(infix: str, truth_table: dict):
    """Pretty-print a truth table."""
    variables = truth_table['variables']
    rows = truth_table['rows']

    header = ' | '.join(f'{v:^5}' for v in variables) + ' || ' + f'{"Result":^8}'
    separator = '-' * len(header)
    print(f"\nExpression: {infix}")
    print(separator)
    print(header)
    print(separator)
    for row in rows:
        vals = ' | '.join(f'{"T" if row["assignment"][v] else "F":^5}' for v in variables)
        res = 'T' if row['result'] else 'F'
        print(f'{vals} || {res:^8}')
    print(separator)

# 3. Get DNF from Truth Table
def GetDNF(TruthTable: dict)-> str:
    """
    Derive the Disjunctive Normal Form (DNF) from the truth table.
    """
    variables = TruthTable['variables']
    minterms = []

    for row in TruthTable['rows']:
        if row['result']:
            literals = []
            for v in variables:
                if row['assignment'][v]:
                    literals.append(v)
                else:
                    literals.append(f'~{v}')
            if len(literals) == 1:
                minterms.append(literals[0])
            else:
                minterms.append('(' + ' & '.join(literals) + ')')

    if not minterms:
        return 'FALSE'    #contradiction
    if len(minterms) == len(TruthTable['rows']):
        return 'TRUE'     #tautology
    return ' | '.join(minterms)

# 4. Check Equivalence of Two Expressions
def CheckEquivalence(Infix1: str, Infix2: str)-> bool:
    """
    Return True if Infix1 and Infix2 are logically equivalent.
    """
    postfix1 = Infix2Postfix(Infix1)
    postfix2 = Infix2Postfix(Infix2)

    vars1 = set(extract_variables(postfix1))
    vars2 = set(extract_variables(postfix2))
    all_vars = sorted(vars1 | vars2)

    for combo in itertools.product([False, True], repeat=len(all_vars)):
        assignment = dict(zip(all_vars, combo))
        r1 = evaluate_postfix(postfix1, assignment)
        r2 = evaluate_postfix(postfix2, assignment)
        if r1 != r2:
            return False
    return True

# Test Cases
def run_task1():
    test_cases = [
        "R|(P&Q)",
        "~P|(Q&R)>R",
        "P|(R&Q)",
        "(P>Q)&(Q>R)",
        "(P|~Q)>~P=(P|(~Q))>~P",
    ]

    equivalence_pairs = [
        ("P&Q",          "Q&P"),              #commutative AND
        ("P|Q",          "Q|P"),              #commutative OR
        ("~(P&Q)",       "~P|~Q"),            #De Morgan
        ("P>Q",          "~P|Q"),             #implication elimination
        ("P=Q",          "(P>Q)&(Q>P)"),      #biconditional expansion
    ]

     # Part A + B + C: Truth Tables & DNF 
    for i, expr in enumerate(test_cases, 1):
        print(f"Test case {i}: {expr}")
        postfix = Infix2Postfix(expr)
        print(f"Postfix : {' '.join(postfix)}")

        tt = Postfix2Truthtable(postfix)
        print_truth_table(expr, tt)

        dnf = GetDNF(tt)
        print(f"\nDNF: {dnf}")

     #Part D: Equivalence Checks
    print("Equivalent Check")
    for i, (e1, e2) in enumerate(equivalence_pairs, 1):
        result = CheckEquivalence(e1, e2)
        status = "Equivalent" if result else "Not Equivalent "
        print(f"\n{i}. {e1:30s}  ↔  {e2}")
        print(f"   -> {status}")

# ==========================================
# TASK 2: cau2.py (CSV Data Analysis)
# ==========================================

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

def run_task2():
    l_start = time.perf_counter()
    raw_dataset=[]
    try:
        #If the file is not found even if it's there, paste in the absolute path
        with open('524k0033_524k0032_524k0031.csv', 'r') as f:
         reader = csv.DictReader(f) #Turn data(row) into a dict, like mentioned before
         raw_dataset=list(reader)
            
    except FileNotFoundError:
        print("Can't find the student.csv")
        return # Changed exit to return to avoid closing the entire menu program
       
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
        df = pd.read_csv("524k0033_524k0032_524k0031.csv")
        
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

# ==========================================
# TASK 3: rsa_1.py (RSA Encryption)
# ==========================================

def run_task3():
    # 1. Tạo cặp khóa RSA (Key size: 2048 bits)
    print("Đang tạo khóa RSA 2048-bit...")
    public_key, private_key = rsa.newkeys(2048)
    
    # 2. Chuẩn bị 10 tin nhắn với độ dài tăng dần (Plaintext)
    messages = [
        "Hello", 
        "Hello World", 
        "Discrete Structures TDTU", 
        "This is a test message for RSA encryption", 
        "Cryptography libraries are allowed in this essay", 
        "We need to measure encryption and decryption time", 
        "With x-coordinates are plaintext message lengths", 
        "And y-coordinates are time consumptions to draw a graph", 
        "Discuss the limitations of the RSA cryptosystem carefully", 
        "Conclude with recommendations for improving the RSA implementation"
    ]
    
    msg_lengths = []
    enc_times = []
    dec_times = []

    print("\n--- TEST 10 MESSAGE ---")
    # 3. Mã hóa và Giải mã từng tin nhắn, đo lường thời gian
    for msg in messages:
        msg_bytes = msg.encode('utf-8')
        msg_lengths.append(len(msg))
        
        # Đo thời gian mã hóa
        start_enc = time.perf_counter()
        crypto = rsa.encrypt(msg_bytes, public_key)
        end_enc = time.perf_counter()
        enc_time = (end_enc - start_enc) * 1000 # Đổi ra milliseconds
        enc_times.append(enc_time)
        
        # Đo thời gian giải mã
        start_dec = time.perf_counter()
        decrypted_bytes = rsa.decrypt(crypto, private_key)
        end_dec = time.perf_counter()
        dec_time = (end_dec - start_dec) * 1000 # Đổi ra milliseconds
        dec_times.append(dec_time)
        
        # Xác minh kết quả
        assert msg == decrypted_bytes.decode('utf-8')
        print(f"Độ dài: {len(msg):<3} chars | Mã hóa: {enc_time:.4f} ms | Giải mã: {dec_time:.4f} ms")

    # 4. Vẽ đồ thị
    plt.figure(figsize=(10, 5))
    plt.plot(msg_lengths, enc_times, label='Encryption Time (ms)', marker='o', color='blue')
    plt.plot(msg_lengths, dec_times, label='Decryption Time (ms)', marker='s', color='red')
    
    plt.title('RSA Cryptosystem: Time vs Message Length')
    plt.xlabel('Plaintext Message Length (characters)')
    plt.ylabel('Time Consumption (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()

# ==========================================
# MAIN MENU INTERFACE
# ==========================================

def main_menu():
    while True:
        print("\n" + "="*30)
        print("         MAIN MENU")
        print("="*30)
        print("1. Execute Task 1 (524k0031 - Propositional Logic Truth Tables)")
        print("2. Execute Task 2 (524k0033 - Student Data Analysis/CSV)")
        print("3. Execute Task 3 (524k0032 - RSA Encryption Test)")
        print("4. Exit")
        print("="*30)
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nExecuting Task 1...")
            run_task1()
        elif choice == '2':
            print("\nExecuting Task 2...")
            run_task2()
        elif choice == '3':
            print("\nExecuting Task 3...")
            run_task3()
        elif choice == '4':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

main_menu()