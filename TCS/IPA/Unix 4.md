# UNIX Commands
This page lists some of the more commonly used UNIX commands.

## About UNIX
*   Commands are typed at a prompt. Most often, the prompt is a percent sign (%) or dollar sign ($) but sometimes it is the name of the machine followed by the percent or dollar sign.
*   Commands are case sensitive and are usually lower case. This means that `ls` and `LS` are completely different commands.
*   Spaces are very important. There is always a space between the command and the file or directory it acts upon.
*   To execute a UNIX command, press Enter at the end of the command line. If the command is accepted, the prompt and cursor will simply appear on the next line awaiting your next command. If the command is rejected, an error message such as "Command not found" appears. Check your spelling, spaces, etc and try to reenter the command. To negate a command before you have pressed Enter, press **CTRL + C**.
*   To determine your default shell, type `echo $SHELL`.
*   To change your default shell, run `/usr/local/bin/chsh` and follow the prompt. Do NOT use flags on the command. This is a custom script and not the standard chsh you might find on Linux machines. After running the command, allow 24 hours for the default shell to take effect.
*   Dot files begin with a dot (.) and are used primarily to control system functions. Unless you are an advanced UNIX user, you should not add or delete anything from a dot file.

## Common UNIX Commands

| Command | Action |
| :--- | :--- |
| `cat <file>` | Print contents of file in the command window |
| `cd <directory>` | Change directories |
| `cp <file> <file2>` | Copy the contents of file into file2 |
| `history` | List history of all commands issued at system prompt |
| `ls` | List the files and subdirectories in a directory |
| `ls -F` | List the difference between files and directories--directories have a slash (/) |
| `ls -l` | List files with status/detail information |
| `ls -lt` | List file information in long format, sorted by time with newest files or newly changed files appearing first |
| `ls -a` | List all the files in a directory including dot files |
| `fs lq` | Lists AFS quota, space used, percentage used |
| `fs q` | Lists percentage of quota used |
| `mkdir <directory>` | Make a directory |
| `mv <file> <file2>` | Move file to file 2 |
| `pwd` | Print the pathname of the current directory |
| `rm <file>` | Remove or delete files |
| `rmdir <directory>` | Remove directory |
| `Ctrl + C` | To negate a command that you have entered. |

## Command Examples

### Navigating the File System (cd command)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To move to your home directory | Type `cd` and press **Enter**. | | No matter where you are in the file system, you can use the `cd` (change directory) command to get you back to your home directory immediately. |
| To move to a subdirectory of your own | Type `cd <path>` and press **Enter**. | `cd public` <br><br> *To change from your home directory to your public directory.* | When you are changing directories down from your current working directory, it is not necessary to type the full pathname. |
| To move to another person's home directory | Type `cd <path>` and press **Enter**. | `cd /afs/andrew.cmu.edu/usr11/juser` | In this example, the `<path>` is the full path of the other person's directory. |

### Tilde (~)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To abbreviate the pathname. | Type `cd ~<Andrew ID>` and press **Enter**. | `cd ~juser` <br><br> *To change into juser's directory without typing in the full path name.* | The tilde is helpful when you don't know someone's complete pathname, or when you just want to save typing time. <br><br> The tilde can be used with any UNIX command; however, you should never use the tilde in command files such as .login or in your preferences file. In these cases, the tilde may not be recognized and can prevent Andrew and UNIX from working properly for you. |

### Where am I? (pwd)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To "ask" UNIX which directory you are in. | Type `pwd` and press **Enter**. | | |

### View directory contents (ls)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| View names of files and subdirectories in a directory. | Type `ls` and press **Enter**. | | The `ls` command does NOT list any dot files (i.e., files that begin with dot (.) |
| To list files with status information | Type `ls -l` and press **Enter**. | | The `ls -l` command lists the file name, its owner, date last changed, and size. Files that are directories are preceded with a "d"; plain files have an -rw-. |
| To easily view differences between files and directories. | Type `ls -F` and press **Enter**. | | Directories will be listed with a "/". |
| To list ALL files, including Dot files. | Type `ls -a` and press **Enter**. | | |
| Recursive file listing | Type `ls -R` and press **Enter**. | | Lists the files in the current directory as well as those in the subdirectories. |

### Create Directory (mkdir)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| Create a directory | Type `mkdir <directoryname>` and press **Enter**. | `mkdir playground` <br><br> *To make a new directory called playground.* | Once you've made the directory, use the `ls` command to verify. |

### Copy Files (cp)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To copy a file in the same directory. | Type `cp <file> <file.copy>` and press **Enter**. | `cp resume resume.copy` <br><br> *To make a copy of a file named "resume" in the same directory.* | |
| To copy a file into another directory. | Type `cp <file> <directory>` and press **Enter**. | `cp resume private` <br><br> *To make a copy of a file named "resume" in the private directory.* | |
| To copy a file into another user's account. | Type `cp <path>/<file> <path>/<file>` and press **Enter**. | `cp ~juser/notes sample/notes.joe` <br><br> *To copy a file named "notes" from your friend Joe's account into your sample directory and name the file notes.joe.* | |

### Move Files or Directories (mv)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To move a file to a new file in the same directory (i.e., rename a file). | Type `mv <file> <file2>` and press **Enter**. | `mv notes.joe notes.working` <br><br> *To move a file named "notes.joe" to a file named "notes.working." In this case, mv is simply renaming the file.* | The difference between `mv` and `cp` is that `cp` places a copy of the file in a new location without disturbing the original copy. The `mv` commands deletes the file from its old location after saving it in the new location. |
| To move a file to a new file in a different directory | Type `mv <file> <path>/<file>` and press **Enter**. | `mv notes public/notes` <br><br> *To move a file named "notes" from your home directory into your public directory, while IN your home directory.* | The `mv` command is also used to move directories. |

### Remove a File (rm)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To remove a file. | Type `rm <file>` and press **Enter**. | `rm notes.working` <br><br> *To remove the file named "notes.working"* | |
| Prompt remove | Type `rm -i` and press **Enter**. | | To invoke a prompt before removing a file; waits for a "Y" or "N" response. |

### Remove a Directory (rmdir)
| Function | Command | Example | Notes |
| :--- | :--- | :--- | :--- |
| To remove a directory (that does not contain files). | Type `rmdir <directory name>` and press **Enter**. | `cd [Enter]` <br> `rmdir sample` <br><br> *To remove a directory named "sample" which is a subdirectory of your home directory.* | Because the "sample" directory is in a subdirectory of your home directory, you must first move to your home directory (`cd`). |
| To force removal of a directory that contains files. | Type `rmdir -r <directory name>` and press **Enter**. | | Removes a directory even if it contains files. |
