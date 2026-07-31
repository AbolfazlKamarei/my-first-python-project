# function
import math
print("i am student")
a = 1
b = 2
c = a + b
print(c)
name = 'Abolfazl'
print(name)

#  5 variables
# int adad sahih, float adad ashari
# bool dorost & nadorost, str matn, complex formol neveshtan
count = 10
print(count)
count = count + 1
print(count)
score = 9.5
finished = True  # True & False
full_name = "Abolfazl Kamarei"
formolla = 1 + 2j  # complex

# function noa variable ro neshon mide
print(type(count))
print(type(score))

# namgozari variables # _name ok vali avalesh adad nemishe gozasht
# 1name qalate & _name11 dorost
# dakhel variables az esm ba mosama estefade konid
# font kochak benenvis)))
class_name = "Abolfazl"  # classname qalat & c1 qalat
print(class_name)
# variable str
full_name1 = 'abolfazl\' kamarei'
print(full_name1)
full_name2 = "abolfazl \\\"kamarei"
print(full_name2)

# back slash \ agar mikhay dar 2 satr neveshte shavad \n
# rahe dige 3 double cotenshen """"""

full_name3 = 'abolfazl \n kamarei'
print(full_name3)

full_name4 = """
i am
smart
and
careful
love3>

"""
print(full_name4)
full_name5 = '''
a
b
c
d
'''
print(full_name5)

# tol function str ba len & hame chi hesabe space ham hesabe baraye len
full_name6 = 'abolfazl kamarei'
print(len(full_name6))
# squar braket [] . adad midi mogheiat ro ba horof mide
print(full_name6[0])
print(full_name6[1])
# 0 ham 1 hesab mishe alan 16 tabod ba 0 mishe 16 (full_name6)
# [1] az chap be rast . [-1] az rast be chap
print(full_name6[-1])
# baze bedi [0:6] & -1 mishe enteha
print(full_name6[0:6])
print(full_name6[9:-1])
# balayi kalame akhar ro nandan
# baraye on bayad [9:]
print(full_name6[9:])
print(full_name6[:])
print(full_name6[:13])


# vasl kardan variabels
_name1 = "abolfazl"
_name2 = "kamarei"
_full_name = _name1 + " " + _name2
print(_full_name)

# Formating string . ravesh digar vasl kardan ba beraket {}

full_name111 = f"{_name1} some text {_name2} {2+2} 2+2"
print(full_name111)


# metod ba noghte .

namme = "aBolfAzl"
print(namme.upper())  # horof bozorg ba upper kolan

print(namme.lower())  # horof kochak kolan

print(namme.title())  # title harf aval ro bozorg mikone faghat o faghat


# baraye inke white space     ra pak konim bayad
man = "  abolfazl kamarei   "  # strip fazaye aval va akhar ro pak mikone
print(man.strip())
print(man.rstrip())  # fazaye rast ra pak mikone
print(man.lstrip())  # fazaye chap ro pak mikone

# day 2
# baraye inke bedonim in harf dakhel f hast bayad :
print(man.find('abolfazl'))  # javab 2 mishe . mogheiat mide agar bashe kalame
# -1 agar khoroji dad yani nist da f & function

# ba in () javab bool(True or False) mide yani :
print('abolfazl' in man)  # aya d dar str hast?
print('d' in man)  # aya d dar str hast?
print('d' not in man)  # aya d dar str nist?

# nokte akhar variable & method . agar str jaygozari mihay anjam bedi
ma = "abolafzl kamarei"
print(ma.replace("abolafzl", "ali"))  # ali ro jaygozin abolfazl kard

# adad # + - * /
a1 = 1
b1 = 2
print(3/2)
print(3//2)  # ghesmat sahih adad ro mide
print(2**3)  # tavan resani
print(round(3.14))  # rond mikone ada ro
print(round(3.55))  # rond be bala javab in 4 mishe
print(abs(-1.56))

# baraye riyazi bayad ba import math
print(math.pi)
print(math.sin(45))


# "1" ba 1 fargh dare str & int
f1 = "11"
f2 = 100
print(int(f1) + f2)

f3 = "class "
f4 = 201
print(f3 + str(f4))

# ashari
print(float(f4))
# baray bool hame ja True ama baraye False moghae( 0   ""   None  ) be ghetr az inha hamash True
print(bool(f4))
# tamam chizi ke lazem bod baraye variables yad gereftim ta injaaaaaaaa@@@@

print("endlesson11")

# Operator
