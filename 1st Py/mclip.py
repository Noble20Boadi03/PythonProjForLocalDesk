#! python3
#A program that copies and paste text

text = {'online':"""Dude, are all the squad online?""",
        'sleep':"""Let me catch some sleep, will ya!"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: pyhton mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text for ' + keyphrase + ' has been copied to clipboard')
else:
    print('There is no text for ' + keyphrase)
