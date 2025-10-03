try:
    if(undefined_variable>5):
        undefined_variable=5
except NameError as e:
    # Do whatever you want if the variable is not defined yet in the program.
    print("oofus")