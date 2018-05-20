#!/usr/bin/python

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
' ':'\n',
'?':':question:',
'!':':exclamation:',
'.':':small_blue_diamond:'
}

class Emojiador:

	def textToEmoji(texto):

		string = ''.join(texto)
		emojedString = ''

		for x in range(0,len(string)):
			char = string[x]
			emojedString = emojedString + emojis.get(char,"?")
			
		return(emojedString)