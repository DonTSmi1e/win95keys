# Win95Keys

| Branch |                                                                                        Run status                                                                                        |
|:------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  Main  | [![Run](https://github.com/syntaxerror-usl/win95keys/actions/workflows/run-main.yml/badge.svg?branch=main)](https://github.com/syntaxerror-usl/win95keys/actions/workflows/run-main.yml) |

## A simple program to generate all possible keys for Microsoft Windows 95

### Task list
- [x] Make an optimization
- [x] Perform program control with arguments
- [ ] Optimize work with branches
- [ ] Release 1.0.0

### How to use
```
$ python3 win95keys.py

    Hi there!
    This simple program generates all possible retail installation keys
    for Windows 95.
    By the way, if you have a wooden PC,
    the system may slow down a little during the process.
    I recommend using PyPy for faster script performance.

```

Run the program with the `-g` argument for normal mode.

```
$ python3 win95keys.py -g
Generating keys, please wait...
107-0000000
107-0000007
107-0000016
107-0000025
107-0000034
107-0000043
...
```

If you need fast work, you can disable the output with the `-s` argument

```
$ python3 win95keys.py -g -s
Generating keys, please wait...

Done!
Keys: 1428653
Time for generate: 2 seconds
Here are your well-deserved 5 keys.
193-5226749
193-2978108
193-5836733
193-0817667
193-3928999
```

You can also save all generated keys to the `keys.txt` file by running the program with the `-gs` argument instead of `-g`
**_However, this will be a very lengthy process and will also take up 1 GB of your hard drive._**

```
$ python3 win95keys.py -gs -s
Generating keys, please wait...

Done!
Keys: 1428653
Time for generate: 2 seconds
Here are your well-deserved 5 keys.
314-1961774
314-1081963
314-5726546
314-6689319
314-8597805
Saving keys in keys.txt, please wait..
```

As an additional feature, there is a `-r` argument to generate one random key.

```
$ python3 win95keys.py -r

Please wait...
Generating keys, please wait...
300-2316599
```

Finally, use the `-v` argument to find out which version of the program is running.

```
$ python3 win95keys.py -v

    win95keys
    
    Version: 1.0.0
```

### Why is this program needed?
Actually this program is useless. Maybe for educational purposes you will certainly be interested in learning these keys.
