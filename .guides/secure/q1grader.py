import os, random, re, io, subprocess, shutil, sys
from subprocess import Popen, PIPE, STDOUT

sys.path.append('/usr/share/codio/assessments')
from lib.grade import send_partial_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT

score = 0
feedback = ""

## check function of code using output - keyboard flag to indicate input type
def check_output(file, arguments, expected_output, keyboard=False):

  expected_output = expected_output.rstrip('\x00')
  
  if keyboard:
    #https://stackoverflow.com/questions/33976094/subprocess-stdin-input
    p = Popen(['python3', file], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    student_output = p.communicate(input=str.encode(arguments))[0]
  else:
    student_output = subprocess.check_output(['python3', file]).rstrip()
  #check generated output - we'll just look for the number and not worry about accompanying string
  if expected_output in student_output.decode("utf-8").strip():
    return True
  else:
    return False

  
## Run the test cases

# visible test case

result = check_output('simple_interest.py',"1000\n5.3\n1\n", "$1053.00",True)
feedback+="<h2>Test case 1: Visible\n</h2>"
feedback+="Input values: principal=1000, interest_rate=5.3, time_period=1\n"
if result == True:
  score +=5 # functionality matched
  feedback+="✅ Your output matched expected output.\n"
else:
  feedback+="❌ Your output does not match the expected output.\n"
  # on failure this returns the value of the test cases and the expected output
  feedback+="The expected <strong>Ending_balance</strong> was $1053.00\n"
  
# hidden test case

result = check_output('simple_interest.py',"5000\n4.9\n3\n", "$5735.00",True)
feedback+="<hr>\n<h2>Test case 2: Hidden\n</h2>"
if result == True:
  score +=5 # functionality matched
  feedback+="✅ Your output matched expected output.\n"
else:
  feedback+="❌ Your output does not match the expected output.\n"

  
# read student code
with open('simple_interest.py') as response:
  answer = response.read()
    
# check that they used an f string
# Looking to match something like this: print(f"Ending Balance: ${(simple_interest + principal):.2f}")
feedback+="<hr>\n<h2>Test case 3: Checking to make sure you are using an f-string\n</h2>"
if re.search('print\( *f[\"\']',answer) and re.search('\:\.2f', answer):
  feedback+="✅ You have used an f string to format your output"
  score +=5 # they used and f-string
else:
  feedback+="❌ Your code must use an f string to output the ending balance"


feedback+= "<h2>On this question you earned " + str(score) + " out of 15</h2>\n"
possible = 15
percent = (score/possible)*100
res = send_partial_v2(percent, feedback, FORMAT_V2_HTML)
exit(0 if res else 1)