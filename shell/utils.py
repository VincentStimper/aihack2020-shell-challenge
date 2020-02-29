import numpy as np
import urllib.request
import zipfile
import os

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

def download_data()
    """
    Download and extract the shell challenge data
    """
    print("Starting download ...")
    urls = [
        "https://github.com/aihack20/shell_challenge/releases/download/data/clean_dataset.zip",
        "https://github.com/aihack20/shell_challenge/releases/download/data/raw_dataset.zip",
    ]
    os.makedirs("shell_data", exist_ok=True)
    for url in urls:
        with urllib.request.urlopen(url) as src:
            with open("tmp.zip", "wb") as dest:
                dest.write(src.read())
        print("Unpacking archive ...")
        with zipfile.ZipFile("tmp.zip") as f:
            f.extractall("shell_data")
    print("Done!")