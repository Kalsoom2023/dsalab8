Objective
In this lab, we will explore how to evaluate mathematical expressions written in Prefix and Postfix notation. We will implement evaluators for these notations, using stacks to help process the operations.

Key Concepts:
Prefix Notation (Polish Notation): The operator comes before its operands. For example, + 3 4 is equivalent to 3 + 4 in infix notation.
Postfix Notation (Reverse Polish Notation): The operator comes after its operands. For example, 3 4 + is equivalent to 3 + 4 in infix notation.
Expressions
Prefix Expression Example:
Prefix: + 3 * 2 5
Infix: 3 + (2 * 5)
Postfix: 3 2 5 * +
Postfix Expression Example:
Postfix: 3 4 + 5 *
Infix: (3 + 4) * 5
Prefix: * + 3 4 5
Both Prefix and Postfix expressions have the advantage of being unambiguous, unlike infix expressions, which may require parentheses to clarify operator precedence.

Approach
We'll implement two evaluators:

Prefix Evaluator: The expression is evaluated starting from the rightmost operator. We use a stack to store operands and apply operators when encountered.
Postfix Evaluator: The expression is evaluated starting from the leftmost operator. Operands are pushed to the stack, and operators apply to operands popped from the stack.
Prefix Evaluator
Steps for Evaluating Prefix Expressions:
Traverse the expression from right to left.
For each character:
If it's an operand (number), push it onto the stack.
If it's an operator, pop two operands from the stack, apply the operator, and push the result back onto the stack.
The result will be the only value left in the stack.
C++ Code Example (Prefix Evaluator):
cpp
Copy code
#include <iostream>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

int evaluatePrefix(const string& expr) {
    stack<int> s;
    for (int i = expr.length() - 1; i >= 0; i--) {
        char c = expr[i];
        
        if (isdigit(c)) {
            s.push(c - '0'); // Convert char to integer
        }
        else if (c == '+' || c == '-' || c == '*' || c == '/') {
            int operand1 = s.top(); s.pop();
            int operand2 = s.top(); s.pop();
            int result;
            
            switch (c) {
                case '+': result = operand1 + operand2; break;
                case '-': result = operand1 - operand2; break;
                case '*': result = operand1 * operand2; break;
                case '/': result = operand1 / operand2; break;
            }
            s.push(result);
        }
    }
    return s.top(); // The final result
}

int main() {
    string expr = "+ 3 * 2 5";  // Example: (3 + (2 * 5))
    cout << "Prefix Expression Result: " << evaluatePrefix(expr) << endl;
    return 0;
}
Example Output:
mathematica
Copy code
Prefix Expression Result: 13
Time Complexity:
O(n), where n is the number of characters in the expression.
Postfix Evaluator
Steps for Evaluating Postfix Expressions:
Traverse the expression from left to right.
For each character:
If it's an operand (number), push it onto the stack.
If it's an operator, pop two operands from the stack, apply the operator, and push the result back onto the stack.
The result will be the only value left in the stack.
C++ Code Example (Postfix Evaluator):
cpp
Copy code
#include <iostream>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

int evaluatePostfix(const string& expr) {
    stack<int> s;
    stringstream ss(expr);
    string token;
    
    while (ss >> token) {
        if (isdigit(token[0])) {
            s.push(stoi(token));  // Convert string to integer
        }
        else if (token == "+" || token == "-" || token == "*" || token == "/") {
            int operand2 = s.top(); s.pop();
            int operand1 = s.top(); s.pop();
            int result;
            
            if (token == "+") result = operand1 + operand2;
            else if (token == "-") result = operand1 - operand2;
            else if (token == "*") result = operand1 * operand2;
            else if (token == "/") result = operand1 / operand2;
            
            s.push(result);
        }
    }
    return s.top(); // The final result
}

int main() {
    string expr = "3 4 + 5 *";  // Example: (3 + 4) * 5
    cout << "Postfix Expression Result: " << evaluatePostfix(expr) << endl;
    return 0;
}
Example Output:
mathematica
Copy code
Postfix Expression Result: 35
Time Complexity:
O(n), where n is the number of tokens in the expression.
Comparison of Prefix and Postfix Notations:
Feature	Prefix Notation	Postfix Notation
Operator Location	Before operands	After operands
Traversal Direction	Right to left	Left to right
Parentheses Needed	No	No
Evaluation Algorithm	Right to left, stack-based	Left to right, stack-based
Usage in Programming	Less common	Common in calculators and parsers
Conclusion
In this lab, we implemented Prefix and Postfix evaluators using stacks. Both notations allow for unambiguous expression evaluation and are widely used in parsing expressions and implementing calculators. Understanding how to traverse and evaluate these notations is crucial for implementing efficient expression parsers and evaluators.
