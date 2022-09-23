from GoogleNews import GoogleNews
googlenews = GoogleNews()
import pandas as pd


news = GoogleNews(period='7d')
news.search("NITA_U")
result = news.result()
print(str(result))
Counting = len(result)
print(Counting)

data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()