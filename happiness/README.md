# Automated Data Analysis Report

## Summary Statistics of the Dataset
```shell              year  Life Ladder  Log GDP per capita  Social support  ...   Generosity  Perceptions of corruption  Positive affect  Negative affect
count  2363.000000  2363.000000         2335.000000     2350.000000  ...  2282.000000                2238.000000      2339.000000      2347.000000
mean   2014.763860     5.483566            9.399671        0.809369  ...     0.000098                   0.743971         0.651882         0.273151
std       5.059436     1.125522            1.152069        0.121212  ...     0.161388                   0.184865         0.106240         0.087131
min    2005.000000     1.281000            5.527000        0.228000  ...    -0.340000                   0.035000         0.179000         0.083000
25%    2011.000000     4.647000            8.506500        0.744000  ...    -0.112000                   0.687000         0.572000         0.209000
50%    2015.000000     5.449000            9.503000        0.834500  ...    -0.022000                   0.798500         0.663000         0.262000
75%    2019.000000     6.323500           10.392500        0.904000  ...     0.093750                   0.867750         0.737000         0.326000
max    2023.000000     8.019000           11.676000        0.987000  ...     0.700000                   0.983000         0.884000         0.705000

[8 rows x 10 columns]

```## Categorical variables
```shell       Country name
count          2363
unique          165
top       Argentina
freq             18

```## Missing Values and Outliers
```shellCountry name                          0
year                                  0
Life Ladder                           0
Log GDP per capita                   28
Social support                       13
Healthy life expectancy at birth     63
Freedom to make life choices         36
Generosity                           81
Perceptions of corruption           125
Positive affect                      24
Negative affect                      16
dtype: int64

```## Outliers
```shellyear                                  0
Life Ladder                           2
Log GDP per capita                    1
Social support                       48
Healthy life expectancy at birth     20
Freedom to make life choices         16
Generosity                           39
Perceptions of corruption           194
Positive affect                       9
Negative affect                      31
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
### The Journey of Human Happiness: A Tale of Numbers

In a world ever-accelerating towards the future, where the hustle and bustle often drown out the whispers of joy, there lies a treasure trove of insights waiting to be uncovered. It is a land where data breathes life into the abstract, revealing the intricate tapestry of human happiness. Our tale begins in the year 2005, a pivotal moment in time, where our journey through the realms of the "Life Ladder" begins—a metaphorical staircase where each rung signifies a step closer to our understanding of what truly makes us flourish.

#### The Setting: A World of Data

Picture, if you will, a grand library filled with scrolls of numbers and graphs—a place where each parchment tells the stories of 165 nations, each grappling with its own unique set of challenges and triumphs. The “Life Ladder,” a towering column of hope, beckons us to explore how happiness intertwines with various societal factors. As we step into this realm, we find ourselves surrounded by the whispers of voices from around the globe, captured in pixels and points of data.

#### The Climb: Unraveling the Threads of Happiness

As we ascend the Life Ladder, we discover that the average happiness score across the years hovers around 5.48, with peaks and valleys that tell us of the ebbs and flows of human emotion. The highest score reached a radiant 8.02, while the lowest dipped to 1.28—a stark reminder of the struggles many face. With each step we take, we notice the correlation between happiness and other societal metrics.

The numbers reveal that Log GDP per capita stands as a steadfast companion on this climb, boasting a strong correlation of 0.78 with the Life Ladder. It seems that the wealthier a nation becomes, the higher its citizens tend to score on the happiness scale. Yet, wealth alone does not guarantee joy—social support, another vital thread, shows a correlation of 0.72, reminding us that community and connection are essential in our quest for a fulfilling life.

In our exploration, we stumble upon intriguing anomalies—outliers scattered across the landscape like hidden gems. Two countries, it seems, have soared or stumbled far beyond the average, prompting us to delve deeper into their stories. What events led to such dramatic shifts in happiness? Were they joyous celebrations or devastating losses? Each outlier beckons us to listen closely to their tale.

#### The Complex Web: Interconnected Factors

As we navigate further, the data unveils a complex web of interconnections. Freedom to make life choices strides boldly with a correlation of 0.54, indicating that autonomy plays a significant role in our overall happiness. Those who feel empowered to steer their own lives tend to report higher satisfaction. Yet, lurking in the shadows, we encounter the specter of corruption, revealing a negative correlation of -0.43 with the Life Ladder. It whispers a cautionary tale: where corruption thrives, happiness often withers.

The emotional landscape is equally telling. Positive affect dances hand-in-hand with happiness, exhibiting a strong correlation of 0.52. The more moments of joy and positivity individuals experience, the higher they ascend the Life Ladder. Conversely, negative affect constricts our ascent, with a correlation of -0.35. Here, we are reminded of the profound impact of mental well-being on our overall happiness.

#### The Conclusion: Reflections on Our Journey

As we reach the summit of our exploration, we pause to reflect on the myriad stories told through numbers. The data reveals not just the state of happiness across nations but the intricate interactions between wealth, social structures, and emotional health. Each statistic, each correlation, is a testament to the human experience—a mosaic reflecting our triumphs and trials.

Our journey through this landscape of data implores us to consider the implications of these insights. How can we, as global citizens, foster environments that nurture happiness? How can we bridge the gaps uncovered by the data? The answers lie not only in economic growth but in building supportive communities, empowering individuals, and ensuring that the voices of all citizens are heard.

As we close the final scroll of our grand narrative, let us carry forth the lesson that happiness is not merely a number on a chart; it is a collective journey, an ongoing story that we author together. Let us strive to create a world where each step on the Life Ladder is accompanied by the warm embrace of connection, purpose, and joy.
