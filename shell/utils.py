import numpy as np

def rm_nan(X, axis=0):
    """
    Cuts out slices along axis containing nans
    :param X: Numpy matrix containing nans
    :param axis: axis along which nans shall be cut out
    :return: X matrix without nans
    """

    bool_nan = np.isnan(X)
    where_nan = np.where(bool_nan)
    ind_cut = np.unique(where_nan[axis])
    X_ = np.delete(X, ind_cut, axis)
    return X_