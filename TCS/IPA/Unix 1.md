## UNIX MCQ Practice Questions

### Section: Intro to UNIX

**Q1.** Which of the following is not a part of all the versions of UNIX?

* a) System Calls
* b) Graphical user interface
* c) Kernel and Shell
* d) Commands and utilities

**Q2.** What is UNIX?

* a) an operating system
* b) a text editor
* c) programming language
* d) software program

**Q3.** Which of the following is not a function of an OS?

* a) Memory management
* b) Disk management
* c) Application management
* d) Virus protection

**Q4.** What are the three main components of the UNIX Architecture?

* a) Kernel, Data, PC
* b) PCB, Utilities Shell
* c) Shell, Kernel, Shared memory
* d) Kernel, Shell, Utilities

**Q5.** The operating system manages

* a) Devices
* b) Memory
* c) All of the above
* d) Processes

### Section: Basic Commands

**Q1.** A file's modification time can be changed by using:

* a) new access
* b) change
* c) touch
* d) cat

**Q2.** Which command is used to recursively copy the files?

* a) cp -a
* b) cp -all
* c) cp -r
* d) cp -v

**Q3.** The command `echo welcome > /dev/tty`

* a) Both (a) and (c)
* b) Echoes welcome only in the terminal in which it is run
* c) Echoes welcome in all the terminals that are switched on
* d) Echoes welcome in all the terminals that are logged on

**Q4.** Which command can be used to append some text at the end of some file?

* a) cat >
* b) append
* c) cat
* d) cat >>

**Q5.** Which Command is used to Sort the lines of data in a file in reverse order?

* a) St
* b) Sort -r
* c) Sh
* d) Sort

### Section: Filters and Pipes

**Q1.** Correct syntax for matching patterns `bunk` or `bank` at the end of a line:

* a) `grep 'b[au]nk$' myFile`
* b) `grep b[a-u]nk$ myFile`
* c) `grep 'b[au]nk$' myFile`
* d) `grep b[au]nk$ myFile`

**Q2.** Regex matching a b c d 5 6 7 8 X Y Z:

* a) `[a-d/5-8/X-Z]`
* b) `[a-d][5-8][X-Z]`
* c) `['a-d''5-8''X-Z']`
* d) `[a-d5-8X-Z]`

