#! python3
# myclip.py - A multi-clipboard program

Text = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}
import sys, pyperclip

if (len(sys.argv)!=2):
    print("Please enter exactly 2 command line arguments")
    input()

keyphrase = sys.argv[1]

if (Text[keyphrase]):
    pyperclip.copy(Text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
    input()
else:
    print('There is no text for ' + keyphrase)
    input()