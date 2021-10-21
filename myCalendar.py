import stdio
import sys
import calendar

#Dictionary to relate the month name to the month number based on chronological order
month ={1:'January', 2:'February', 3:'March', 
        4:'April', 5:'May', 6:'June', 7:'July',
        8:'August', 9:'September', 10:'October',
        11:'November', 12:'December'}

#command line arguments to set the requested year and month
y = int(sys.argv[1])
m = int(sys.argv[2])

#command line arguments used to set the heading of the calendar with month and year label
stdio.writeln(month[m] + ' ' + str(y))
#print out text for days of the week columns
stdio.writeln(' ' + 'Mo' + ' ' + 'Tu' + ' ' + 'We' + ' ' + 'Th' +' ' + 'Fr' + ' ' + 'Sa' + ' ' + 'Su')

#function from calendar module provides days of a particular month by week
x = calendar.monthcalendar(y, m)
#print out days by week
stdio.writeln(x[0])
stdio.writeln(x[1])
stdio.writeln(x[2])
stdio.writeln(x[3])
stdio.writeln(x[4])




