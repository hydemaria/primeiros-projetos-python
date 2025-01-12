print("Seja muito bem vindo ao quizz da Maria! Este quizz tem o objetivo de fazer umas perguntas sobre a religião Wicca e práticas de Bruxaria!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S": 
    quit()

score = 0

print("Começando...")
print("A Wicca é uma religião neopagã que surgiu no século XX. \n (A) Verdadeiro \n (B) Falso \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Verdadeiro!")
    score = score + 1
else: 
    print("Falso!")

print("O principal princípio da Wicca é: Faça o que quiseres, contanto que não prejudique ninguém")
answer_2 = input("Resposta: ")

if answer_2 == "A": 
    print("Verdadeiro!")
    score = score + 1
else: 
    print("Falso!")

print ("A Wicca possui um livro sagrado equivalente à Bíblia.")
answer_3 = input("Resposta: ")

if answer_3 == "B":
    print("Verdadeiro!")
    score = score + 1
else: 
    print("Falso!")

print(f"Quizz acabou... Pontuação: {score}/3")