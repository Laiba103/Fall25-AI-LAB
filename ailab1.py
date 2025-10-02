
print("----- Dynamic Calculator -----")
print("Enter 'exit' to quit\n")

while True:
    expr = input("Enter expression: ")

    if expr.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        
        expr = expr.replace("×", "*").replace("÷", "/")
        expr = expr.replace(")(", ")*(")
        new_expr = ""
        prev = ""
        for ch in expr:
            if ch == "(" and (prev.isdigit() or prev == ")"):
                new_expr += "*" + ch
            else:
                new_expr += ch
            prev = ch

        result = eval(new_expr)
        print("Result:", result)

    except Exception as e:
        print("Error:", e)
