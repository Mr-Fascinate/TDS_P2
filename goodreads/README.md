# Automated Data Analysis Report

## Summary Statistics of the Dataset
```shell           book_id  goodreads_book_id  best_book_id       work_id   books_count  ...      ratings_1      ratings_2      ratings_3     ratings_4     ratings_5
count  10000.00000       1.000000e+04  1.000000e+04  1.000000e+04  10000.000000  ...   10000.000000   10000.000000   10000.000000  1.000000e+04  1.000000e+04
mean    5000.50000       5.264697e+06  5.471214e+06  8.646183e+06     75.712700  ...    1345.040600    3110.885000   11475.893800  1.996570e+04  2.378981e+04
std     2886.89568       7.575462e+06  7.827330e+06  1.175106e+07    170.470728  ...    6635.626263    9717.123578   28546.449183  5.144736e+04  7.976889e+04
min        1.00000       1.000000e+00  1.000000e+00  8.700000e+01      1.000000  ...      11.000000      30.000000     323.000000  7.500000e+02  7.540000e+02
25%     2500.75000       4.627575e+04  4.791175e+04  1.008841e+06     23.000000  ...     196.000000     656.000000    3112.000000  5.405750e+03  5.334000e+03
50%     5000.50000       3.949655e+05  4.251235e+05  2.719524e+06     40.000000  ...     391.000000    1163.000000    4894.000000  8.269500e+03  8.836000e+03
75%     7500.25000       9.382225e+06  9.636112e+06  1.451775e+07     67.000000  ...     885.000000    2353.250000    9287.000000  1.602350e+04  1.730450e+04
max    10000.00000       3.328864e+07  3.553423e+07  5.639960e+07   3455.000000  ...  456191.000000  436802.000000  793319.000000  1.481305e+06  3.011543e+06

[8 rows x 16 columns]

```
## Categorical variables
```shell             isbn       authors  ...                                          image_url                                    small_image_url
count        9300         10000  ...                                              10000                                              10000
unique       9300          4664  ...                                               6669                                               6669
top     375700455  Stephen King  ...  https://s.gr-assets.com/assets/nophoto/book/11...  https://s.gr-assets.com/assets/nophoto/book/50...
freq            1            60  ...                                               3332                                               3332

[4 rows x 7 columns]

```
## Missing Values and Outliers
```shellbook_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
dtype: int64

```
## Outliers
```shellbook_id                         0
goodreads_book_id             345
best_book_id                  357
work_id                       601
books_count                   844
isbn13                        556
original_publication_year    1031
average_rating                158
ratings_count                1163
work_ratings_count           1143
work_text_reviews_count      1005
ratings_1                    1140
ratings_2                    1156
ratings_3                    1149
ratings_4                    1131
ratings_5                    1158
dtype: int64

```
## Correlation Matrix
Below is the correlation matrix of numerical features:

![Correlation Matrix](correlation_matrix.png)

## Outliers Visualization
Below is the outliers detection chart:

![Outliers](outliers.png)
## Distribution
Below is the distribution plot :

![Distribution](distribution_.png)
## Story
**Title: The Librarian's Legacy: Unearthing the Hidden Tales of 10,000 Books**

**Introduction: The Whisper of the Library**

In the heart of a quaint town, nestled between the rustling leaves of ancient oaks, stood a library that had seen centuries unfold. It was more than just a building of bricks and mortar; it was a treasure trove of stories, a sanctuary for dreamers, and a refuge for the lost. Inside, the scent of yellowed pages mingled with the soft glow of reading lamps, creating an enchanting atmosphere. Yet, beyond the confines of its walls, a digital world was awakening, one that held the secrets of its vast collection—a dataset of 10,000 books, each with tales yearning to be told.

**Body: The Dance of Data**

As the diligent librarian, Anna, delved into this dataset, she felt like an archaeologist unearthing ancient scrolls. The first revelation came from the summary statistics. Here lay the lifeblood of the library's collection: a mean books count of 75.7, but with some outliers boasting over 3,000 books. What stories were housed within those crowded shelves, where words and dreams mingled? 

The data revealed a spectrum of ratings: from the solitary voices of readers who left a single star, to the rapturous applause of thousands who bestowed five stars upon their favorites. The average rating of 4.1 was a testament to the quality that the library nurtured. Yet, Anna couldn't help but notice a curious trend; the ratings seemed to dance in tandem with the number of reviews, sparking a question: did the quantity of voices amplify the quality of stories, or was it the other way around?

As she sifted through the categorical statistics, the name "Stephen King" emerged like a lighthouse in the fog. With 60 titles, he was the most prolific author in the dataset. What was it about his storytelling that captivated readers across generations? The uniqueness of authors, with 4,664 participating in this literary tapestry, painted a vivid picture of diverse voices clamoring to be heard. Yet, Anna discovered 700 missing ISBNs—lost identifiers of books that may have slipped through the cracks of time. Were there hidden gems waiting to be rediscovered?

The missing values, she noted, hinted at a larger narrative—books that had once been published and cherished but now faded into obscurity. The absence of data echoed the unrecorded stories of countless authors whose works had been forgotten, their voices silenced in the digital age.

With each analysis, Anna felt the pulse of the library quicken. The correlation matrix revealed intricate relationships: books with higher ratings often had more reviews, a web of feedback that fed into itself, creating a community of readers bound by shared experiences. But there were darker currents too; the more books an author had, the lower their average rating. Was it possible that quantity diluted quality? Or was it merely a reflection of the diverse tastes of readers?

**Conclusion: A Legacy Reimagined**

As Anna stood amidst the stacks, the library transformed before her eyes. The dataset had woven a rich tapestry of insights, revealing the lives bound within each spine. The implications were profound; these stories were not just words on a page, but reflections of human experience—joy, sorrow, triumph, and defeat.

With newfound purpose, Anna envisioned a revitalized library experience. She would host community reading events, invite local authors to speak, and even create a digital platform where readers could share their thoughts in real time. The library would no longer be just a place to borrow books; it would become a vibrant hub of storytelling, a meeting ground for hearts and minds.

As she closed the lid on her laptop, Anna looked around at the shelves filled with stories waiting to be told. The data had spoken, revealing not just the past, but a path forward. The legacy of the library, now intertwined with the digital age, was ready to inspire new generations. And in this melding of tradition and innovation, the library's heart continued to beat, echoing the timeless dance of stories that would never fade away.
