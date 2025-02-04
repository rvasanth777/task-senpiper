def check_braces(string):
    stack = []
    for char in string:
        if char in "{(":
            stack.append(char)
        elif char in "})":
            if not stack or (stack[-1] == "{" and char != "}") or (stack[-1] == "(" and char != ")"):
                return False
            stack.pop()
    return not stack

input_str = "List { information {{about the FILEs (the current directory by default). Sort entries alphabetically if} none of -cftuvSUX }nor --sort } is specified."
print(check_braces(input_str))

