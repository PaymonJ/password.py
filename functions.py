def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def validateInput(userInput, switches):
    for i in range(1, len(userInput)):
        for switch in switches:
            if str(userInput[i]).lower() == str(switch).lower():
                switches[switch] = True