def nonDups (values): 
    returnValues = []
    doups = False
    outter = 0
    inner = 0
    for outter in range(len(values)):
        doups = False
        for inner in range(len(values)): 
            if (inner != outter):
                if (values[outter] == values[inner]):
                    doups = True
        if (doups != True):
            returnValues.append(values[outter])
    return returnValues

def nonDupLetters (inputString):
    returnString = []
    dups = False
    for outter in range(len(inputString)):
        dups = False
        for inner in range(len(inputString)):
            if (outter != inner):
                if (inputString[outter] == inputString[inner]):
                    dups = True
        if (dups != True):
            returnString.append(inputString[outter])
    return returnString

def totalASCIIValueOfString(inputString):
    total = 0
    for index in range(len(inputString)):
        total = total + ord(inputString[index])
    return total

def isPalindrome(inputString):
    reverseString = ''
    index = len(inputString) - 1
    while (index > -1):
        reverseString = reverseString + inputString[index]
        index = index - 1
    if (reverseString == inputString):
        return True
    else:
        return False

def main():
    testValues = [1, 1, 1, 3, 7, 11, 7]
    testValues1 = [1, 3, 3, 5, 7]
    testValues2 = [-1, 0, 1]
    testValues3 = [-2, -2, -1, 0, 1, 0, -1]
    test = nonDups(testValues)
    test1 = nonDups(testValues1)
    test2 = nonDups(testValues2)
    test3 = nonDups(testValues3)
    output = ('The orginal test values were: ' + str(testValues)
    + '\nThe final output from finding the non duplicate numbers are: ')
    for index in range(len(test)):
        output = output +(str(test[index]) + ' ')
    print(output)
    output = ('The orginal test values were: ' + str(testValues1)
    + '\nThe final output from finding the non duplicate numbers are: ')
    for index in range(len(test1)):
        output = output + (str(test1[index]) + ' ')
    print(output)
    output = ('The orginal test values were: ' + str(testValues2)
    + '\nThe final output from finding the non duplicate numbers are: ')
    for index in range(len(test2)):
        output = output + (str(test2[index]) + ' ')
    print(output)
    output = ('The orginal test values were: ' + str(testValues3)
    + '\nThe final output from finding the non duplicate numbers are: ')
    for index in range(len(test3)):
        output = output + (str(test3[index]) + ' ')
    print(output)
    testString = 'Hello World'
    testString1 = 'mom'
    testString2 = 'redivider'
    test4 = nonDupLetters(testString)
    test5 = totalASCIIValueOfString(testString)
    test6 = isPalindrome(testString)
    test7 = isPalindrome(testString1)
    test8 = isPalindrome(testString2)
    output = ('The orginal test values were: ' + testString
    + '\nThe final output from finding the non duplicate numbers are: ')
    for index in range(len(test4)):
        output = output + (str(test4[index]) + ' ')
    print(output)
    output = ('The orginal test values were: ' + testString
    + '\nThe final output from finding the ASCII value total is: ')
    output = output + str(test5)
    print(output)
    output = ('Is ' + testString + ' a palindrome? ' + str(test6))
    print(output)
    output = ('Is ' + testString1 + ' a palindrome? ' + str(test7))
    print(output)
    output = ('Is ' + testString2 + ' a palindrome? ' + str(test8))
    print(output)
    print('Press the enter key to exit!!!')
    input()
    
main()
