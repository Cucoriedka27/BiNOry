# BiNory
## What is it?
BiNory is an esoteric programming language or esolang for short. It's intention is to look like binary so it only uses the characters `1` and `0`.

- Idea by Čučoriedka
- Interpreter in python by Čučoriedka

## Definition
BiNory is a stack based language that only uses the characters `1` and `0`.

### Instructions

- `1` Pushes the value 1 on top of the stack.
- `0` Pops the top value on the stack and does an operation based on the following opcode table, if the opcode is incorrect then 

|opcode|description|
|------|-----------|
|`0`| Pops the top value |
|`1`| Pops the top 2 values, adds them together, and pushes the result onto the stack |
|`2`| Pops the top value, and pushes its negative |
|`3`| Pops the top value, and pushes the same value onto the stack twice |
|`4`| Pushes the ammount of values on the stack |
|`-1`| Pops the top value, and rotates the top n values (where n is the positive of the value popped) down if positive, or up if negative (eg. `5 4 3 2 1` if rotated by `3` will become ` 5 4 2 1 3` and with `-3` will become `5 4 1 3 2`)|
|`-2`| Pops the top value, and outputs it as an ASCII character |
|`-3`| Pushes 1 value from the input stream of the console  as an ascii character, and a `1` if there is another value or `0` if there isn't |
|`-4`| Pops the top value, and jumps that ammount of instructions forward (clamps the pointer between the start and end of the code) |