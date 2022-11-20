import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import math

def cal_mean_var(S,mu, sgma,SS,t):
    S = float(S)
    mu = float(mu)
    sgma = float(sgma)
    t = float(t)
    mean_t = round(S*math.exp(mu*t), 4)
    var_t = round(S*S*(math.exp(2*mu*t)*(math.exp(sgma*sgma*t) - 1)),4)
    mean_c = round(np.mean(SS),4)
    var_c = round(np.var(SS),25)
    print(var_c)
    return mean_t, mean_c, var_t, var_c,t


def geometric_brownian_motion(s,t, mu, sgma, n):
    plt.figure(facecolor="black")
    ax = plt.axes()
    ax.set_facecolor("black")
    ax.spines['bottom'].set_color('cyan')
    ax.spines['left'].set_color('cyan')
    ax.xaxis.label.set_color('cyan')
    ax.yaxis.label.set_color('cyan')
    ax.tick_params(axis='x', colors='cyan')
    ax.tick_params(axis='y', colors='cyan')
    t = float(t)
    n = int(n)
    s = float(s)
    mu = float(mu)
    sgma =float(sgma)
    ti = np.linspace(0,t,10000)
    N = 10000
    SS = []
    for j in range(n):
        S = np.zeros(10000)
        S[0] = s
        for i in range(int(N-1)):
            z = np.random.normal()
            S[i+1] = S[i]*(math.exp((mu- (sgma**2)/2)*(ti[i+1] - ti[i]) + (sgma*(math.sqrt(ti[i+1] - ti[i]))*z)))
            
        plt.plot(ti, S)
        SS.append(S[9999])

    print(SS)
        
    plt.savefig('media/geometric_paths.png')
    return s,mu,sgma,SS,t
