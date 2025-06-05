import sys

class InStream:
    def __init__(self):
        self.buffer = ""

    def next_char(self):
        if not self.buffer:
            self.buffer = list(input())

        char = self.buffer.pop(0)
        has_more = 1 if self.buffer else 0
        return char, has_more

def rotate(stack, n):
    if n == 0:
        return stack
    if n > 0:
        value = stack.pop(len(stack) - n)
        stack.append(value)
        return stack
    if n < 0:
        stack.insert(len(stack) + n, stack.pop())
        return stack

def main():
    debug = True
    code = ""
    arguments = sys.argv
    arguments.pop(0)
    if len(arguments == 0):
        print("Usage: python binory.py filepath.bino")
        return
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
                op = stack.pop()
                match op:
                    case 0:
                        stack.pop()
                    case 1:
                        stack.append(stack.pop() + stack.pop())
                    case 2:
                        stack.appent(-stack.pop())
                    case 3: 
                        value = stack.pop()
                        stack.append(value)
                        stack.append(value)
                    case 4: 
                        stack.appent(len(stack))
                    case -1:
                        value = stack.pop()
                        stack = rotate(stack, value)
                    case -2:
                        print(chr(stack.pop))
                    case -3:
                        char, has_more = instream.next_char()
                        stack.append(char)
                        stack.append(has_more)
                    case -4:
                        ip += stack.pop() - 1
        ip += 1

if __name__ == "__main__":
    main()