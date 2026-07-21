def length_of_parenthesis(s):
    i = 0
    temp = ''

    if 0 <= len(s) <= 3 * (10 * 4):
        for ch in s:
            if ch in '()':
                if i % 2 == 0:
                    if ch == '(':
                        temp += ch
                        i += 1
                else:
                    if i % 2 != 0:
                        if ch == ')':
                            temp += ch
                            i += 1
            else:
                print("String not following constraints rules, please try again...")
    else:
        print("Check the size of string.!")
        
    return len(temp)


s = ")()()"
length_of_parenthesis(s)
