import itertools #Combination using
import re

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

    Returns a dict:
        {
          'variables': [list of variable names],
          'rows': [
              {'assignment': {var: bool, ...}, 'result': bool},
              ...
          ]
        }
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

    For each row where the result is True, create a minterm:
      - If variable is True  -> use variable name as-is
      - If variable is False -> prefix with '~'
    Join minterms with ' | '.
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
    Return True if Infix1 and Infix2 are logically equivalent
    (i.e. they produce the same truth values for every combination
    of variable assignments over their combined variable set).
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
 
def run_all_tests():
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


if __name__ == "__main__":
    run_all_tests()