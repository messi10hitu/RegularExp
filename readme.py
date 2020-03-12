import re

# 4 functions of RegEx
"""
Function	          Description
findall	>>>        Returns a list containing all matches
search	>>>        Returns a Match object if there is a match anywhere in the string
split	>>>        Returns a list where the string has been split at each match
sub	    >>>        Replaces one or many matches with a string
"""
# character and their descriptions
"""
Character	                Description	
[]	                  A set of characters	"[a-m]"	
\'\'	              Signals a special sequence (can also be used to escape special characters)	"\d"	
.	                  Any character (except newline character)	"he..o"	
^	                  Starts with	"^hello"	
$	                  Ends with	"world$"	
*	                  Zero or more occurrences	"aix*"	
+	                  One or more occurrences	"aix+"	
{}	                  Exactly the specified number of occurrences	"al{2}"	
|	                  Either or	"falls|stays"	
()	                  Capture and group
"""
# findall()
txt = "the rain in spain"
x = re.findall("ai", txt)  # here ai comes 2 time
print(x)

txt = "the rain in spain"
x = re.findall("[a-m]", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)  # if no matches found it will return the empty list
print(x)

# search()
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)  # if no matches found it will return none in search
print(x)
