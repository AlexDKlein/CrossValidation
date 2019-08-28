import numpy as np

class HyperParameterTuner():
    """
        Parameters
        ==========
        params: dict
            ...
        cv_method: callable
            ...
        quantile: float, default=0.25
            ...
        bandwidth: float, dict, or None, default=None
            ...
        constraints: dict, callable, or None, default=None
            ...
        mode: str, default='tree'
            ...
        
        Usage
        ==========
            ...
    """
    
    def __init__(self, params, cv_method, quantile=0.25, bandwidth=None, constraints=None, mode='tree'):
        self.params = params
        self.cv_method = cv_method
        self.quantile = quantile
        self.bandwidth = bandwidth
        self.constraints = constraints
        self.mode = mode


    def fit(self, X, y=None, rounds=-1, verbose=True, **kwargs):
        pass

    def expected_improvement(self, params):
        """
        Return the probability that the cv score for the given parameters falls 
        below the quantile indicated by the object's 'quantile' attribute.
        """
        pass

    def suggest(self, candidates=-1):
        pass

    @property
    def _open_params(self):
        return {k:v for k,v in self.params.items() 
                if np.iterable(v)
                and not isinstance(v, (str, tuple))
                and not len(v) == 1}
    
    @property
    def _locked_params(self):
        return {k: v if isinstance(v, (str, tuple))
                or not np.iterable(v) 
                or len(v) > 1 else v[0]
                for k,v in self.params.items() 
                if k not in self._open_params}
        

    