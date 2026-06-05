import sys

def ping():
    print("ok")

def hello():
    print("Hello World")

def add():
    print("1+1=", 1+1)

COMMANDS = {"ping": ping, "hello": hello, "add":add}

def main():
    # If the amount of args is less than 2 or the second arg isn't in the commands array, display our commands & exit
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"usage: aa {{{'|'.join(COMMANDS)}}}", file=sys.stderr)
        sys.exit(1)
    COMMANDS[sys.argv[1]]()