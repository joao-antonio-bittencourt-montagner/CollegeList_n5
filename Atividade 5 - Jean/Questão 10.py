import Funções

d = str(input("Digite a data de nascimento : ex: 31/12/2000 "))

dia = ""
dia = d[0]
dia += d[1]

mes = ""
mes = d[3]
mes += d[4]
mes = int(mes)
mes = Funções.mes(mes)

ano = ""
ano = d[6]
ano += d[7]
ano += d[8]
ano += d[9]

print("%s de %s de %s" %(dia, mes, ano))