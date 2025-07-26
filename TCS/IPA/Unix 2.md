# 📘 UNIX MCQs – Practice Set

---

### Q1.

The command used to find the count of only words in a file?
**A.** `wc -w <filename>`
**B.** `wc --words <filename>`
**C.** `wc <filename>`
**D.** None of the options

---

### Q2.

Which command is used to change permission levels of a file or directory?
**A.** `passwd`
**B.** `unset`
**C.** `return`
**D.** `chmod`

---

### Q3.

What will be the output of the below awk script?

```bash
awk 'BEGIN{s=0 while (s<55) {print s;++s}}'
```

**A.** Prints the numbers from 0 to 55.
**B.** Prints the numbers from 0 to 54.
**C.** Command will throw a syntax error
**D.** It will go into infinite loop.

---

### Q4.

What is the syntax to combine the content of two files (file1, file2) into another file (newfilename)?
**A.** `cat file1 file2 > newfilename`
**B.** `cat file1 file2 >> newfilename`
**C.** `cat file1 file2 < newfilename`
**D.** `cat file1 file2 << newfilename`

---

### Q5.

Which command deletes only the folder which is empty?
**A.** `rm`
**B.** `rmdir`
**C.** `rm -rf`
**D.** `rmdir -i`

---

### Q6.

Which symbol is used with `grep` to match the pattern `pat` at the beginning of a line?
**A.** `^pat`
**B.** `pat^`
**C.** `$pat`
**D.** `pat$`

---

### Q7.

User is in `/home/u123456/project/module1`. After running `$ cd`, what is the previous directory?
**A.** `/home/u123456/project/module1`
**B.** `project/module1`
**C.** `~/project/module1`
**D.** `/usr/u123456/project/module1`

---

### Q8.

Which command deletes the lines containing the pattern `'this'` from the file?
**A.** `delete -f this file`
**B.** `SED /this/d file`
**C.** `Sed '/this'/d file`
**D.** `sed '/this/d file`

---

### Q9.

Assuming the files `fileA`, `fileB`, `fileAB`, `fileBC`, and `fileABC`, what does
`ls testDir | grep file[AB]` return?
**A.** `fileA`
**B.** `fileB`
**C.** `fileABC`
**D.** `fileBC`

---

### Q10.

Which is the command used in Unix to remove duplicate lines?
**A.** `sort -u`
**B.** `sort uniq`
**C.** `uniq`
**D.** `uniqe`

---

### Q11.

Which of the given options are environment variables?
**A.** `HOME`
**B.** `PATH`
**C.** `head`
**D.** `sort`

---

### Q12.

Given `filea.txt` contains:

```
hi all  
hello everyone  
good morning
```

Which commands will print the first line?
**A.** `head -1 filea.txt`
**B.** `awk 'NR==1' filea.txt`
**C.** `sed -n '1p' filea.txt`
**D.** `echo $1 filea.txt`

---

### Q13.

What will be the output of:

```bash
sort file1 | uniq -u
```

**A.** Command has syntax error
**B.** Finds the unique lines in the file and sort it
**C.** Displays duplicate lines in the file
**D.** Displays distinct (non-repeated) lines in the file

---

### Q14.

Which command gives the length of the longest line in a file?
**A.** `wc -l <"filename">`
**B.** `wc -L`
**C.** `wc -c1`
**D.** `wc -longest`

---

### Q15.

Which command is used to compress a file in Unix?
**A.** `zip`
**B.** `gzip`
**C.** `compress`
**D.** `comp`

---

### Q16.

Given:

```bash
awk 'BEGIN{FS=" ";s=0}{s=s+$2}END{print s}' file
```

What is the output?
**A.** Sum of first column
**B.** Sum of second column
**C.** Average of first column
**D.** Average of second column

---

### Q17.

Command to change the access time of a file to **12:10 PM, 28th Feb 1999**?
**A.** `touch -a 2802991210 filename`
**B.** `touch -a 1210280299 filename`
**C.** `touch -a 0228121099 filename`
**D.** `touch -a 9902281210 filename`

---

### Q18.

Command to search the pattern “Hello UNIX” in a file, ignoring case?
**A.** `grep -i "Hello UNIX" filename`
**B.** `grep -c "Hello UNIX" filename`
**C.** `grep -i filename 'Hello UNIX'`
**D.** `grep -c filename 'Hello UNIX'`

---

### Q19.

Given `animal.txt`:

```
1 cow  
2 goat  
3 dog  
4 cat  
5 hen
```

What will the output be?

1. `grep -o cat animal.txt`
2. `grep 'cat' animal.txt`
   **A.** None / cat
   **B.** cat / None
   **C.** 4 cat / caat
   **D.** cat / 4 cat

---

### Q20.

Given `Example.txt`:

```
Java Programming Language.  
Java and Python are programming languages.  
Python Programming language
```

What is the output of:

```bash
grep -v Java Example.txt
```

**A.** Java and Python are programming languages. Python Programming language.
**B.** Java Programming Language. Java and Python are programming languages.
**C.** Python Programming language.
**D.** Java Programming Language. Python Programming language.

---

### Q21.

File permission of 754 (octal) is equal to which symbolic format?
**A.** `-rwxr-xr--`
**B.** `-rw--w-r-x`
**C.** `-rwxr-xr-x`
**D.** `-rwxrw-r--`

---

# ✅ Answers

1. A
2. D
3. C
4. A
5. B
6. A
7. A *(refers to current directory **before** running `cd`)*
8. D
9. A, B *(matches `fileA`, `fileB`, `fileAB`, etc.)*
10. C *(also valid: A, but `uniq` is the more direct command)*
11. A, B
12. A, B, C
13. D
14. B
15. A, B, C
16. B
17. C
18. A
19. D
20. C
21. A

