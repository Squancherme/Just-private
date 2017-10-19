#计算符号，空格，英文，其他
def fcuntion(string):
      letters = 0
      space = 0
      others = 0
      digit = 0
      for each in string:
            if each.isalpha():
                  letters += 1
            elif each.isdigit():
                  digit += 1
            elif each == ' ':
                  space += 1
            else :
                  others += 1
      print('%d %d %d %d' % (letters,digit,space,others))
fcuntion('12345,.drt   ')  
                  
