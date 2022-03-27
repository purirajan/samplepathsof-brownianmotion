# Algorithm: Assuming a geometric Brownian motion dSt = µStdt + σStdWt  where St is the time t value of the underlying asset.
#  It is based on Algorithm 1.11 (Euler discretization of a SDE). 
###################################################
# Arguments:  S0 = 100 µ = 0.1, r = 0.05, δ = 0.025 σ = 0.2, Wt is a Wiener process with W0 = 0, St, t ∈ [0, 1], respectively.
########################################################
import matplotlib.pyplot as plt
import numpy as np

def main():
      
    T = 1 # maturity date
    mu = 0.1# drift
    sigma = 0.2 # standard deviation
    S0 = 100 # initial stock price.
    dt = 0.001# change in time period.
    N = round(T/dt)
    P = 5 # number of sample path 
    t = np.linspace(0, T, N)
    np.random.seed(seed=100)
    for  i in range (P):
        
        W = np.random.standard_normal(size = N) 
        W = np.cumsum(W)*np.sqrt(dt)
        X = (mu-0.5*sigma**2)*t + sigma*W 
        S = S0*np.exp(X) # geometric brownian motion.
        plt.plot(t, S)
    plt.xlabel(" time(t)")
    plt.ylabel(" S(t)")
    plt.show()
main()
