"""
author = Eda Aydın
"""

# Please make sure to install wordcloud : pip install wordcloud

# import libraries
import pandas as pd  # Import pandas for data manipulation using data frames
import numpy as np  # Import Numpy for data statistical analysis
import matplotlib.pyplot as plt  # Import matplotlib for data visualization
import seaborn as sns  # Statistical data visualization

df_alexa = pd.read_csv("amazon_alexa.tsv", sep="\t")

print(df_alexa.keys())
print(df_alexa['verified_reviews'])

# VISUALIZING THE DATA

positive = df_alexa[df_alexa["feedback"] == 1]
negative = df_alexa[df_alexa["feedback"] == 0]

count = sns.countplot(df_alexa["feedback"], label="Count")
plt.show(count)

count1 = sns.countplot(x="rating", data=df_alexa)
plt.show(count1)

count2 = df_alexa["rating"].hist(bins=5)
plt.show(count2)

plt.figure(figsize=(30,3))
bar_plot = sns.barplot(x="variation", y="rating", data=df_alexa, palette="deep")
plt.show(bar_plot)

# WORD CLOUD

words= df_alexa["verified_reviews"].tolist()
len(words)
print(words)

words_as_one_string = " ".join(words)
print(words_as_one_string)
len(words_as_one_string)

from wordcloud import WordCloud

plt.figure(figsize=(20,20))
plt.imshow(WordCloud().generate(words_as_one_string))

# DATA CLEANING / FEATURE ENGINEERING

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
alexa_countvectorizer = vectorizer.fit_transform(df_alexa["verified_reviews"])
print(alexa_countvectorizer.shape)
type(alexa_countvectorizer)

print(vectorizer.get_feature_names())
print(alexa_countvectorizer.toarray())

word_count_array = alexa_countvectorizer.toarray()
print(word_count_array.shape)
print(word_count_array[0,:])

index = 13
plt.plot(word_count_array[index, :])
print(df_alexa["verified_reviews"][index])

df_alexa["length"] = df_alexa["verified_reviews"].apply(len)
print(df_alexa.head())

df_alexa["length"].hist(bins=100)

min_char = df_alexa["length"].min()
print(df_alexa[df_alexa["length"] == min_char]["verified_reviews"].iloc[0])

max_char = df_alexa["length"].max()
print(df_alexa[df_alexa["length"] == max_char]["verified_reviews"].iloc[0])

