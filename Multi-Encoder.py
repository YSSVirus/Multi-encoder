#!/usr/bin/python3

#Here we import all of our needed libraries
import os #So we can get the file path for a more helpfule help menu
from sys import stdout, argv
"""
stdout: We import this so we can print to standard output, this causes less issues when text doesnt want to display
argv: We import this so we can can take arguments from the user
""" 
from pathlib import Path # We import this so we can find the file path
import argparse # This is a super helpful argument parser, it helps simplify arguments and a  help menu along with a few other things.
import urllib.parse # This is what we use for encoding key characters
import base64 # importing package to base64 encode


def aggressive_url_encode(string): # Here we pass our string variable to our url encode function
    url_encoded = "".join("%{0:02x}".format(ord(char)) for char in string)
    """
    1. The ord function returns the Unicode code from a given character.
    2. Next we use the format function
    4. Next we use the join function with the hex declaration to join all or now hex text
    5. Next we look at the for loop, this tells us that it swaps out char with every character in the users string until it encodes everything
    6. The blank quotes in front make this combine with nothing seperating.
    Final: This command takes the users input, and seperates each letter, then encodes to unicode, then encodes it in hex, then we join all our now hex encoded characters with no seperator"""
    if args.QUIET == quiet:
    	stdout.write(url_encoded + '\n' )
    elif test == none:
    	stdout.write('The input ' + string + ' has been changed to' + '\n' + url_encoded + '\n \n') # This prints the encoded output in a nicee neat readable format 	
    else:
    	print('There was an error with URL encoding all characters1')
    return

def url_plus_encode(line):
	url_encoded = urllib.parse.quote_plus(line) # Here we use urllib.parse to use "url quote plus" encoding
	
	if args.QUIET == quiet:
		stdout.write(url_encoded + '\n' )
	elif test == none:
		stdout.write('The input ' + line + ' has been changed to' + '\n' + url_encoded + '\n \n') # This prints the encoded output in a nicee neat readable format
	else:
		print('There was an error with key character (quote_plus) encoding')
	return#This is where we url encode key characters

def base64_encode(line):
	byte_message = bytes(line, 'utf-8') # here we convert to bytes to make it encodable
	encoded = base64.b64encode(byte_message)# this is encoding the message in base 64
	encoded = encoded.decode("utf-8")#this is decoding the bytes back to utf8 giving us a clean base64 string
	if args.QUIET == quiet:
		stdout.write(encoded + '\n')# This prints the encoded output in a nicee neat readable format
	elif test == none:
		stdout.write('The input ' + line + ' was base64 encoded and now ' + '\n' + encoded + '\n \n')# This prints the encoded output in a nicee neat readable format
	else:
		print('There was an error with the base64 encoding')
	return#Here we encode in base64

def encode_all(line):
	url_plus_encode(line) # calling url encoding of key characters from our other function
	aggressive_url_encode(line)# calling url encoding of all characters from our other function
	base64_encode(line)# calling base64 encoding of all characters from our other function
	return#Here we simply call all functions that encode

def encoding_func():
	with open (file) as f: # open the text file lets call it f
		for line in f: #call file line by line if were using the line lets call it line
			if args.all_characters == ac: # this will be set to True if the user has the -ac argument. This is due to the action we set
				aggressive_url_encode(line)#calling our function to url encode all characters

			elif args.key_characters == kc:# this will be set to False if the user has the -ac argument. This is due to the action we set
				url_plus_encode(line)#calling our function to url encode all characters

			elif args.base_64 == base_64: # This is where we test if they actually used the base 64 option
				base64_encode(line)#calling our function to url encode all characters

			elif args.all_encoding == all_encoding:
				encode_all(line)#calling our function to url encode all characters

			else: # area of -kc -ac arguments erroring out
				print("There was an error with an encoding argument.Check the help instructions with python3 " + multi_encoder_path + " --help")
				# This is an error for for one of the encoding arguments
				exit()

def main():
	if file.exists(): # if then statement if it exists or if it does not
				encoding_func()
	else: # area of if then statement erroring out
		line = args.payload
		if args.all_characters == ac: # this will be set to True if the user has the -ac argument. This is due to the action we set
			aggressive_url_encode(line)#calling our function to url encode all characters

		elif args.key_characters == kc:# this will be set to False if the user has the -ac argument. This is due to the action we set
			url_plus_encode(line)#calling our function to url encode all characters

		elif args.base_64 == base_64: # This is where we test if they actually used the base 64 option
			base64_encode(line)#calling our function to url encode all characters

		elif args.all_encoding == all_encoding:
			encode_all(line)#calling our function to url encode all characters

		else: # area of -kc -ac arguments erroring out
			print("There was an error with an encoding argument.Check the help instructions with python3 " + multi_encoder_path + " --help")
			# This is an error for for one of the encoding arguments
			exit()