**Q3.** In expression `grep 'A'stop\!' sign' myfile`, `\` is used to:

* a) escape the ! character
* b) print lines in new line
* c) match pattern `stop!`
* d) match `stops!`, `stop!`, etc.

**Q4.** Meaning of `$` character in single quoted regex:

* a) anchor in double quotes
* b) anchor in single quotes
* c) anchor if at end in single quotes
* d) shell variable syntax

**Q5.** Regex to match `TCS` only at the beginning:

* a) ^TCS
* b) TCS\$
* c) ^TCS
* d) \$TCS

### Section: Shell Scripting

**Q1.** Command to view previous commands:

* a) history
* b) Delete
* c) add
* d) Update

**Q2.** Syntax for back quotes in shell scripting:

* a) var=`command`
* b) var='command'
* c) var="command"
* d) var="'command'"

**Q3.** Supported operators in shell:

* a) All of the above
* b) Arithmetic
* c) Boolean
* d) Relational

**Q4.** Methods to execute shell script:

* a) \$ sh filename or \$ ./filename
* b) \$ ./filename
* c) \$ ./filename or \$/'
* d) \$h ./filename

**Q5.** Symbol to represent characters:

* a) Regular Expression
* b) Alphanumeric
* c) Isnumeric
* d) Wild Card

### Section: Environment Variable

**Q1.** Can env vars change program behavior?

* a) Yes
* b) No

**Q2.** Displays all env vars:

* a) environ
* b) env
* c) HOME
* d) HOM

**Q3.** Variable for current username:

* a) PATH
* b) HOME
* c) LOGNAME
* d) none

**Q4.** Command to determine value of a variable:

* a) echo
* b) cat
* c) ls
* d) set

### Section: Process and Job

**Q1.** Command to bring process to foreground:

* a) ps %
* b) fg %
* c) bg %
* d) ps &

**Q2.** Process that exits but parent didn’t collect exit status becomes:

* a) new
* b) stopped
* c) orphan
* d) zombie

**Q3.** Command to suspend process:

* a) + s
* b) zz
* c) + z
* d) All of above

**Q4.** Command to list all processes:

* a) ps -x
* b) ps
* c) ps -f
* d) ps -e

**Q5.** Invalid process state:

* a) none of these
* b) Ready
* c) New
* d) Running

### Section: Final UNIX

**Q1.** Find lines with word "not" in `myText.doc`:

* a) find -name "not" myText.doc
* b) grep "not" myText.doc
* c) grep -w not myText.doc
* d) find -type w not myText.doc

**Q2.** Which are relative paths? (multi-choice)

* a) /usr/home/unixData/backups
* b) unixData/backups
* c) \~/unixData/backups
* d) /home/unixData/backups

**Q3.** Heart of OS that manages memory and tasks:

* a) H/W
* b) Kernel
* c) Shell
* d) process

**Q4.** Incorrect info about UNIX filesystem:

* a) i-node contains metadata and block pointers
* b) All files/dirs in data blocks
* c) Superblock stores free block list and counts
* d) Each i-node is 256-bytes

**Q5.** Command to set env var for shell scope:

* a) All of these
* b) export
* c) set
* d) export and set

**Q6.** UNIX modes of operation: (multi-choice)

* a) Kernel Mode
* b) Direct Mode
* c) Boot Mode
* d) User Mode

**Q7.** Symbol to separate multiple commands:

* a) \$
* b) |
* c) #
* d) ;

**Q8.** `diff file1.txt file2.txt` shows `4d3 < I am leaving.` What it means?

* a) Delete 4 lines from file1
* b) Delete line 4 in file1
* c) Delete line 4 from file1 and line 3 from file2
* d) Delete line 4 in file2

**Q9.** Shell script comment starts with:

* a) !
* b) //
* c) #
* d) -

**Q10.** Program that runs other programs:

* a) echo
* b) shell
* c) cat
* d) ls

**Q11.** Output of `echo "var=5; ++var" | bc`

* a) 6
* b) None of these
* c) 56
* d) 5

**Q12.** Command to find PID of current shell:

* a) echo \$
* b) \$PATH
* c) \$SHELL
* d) echo \$\$

**Q13.** Variable to find location of commands:

* a) HOME
* b) PATH
* c) ROOT
* d) BIN

**Q14.** Command for job priority:

* a) ps
* b) nice
* c) top
* d) nohup

**Q15.** Command to compute 4+2:

* a) bc < 4+2
* b) bc << 4+2
* c) bc <<< 4+2
* d) None of these

**Q16.** How to connect multiple commands:

* a) None of these
* b) Filters
* c) Pipe
* d) Shell

**Q17.** System call to create process:

* a) invoke
* b) init
* c) fork
* d) create

**Q18.** Every process has one parent; can have many children:

* a) FALSE
* b) TRUE

**Q19.** Output of `[ "awesome" = "awesome" ]; echo $?`

* a) 0
* b) awesome
* c) 'awesome'='awesome'
* d) 1

**Q20.** Output of `seq 1 0.1 19|grep -c '0$'`

* a) Syntax error
* b) 19
* c) 1
* d) 28

---

## Answers Key

**Intro to UNIX:** 1-b, 2-a, 3-d, 4-d, 5-c
**Basic Commands:** 1-c, 2-c, 3-b, 4-d, 5-b
**Filters and Pipes:** 1-a, 2-d, 3-a, 4-c, 5-c
**Shell Scripting:** 1-a, 2-a, 3-a, 4-a, 5-d
**Environment Variables:** 1-a, 2-b, 3-c, 4-a
**Process and Job:** 1-b, 2-d, 3-c, 4-d, 5-a
**Final UNIX:** 1-c, 2-b,c, 3-b, 4-d, 5-b, 6-a,d, 7-d, 8-b, 9-c, 10-b, 11-a, 12-d, 13-b, 14-b, 15-c, 16-c, 17-c, 18-b, 19-a, 20-d
