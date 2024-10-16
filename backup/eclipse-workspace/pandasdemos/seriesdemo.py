import pandas as pd

reviews = pd.Series([4.6, 4.4, 4.8, 5])

print(reviews)
print(reviews.describe())
print("over    ")
print(reviews[0])

print(reviews.count())
print(reviews.mean())
print(reviews.min())
print(reviews.max())
print(reviews.std())

reviews1 = pd.Series([4.6, 4.4, 4.8, 5],index=['python','java','django','devops'])
print(reviews1)

reviews = pd.Series({'python':4.6,'java':4.6})
print(reviews)
print(reviews['python'])
print(reviews.java)

courses = pd.Series(['java','python','aws'])
print(courses)
print(courses.str.upper())
