def calculator():
    print("----- Dynamic Calculator -----")
    print("Enter 'exit' to quit\n")
    
    while True:
        expr = input("Enter expression: ")
        
        if expr.lower() == "exit":
            print("Calculator closed.")
            break
        
        try:
            result = eval(expr)   
            print("Result:", result)
        except:
            print("Invalid expression, try again.")

calculator()