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

# print(invalid_tweets(tweets))


#### 1873) Calculate Special Bonus

data = { "employee_id": [2, 3, 7, 8, 9],
         "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
         "salary": [3000, 3800, 7400, 6100, 7700] }

employees = pd.DataFrame(data)

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df[['bonus']] = 0

    mask = (df.employee_id % 2 == 1) & (~df.name.str.startswith('M'))

    df.loc[mask, 'bonus'] = df.salary

    df = df[['employee_id', 'bonus']]

    df = df.sort_values('employee_id')

    return df

# print(calculate_special_bonus(employees))

###### 1667) Fix names in a table

users = pd.DataFrame({ 'user_id': [1, 2],
                    'name': ['aLice', 'bOB'] })

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df['name'] = df.name.str.lower()
    df['name'] = df['name'].str.capitalize()

    df = df.sort_values('user_id')

    return df

#print(fix_names(users))

#### 1517) Find Users With Valid E-mails

users = pd.DataFrame({ 'user_id': [1, 2, 3, 4, 5, 6, 7],
                    'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
                    'mail': [ 'winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com',
                              'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com',
                              ',shapo@leetcode.com' ] })

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mask = users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$")

    df = users.loc[mask]
    return df

# print(valid_emails(users))

##### 1527) Patients With a Condition

data = { 'patient_id': [1, 2, 3, 4, 5],
         'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
         'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201'] }

patients = pd.DataFrame(data)


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = (patients['conditions'].str.contains(' DIAB1')) | (patients['conditions'].str.startswith('DIAB1'))

    df = patients.loc[mask]

    return df

# print(find_patients(patients))

##### 177) Nth Highest Salary

data = { 'id': [1, 2, 3],
         'salary': [100, 200, 300] }

employee = pd.DataFrame(data)


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = sorted(employee['salary'].unique(), reverse=True)

    if len(unique_salaries) < N:
        result = pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    elif N <= 0:
        result = pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    else:
        nth_salary = unique_salaries[N - 1]
        result = pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})

    return result

# print(nth_highest_salary(employee, 2))

##### 176) 2nd Highest salary

data = { 'id': [1, 2, 3],
         'salary': [100, 200, 300] }

employee = pd.DataFrame(data)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sort_sal = sorted(employee.salary.unique())

    index = len(sort_sal)-2

    if index >= 0:
        val = sort_sal[index]

    if index < 0:
        val = None

    df = pd.DataFrame({'SecondHighestSalary': [val]})

    return df

# print(second_highest_salary(employee))

#### 184) Department Highest Salary

employee_data = { 'id': [1, 2, 3, 4, 5],
                  'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
                  'salary': [70000, 90000, 80000, 60000, 90000],
                  'departmentId': [1, 1, 2, 2, 1] }

employee = pd.DataFrame(employee_data)

department_data = { 'id': [1, 2],
                    'name': ['IT', 'Sales'] }

department = pd.DataFrame(department_data)

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns = {'id': 'departmentId'})

    joined_dep_emp = pd.merge(employee, department, how = 'left', on = 'departmentId')
    max_sal = joined_dep_emp.groupby('departmentId').agg({'salary': 'max'})

    out_raw = pd.merge(joined_dep_emp, max_sal, 'inner', on = ['salary', 'departmentId'])
    out = out_raw[['name_y', 'name_x', 'salary']]
    out = out.rename(columns = {'name_y': 'Department',
                      'name_x': 'Employee',
                      'salary': 'Salary'})

    return out

# print(department_highest_salary(employee, department))

#### 178) Rank Scores

data = { "id": [1, 2, 3, 4, 5, 6],
         "score": [3.50, 3.65, 4.00, 3.85, 4.00, 3.65] }

scores = pd.DataFrame(data)

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    list_sort = sorted(scores['score'])
    rank = sorted(scores['score'].rank(method='dense', ascending = False))

    out = pd.DataFrame()
    out['score'] = list_sort[::-1]
    out['rank'] = rank

    return out

print(order_scores(scores))