def isPalindrome():
    str = input('Please enter the string to be checked \r\n')
    result = str == str[::-1]
    if result:
        print(f'string {str} is Palindrome')
    else:
       print(f'string {str} is not Palindrome') 

isPalindrome()