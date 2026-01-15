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

print(find_products(products))