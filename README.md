# win95keys
[![Run](https://github.com/syntaxerror-usl/win95keys/actions/workflows/python-app.yml/badge.svg)](https://github.com/syntaxerror-usl/win95keys/actions/workflows/python-app.yml)
## A simple program to generate all possible keys for Microsoft Windows 95

### How to use
* Clone repository
* Run win95keys.py
```
$ python3 win95keys.py
Hi there!
This simple program generates all possible retail installation keys for Windows 95.

An example on which the generation is based: 111-11111111
111 - Blacklist
1111111 - Sum divisible by 7
Source: https://www.youtube.com/watch?v=cwyH59nACzQ

By the way, if you have a wooden PC, the system may slow down a little during the process.
Well, 'Blacklist' is actually any number between 000 and 332. It will only be used one for all keys.
Let's start? ('yes' to start, else - ignore):
```

### What's next
Enter "yes" to start the main program loop. It will last about two minutes.
```
...

Done!
Keys: 1428653
Time for generate: 62 seconds
Here are your well-deserved 5 keys.
196-2148668
196-0194016
196-5019256
196-6894242
196-7876383
```

### Save to file
To really see all possible keys, you need to save the keys in a txt file. This will take a very long time, since all keys will take ~1 GB.
```
...

--- Save ---
It will take an incredibly long time (+1-2gb on hdd), maybe not?
Save to file? ('yes' to save, else - ignore):
```

### Special function
If you run the program with the -r argument, after a couple of minutes you will get one random key.
```
$ python3 win95keys.py -r
Generating keys, please wait...
Random key: 302-1624877
```

### Why is this program needed?
Actually this program is useless. Maybe for educational purposes you will certainly be interested in learning these keys.
