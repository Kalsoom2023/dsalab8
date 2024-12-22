class ExpressionEvaluator:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(c):
        return c in '+-*/^'

    def infix_to_postfix(expression):
        stack = []
        postfix = []

        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and ExpressionEvaluator.precedence[char] <= ExpressionEvaluator.precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ''.join(postfix)

    def evaluate_postfix(expression):
        stack = []
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                elif char == '/':
                    stack.append(a / b)
        return stack[0]


# Example
infix_expr = "(10-7)*(9+1)"
postfix_expr = ExpressionEvaluator.infix_to_postfix(infix_expr)
result = ExpressionEvaluator.evaluate_postfix(postfix_expr)

print("Postfix:", postfix_expr, "| Result:", result)

#################################################################################
def infix_to_prefix(expression):
    # Reverse the expression and swap parentheses
    reversed_expr = expression[::-1]
    
    reversed_expr = reversed_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    postfix = ExpressionEvaluator.infix_to_postfix(reversed_expr)
    return postfix[::-1]

# Example
infix_expr = "(a-b)*c"
prefix_expr = infix_to_prefix(infix_expr)
print("Prefix:", prefix_expr)
###################################################################################
def logical_to_postfix(expression):
    return ExpressionEvaluator.infix_to_postfix(expression)

# Example
query = "(a AND c) OR b"
postfix_query = logical_to_postfix(query.replace("AND", "&").replace("OR", "|"))
print("Postfix Logical Query:", postfix_query)
##################################################################################
variables = {'X': 9, 'Y': 8, 'Z': 3}

def evaluate_postfix_with_vars(expression, variables):
    stack = []
    for char in expression:
        if char.isnumeric():
            stack.append(variables.get(char, int(char)))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '*':
                stack.append(a * b)
    return stack[0]

# Example
postfix_expr = "XY+Z*"
result = evaluate_postfix_with_vars(postfix_expr, variables)
print("Result:", result)
#################################################################################
def chatbot_response(query):
    expression = query.replace("What is", "").strip().strip("?")
    postfix = ExpressionEvaluator.infix_to_postfix(expression)
    result = ExpressionEvaluator.evaluate_postfix(postfix)
    return f"The result is {result}"

# Example
query = "What is (8+4)*23?"
response = chatbot_response(query)
print(response)
############################################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def prefix_to_tree(expression):
    stack = []
    for char in reversed(expression):
        if char.isalnum():
            stack.append(Node(char))
        else:
            node = Node(char)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[0]

def inorder_traversal(node):
    if not node:
        return ""
    return f"({inorder_traversal(node.left)}{node.value}{inorder_traversal(node.right)})"

# Example
prefix_expr = "= - * c * a b"
root = prefix_to_tree(prefix_expr)
print("Infix from Prefix Tree:", inorder_traversal(root))
#######################################################################
def evaluate_rpn(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack[0]

# Example
postfix_expr = "90 2 53 - *"
result = evaluate_rpn(postfix_expr)
print("Result:", result)

