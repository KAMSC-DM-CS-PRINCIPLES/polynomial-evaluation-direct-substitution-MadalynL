def evaluate_polynomial_horner(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using Horner's method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result
    s = coefficients[0]
    k =1
    while k<degree:
        s = x*s + coefficients[k]
        k +=1
    return s

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial_horner function
    # TODO: Ask user if they want to run again
    YN = true
    while YN:
        degree = int(input("Degree: "))
        x = int(input("x: "))
        constant_term = int(input("Constant term: "))
        coefficients = []
        for i in range (degree) :
            coefficients.append(input("coefficient: "))
        evaluate_polynomial_horner(degree, x, constant_term, *coefficients)
        ans = input("Do you want to run again y/n")
        if ans == "n":
            YN = False
