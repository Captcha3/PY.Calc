#imported devices
import sys
import math
import os
import time
from statistics import mean

#Introduction
print('Welcome to PY.Calc')
print('I did not use my own code as a base. Please refer to\nhttps://www.programiz.com/python-programming/examples/calculator\nfor original code\n')
print("Type 'HELP' for a list of commands available")
print("Type 'QUIT' to exit\n")

#Operations
def a(x, y):
        return x + y
def b(x, y):
        return x - y
def c(x, y):
        return x * y
def d(x, y):
        return x / y
def e(x):
        return x * x
def f(x):
        return 2 * pi * x
def g(x, y):
        return x + x + y + y
def h(x):
        return pi * (x * x)


#Clear Screen Script
def clr():
        if sys.platform == 'win32':
                UsrWinVer = str(sys.getwindowsversion().major)
                os.system('cls')
        else:
                os.system('clear')

#Important variables
pi = 3.14159265359
ops = 000

#Calculator Body
while (ops < 999):
        quit = 000
        ltr = input()
        
        if ltr in {'null'}:
                print(math.inf)

        #addition = a
        elif ltr in {'a', 'A'}:
                inter = float(input('\nFirst Number: '))
                inte = float(input('\nSecond Number: '))
                print(inter,'+',inte,'=', a(inter,inte))
        
        #subtraction = b
        elif ltr in {'b', 'B'}:
                inter = float(input('\nLarge Number: '))
                inte = float(input('\nSmall Number: '))
                print(inter,'-',inte,'=', b(inter,inte))
        
        #multiplication = c
        elif ltr in {'c', 'C'}:
                inter = float(input('\nFirst Number: '))
                inte = float(input('\nSecond Number: '))
                print(inter,'*',inte,'=', c(inter,inte))
        
        #division = d
        elif ltr in {'d', 'D'}:
                inter = float(input('\nLarge Number: '))
                inte = float(input('\nSmall Number: '))
                print(inter,'/',inte,'=', d(inter,inte))
        
        #square root = e
        elif ltr in {'e', 'E'}:
                inter = float(input('\nNumber: '))
                print(inter,'*',inter,'=', e(inter))
        
        #square root = f
        elif ltr in {'f', 'F'}:
                inter = float(input('\nNumber:'))
                print(math.sqrt(inter))
        
        #perimeter of square = g
        elif ltr in {'g', 'G'}:
                inte = float(input('Length: '))
                inter = float(input('Width: '))
                print('perimeter: ',g(inte, inter))
        
        #area of square = h
        elif ltr in {'h', 'H'}:
                inte = float(input('Length: '))
                inter = float(input('Width: '))
                print('area: ',c(inte, inter))
        
        #circumference = i
        elif ltr in {'i', 'I'}:
                inter = float(input('\nRadius: '))
                print('Circumference: ',2*(pi*inter))
        
        #area of circle = j
        elif ltr in {'j', 'J'}:
                num = float(input('Radius: '))
                print('Area: ',h(num))
                
        #Dataset = k
        elif ltr in {'k', 'K'}:
                var = float(input('Ammount of Data Variables: '))
                dset = 'Variables go here'
                dsort = 'Organization'
                if var == 1:
                        numb = float(input('Really? choose a variable, I guess\n'))
                        print('Here\'s your ONE VARIABLE data set - ',numb)

                elif var == 2:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        
                        dset = numb1, numb2
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)

                elif var == 3:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        
                        dset = numb1, numb2, numb3
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)

                elif var == 4:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        
                        dset = numb1, numb2, numb3, numb4
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                
                elif var == 5:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)

                elif var == 6:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        numb6 = float(input('Variable 6: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5, numb6
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                        
                elif var == 7:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        numb6 = float(input('Variable 6: '))
                        numb7 = float(input('Variable 7: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5, numb6, numb7
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                        
                elif var == 8:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        numb6 = float(input('Variable 6: '))
                        numb7 = float(input('Variable 7: '))
                        numb8 = float(input('Variable 8: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5, numb6, numb7, numb8
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                        
                elif var == 9:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        numb6 = float(input('Variable 6: '))
                        numb7 = float(input('Variable 7: '))
                        numb8 = float(input('Variable 8: '))
                        numb9 = float(input('Variable 9: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5, numb6, numb7, numb8, numb9
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                
                elif var == 10:
                        numb1 = float(input('Variable 1: '))
                        numb2 = float(input('Variable 2: '))
                        numb3 = float(input('Variable 3: '))
                        numb4 = float(input('Variable 4: '))
                        numb5 = float(input('Variable 5: '))
                        numb6 = float(input('Variable 6: '))
                        numb7 = float(input('Variable 7: '))
                        numb8 = float(input('Variable 8: '))
                        numb9 = float(input('Variable 9: '))
                        numb10 = float(input('Variable 10: '))
                        
                        dset = numb1, numb2, numb3, numb4, numb5, numb6, numb7, numb8, numb9, numb10
                        dsort = sorted(dset)
                        
                        print('Data Set: ',dsort)
                else:
                        print('Invalid Input. Data Sets can currently go up to 10 variables.\nReturning to main prompt.')

        #average = l
        elif ltr in{'l', 'L'}:
                ltr = input('Would you like to use the previous Dataset? ')
                if ltr in {'y', 'Y', 'yes', 'Yes', 'YEs', 'YES'}:
                        print('Work in Progress')
                elif ltr in {'n', 'N', 'no', 'No', 'NO'}:
                        var = input('Creating a new Dataset. How many Variables? ')
                        dset = 'example'
                        dsort = sorted(dset)
                        if var == 1:
                                numb = float(input('Really? choose a variable, I guess\n'))
                                print('Here\'s your ONE VARIABLE data set - ', numb)

                        elif var == 2:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                        
                                dttl = numb1 + numb2
                                davg = dttl / 2
                                print('Average: ',davg,'\n')
                        elif var == 3:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                        
                                dttl = numb1 + numb2 + numb3
                                davg = dttl / 3
                                print('Average: ',davg,'\n')
                        elif var == 'pi':
                                print('Really? Go back to the Prompt')
                        elif var == 4:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4
                                davg = dttl / 4
                                print('Average: ',davg,'\n')
                        elif var == 5:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5
                                davg = dttl / 5
                                print('Average: ',davg,'\n')
                        elif var == 6:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                                numb6 = float(input('Variable 6: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5 + numb6
                                davg = dttl / 6
                                print('Average: ',davg,'\n')
                        elif var == 7:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                                numb6 = float(input('Variable 6: '))
                                numb7 = float(input('Variable 7: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5 + numb6 + numb7
                                davg = dttl / 7
                                print('Average: ',davg,'\n')
                        elif var == 8:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                                numb6 = float(input('Variable 6: '))
                                numb7 = float(input('Variable 7: '))
                                numb8 = float(input('Variable 8: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5 + numb6 + numb7 + numb8
                                davg = dttl / 8
                                print('Average: ',davg,'\n')
                        elif var == 9:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                                numb6 = float(input('Variable 6: '))
                                numb7 = float(input('Variable 7: '))
                                numb8 = float(input('Variable 8: '))
                                numb9 = float(input('Variable 9: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5 + numb6 + numb7 + numb8 + numb9
                                davg = dttl / 9
                                print('Average: ',davg,'\n')
                        elif var == 10:
                                numb1 = float(input('Variable 1: '))
                                numb2 = float(input('Variable 2: '))
                                numb3 = float(input('Variable 3: '))
                                numb4 = float(input('Variable 4: '))
                                numb5 = float(input('Variable 5: '))
                                numb6 = float(input('Variable 6: '))
                                numb7 = float(input('Variable 7: '))
                                numb8 = float(input('Variable 8: '))
                                numb9 = float(input('Variable 9: '))
                                numb10 = float(input('Variable 10: '))
                        
                                dttl = numb1 + numb2 + numb3 + numb4 + numb5 + numb6 + numb7 + numb8 + numb9 + numb10
                                davg = dttl / 10
                                print('Average: ',davg,'\n')
                        else:
                                print('Invalid Input. Data Sets can currently go up to 10 variables.\nReturning to main prompt.\n')
                else:
                        print('Invalid Answer. Returning to Main Prompt.\n')
                                
                
        #all = all
        elif ltr in {'all', 'All', 'ALL'}:
                print('\nFirst number is being squared and square rooted')
                num = float(input('number: '))
                inter = float(input('Large Number: '))
                inte = float(input('Small Number: '))
                print('Addition: ',a(inter,inte))
                print('Subtraction: ',b(inter,inte))
                print('Multiplication: ',c(inter,inte))
                print('Division: ',d(inter,inte))
                print('square: ',e(num))
                print('square root: ',math.sqrt(num))
        
        #area/perimeter = ap
        elif ltr in {'ap', 'Ap', 'AP'}:
                num = float(input('Length: '))
                numb = float(input('Width: '))
                print('Perimeter: ',g(num, numb))
                print('Area: ',c(num, numb))
        
        #area/circumference = ac
        elif ltr in {'ac', 'Ac', 'AC'}:
                numb = float(input('Radius: '))
                print('Circumference: ',2*(pi*numb))
                print('Area: ',h(numb))
        
        #help
        elif ltr in {'help', 'Help', 'HELP'}:
                clr()
                print("\t-:# Single Operations #:-\n\n a. Addition\n b. Subtraction\n c. Multiplication\n d. Division\n e. Square\n f. Square Root\n g. Perimeter\n h. Area (Square)\n i. Circumference\n j. Area (Circle)\n k. Dataset\n\n\t-:# Commands doing more than one Operation #:-\n\n ap. Area and Perimeter\n ac. Area and Circumference\n\n")
                print("Type 'ALL' to perform all operations\n\tOnly performs Addition through to Square Root\n")
                print("Type 'CLEAR' to clear the Screen\n\tWorks on Terminal Interfaces only\n\nType 'QUIT' to exit\n")
                
        #Clear Screen
        elif ltr in {'clear', 'Clear', 'CLEAR', 'cls', 'clr'}:
                clr()
        
        #Easter Egg
        elif ltr == 'easteregg':
                #10 seconds
                clr()
                print('\n')
                print('\t###   ##')
                print('\t ##  #  #')
                print('\t ##  #  #')
                print('\t ##  #  #')
                print('\t ##  #  #')
                print('\t ##  #  #')
                print('\t####  ##')
                print('\n')
                
                #9 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t ##')
                print('\t#  #')
                print('\t#  #')
                print('\t ###')
                print('\t   #')
                print('\t  #')
                print('\t #')
                print('\n')
                
                #8 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t ##')
                print('\t#  #')
                print('\t#  #')
                print('\t ##')
                print('\t#  #')
                print('\t#  #')
                print('\t ##')
                print('\n')
                
                #7 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t####')
                print('\t   #')
                print('\t   #')
                print('\t  #')
                print('\t  #')
                print('\t #')
                print('\t #')
                print('\n')
                
                #6 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t   #')
                print('\t  # ')
                print('\t #  ')
                print('\t ## ')
                print('\t#  #')
                print('\t#  #')
                print('\t ## ')
                print('\n')
                
                #5 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t####')
                print('\t#   ')
                print('\t### ')
                print('\t   #')
                print('\t#  #')
                print('\t ##')
                print('\n')
                
                #4 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t  ##')
                print('\t # #')
                print('\t#  #')
                print('\t####')
                print('\t   #')
                print('\t   #')
                print('\t   #')
                print('\n')
                
                #3 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t####')
                print('\t   #')
                print('\t  # ')
                print('\t### ')
                print('\t   #')
                print('\t   #')
                print('\t### ')
                print('\n')
                
                #2 seconds
                time.sleep(1)
                clr()
                print('\n')
                print('\t ## ')
                print('\t#  #')
                print('\t   #')
                print('\t  # ')
                print('\t #  ')
                print('\t#   ')
                print('\t####')
                print('\n')
                
                #1 second
                time.sleep(1)
                clr()
                print('\n')
                print('\t### ')
                print('\t ## ')
                print('\t ## ')
                print('\t ## ')
                print('\t ## ')
                print('\t ## ')
                print('\t####')
                print('\n')
                time.sleep(1)
                clr()
                
                #Rocket Standby
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t /   \ ')
                time.sleep(.3)
                clr()
                
                #rocket launch
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t &|_|& ')
                print('\t /   \ ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t &|_|& ')
                print('\t&/   \&')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t &|@|& ')
                print('\t&&|_|&&')
                print('\t&/   \&')
                time.sleep(.2)
                clr()

                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t /   \ ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t &#*#& ')
                print('\t  &&&  ')
                print('\t   &   ')
                print('\t /   \ ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                print('\t /   \ ')
                time.sleep(.2)
                clr()
                
                #Rocket Flying
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t   #   ')
                print('\t  #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                print('\t /   \ ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\t   |   ')
                print('\t  |@|  ')
                print('\t  |_|  ')
                print('\t   #   ')
                print('\t  #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\t+  |   ')
                print('\t  |@| +')
                print('\t  |_|  ')
                print('\t   #   ')
                print('\t  #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\t + |   ')
                print('\t+ |@| +')
                print('\t  |_|+ ')
                print('\t   #   ')
                print('\t  #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\t+  |   ')
                print('\t +|@| +')
                print('\t  |_|  ')
                print('\t+  # + ')
                print('\t  #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                time.sleep(.2)
                clr()
                
                print('\n')
                print('\t+  |+  ')
                print('\t  |@|  ')
                print('\t +|_| +')
                print('\t   # + ')
                print('\t+ #*#  ')
                print('\t #***# ')
                print('\t &#*#& ')
                print('\t &&#&& ')
                print('\t  &&&  ')
                print('\t   &   ')
                time.sleep(.3)
                clr()
                
                print('\tCONGRADUATIONS')
                print('That was the Easter Egg I made.\nPlease feel free to Continue \nusing PY.Calc')
                
        #quit
        elif ltr in {'quit', 'Quit', 'QUIT'}:
        
                #Are You Sure prompt
                while(quit < 3):
                        print('\nAre you sure?')
                        yen = input()
                        if yen in {'y', 'Y', 'yes', 'Yes', 'YEs', 'YES'}:
                                sys.exit('\nUser Sufficiently Terminated PY.Calc\n')
                        elif yen == 'n':
                                quit = quit + 2
                        else:
                                print('Invalid Answer')
                                quit = quit + 1
                                
                #Message when the 'N' key is pressed or when 3 mistypes occur
                else:
                        print('\nInsufficent confirmation(s) to terminate PY.Calc.\nResuming calculations.\n')

        #Error Message with invalid Command
        else:
                print("Invalid Command. Type 'Help' for a list of commands\n")
        ops = ops + 1
else:
        while(quit < 3):
                quit = 000
                yen = input()
                print('999 Operations have been performed.\n Would you like to Quit?')
                if yen in {'y', 'Y', 'yes', 'Yes', 'YEs', 'YES'}:
                        sys.exit('User Sufficiently Terminated Py.Calc')
                elif yen in {'n', 'N', 'no', 'No', 'NO'}:
                        quit = quit + 3
                else:
                        print('Invalid Answer')
                        quit = quit + 1
        else:
                ops = 000
