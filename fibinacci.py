class fibinacci:
    def __init__(self):
  pass
    def series(self):
	self.number=int(raw_input("enter number of terms to print:"))
	print 0,
	ele=0
	printers=1
	fib=1
	while printers<self.number:
	    print fib,
	    temp=fib
	    fib=fib+ele
	    ele=temp
	    printers+=1
a=fibinacci()
a.series()
	    
	    
	    
		
