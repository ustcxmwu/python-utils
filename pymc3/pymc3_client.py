from pymc3 import *

import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    size = 200
    true_intercept = 1
    true_slope = 2
    x = np.linspace(0, 1, size)
    true_regression_line = true_intercept + true_slope * x
    y = true_regression_line + np.random.normal(scale=.5, size=size)

    data = dict(x=x, y=y)

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, xlabel='x', ylabel='y', title='Generated data and underlying model')
    ax.plot(x, y, 'x', label='sampled data')
    ax.plot(x, true_regression_line, label='true regression line', lw=2.)
    plt.legend(loc=0)
    # plt.show()

    # with Model() as model:  # model specifications in PyMC3 are wrapped in a with-statement
    #     # Define priors
    #     sigma = HalfCauchy('sigma', beta=10, testval=1.)
    #     intercept = Normal('Intercept', 0, sigma=20)
    #     x_coeff = Normal('x', 0, sigma=20)
    #
    #     # Define likelihood
    #     likelihood = Normal('y', mu=intercept + x_coeff * x, sigma=sigma, observed=y)
    #
    #     # Inference!
    #     trace = sample(200, cores=2)  # draw 3000 posterior samples using NUTS sampling

    with Model() as model:
        # specify glm and pass in data. The resulting linear model, its likelihood and
        # and all its parameters are automatically added to our model.
        glm.GLM.from_formula('y ~ x', data)
        trace = sample(3000, cores=2)  # draw 3000 posterior samples using NUTS sampling

    plt.figure(figsize=(7, 7))
    traceplot(trace[100:])
    plt.tight_layout()
    # plt.show()

    plt.figure(figsize=(7, 7))
    plt.plot(x, y, 'x', label='data')
    plot_posterior_predictive_glm(trace, samples=100, label='posterior predictive regression lines')
    plt.plot(x, true_regression_line, label='true regression line', lw=3., c='y')
    plt.title('Posterior predictive regression lines')
    plt.legend(loc=0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
