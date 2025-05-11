# example of effect of size on monte carlo sample
from numpy.random import normal
from matplotlib import pyplot
# define the distribution
mu = 50
sigma = 5
# generate monte carlo samples of differing size
sizes = [10, 50, 100, 1000]
for i in range(len(sizes)):
	# generate sample
	sample = normal(mu, sigma, sizes[i])
	# plot histogram of sample
	pyplot.subplot(2, 2, i+1)
	pyplot.hist(sample, bins=20)
	pyplot.title('%d samples' % sizes[i])
	pyplot.xticks([])
# show the plot
pyplot.show()