def erf25(x):
    """Implements 7.1.25 erf approximation from Abramowitz and
       Stegun (1972), pg. 299. Accurate for abs(eps(x)) <= 2.5e-5."""
    
    #Constants
    
    p = 0.47047
    a1 = 0.3480242
    a2 = -0.0958798
    a3 = 0.7478556
    e = 2.7182818
    
    #t
    
    t = 1.0/(1.0 + (p * x))
    
    #Erf Calculation
    
    erf = 1.0 - (((a3 * t + a2) * t + a1) * t)
    erf *= e ** -(x ** 2)
    
    if x < 0: return -round(erf,7)
    else: return round(erf,7)

def erf26(x):
    """Implements 7.1.26 erf approximation from Abramowitz and
       Stegun (1972), pg. 299. Accurate for abs(eps(x)) <= 1.5e-7."""
    
    #Constants
    
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    e = 2.718281828
    
    #t
    
    t = 1.0/(1.0 + (p * x))
    
    #Erf calculation
    
    erf = 1.0 - (((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t)
    erf *= e ** -(x ** 2)
    
    if x < 0: return -round(erf,9)
    else: return round(erf,9)
    
def erf27(x):
    """Implements 7.1.27 erf approximation from Abramowitz and
       Stegun (1972), pg. 299. Accurate for abs(eps(x)) <= 5e-4."""

    #Constamts
    
    a1 = 0.278393
    a2 = 0.230389
    a3 = 0.000972
    a4 = 0.078108
    
    #Erf calculation
    
    erf = 1.0 - ((1.0 + ((((a4 * x + a3) * x + a2) * x + a1) * x)) ** -4)
    
    if x < 0: return -round(erf,6)
    else: return round(erf,6)

def erf28(x):
    """Implements 7.1.28 erf approximation from Abramowitz and
       Stegun (1972), pg. 299. Accurate for abs(eps(x)) <= 3e-7."""
       
    #Constants
   
    a1 = 0.0705230784
    a2 = 0.0422820123
    a3 = 0.0092705272
    a4 = 0.0001520143
    a5 = 0.0002765672
    a6 = 0.0000430638
   
    #Erf calculation
   
    erf = 1.0 - ((1.0 + ((((((a6 * x + a5) * x + a4) * x + a3) * x + a2) * x + a1) * x)) ** -16)
   
    if x < 0: return -round(erf,10)
    else: return round(erf,10)