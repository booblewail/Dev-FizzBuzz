# FizzBuzz problem with bad coding practices
# For CompClub Dev Portfolio
#
# By Calvin Zhao z5413994
# Date - 3/3/2024

for badvariablename    in range(1, 101):            # random or extra white spaces
    if badvariablename % 5 == 0 and badvariablename % 3 == 0:
                                                    # random or extra white spaces
        print ("CompClub")

    elif badvariablename % 3 == 0:

        print   ("Comp")                            # random or extra white spaces
    elif badvariablename % 5 ==    0:
                                                    # inconsistent white spaces
        #bad commenting random spots not consistent
        print("Club")
    else:
        print(badvariablename)                      # long variable name, not snake or camel case
