#!/usr/bin/python

import sys

emojis = {
'a':':a:',
'b':':b:',
'c':':copyright:',
'd':':leftwards_arrow_with_hook:',
'e':':e-mail:',
'f':':flags:',
'g':':six:',
'h':':pisces:',
'i':':information_source:',
'j':':saxophone:',
'k':':ski:',
'l':':high_heel:',
'm':':m:',
'n':':capricorn:',
'o':':o2:',
'p':':parking:',
'q':':leo:',
'r':':registered:',
's':':heavy_dollar_sign:',
't':':hammer:',
'u':':ophiuchus:',
'v':':aries:',
'w':':trident:',
'x':':x:',
'y':':v:',
'z':':zzz:',
' ':' \n',
'?':':question:',
'!':':exclamation:'
}

def main():

	string = ''.join(sys.argv[1:])
	emojedString = ''

	for x in range(0,len(string)):
		char = string[x]
		emojedString = emojedString + emojis[char]
		
	print(emojedString)


if __name__ == "__main__":
	main()