script = os.path.realpath(__file__)#Here we get this filenames full path
multi_encoder_path = str(script)#Now we convert this to strings so we can use it how ever we like, if nnot it has it in an odd format that doesnt concatinate well.

help_1 = 'To encode using all methods use: python3 '
help_2 = ' -all -L list.txt\nOr for more help\nPython3 '
#With these commands were setting up the helpmenu so we can make  it a single variable so argparse wont be confused
usage_message = help_1 + multi_encoder_path + help_2 + multi_encoder_path + ' --help'
#here we fully create the help by add the path for the script

parser = argparse.ArgumentParser(usage=usage_message, description='This script is made for url encoding either key characters or all characters.')
#here we crate the parser argument, we add in usage and description so users have a better understanding of the script
encoding_parser = argparse.ArgumentParser() # This is a small seperation this is our encoding parser, this is seperated as i had to make seperate rules
encoding = parser.add_mutually_exclusive_group(required=True) #This makes one of the the options mandetory
user_list = parser.add_mutually_exclusive_group(required=True)# this allows us to expand the argument without making it look ugly later on


user_list.add_argument('-L', default='unencoded.txt',dest='FILE' , help='This is for defining the list of strings to encode') 
# This is the argument that holds the text to convert file its required as we need text to convert dont we? This is the simple version showed to the user
user_list.add_argument('-l','--l','--L', dest='FILE', help=argparse.SUPPRESS)#this is extras that are included incase they mistype

user_list.add_argument('-P', dest='payload' , help='This is for defining the string to encode') 
# This is the argument that holds the text to convert file its required as we need text to convert dont we? This is the simple version showed to the user
user_list.add_argument('-p','--p','--P', dest='payload', help=argparse.SUPPRESS)#this is extras that are included incase they mistype

parser.add_argument('-q', const='quiet', nargs='?', dest='QUIET', help='This makes the output quiet exept for the encoding output, This is eespecially nice for piping the output into a file or have a massive input list')
parser.add_argument('-Q','--Q','--q', const='quiet', dest='QUIET', nargs='?', help=argparse.SUPPRESS)

encoding.add_argument('-kc', nargs='?', const='key_characters', dest='key_characters', help='Use any of these to url encoding only KEY characters.')
#This is the argument that encodes key characters, I set it to store_false so we can make this decision between the two an easy boolean (true/false) question
encoding.add_argument('-KC','-kC','-Kc','--kc','--KC','--kC','--Kc', nargs='?', const='key_characters', dest='key_characters', help=argparse.SUPPRESS)#this is extras that are included incase they mistype

encoding.add_argument('-ac', nargs='?', dest='all_characters',const='all_characters', help='Use any of these to url encoding ALL characters')
encoding.add_argument('-AC','-aC','-Ac','--ac','--AC','--aC','--Ac', nargs='?', dest='all_characters', const='all_characters', help=argparse.SUPPRESS)#this is extras that are included incase they mistype

#This is the argument that encodes all characters, I set it to store_true so we can make this decision between the two an easy boolean (true/false) question
encoding.add_argument('-base64', nargs='?', dest='base_64', const='base_64', help='Use this to base 64 encode each line of a file') # Here we detect if they want base 64 encoding
encoding.add_argument('-BASE64','--BASE64','--base64','-Base64', dest='base_64', nargs='?', const='base_64', help=argparse.SUPPRESS)#this is extras that are included incase they mistype

encoding.add_argument('-all', nargs='?', const='all_encoding', dest='all_encoding', help='Use this to encode each line in all types we can')#Adding the all encoding method
encoding.add_argument('-All','-ALL','-ALl','-alL','--All','--ALL','--ALl','--AlL','--all', dest='all_encoding', nargs='?', const='all_encoding', help=argparse.SUPPRESS)#this is extras that are included incase they mistype


encoding_args = encoding_parser.parse_args([]) #Here we made it a simple call to a variable to parse arguments

kc = 'key_characters' # place holder for if than gets called only with -kc argument
ac = 'all_characters'# place holder for if than gets called only with -ac argument
base_64 = 'base_64'# place holder for if than gets called only with -base64 argument
quiet = 'quiet'
all_encoding = 'all_encoding'# place holder for if than gets called only with -all argument
none = 'None'
args = parser.parse_args() #Here we made it a simple call to a variable to parse arguments
test = str(args.QUIET)
file = Path(args.FILE) #get the path from the file args.l is how we call the -l argument

main()
