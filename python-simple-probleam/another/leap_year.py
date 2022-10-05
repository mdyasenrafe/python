def leapYear(number):
    if(type(number) == int) :
            if (number % 4 ==0) : 
                print( "this is year is leap Year")
            else:
               print( "this is year is not leap year")
    else:
      print("please enter a number")
leapYear(2001)
