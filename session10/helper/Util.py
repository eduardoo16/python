class Util:

    @staticmethod
    def myLenght(it):
        try:
            return sum (1 for i in it)
        except:
            return -1

print (Util.myLenght({1:1, 2:2, 3:3}))
print (Util.myLenght("123eadsd"))
print (Util.myLenght([1,3,4,5,8,4,651,32,"s"]))
print (Util.myLenght(123))