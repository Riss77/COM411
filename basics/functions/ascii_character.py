

print("\nProgram Started!\n")

code = int(input("Please enter an ASCII code:\n"))

if abs(code) in range(abs(code), 127, 1):
    print(f"The character represented by the ASCII code {abs(code)} is: {chr(code)}")

else:
    print("This code is not compatible\n")

print("Program Ended!\n")