

def print_line(line):
    print(line)   

def do_four(function, param1):
    function(param1)
    function(param1)
    function(param1)
    function(param1)

def print_block(line):
    print("+ - - - - + - - - - +")
    do_four(print_line, line)

def do_two(function, line):
    function(line)
    function(line)

do_two(print_block, "|   ---   |   ---   |")
print("+ - - - - + - - - - +")

