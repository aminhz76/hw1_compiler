import enum


class Type(enum.Enum):
    assign = '='
    nextLine = '\n'
    openParan = '('
    closeParan = ')'
    add = '+'
    minus = '-'
    mul = '*'
    div = '/'
    numberInt = int()
    numberDouble = float()
    var = ""


class Token:
    def __init__(self, type, value):
        self.type = Type[str(type)].name
        self.value = value


if __name__ == "__main__":
    arr = []
    # t = Token('var', "amin")
    # arr.append(t)
    # print(arr[0].type, arr[0].value)

    input = input("Enter a value : ")
    i = 0
    state = 0
    left = 0
    right = 0
    temp = ""
    while (i < len(input)):
        # print(i)
        # print("input : " + input[i])
        temp = ""
        if (input[i].isalpha()) or (input[i] == '_'):
            # print("state")
            # print(state)
            state = 0
            left = i
            right = i
        while state == 0:
            temp = temp + input[right]
            # print("temp :" + temp)
            right += 1
            if (right >= len(input)):
                state = -1
                i = right
                t = Token('var', temp)
                arr.append(t)
                # print("in last char :")
                break
            print(right)
            if (input[right].isalpha() == False):
                if input[right] != '_':
                    if (input[right].isdigit() == False) :
                        state = -1
                        i = right - 1
                        t = Token('var', temp)
                        arr.append(t)
        i += 1

    i = 0
    for i in range(len(arr)):
        print(arr[i].type, arr[i].value)
    # print(arr[0].type,arr[0].value)
