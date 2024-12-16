# Automated Data Analysis Report

## Summary Statistics of the Dataset
```shell           overall      quality  repeatability
count  2652.000000  2652.000000    2652.000000
mean      3.047511     3.209276       1.494721
std       0.762180     0.796743       0.598289
min       1.000000     1.000000       1.000000
25%       3.000000     3.000000       1.000000
50%       3.000000     3.000000       1.000000
75%       3.000000     4.000000       2.000000
max       5.000000     5.000000       3.000000

```## Categorical variables
```shell             date language   type              title                 by
count        2553     2652   2652               2652               2390
unique       2055       11      8               2312               1528
top     21-May-06  English  movie  Kanda Naal Mudhal  Kiefer Sutherland
freq            8     1306   2211                  9                 48

```## Missing Values and Outliers
```shelldate              99
language           0
type               0
title              0
by               262
overall            0
quality            0
repeatability      0
dtype: int64

```## Outliers
```shelloverall          1216
quality            24
repeatability       0
dtype: int64

```## Correlation Matrix
Below is the correlation matrix of numerical features:

![Correlation Matrix](correlation_matrix.png)

## Outliers Visualization
Below is the outliers detection chart:

![Outliers](outliers.png)
## Distribution
Below is the distribution plot :

![Distribution](distribution_.png)
## Story
Failed to generate story.
