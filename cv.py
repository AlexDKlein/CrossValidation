import numpy as np
import joblib

class CV():
    def __init__(self, estimator, folds=5, callbacks=None, seed=None, n_jobs=1):
        self.estimator = estimator
        self.folds = folds
        self.callbacks = callbacks
        self.seed = seed
        self.n_jobs = n_jobs
        self.results = dict()


    def fit(self, X, y=None):
        pass

    def _construct(self):
        pass

    def _callbacks(self):
        pass

    def _eval_stage(self):
        pass