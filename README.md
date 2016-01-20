# Assignment 2

Now that you have most of your Python environment installed, we're going to start getting used to some interesting things about Python, before we make a side trip to talk about regular expressions.

## Running Python

The following is a very short program - you should recognize what it does:

```
#!/usr/bin/env python
# encoding: utf-8

"""
my first little program

Created by Brant Faircloth on 18 Jan 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.

"""

import sys

print("Python {}".format(sys.version_info))
print("Hello world")

```

1. Take 3 screenshots showing 3 of the different ways that you can run the contents of the program above.  It does not matter which 3 you use, just that they are different.  I can think of at least 4 ways to do this, and there are probably several more.

## Imports

The following lines of code all import pieces of the [numpy](https://en.wikipedia.org/wiki/NumPy) module in different ways:

`import numpy`

`from numpy import *`

`from numpy import random`

1. How are these different from each other?  Be specific.
2. Which of the above do you think is preferred?  Why?
3. What happens to the `stdlib` module `random` if you run `from numpy import random`?  Provide an example.


## Paths

Paths are really important.  Paths are also *really confusing* and they can be really frustrating, because the term `path` can actually have a couple of different meanings.

1. On your computer, create a file on the Desktop.  What's the path to that file (e.g. the file path)?
1. If you created a file in the `root` directory of your computer, what would that file path be?
1. On your computer, there is a setting/variable called $PATH.  What does that setting do?
1. On your computer, there is a setting/variable called $PYTHONPATH.  What does that setting do?

## Modules

1. Pick a module from the Python `stdlib` or a third-party module.  Write a 250 word summary of the purpose of that module and how it might be useful to you as we move through this class.  Feel free to do this in iPython and include examples to make your points clearer (or to briefly illustrate what the module does).  Feel free also to look at the documentation of that module and/or any online resources, but please cite those.
