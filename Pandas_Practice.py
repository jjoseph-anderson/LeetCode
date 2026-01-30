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

# print(order_scores(scores))

#### 196) Delete Duplicate Emails

person = pd.DataFrame({ 'id': [1, 2, 3],
                    'email': ['john@example.com', 'bob@example.com', 'john@example.com'] })

# time complexity sorting is O(nlogn) and drop duplicates is O(n)
# hence time complexity is O(nlogn) could replace sort and put in (, keep="first") into drop dupl
# making time complexity O(n)
def delete_duplicate_emails(person: pd.DataFrame) -> None:

    person.sort_values(["id"], inplace = True)
    person.drop_duplicates(subset=["email"], inplace=True)

# print(delete_duplicate_emails(person))

#### 1795) Rearrange Products Table

products = pd.DataFrame({ 'product_id': [0, 1],
                          'store1': [95, 70],
                          'store2': [100, None],
                          'store3': [105, 80] })


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products.melt(id_vars=["product_id"], value_vars=["store1", "store2", "store3"],value_name = "price", var_name = "store")

    df = df.dropna()

    return df

# print(rearrange_products_table(products))

#### 1741) Find Total Time Spent by Each Employee
data = { "emp_id": [1, 1, 1, 2, 2],
         "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
         "in_time": [4, 55, 1, 3, 47],
         "out_time": [32, 200, 42, 33, 74] }

employees = pd.DataFrame(data)

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(by = ["event_day","emp_id"], as_index=False).sum()
    df['total_time'] = df['out_time'] - df['in_time']
    df = df[['event_day','emp_id','total_time']]
    df = df.rename(columns = {'event_day': 'day'})

    return df.sort_values('emp_id')

# print(total_time(employees))

##### 511) Game Play Analysis I

data = { "player_id": [1, 1, 2, 3, 3],
         "device_id": [2, 2, 3, 1, 4],
         "event_date": ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"],
         "games_played": [5, 6, 1, 0, 5] }

activity = pd.DataFrame(data)

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(by = 'player_id', as_index = False).min()

    df = df[['player_id', 'event_date']]
    df = df.rename(columns = {'event_date' : 'first_login'})

    return df

# print(game_analysis(activity))

# could just get minimum of 'event_date' column
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(by = 'player_id', as_index = False)['event_date'].min()

    df = df.rename(columns = {'event_date' : 'first_login'})

    return df

# print(game_analysis(activity))

##### 2356) Number of Unique Subjects Taught by Each Teacher

data = { 'teacher_id': [1, 1, 1, 2, 2, 2, 2],
         'subject_id': [2, 2, 3, 1, 2, 3, 4],
         'dept_id': [3, 4, 3, 1, 1, 1, 1] }
teacher = pd.DataFrame(data)

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(by = 'teacher_id', as_index = False)['subject_id'].nunique()

    df = df.rename(columns = {'subject_id':'cnt'})

    return df

# print(count_unique_subjects(teacher))

##### 596) Classes With at Least 5 Students

data = { 'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
         'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math'] }

courses = pd.DataFrame(data)

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by = 'class', as_index = False).count()

    df = df[df['student'] >= 5]

    df = df[['class']]

    return df

# print(find_classes(courses))

#### 586) Customer Placing the Largest Number of Orders

data = { 'order_number': [1, 2, 3, 4],
         'customer_number': [1, 2, 3, 3] }

orders = pd.DataFrame(data)

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(by = 'customer_number', as_index = False).count()

    df = df[df.order_number == max(df.order_number)]

    df = df[['customer_number']]

    return df

# print(largest_orders(orders))

#### 1484) Group Sold Products By The Date

data = { 'sell_date': [ '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30' ],
         'product': [ 'Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt' ] }

activities = pd.DataFrame(data)

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = (activities.drop_duplicates().groupby('sell_date')['product'].agg(num_sold = 'count',products = list).reset_index())

    df.products = df.products.apply(lambda x: ','.join(sorted(x)))

    return df

# print(categorize_products(activities))

##### 1693) Daily Leads and Partners

data = { 'date_id': [ '2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7' ],
         'make_name': [ 'toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda' ],
         'lead_id': [ 0, 1, 1, 0, 1, 1, 2, 0, 1, 2 ],
         'partner_id': [ 1, 0, 2, 1, 0, 2, 1, 1, 2, 1 ] }

daily_sales = pd.DataFrame(data)

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(by = ['date_id','make_name'], as_index = False).nunique()

    df = df.rename(columns = {'lead_id': 'unique_leads','partner_id': 'unique_partners'})

    return df

# print(daily_leads_and_partners(daily_sales))

#### 1050) Actors and Directors Who Cooperated At Least Three Times

actor_director = pd.DataFrame({ "actor_id": [1, 1, 1, 1, 1, 2, 2],
                    "director_id":[1, 1, 1, 2, 2, 1, 1],
                    "timestamp": [0, 1, 2, 3, 4, 5, 6] })

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(by = ['actor_id', 'director_id'], as_index = False).count()

    df = df[df.timestamp >= 3]

    return df[['actor_id', 'director_id']]

#print(actors_and_directors(actor_director))

#### 1378) Replace Employee ID With The Unique Identifier

employees = pd.DataFrame({ "id": [1, 7, 11, 90, 3],
                           "name": ["Alice", "Bob", "Meir", "Winston", "Jonathan"] })

employee_uni = pd.DataFrame({ "id": [3, 11, 90],
                              "unique_id": [1, 2, 3] })

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, employee_uni, on='id', how='left')

    return df[['unique_id', 'name']]

#print(replace_employee_id(employees, employee_uni))

#### 1280) Students and Examinations

students = pd.DataFrame({ "student_id": [1, 2, 13, 6],
                          "student_name": ["Alice", "Bob", "John", "Alex"] })

subjects = pd.DataFrame({ "subject_name": ["Math", "Physics", "Programming"] })

examinations = pd.DataFrame({ "student_id": [1, 1, 1, 2, 1, 13, 13, 13, 13, 2, 2],
                              "subject_name": [ "Math", "Physics", "Programming", "Programming", "Physics", "Math", "Math", "Programming", "Physics", "Math", "Math" ] })

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    full = students.assign(key=1).merge(subjects.assign(key=1), on="key").drop("key", axis=1)

    exam_counts = (examinations.groupby(["student_id", "subject_name"], as_index=False).size().rename(
        columns={"size": "attended_exams"}))

    df = full.merge(exam_counts, on=["student_id", "subject_name"], how="left")

    df["attended_exams"] = df["attended_exams"].fillna(0).astype(int)
    df = df.sort_values(['student_id', 'subject_name'])

    return df

print(students_and_examinations(students, subjects, examinations))