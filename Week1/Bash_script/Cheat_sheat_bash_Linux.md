# Bash Script (Linux commands)

Here you will see a summary of the common commands use in Linux (Unix) environment. We will just give examples of the ones we will use more frequently during the workshop. This commands can't be used in Windows environment unless you use a [Linux emulator](https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi5tb-ijtPPAhWD7hoKHdyTA-IQFggmMAE&url=https%3A%2F%2Fwww.cygwin.com%2F&usg=AFQjCNHet6tpyafCXeYZCDWdFVdg2_A4IQ&sig2=jK-xBiPuohBaZkfcHhnHUw).
If you need information in the terminal about an specific Linux/Unix command you can type a command line on the terminal:
```Bash
$ man ls
```
To escape from the manual, just type: *q*

### File Commands

<img src="File_commands.png" alt="File commands" style="width: 300px;"/>

Examples - Create a File:
``` bash
$ nano file.txt
Method 1: In nano editor:
1. echo "Hello World!"
2. "ctrl + x", and save
Method 2: Using cat:
1. cat >file2.txt
2. type in "Hello Universe!"
3. "ctrl + d"
```

Examples - working with directories:
``` bash
$ ls
$ ls -al
$ ls -alrt
$ pwd
$ mkdir codes
$ mkdir temp temp1
$ mkdir temp2/ok
$ cat file.txt
$ cat file.txt file2.txt > fileOut.txt
$ rm file.txt
$ rm -r temp2/ok
$ rm -r temp2
$ df -h
$ 
```

**Note:** **rm \*** it is a dangerous command that should be use with care, you might lose all your work!!
### Directory

<img src="Directory_access.png" alt="Directory Access" style="width: 300px;"/>




[Reference](https://drive.google.com/drive/u/0/folders/0B_LZEs2baSXxb0FwcXRLeGRrV2c)
