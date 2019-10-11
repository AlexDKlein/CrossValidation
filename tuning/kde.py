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
        """
            Set and return the bandwidth to be used in future kernel density
            estimations.
            
            Parameters
            ==========
            method: callable, default=None
                The method used to calculate or estimate the bandwidth.
                Custom methods must take an array-like matching the KDE 
                object's `data` attribute and return a 1-d array of length
                `ndim(data)`. By default, use Silverman's rule of thumb.

            Returns 
            =========
            output: np.ndarray[ndim=1, dtype=float]
                The results of the bandwidth calculation.

        """
        if method is None:
            n, d = np.shape(self.data)
            coeff = (4 / (d + 2)) ** (1 / (d + 4)) * n ** (-1 /  (d + 4))
            self.bandwidth  = np.sqrt(np.std(self.data, axis=0) * coeff)
        else:
            self.bandwidth = method(self.data)
        return self.bandwidth

    