import math


#定义求占空比的函数
#period=cubemx.tim.conter period
#A,B分别为正弦波的幅值和，脉冲的幅值
#f，f1是正弦波的频率和时间块的频率
def get_spwm(period,A,B,f,f1):
    num=int(f1/(2*f)+1)
    for k in range(1,num):
        D=abs(f1/(math.pi*f)*(A/B)*math.sin(math.pi*f/f1)*math.sin((2*k-1)*math.pi*f/f1)*period-1)
        print("{},\t".format(int(D)))


get_spwm(1000,3.3,3.3,50,1000)
