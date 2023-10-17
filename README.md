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
  (wip but will be an array/tape command)

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

- other (wip)


## Examples

- Add 0 to the stack
  `1 1 11100 10`

- Hello World
  `fuck no` (I dare Čučoriedka to make one.)

