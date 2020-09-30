import time
import sys

indentIncrease = True
indentValue = 0

try:
    while True:
        print(' '*indentValue, end = '')
        print('********')
        time.sleep(0.1)

        if indentIncrease:
            indentValue = indentValue + 1
            if (indentValue == 40):
                indentIncrease = False
        else:
            indentValue = indentValue - 1
            if (indentValue == 0):
                indentIncrease = True

except KeyboardInterrupt:
    sys.exit()