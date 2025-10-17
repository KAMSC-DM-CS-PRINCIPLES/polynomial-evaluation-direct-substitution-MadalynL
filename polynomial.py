def evaluate_polynomial(degree, x, constant_term, *coefficients):
    s=constant_term
    k=1
    power=x
    if degree!=len(coefficients):
        raise ValueError("Degree of polynomial must be equal to number of coefficients")
    while k<degree+1:
        s+=coefficients[k-1]*power**k
        k+=1
    return s
