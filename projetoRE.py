""" 
Python script for Regular Expressions

Patterns:
-Personal ID (ddd.ddd.ddd-dd)
-Phone Number (dddd-dddd | ddddd-dddd)
-E-mail Address [ (1+ word digits or a .)@(1+ word digits except _)(.com | .org | .br) ]
-URL (www.( 1+ word digits )(.com | .org | .br) )

"""
import re

#Patterns
id_pattern = re.compile(r'^\d\d\d\.\d\d\d\.\d\d\d-\d\d')
phone_pattern = re.compile(r'^\d{4,5}-\d\d\d\d')
email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.(com|org|br)')
url_pattern = re.compile(r'^www\.[a-zA-Z0-9]+\.(com|org|br)')


#Match Function
def match_string(String, File):
    if id_pattern.fullmatch(String):
        File.write("ID Pattern Matched for: {}\n".format(String))
    elif phone_pattern.fullmatch(String):
        File.write("Phone Number Pattern Matched for: {}\n".format(String))
    elif email_pattern.fullmatch(String):
        File.write("Email Pattern Matched for: {}\n".format(String))
    elif url_pattern.fullmatch(String):
        File.write("URL Pattern Matched for: {}\n".format(String))
    else:
        File.write("No Matches for: {}\n".format(String))


#Match Test
with open("input.txt", 'r') as input_file:
    with open("output.txt", 'w') as output_file:
        while(1):
            sentence = input_file.readline()
            if sentence == '':
                break
            else:
                match_string(sentence[:len(sentence)-1], output_file)