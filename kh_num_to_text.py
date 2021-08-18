KHMER_DIGIT_WORD = [
  "",
  "មួយ",
  "ពីរ",
  "បី",
  "បួន",
  "ប្រាំ",
  "ប្រាំមួយ",
  "ប្រាំពីរ",
  "ប្រាំបី",
  "ប្រាំបួន",
]

KHMER_TENTH = [
  "",
  "ដប់",
  "ម្ភៃ",
  "សាមសិប",
  "សែសិប",
  "ហាសិប",
  "ហុកសិប",
  "ចិតសិប",
  "ប៉ែតសិប",
  "កៅសិប",
]

def int2Word(num, space):
  if num == 0:
    return "សូន្យ"
  else:
    return int2Khmer(num, space)
  

def int2Khmer(num , space):
    if num >= 1000000:
        return "{}លាន{}{}".format( int2Khmer(int(num / 1000000), space), space, int2Khmer(num % 1000000, space))
    elif num >= 100000:
        return "{}សែន{}{}".format(int2Khmer(int(num / 100000), space), space, int2Khmer(num % 100000, space))
    elif num >= 10000:
        return "{}ម៉ឺន{}{}".format( int2Khmer(int(num / 10000), space), space, int2Khmer(num % 10000, space))
    elif num >= 1000:
        return "{}ពាន់{}{}".format( int2Khmer(int(num / 1000), space), space,  int2Khmer(num % 1000, space))
    elif num >= 100 :
        return "{}រយ{}{}".format( int2Khmer(int(num / 100), space), space,  int2Khmer(num % 100, space))
    elif num >= 10 :
        return "{}{}{}".format( KHMER_TENTH[int(num / 10)], space, KHMER_DIGIT_WORD[num % 10])
    elif num > 0 :
        return KHMER_DIGIT_WORD[num]
  

    return ""

def khmer2RomanNum(roman):
    khNum = ""
    khNum = roman.replace( "០", "0")
    khNum = khNum.replace( "១", "1")
    khNum = khNum.replace( "២", "2")
    khNum = khNum.replace( "៣", "3")
    khNum = khNum.replace( "៤", "4")
    khNum = khNum.replace( "៥", "5")
    khNum = khNum.replace( "៦", "6")
    khNum = khNum.replace( "៧", "7")
    khNum = khNum.replace( "៨", "8")
    khNum = khNum.replace( "៩", "9")
    khNum = khNum.replace( ",", "")
    khNum = khNum.replace( ".", ".")
    return khNum


def Num2Word(num, space):
    #num = str(num)
    nums = khmer2RomanNum(num).split( ".")
    digit =int(nums[0])
    if len(nums) == 1:
        return int2Word(digit, space)
  
    precision  = int(nums[1])
    lead_zero = ""
    for  value in nums[1]:
        if value == "0":
            lead_zero += space
            lead_zero += "សូន្យ"
        else:
            break
        
    return "{}{}ចុច{}{}{}".format( int2Word(digit, space), space, lead_zero, space, int2Khmer(precision, space))


