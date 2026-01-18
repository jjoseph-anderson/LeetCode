import pandas as pd

### 595) Big Countries

data = { "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
         "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
         "area": [652230, 28748, 2381741, 468, 1246700],
         "population": [25500100, 2831741, 37100000, 78115, 20609294],
         "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000] }
world = pd.DataFrame(data)

# time O(n) Bolean filter complexity
# space O(n) Bolean Mask time complexity
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world.population >= 25000000) | (world.area >= 3000000)]

    df = df[['name', 'population', 'area']]

    return df

# print(big_countries(world))

#### 1757) Recyclable and Low Fat Products

data = { "product_id": [0, 1, 2, 3, 4],
         "low_fats": ["Y", "Y", "N", "Y", "N"],
         "recyclable": ["N", "Y", "Y", "Y", "N"] }
products = pd.DataFrame(data)

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products.low_fats == 'Y') &(products.recyclable == 'Y')]

    df = df[['product_id']]

    return df

# print(find_products(products))

#### 183) Customers who never order
customers = pd.DataFrame({ "id": [1, 2, 3, 4],
                           "name": ["Joe", "Henry", "Sam", "Max"] }) # Orders table
orders = pd.DataFrame({ "id": [1, 2], "customerId": [3, 1] })

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]

    df = df.rename(columns={"name": "Customers"})

    df = df[['Customers']]

    return df

# print(find_customers(customers, orders))

##### 1148) Article Views I

data = { "article_id": [1, 1, 2, 2, 4, 3, 3],
         "author_id": [3, 3, 7, 7, 7, 4, 4],
         "viewer_id": [5, 6, 7, 6, 1, 4, 4],
         "view_date": [ "2019-08-01", "2019-08-02", "2019-08-01", "2019-08-02", "2019-07-22", "2019-07-21", "2019-07-21" ] }

views = pd.DataFrame(data)

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views.author_id == views.viewer_id]

    df = df[['author_id']].rename(columns = {"author_id": "id"})

    df = df.drop_duplicates()

    df = df.sort_values(by = "id")

    return df

# print(article_views(views))

#### 1683 Invalid Tweets

data = { 'tweet_id': [1, 2],
         'content': ['Let us Code', 'More than fifteen chars are here!'] }

tweets = pd.DataFrame(data)

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets

    for i in range(len(tweets)):
        if len(tweets['content'][i]) <= 15:
            df = df.drop(i)

    df = df.reset_index(drop=True)

    return df[['tweet_id']]

# print(invalid_tweets(tweets))

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    invalid = tweets[tweets['content'].str.len() > 15]

    return invalid[['tweet_id']]

print(invalid_tweets(tweets))
