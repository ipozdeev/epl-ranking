import pandas as pd
import numpy as np


def get_first_eigenvector(a):
    """Find the largest eigenvector of a matrix.

    Parameters
    ----------
    a : pandas.DataFrame

    Returns
    -------
    pandas.Series

    """
    d, lam = np.linalg.eig(a)

    max_idx = d.real.argmax()

    res = pd.Series(lam[:, max_idx].real, index=a.columns)

    if res.lt(0).any():
        res *= -1

    return res
