Sorry for the name ! 

This is a massively over-engineered implementation of a simple task, meant to help me learn domain-driven design and python packaging. And other things. 

But it works and can be useful. 

### Purpose 

It's a CLI interface that allows you to 

1. record start/end time of your work with around a click, instead of opening a csv and typing date-time. You may directly add a work session that you pre-define yourself (useful e.g. if you forgot to run the program while working, or if it crashed). 

2. fits all that into a template bill with around a click, instead of manually filling yourself your file. 

### Usage 


1. Keeping track of work : when you start working, open a terminal window and start
recording your work session running `freebilly record-session`. See
`freebilly record-session --help` for more information. You may directly supply a work session with `freebilly supply-session`. See `freebilly supply-session --help`. 
3. Billing : build whatever bill template you want (for example, a `.tex` file), and fill it with your work log information and other extra things by running `freebilly produce-bill`
on your terminal. See `freebilly produce_bill --help` for more information. 

### Installation

It's stored in the TestPyPi package repository, which doesn't have everything PyPi does. So make sure your environment has the dependencies 
specified in `setup.cfg`. Then run : 

`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps freebilly`
