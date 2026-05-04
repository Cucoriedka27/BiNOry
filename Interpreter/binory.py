import sys
import random

class InStream:
    def __init__(self):
        self.buffer = ""

    def next_char(self):
        if not self.buffer:
            self.buffer = list(input())

        char = self.buffer.pop(0)
        has_more = 1 if self.buffer else 0
        return char, has_more
    
def safePop(stack, n=None):
    try: 
        return stack.pop(n)
    except IndexError:
        return random.randint(0, 1)

def rotate(stack, n):
    if n == 0:
        return stack
    if n > 0:
        if len(stack) - n < 0:
            stack.append(random.randint(0, 1))
        else:
            value = safePop(stack, len(stack) - n)
            stack.append(value)
        return stack
    if n < 0:
        if len(stack) + n < 0:
            safePop(stack)
        else:
            stack.insert(len(stack) + n, safePop(stack))
        return stack


def main():
    debug = False
    code = ""
    arguments = sys.argv
    arguments.pop(0)

    if len(arguments) == 0:
        print("Usage: python binory.py filepath.bino [debug: True/False]")
        return
    
    with open(arguments[0], "r") as f:
        code = f.read()
    
    if len(arguments) >= 2:
        if arguments[1] == "True":
            debug = True

    if debug: 
        code = ''.join(filter(lambda x: x in '10+', code))
    else:
        code = ''.join(filter(lambda x: x in '10', code))

    ip = 0
    stack = []
    instream = InStream()

    while True:
        if ip >= len(code) or ip < 0:
            break

        match code[ip]:
            case '+':
                if debug:
                    print(stack)
            case '1': 
                stack.append(1)
            case '0':
                op = safePop(stack)
                match op:
                    case 0:
                        safePop(stack)
                    case 1:
                        stack.append(safePop(stack) + safePop(stack))
                    case 2:
                        stack.append(-safePop(stack))
                    case 3: 
                        value = safePop(stack)
                        stack.append(value)
                        stack.append(value)
                    case 4: 
                        stack.append(len(stack))
                    case -1:
                        value = safePop(stack)
                        stack = rotate(stack, value)
                    case -2:
                        print(chr(safePop(stack)), end="")
                    case -3:
                        char, has_more = instream.next_char()
                        stack.append(ord(char))
                        stack.append(has_more)
                    case -4:
                        ip += safePop(stack) - 1
        ip += 1

if __name__ == "__main__":
    main()