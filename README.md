# Share-Market-Analysis-Time-Series
Google Colab Link: https://colab.research.google.com/drive/1c_gVxIpfsyQO-r8i4ucS_kfMP5P4111h


This is analysis of a dataset from kaggle
[MorningStar Dataset](https://www.kaggle.com/datasets/ranjitmishra/morningstar-bank-data-set)

# EDA
1. Null Values
2. Duplicates
3. Outliers
4. Correlation
5. Seasonal decomposition
6. Univariate, Bivariate and Multivariate Analysis


#### Example Code for Seasonality Decomposition

```python
result = seasonal_decompose(df['BAC','Close'], model='multiplicative', freq = 30)
fig = plt.figure()  
fig = result.plot()  
fig.set_size_inches(30, 10)
```


