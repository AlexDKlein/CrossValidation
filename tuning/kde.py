import numpy as np

class KDE():
    """
        Multivariate kernel density estimator.
        
        Parameters
        ==========
        data: array-like
        
        dtypes: str or iterable of str/dtypes

        bandwidth: str, one of ['mise', 'approx', 'cross_val', 'silverman']
    """
    def __init__(self, data, dtypes=None, bandwidth=None):
        self.data = data
        self.dtypes = dtypes
        self.bandwidth = bandwidth

    def __call__(self, *args, **kwargs):
        pass

    
    def get_bandwidth(self, method=None):
        n, d = np.shape(self.data)
        coeff = (4 / (d + 2)) ** (1 / (d + 4)) * n ** (-1 /  (d + 4))
        return np.std(self.data, axis=0) * coeff

    