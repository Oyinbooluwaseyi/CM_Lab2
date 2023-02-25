import methods as m


a = input("Введите a: ")
b = input("Введите b: ")
E = input("Введите E: ")
#a="2"
#b="3"
#for e in range(2,8):
E = 10**(-e)
res_gold = m.gold(a, b, E)
print("Для функции f(x)=(ln(x)/x)^3 в границах интервала ["+a+";"+b+"] с точностью E = "+str(E))
print("По методу золотого сечения экстремум функции: f(x)=" +
        str(round(res_gold[0], 3))+", где x="+str(round(res_gold[1], 3))+" за "+str(res_gold[2])+" итераций")

res_newton = m.newton(a, b, E)
print("По методу Ньютона экстремум функции: f(x)="+str(round(res_newton[0], 3))+", где x="+str(
        round(res_newton[1], 3)) + " за "+str(res_newton[2])+" итераций")
# print("Максимум функции: "+max)
