operand_1_input = int(input("enter first operand :"))
operator = input("enter an operator(+,-,*,/,%):")
operand_2_input = int(input("enter second operand :"))

if("+" in operator):
    print("result:",operand_1_input + operand_2_input)
elif("-" in operator):
    print("result:",operand_1_input - operand_2_input)
elif("*" in operator or "x" in operator):
    print("result:",operand_1_input * operand_2_input)
elif("/" in operator):
    print("result:",operand_1_input / operand_2_input)
elif("%" in operator):
    print("result:",operand_1_input % operand_2_input)