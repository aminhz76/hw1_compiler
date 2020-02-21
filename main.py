
Type = {"assign":"=", "numberDouble": float() , "numberInt":int() ,"div":"/","mul":"*","add":"+","minus":"-","closeParan":")","openParan":"(","nextLine":"\n","var":""}


class Token:
    def __init__(self, type, value):
        # print(type)
        if type in Type.keys():
            self.type = type
        else:
            raise ValueError('your input is incorrect')
        self.value = value


if __name__ == "__main__":
    arr = []
    # t = Token('numberDouble', 2.2)
    # arr.append(t)
    # print(arr[0].type, arr[0].value)

    input = input("Enter a value : ")
    i = 0
    state = 0
    left = 0
    right = 0
    temp = ""
    doubleFlag = False
    while i < len(input):
        # print(i)
        # print("input : " + input[i])
        temp = ""
        if (input[i].isalpha()) or (input[i] == '_'):
            state = 0
            left = i
            right = i
        if input[i].isdigit():
            state = 1
            left = i
            right = i
        if (input[i] == '+') or (input[i] == '-') or (input[i] == '*') or (input[i] == '/'):
            state = 2
            if input[i] == '+':
                state = -1
                t = Token('add','+')
                arr.append(t)
            elif input[i] == '-':
                state = -1
                t = Token('minus','-')
                arr.append(t)
            elif input[i] == '*':
                state = -1
                t = Token('mul','*')
                arr.append(t)
            elif input[i] == '/':
                state = -1
                t = Token('div','/')
                arr.append(t)
        if input[i] == '=':
            state = -1
            t = Token('assign', '=')
            arr.append(t)
        if (input[i] == '(') or (input[i] == ')') :
            state = -1
            if input[i] == '(':
                t = Token('openParan', '(')
                arr.append(t)
            elif input[i] == ')':
                t = Token('closeParan', ')')
                arr.append(t)
        if(input[i] == '\n'):
            state = -1
            t = Token('nextLine', '\n')
            arr.append(t)
        while state == 0:
            temp = temp + input[right]
            # print("temp :" + temp)
            right += 1
            if right >= len(input):
                state = -1
                i = right
                t = Token('var', temp)
                arr.append(t)
                # print("in last char :")
                break
            # print(right)
            if (input[right].isalpha() == False):
                if input[right] != '_':
                    if (input[right].isdigit() == False) :
                        state = -1
                        i = right - 1
                        t = Token('var', temp)
                        arr.append(t)
        while state == 1 :
            temp = temp+input[right]
            right+=1
            if right >= len(input):
                if(doubleFlag == False):
                    # print("if one :")
                    doubleFlag = False
                    state = -1
                    i = right
                    t = Token('numberInt', temp)
                    arr.append(t)
                    break
                elif (doubleFlag == True):
                    # print("if two :")
                    doubleFlag = False
                    state = -1
                    i = right
                    t = Token('numberDouble', temp)
                    arr.append(t)
                    break
            if (input[right].isdigit() == False):
                if (input[right] == '.'):
                    if (doubleFlag == False) :
                        doubleFlag = True
                    elif (doubleFlag == True):
                        print("Error on : "+temp)
                        i = len(input)
                        break
                elif input[right] != ' ':
                    print("Error on : " + temp+input[right])
                    i = len(input)
                    break
                elif(doubleFlag == True ):
                    state = -1
                    i = right - 1
                    t = Token('numberDouble', temp)
                    arr.append(t)
                elif(doubleFlag == False):
                    state = -1
                    i = right - 1
                    t = Token('numberInt', temp)
                    arr.append(t)
        i += 1

    i = 0
    for i in range(len(arr)):
        print(arr[i].type, arr[i].value)
