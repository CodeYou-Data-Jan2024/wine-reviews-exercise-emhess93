#import pandas
import pandas as pd

#read in wine mag file
WRevs = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

#create dataframe with name, count of reviews, and average points
wine_reviews = WRevs.groupby(['country']).points.agg([len, "mean"]).round(decimals=1)

#format columns
wine_reviews = wine_reviews.rename(columns={'len':"count", 'mean':"points"})

print(wine_reviews)
#write data summary to new file in data folder named reviews-per-country.csv

wine_reviews.to_csv("data/reviews-per-country.csv")

