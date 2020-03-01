# Anomaly Detection with Logistic Regression

Our notebook `ĺogistic_regression.ipynb is available in Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VincentStimper/aihack2020-shell-challenge)

## Summary

To classify the anomalies in the data, we split the data into chunks consisting of 10 time steps,
i.e. 90 minutes. This is time window is much longer than thermal and mechanical processes. Hence,
the data within this time frame should be sufficient to explain why and how the anomaly arised.

A chunk of data belongs to the anomaly class if an anomaly happens at its end. The challenge
is that there only 9 anomalies. However, avoiding them is very beneficial. Therefore,
we could risk some false positives if we can find them.

![PCA of chunked data](https://github.com/VincentStimper/aihack2020-shell-challenge/blob/master/images/pca.png "PCA of chunked data")