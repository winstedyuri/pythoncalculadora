valorCompra = float(input("Digite o valor da compra: "))

valorRecebido = float(input("Digite o valor recebido: "))

troco =  valorRecebido - valorCompra

quantidadeNotasDeCem = 0
quantidadeNotasDeCinquenta = 0 
quantidadeNotasDeVinte = 0
quantidadeNotasdeDez = 0 
quantidadeNotasdeCinco = 0
quantidadeNotasdeDois = 0
quantidadeNotasdeUm = 0  
quantidadeDeMoedasDeCinquenta = 0
quantidadeDeMoedasDeVinteEcinco = 0 
quantidadeDeMoedasDeDez = 0
quantidadeDeMoedasDeCinco = 0
quantidadeDeMoedasDeUm = 0

if valorCompra > valorRecebido:
    print("Senhor(a) está faltando dinheiro: ", troco)
    
if troco >= 100:
    quantidadeNotasDeCem = troco // 100
    troco = troco % 100
    print("Quantidade notas de 100 =", quantidadeNotasDeCem)

if troco >= 50:
    quantidadeNotasDeCinquenta = troco // 50
    troco = troco % 50
    print("Quantidade notas de 50 =", quantidadeNotasDeCinquenta)

if troco >= 20:
    quantidadeNotasDeVinte = troco // 20
    troco = troco % 20
    print("Quantidade notas de 20 =", quantidadeNotasDeVinte)

if troco >= 10:
    quantidadeNotasDeDez = troco // 10
    troco = troco % 10
    print("Quantidade notas de 10 =", quantidadeNotasDeDez)

if troco >= 5:
    quantidadeNotasDeCinco = troco // 5
    troco = troco % 5 
    print("Quantidade notas de 5 =", quantidadeNotasDeCinco)

if troco >= 2:
    quantidadeNotasDeDois = troco // 2
    troco = troco % 2  
    print("Quantidade notas de 2 =", quantidadeNotasDeDois)

if troco >= 1:
    quantidadeNotasdeUm = troco // 1
    troco = troco % 1
    print("Quantidade notas de 1 =", quantidadeNotasdeUm)

if troco >= 0.5:
    quantidadeDeMoedasDeCinquenta = troco // 0.5
    troco = troco % 0.5 
    print("Quantidade moedas de 0.5 =", quantidadeDeMoedasDeCinquenta)

if troco >= 0.25:
    quantidadeDeMoedasDeVinteEcinco = troco // 0.25
    troco = troco % 0.25  
    print("Quantidade moedas de 0.25 =", quantidadeDeMoedasDeVinteEcinco)

if troco >= 0.1:
    quantidadeDeMoedasDeDez = troco // 0.1
    troco = troco % 0.1
    print("Quantidade moedas de 0.10 =", quantidadeDeMoedasDeDez)

if troco >= 0.05:
    quantidadeDeMoedasDeCinco = troco // 0.05
    troco = troco % 0.05
    print("Quantidade moedas de 0.05 =", quantidadeDeMoedasDeCinco)    

if troco >= 0.01:
    quantidadeDeMoedasDeUm = troco // 0.01
    troco = troco % 0.01
    print("Quantidade moedas de 0.01 =", quantidadeDeMoedasDeUm)
   
if troco == 0:
    print("Não teve troco, obrigado! Volte sempre ^_^") 

if valorCompra < valorRecebido:
    print("Seu troco é de: ", troco)