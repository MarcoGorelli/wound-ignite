from precise.skatertools.m6.covarianceforecasting import m6_cov
from precise.skaters.portfolioutil.analytic import unitary_long_from_cov, unitary_from_cov, unitary_long_gradual, unitary_long_mininize
from precise.skaters.portfolioutil.longonly import long_from_cov
from precise.skaters.portfolioutil.portfunctions import portfolio_variance, exclude_negative_weights
from pprint import pprint


def test_iterative_gradual():
    n_dim = 8
    dfcov0 = m6_cov(interval='d', n_dim=n_dim, n_obs=60)
    cov0 = dfcov0.values
    w0 = unitary_from_cov(cov0)
    wl = long_from_cov(cov0)
    v0 = portfolio_variance(cov0, w0)
    vl = portfolio_variance(cov0, wl)
    wn, wn_neg = exclude_negative_weights(w0, with_neg_mass=True)
    vn = portfolio_variance(cov0, wn)
    wi, wi_neg = unitary_long_gradual(cov0, with_neg_mass=True)
    vi = portfolio_variance(cov0.copy(), wi)
    rankings = [(v0, 'unitary'), (vl, 'long'), (vn, ('exclude', wn_neg)), (vi,('iterative',wi_neg))]
    print(' ')
    pprint(sorted(rankings))


if __name__=='__main__':
    test_iterative_gradual()