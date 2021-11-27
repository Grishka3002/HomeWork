#18.Напишите программу на Python для выполнения строки, содержащей код Python.  
import sys
import io

codeOut = io.StringIO()
codeErr = io.StringIO()

code = "print 'This is my output.'"

sys.stdout = codeOut
sys.stderr = codeErr

exec(code)

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

print (f(4))

s = codeErr.getvalue()

print ("error:\n%s\n" % s)

s = codeOut.getvalue()

print ("output:\n%s" % s)

codeOut.close()
codeErr.close()