# Partner 1: Stephanie
# Partner 2: Daniel
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''

if "A".casefold in grade:
    print("Great work!")
elif "B".casefold in grade:
    print("Good work!)
elif "C".casefold in grade:
    print("Mediocre work!")
elif "D".casefold in grade:
    print("Terrible work!")
elif "F".casefold in grade:
    print("You should really reconsider getting a private education.")
else:
    print("There were no valid letters in your input.")

''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
if yards < 17:
   yards = yards*2


''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if success == TRUE:
   print("congratulations")


''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[1] == "f":
   print("fun")
else:
   print("not fun")

''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''

if celsius == TRUE:
    fahrenheit = 1.8*celsius + 32


''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if numItems > 0:
   averageCost = averageCost/numItems
   print(averageCost)
else:
   print("No items")


''' 7.
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''

if pollution < cutoff:
    print("safe condition!")
else:
    print("unsafe condition!")

''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
if 90<score<100:
   grade = 'A'
elif score < 90:
   grade = 'B'
elif score < 80:
   grade = 'C'
elif score < 70:
   grade = 'D'
elif score < 60:
   grade = 'F'

''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''

if isdgiit(char) == 1:
    pirnt("digit")
elfi isalpha(char) == 1:
    if islower(char) = =1:
        print("lowercase")
    else:
        print("uppercase")
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''

if neighbors < 50:
   live = 'city'
elif neighbors < 25:
   live = 'suburbia'
elif neighbors < 1:
   live = 'suburbia'
elif neighbors == 0:
   live = 'middle of nowhere'


''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''

if doesSignificantWrk AND makesBreakthrough:
    nobelPrizeCandidate = TRUE

''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''

if tax:
    price = price * taxRate
    

''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''

''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''

rem = currentNumber % 2
if rem == 0:
    currentNumber = currentNumber // 2
else:
    currentNumber = currentNumber * 3
    currentNumber += 1

''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''

four = year % 4
hundred = year % 100
big = year % 400
if four == 0:
    if hundred == 0:
        if big == 0:
            leapYear = True
    else:
        leapYear = True

''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''

num = min([a,b,c])

''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''

even = number % 2
mult = number % 5
rang = range(-100,101)
if even == 0 and mult == 0 and number in rang:
    special = True
else:
    special = False

''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''

vowels = ["a","e","i","o","u"]
if letter in vowels:
    code = 1
elif "y" in letter:
    code = -1
else:
    code = 0

''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''

weekend = ["Saturday","Sunday"]
if dayOfWeek in weekend:
    isWeekend = True
else:
    isWeekend = False

''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''

year = {
    "January": 31,
    "February", 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
numDays = year[month]

''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''

angles = angle1 + angle2 + angle3
if angles = 180:
    validTriangle = True
else:
    validTriangle = False

''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''

wh = electricity
if wh <= 50:
    pay = wh*.5
elif wh <= 150:
    pay = wh*.75
elif wh <= 250:
    pay = wh*1.2
else:
    pay = wh*1.5*1.2
payment = pay

''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''



''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''

num = str(number)
phrase = num + " " + noun
if number != 1:
    phrase += "s"

''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''

if "bacon" in userInput:
    print("Why did you type bacon?")
else:
    print("I like bacon.")

''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''

''' Task 1:

'''

# solution



''' Task 2:

'''

# solution



''' Task 3:

'''

# solution



''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''
