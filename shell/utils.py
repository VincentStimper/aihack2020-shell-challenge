import numpy as np
import urllib.request
import zipfile
import os
import pandas as pd

def download_data():
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


    
def extract_sequences(np_data):
    """
    Extract the continuous signals from the time series (numpy array)
    """
    units = np_data.shape[1] - 1 # last one is index counter
    time_bins = np_data.shape[0]

    counters = []
    ori_index = np_data[:, units].astype(int)
    for i in range(time_bins-1):
        if ori_index[i] != ori_index[i+1] - 1:
            counters.append(i)

    counters.append(time_bins) # counters label the sequences in the dataset
    counters = np.asarray(counters)

    all_data = []
    for i in range(counters.shape[0]-1):
        all_data.append(np_data[counters[i]:counters[i+1], 0:units])
        
    return all_data # return list 
