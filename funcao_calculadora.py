def operacaoNum(num1, num2, operacao):
  if operacao == "+":
    return num1 + num2
  elif operacao == "-":
    return num1 - num2
  elif operacao == "*":
    return num1 * num2
  elif operacao == "/":
    return num1/num2
  else:
    return "Digite uma operacao valida"

exemplo = operacaoNum(1, 5, "9")
print(exemplo)
