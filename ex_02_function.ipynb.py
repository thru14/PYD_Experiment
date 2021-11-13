print("Hello world")
print("本函数用于材料拉伸实验数据处理")
print("接下来请输入实验测量数据")
print("这里是我们准备好的数据")
print("标距 0.3" 
      "直径1 0.5" 
      "直径2 0.6" 
      "屈服荷载 7000" 
      "最大荷载 8000"
      "拉断后标距 0.4"
      "断口处直径1 0.4"
      "断口处直径2 0.5"
      "屈服抗力 7000"
      "最大抗力 8000"
      "荷载增量 8000"
      "变形量1 0.02"
      "变形量2 0.02"
      "变形量3 0.02"
      "变形量4 0.02"
      "变形量5 0.02")
print("接下来就输入数据得出我们的最终结果吧!")
L_0=input("标距=")
d_1=input("直径1=")
d_2=input("直径2=")
F_1=input("屈服荷载=")
F_max=input("最大荷载=")
L_u=input("拉断后标距=")
d_u_1=input("断口处直径1=")
d_u_2=input("断口处直径2=")
P_s=input("屈服抗力=")
P_b=input("最大抗力=")
F_d=input("荷载增量=")
L_d_1=input("变形量1=")
L_d_2=input("变形量2=")
L_d_3=input("变形量3=")
L_d_4=input("变形量4=")
L_d_5=input("变形量5=")
x=float(d_1) 
y=float(d_2)
d_0=((x+y)/2)#原平均直径
z=float(d_0)
S_0=(((z/2)**2)*3.14)#原截面积
n=float(d_u_1)
m=float(d_u_2)
d_u_0=((n+m)/2)#断口处平均直径
p=float(d_u_0)
S_u_0=(((p/2)**2)*3.14)#断口处截面积
a=float(L_d_1)
b=float(L_d_2)
c=float(L_d_3)
d=float(L_d_4)
e=float(L_d_5)
L_d_0=((a+b+c+d+e)/5)#平均变形量
l=float(L_d_0)
A=((3.14*(z**2))/4)#原周长
p=float(P_s)
q=float(P_b)
Q_s=(p/A)#屈服极限
Q_b=(q/A)#强度极限
F=((z**2-p**2)/z**2)#断面收缩率
g=float(L_0)
h=float(L_u)
S=((h-g)/g)#延伸率
r=float(F_d)
s=float(S_0)
L=(l/g)#应变
G=(r/s)#应力
E=G/L#弹性模量
print("弹性模量={}".format(E))
print("屈服极限={}".format(Q_s))
print("强度极限={}".format(Q_b))
print("断面收缩率={:2%}".format(F))
print("延伸率={:2%}".format(S))