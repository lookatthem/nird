def func6(arg39, arg40):
    var45 = func7(arg39, arg40)
    if arg40 < arg39:
        var50 = class8()
    else:
        var50 = class10()
    for var51 in range(7):
        var50.func9(var51, var45)
    var52 = (((472 - (var45 ^ ((1738609990 | ((arg39 & arg40) + (var45 & var45) & var45 + (arg40 & (var45 - var45) - arg39) & -454 & arg39) - (-1319255511 + var45)) | -410 | arg40)) | var45) - arg39) | arg39) ^ arg40
    result = (752 & arg40) + -1668254344 + var45
    return result
class class10(object):
    def func9(self, arg48, arg49):
        return 0
class class8(class10):
    def func9(self, arg46, arg47):
        result = (arg47 + 1) ^ -354940299 - (arg46 | -1071740722 - 1894811874) | -1
        return result
def func7(arg41, arg42):
    var43 = 0
    for var44 in range(5):
        var43 += (var43 - var43) & -6
    return var43
def func1(arg1, arg2):
    var36 = func2(arg1, arg2)
    var37 = 1849592325 ^ ((var36 | -877) - arg1 | (-403 | (-110 | (566434443 - ((((arg1 ^ arg2) + 1202268974) - ((-232 + (var36 - (arg2 - arg2)) & arg1) - var36 & 674)) & arg1) + -247584403)) - arg1) | -520) ^ var36
    var38 = ((((arg1 + arg1) | var37) - var37) + arg2 + var37 & -495 | arg1 & var37) + arg2
    result = var37 ^ arg2 | 783432218 & (arg2 & var37)
    return result
def func2(arg3, arg4):
    var9 = func3(arg3, arg4)
    var13 = func4(arg4, var9)
    var14 = arg3 + 504
    var15 = arg4 + 527 + 1988011251
    var16 = (-1647280161 + -60) - arg4 | var15
    if var16 < arg3:
        var17 = var16 + arg4 + arg4 & var13
    else:
        var17 = var9 ^ var14
    var18 = -648 ^ var15 - -915023606
    var19 = var13 - arg3 | arg3 - -951891390
    var20 = var19 - var9
    var21 = var19 - (var16 - var13) ^ var9
    var22 = var16 & var13
    var23 = (526 - var15 | var20) ^ var21
    var24 = ((var16 & -98247457) ^ var21) - var9
    var25 = var16 ^ arg3 | var9
    var26 = var23 | var16
    var27 = var23 & var9 | var24 - 625
    var28 = var13 ^ var27 ^ var23 ^ var15
    var29 = var27 | var27 & var28 + var16
    var30 = var23 ^ var14 & var16
    var31 = (arg3 + var20) & var16 & var14
    var32 = (var25 & var29 - var22) + var25
    var33 = (var19 - arg4) ^ (1704646425 - var15)
    var34 = (var18 - var29) + (arg3 ^ var28)
    if var18 < var26:
        var35 = var13 | -1820745098 + var29 & arg3
    else:
        var35 = var13 - arg4 + var30 - arg4
    result = var14 ^ var27 & (var18 - var22 ^ var23)
    return result
def func3(arg5, arg6):
    var7 = 0
    for var8 in range(39):
        var7 += -2 | arg6 ^ arg5
    return var7
def func4(arg10, arg11):
    closure = [0]
    def func5(acc, rest):
        var12 = acc + acc
        closure[0] += var12
        if acc == 0:
            return var12
        else:
            result = func5(acc - 1, var12)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 3'
    print 'func_number: 6'
    print 'arg_number: 39'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 53'
    for i in xrange(25000):
        x = 5
        x = func6(x, i)
        print x,
