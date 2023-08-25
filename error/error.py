import sys
def handle_error():
    print("Could not find stream audio")
    sys.exit(-1)
def handle_io_error(error):
    print(f"Could not write stream audio to file and error is {error}")
    sys.exit(-1)