# BiNOry
Esoteric programming language that looks like binary but doesn't function like it.

- Idea by Čučoriedka
- First interpreter/some ideas by ttmso



## Opcodes

- 1
  Adds 1 to the stack.

- 0
  Pops the top value and does an "0 opcode" depending on the value.

- Anything else gets ignored.



## 0 Opcode's

- 0
  Pops the top value and does nothing.

- 1
  Pops the top 2 values, adds them together and add the result on the stack.

- 2
  Negates the top value on the stack.

- 3
  Duplicates the top value on the stack.

- 4
  first argument: the command to execute
  second argument: position on the tape
  third argument (when putting into the tape): number to store

- -1
  Pops a value and rotates that many values on the stack down (if the value is negative it will rotate the bottom values of the stack direction and if its zero nothing will happen).

- -2
  Pops and outputs the top value on the stack as an ascii character.

- -3
  Gets input from the user, adds 0 to the stack and adds the input characters in reverse (last character above the 0) to the stack.

- -4
  Pops the top value off the stack and jumps the amount of lines forward as the value (any non 1 or 0 character get ignored so if there's some text of a new line it acts like there's nothing there).

- -5
  Adds the amount of values on the stack to the stack.


## Tape Commands

- 1
  Pops the value from the stack and stores it on the location in the tape
  
- 2
  Pushes a value on the location in the tape to the stack

- other (probably not)


## Examples

- Add 0 to the stack
  `1 1 11100 10`

- Hello World v1 "H"
  `1110 1111010010 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 10 1110 11100 0`

- Hello World v2 "He"
  `1110 1111010010 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 10 11110100 1110 11100 0 1110 1111010010 1111010010 1111010010 1111010010 10 1111010 11100 10 11110100 1110 11100 0`
  
- Hello World v3 "Hello"
  `1110 1111010010 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 10 11110100 1110 11100 0 1110 1111010010 1111010010 1111010010 1111010010 10 1111010 11100 10 11110100 1110 11100 0 1110 1111010010 1111010010 1 11100 1010 11110100 11110100 1110 11100 0 1110 11100 0 1111010 10 11110100 1110 11100 0`
- Hello World v4 "Hello, Wo"
  `1110 1111010010 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 10 11110100 1110 11100 0 1110 1111010010 1111010010 1111010010 1111010010 10 1111010 11100 10 11110100 1110 11100 0 1110 1111010010 1111010010 1 11100 1010 11110100 11110100 1110 11100 0 1110 11100 0 1111010 10 11110100 1110 11100 0 1110 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 10 1111101010 10 1110111000 1110 1111010010 1111010010 1111010010 1111010010 1110111000 1110 1111010010 1111010010 1111010010 1111010010 1111010010 1110 1111010010 1111010010 1111010010 10 1110 1111010010 1111010010 111100 1010 1110111000 1111010 0 1110111000 1111010 10`

