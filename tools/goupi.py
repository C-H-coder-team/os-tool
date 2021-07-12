
import random
import complete
def dog_pi():
    sth=str(input('主题：'))
    n=int(input('句子数量：'))

    for i in range(1,n):
        rand=int()
        rand=random.randint(1, 20)
        
        if rand == 1:
            complete.complete.op1(sth)
        elif rand == 2:
            complete.complete.op2(sth)
        elif rand == 3:
            complete.complete.op3(sth)
        elif rand == 4:
            complete.complete.op4(sth)
        elif rand == 5:
            complete.complete.op5(sth)
        elif rand == 6:
            complete.complete.op6(sth)
        elif rand == 7:
            complete.complete.op7(sth)
        elif rand == 8:
            complete.complete.op8(sth)
        elif rand == 9:
            complete.complete.op9(sth)
        elif rand == 10:
            complete.complete.op10(sth)
        elif rand == 11:
            complete.complete.op11(sth)
        elif rand == 12:
            complete.complete.op12(sth)
        elif rand == 13:
            complete.complete.op13(sth)
        elif rand == 14:
            complete.complete.op14(sth)
        elif rand == 15:
            complete.complete.op15(sth)
        elif rand == 16:
            complete.complete.op16(sth)
        elif rand == 17:
            complete.complete.op17(sth)
        elif rand == 18:
            complete.complete.op18(sth)
        elif rand == 19:
            complete.complete.op19(sth)
        else:
            complete.complete.op20(sth)