import numpy as np
import matplotlib.pyplot as plt

# generate a canonical (mean=1) list of exponential random variables
def randExp(N = 1):
	return -np.log(np.random.uniform(0.,1.,N))

# generate a list of arrival times for the Poisson process with integrated rate function inverse: irfi
def poissonProcess(irfi, T):
	t = 0
	ts = []
	yc = 0
	while (t<T):
		yc += randExp()
		t = irfi(yc)
		ts.extend(t)
	return ts[:-1]

# the integrated rate function inverse corresponding to f(t) = 60*(t-1)^2
def exampleNonHomogenousIRFI(y):
	s = np.sign(y-20)
	t = s*abs((y-20)/20)**(1./3.)+1
	return t

# the integrated rate function inverse corresponding to f(t) = 20
def exampleHomogenousIRFI(y):
	t = y/20
	return t

def plotPoissonProcess(pp, T):
	tt = np.linspace(0,T,1001)
	pps = 0*tt
	for t in pp:
		pps[tt>t] += 1
	plt.plot(tt,pps)
	plt.xlabel('time axis')
	plt.ylabel('event counter')
	plt.show()

T = 2

ppn = poissonProcess(exampleNonHomogenousIRFI, T)
plotPoissonProcess(ppn, T)

pph = poissonProcess(exampleHomogenousIRFI, T)
plotPoissonProcess(pph, T)
