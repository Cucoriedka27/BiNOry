def run_code(code: str):
    stack = []
    new_code = ""
    for c in code:
        if c == "0" or c == "1":
            new_code += c
    code_pointer = 0
    while code_pointer < len(new_code):
        command = new_code[code_pointer]
        if command == "1":
            stack.append(1)
            code_pointer += 1
        else:
            opcode = stack.pop()
            match opcode:
                case 0:
                    if len(stack) < 1:
                        print(f"Too little values on stack for opcode {opcode}")
                        return
                    stack.pop()
                    code_pointer += 1
                case 1:
                    if len(stack) < 2:
                        print(f"Too little values on stack for opcode {opcode}")
                        return
                    stack.append(stack.pop() + stack.pop())
                    code_pointer += 1
                case 2:
                    if len(stack) < 1:
                        print(f"Too little values on stack for opcode {opcode}")
                        return
                    stack[-1] = -stack[-1]
                    code_pointer += 1
                case 3:
                    if len(stack) < 1:
                        print(f"Too little values on stack for opcode {opcode}")
                        return
                    stack.append(stack[-1])
                    code_pointer += 1
                case -2:
                    if len(stack) < 1:
                        print(f"Too little values on stack for opcode {opcode}")
                        return
                    print(chr(stack.pop()), end="")
                    code_pointer += 1
                case _:
                    print(f"Unknown opcode {opcode}")
                    return


if __name__ == "__main__":
    print("BiNOry")
    print()
    while True:
        run_code(input("> "))
        print()