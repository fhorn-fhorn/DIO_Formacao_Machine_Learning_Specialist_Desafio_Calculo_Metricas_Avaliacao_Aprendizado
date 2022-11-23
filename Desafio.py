#Matriz de Confusão -             O que o programa disse
#                                 Vai chover       Não vai chover
#O que aconteceu Choveu              40 (VP)            10 (FN)
#O que aconteceu Não Choveu          15 (FP)            35 (VN)

VP = 40
VN = 35
FP = 15
FN = 10

print("VP: ", VP)
print("VN: ", VN)
print("FP: ", FP)
print("FN: ", FN)

Sensibilidade = VP / (VP+FN)
print("Sensibilidade : ", Sensibilidade)

Especificidade = VN / (FP+VN)
print("Especificidade: ", Especificidade)

Acuracia = (VP+VN) / (VP+VN+FP+FN)
print("Acuracia      : ", Acuracia)

Precisao = VP / (VP+FP)
print("Precisao      : ", Precisao)

F_Score = 2 * ( (Precisao*Sensibilidade) / (Precisao+Sensibilidade) )
print("F-Score       : ", F_Score)