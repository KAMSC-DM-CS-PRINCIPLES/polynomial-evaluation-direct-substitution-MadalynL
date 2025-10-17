def evaluate_polynomial_horner(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using Horner's method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result

    s = float(coefficients[-1])
    print(f"S0 = {s}")
    for i, coeff in enumerate(reversed(coefficients[:-1]), start=1):
        s = s * x + float(coeff)
        print(f"S{i} = {s}")
    s = s * x + float(constant_term)
    print(f"Final result after adding constant term: {s}")
    return s

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial_horner function
    # TODO: Ask user if they want to run again
    YN = True
    while YN:
        degree = int(input("Degree: "))
        x = float(input("x: "))
        constant_term = float(input("Constant term: "))
        coefficients = []
        for i in range (degree) :
            coefficients.append(float(input("coefficient: ")))
        evaluate_polynomial_horner(degree, x, constant_term, *coefficients)
        ans = input("Do you want to run again y/n")
        if ans == "n":
            YN = False
