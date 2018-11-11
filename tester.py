
### This is a example that shows a simpler way to use re. to split chemical compound string
### Lots of comments to undertand -- not many actual lines of code !!

import re

def testmatcher(compoundstring):

    ## match one uppercase, optional lowecase, optional digits
    ## letters captured in first group, numbers captured in second
    matcher = '([A-Z][a-z]?)([0-9]*)'   ## IMPORTANT, described in email

    print("\n\n>>>>>> Testing on: " + compoundstring)
    ## create a list of parts tuples
    parts = re.findall(matcher, compoundstring)    ### important line
    print("Here is list of split parts: " + str(parts))

    print("\nNow lets look at each one")

    checkcompound = ''

    for part in parts:
        print("Looping for part: " + str(part))

        if part[1]:
            print("Part has a number: " + part[1])
        else:
            print("Part has no number -- must use 1 default")

        ## this is a sanity check, see explanation below
        checkcompound = checkcompound + part[0] + part[1]
        print("Putting together parts as error check: " + checkcompound + "\n")

        ## Here is where you calculate totalweight
        ## -- 1st use symbol to grab element object from dictionary
        ## -- 2nd use getWeight() method on object to get weight
        ## -- 3rd multiply weight by number and add to total


    ### AFTER LOOP
    ## This version of the re. function use  is easier, because it
    ## grabs all of the parts at once.  But, it also just skips any crap
    ## in the middle, and you might give an answer for a incorrect compound.
    ## To check for it, in the loop you reconstruct the compound from it's part.
    ## And here, you simply check if original compound was completely re-built.
    ## IF so, you are good.
    ## If not, you can print an error.

    if (compoundstring == checkcompound):
        print("Ok, you've looped thru all parts, and whole formula was valid")
        print("You can return the weight or print it out")
    else:
        print("User entered invalid compound.")
        print("Original not same as reconstructed parts")
        print("Original: " + compoundstring + " Check: " + checkcompound)
        print("You might decide to print an error message instead of weight")

#### END of testmatcher() function



testmatcher("H2SFe2Ag")

print("\nTRY A BAD FORMULA -- the q is wrong")
testmatcher("H2S3qFe2Ag")  ## try to handle bad forumla -- 'q' is out of place

