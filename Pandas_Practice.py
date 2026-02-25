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

## print(students_and_examinations(students, subjects, examinations))

#### 607) Sales Person

sales_person = pd.DataFrame({
    "sales_id": [1, 2, 3, 4, 5],
    "name": ["John", "Amy", "Mark", "Pam", "Alex"],
    "salary": [100000, 12000, 65000, 25000, 5000],
    "commission_rate": [6, 5, 12, 25, 10],
    "hire_date": ["4/1/2006", "5/1/2010", "12/25/2008", "1/1/2005", "2/3/2007"]
})

# Company table
company = pd.DataFrame({
    "com_id": [1, 2, 3, 4],
    "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
    "city": ["Boston", "New York", "Boston", "Austin"]
})

# Orders table
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
    "com_id": [3, 1, 1, 1],
    "sales_id": [4, 5, 1, 4],
    "amount": [10000, 5000, 50000, 25000]
})

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(sales_person, orders, on='sales_id', how='left')

    df = pd.merge(df1, company, on='com_id', how = 'left')

    mask = df["name_x"].isin(df.loc[df['name_y'] == "RED", "name_x"])

    df = df[~mask]

    df = df.drop_duplicates('name_x')

    df = df.rename(columns = {'name_x':'name'})

    return df[['name']]

# print(sales_person(sales_person, company, orders))

#### 570) Managers with at Least 5 Direct Reports

employees = pd.DataFrame({
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
    "department": ["A", "A", "A", "A", "A", "B"],
    "managerId": [None, 101, 101, 101, 101, 101]
})

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    group = employee.groupby(by = "managerId", as_index = False).count()
    mask = (group.department >= 5)
    higher = group[mask]

    final = pd.merge(employee, higher, left_on = "id", right_on = "managerId", how = "inner")

    final = final.rename(columns = {'name_x':'name'})

    return final[['name']]

# print(find_managers(employees))

#### 175) Combine Two Tables

import pandas as pd

person = pd.DataFrame({
    "personId": [1, 2],
    "lastName": ["Wang", "Alice"],
    "firstName": ["Allen", "Bob"]
})

address = pd.DataFrame({
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "Leetcode"],
    "state": ["New York", "California"]
})

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, on = 'personId', how = "left")

    df = df[['firstName', 'lastName', 'city', 'state']]

    return df

# print(combine_two_tables(person, address))

#### 180) Consecutive Numbers

logs = pd.DataFrame({
    "id":  [1,2,3,4,5,6,7],
    "num": [1,1,1,2,1,2,2]
})

# time complexity is O(n)
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    repeated_3 = []
    for i in range(len(logs.num)-2):
        if logs.num[i] == logs.num[i+1] == logs.num[i+2]:
            repeated_3.append(i)

    df = logs.iloc[repeated_3]

    df = df.rename(columns = {'num':'ConsecutiveNums'})

    df = df[['ConsecutiveNums']]

    df = df.drop_duplicates()

    return df

#### 181) Employees Earning More Than Their Managers

employee = pd.DataFrame({ "id": [1, 2, 3, 4],
                           "name": ["Joe", "Henry", "Sam", "Max"],
                           "salary": [70000, 80000, 60000, 90000],
                           "managerId": [3, 4, None, None]})

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, left_on='managerId', right_on='id', how='left', suffixes = ("", "_mgr"))

    mask = (df.salary > df.salary_mgr)
    df = df[mask]
    df = df[['name']]
    df = df.rename(columns = {'name':'Employee'})

    # can satacl columns like df = df[['name']].rename(columns = {'name':'Employee'})

    return df

#### 182) Duplicate Emails

person = pd.DataFrame({
    "id": [1, 2, 3],
    "email": ["a@b.com", "c@d.com", "a@b.com"]
})

# could brute force it by using a nested for loop O(n^2)

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    mask = person.duplicated(['email'])

    df = person[mask]

    df = df[['email']].rename(columns={'email': 'Email'})

    return df.drop_duplicates()

# print(duplicate_emails(person))

##### 185) Department Top Three Salaries

employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Joe", "Henry", "Sam", "Max", "Janet", "Randy", "Will"],
    "salary": [85000, 80000, 60000, 90000, 69000, 85000, 70000],
    "departmentId": [1, 2, 3, 1, 1, 1, 1]
})

department = pd.DataFrame({
    "id": [1, 2],
    "name": ["IT", "Sales"]
})


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))
    df['rnk'] = df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    result = df[df['rnk'] <= 3][['name_dept', 'name', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result

##### 197) Rising Temperature

weather = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "recordDate": ["2015-01-01", "2015-01-02", "2015-01-03", "2015-01-04"],
    "temperature": [10, 25, 20, 30]
})

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate').reset_index(drop=True)

    ids = []
    for i in range(len(weather) - 1):
        next_day = weather.loc[i, 'recordDate'] + pd.Timedelta(days=1)
        if weather.loc[i+1, 'recordDate'] == next_day:
            if weather.loc[i, 'temperature'] < weather.loc[i+1, 'temperature']:
                ids.append(weather.loc[i+1, 'id'])

    return pd.DataFrame({'id': ids})

#### 262) Trips and Users

trips = pd.DataFrame({
    "id": [1,2,3,4,5,6,7,8,9,10],
    "client_id": [1,2,3,4,1,2,3,2,3,4],
    "driver_id": [10,11,12,13,10,11,12,12,10,13],
    "city_id": [1,1,6,6,1,6,12,12,12,12],
    "status": [
        "completed", "cancelled_by_driver", "completed", "cancelled_by_client",
        "completed", "completed", "completed", "completed", "completed", "cancelled_by_driver"
    ],
    "request_at": [
        "2013-10-01","2013-10-01","2013-10-01","2013-10-01",
        "2013-10-02","2013-10-02","2013-10-02",
        "2013-10-03","2013-10-03","2013-10-03"
    ]
})

trips["request_at"] = pd.to_datetime(trips["request_at"])

users = pd.DataFrame({
    "users_id": [1,2,3,4,10,11,12,13],
    "banned": ["No","Yes","No","No","No","No","No","No"],
    "role": ["client","client","client","client","driver","driver","driver","driver"]
})

import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips["request_at"] = pd.to_datetime(trips["request_at"])
    in_between_mask = ((trips.request_at >= pd.to_datetime("2013-10-01")) &
                       (trips.request_at <= pd.to_datetime("2013-10-03")))

    if in_between_mask.any():

        mask = (users.role == "client")
        clients = users[mask]

        merged1 = pd.merge(trips, clients, left_on="client_id", right_on="users_id", how="left")
        mask = (users.role == "driver")
        drivers = users[mask]

        merged2 = pd.merge(merged1, drivers, left_on="driver_id", right_on="users_id", how="left",
                           suffixes=("_client", "_driver"))
        df = merged2.groupby(by="request_at").apply(
            lambda x: ((x["status"].str.startswith("cancelled")) & (x["banned_client"] == "No")).sum() / x[
                "banned_client"].str.startswith("No").sum()).rename("Cancellation Rate").reset_index()

        # if len(df) <= 1:
        #    return pd.DataFrame({"Day": [], "Cancellation Rate": []})

        df = df.rename(columns={"request_at": "Day"})

        df["Cancellation Rate"] = round(df["Cancellation Rate"], 2)

        return df

    else:
        df = pd.DataFrame({"Day": [], "Cancellation Rate": []})
        return df

##### 577) Employee Bonus

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, on = "empId", how = "left")

    mask = (df.bonus < 1000) | (pd.isnull(df.bonus))

    df = df[mask][['name', 'bonus']]

    return df

##### 584) Find Customer Referee

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer.referee_id != 2) | (pd.isnull(customer.referee_id))

    df = customer[mask][['name']]

    return df

#### 585) Investments in 2016

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    df = insurance

    df = df[df.groupby(by="tiv_2015")['tiv_2016'].transform("count").gt(1) &
    df.groupby(["lat", "lon"])["lat"].transform("count").eq(1)]

    df = df[['tiv_2016']]

    df = df.agg(total_tiv_2016=("tiv_2016", "sum"))

    return round(df, 2)


#### 1407) Top Travellers

users = pd.DataFrame({
    "id": [1, 2, 3, 19],
    "name": ["Alice", "Bob", "Alex", "Alice"]
})

rides = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 9],
    "user_id": [1, 2, 3, 7, 13, 7],
    "distance": [120, 317, 222, 100, 312, 230]
})

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(rides, left_on = "id", right_on = "user_id", how = "left").fillna(0)

    df = df.groupby(by = ["id_x", "name"], as_index = False)['distance'].sum()

    df = df.rename(columns = {"distance": "travelled_distance"})[['name', 'travelled_distance']]

    return df.sort_values(['travelled_distance', 'name'], ascending = [False, True])

### print(top_travellers(users, rides))

###### 619. Biggest Single Number

my_numbers = pd.DataFrame({
    "num": [8, 8, 3, 3, 1, 4, 5, 6]
})


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby(by="num", as_index=False).size()

    mask = (df['size'] == 1)

    if mask.any() == False:
        return pd.DataFrame({'num': [None]})

    else:
        df = df[mask][['num']]
        maximum = max(df.num, default=0)
        mask2 = (df.num == maximum)

        return df[mask2]

##### 1341. Movie Rating

# Movies table
movies = pd.DataFrame({
    "movie_id": [1, 2, 3],
    "title": ["Avengers", "Frozen 2", "Joker"]
})

# Users table
users = pd.DataFrame({
    "user_id": [1, 2, 3, 4],
    "name": ["Daniel", "Monica", "Maria", "James"]
})

# MovieRating table
ratings = pd.DataFrame({
    "movie_id": [1,1,1,1,2,2,3,3,3],
    "user_id":  [1,2,3,4,1,2,1,2,3],
    "rating":   [3,4,2,1,5,2,3,2,4],
    "created_at": pd.to_datetime([
        "2020-01-12","2020-02-11","2020-02-12","2020-01-01",
        "2020-02-17","2020-02-01","2020-03-01","2020-02-22","2020-02-25"
    ])
})

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    join1 = movie_rating.merge(movies, on = "movie_id", how = "left")
    join2 = join1.merge(users, on = "user_id", how = "left")

    # Greatest number of movies
    counted = join2.groupby(by = "name", as_index = False).size().sort_values(['size','name'], ascending = [False, True]).reset_index()

    # Highest average
    mask = join2['created_at'].dt.to_period("M") == "2020-02"
    feb = join2[mask]
    avg = feb.groupby(by = "title", as_index = False)['rating'].mean().sort_values(['rating', 'title'], ascending = [False, True]).reset_index()

    df = pd.DataFrame({"results": [counted['name'][0], avg['title'][0]]})

    return df

##### 620) Not Boring Movies

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    mask_bor = (cinema.description != "boring")
    mask_odd = (cinema.id % 2 == 1)

    df = cinema[mask_bor & mask_odd]

    df = df.sort_values('rating', ascending=False)

    return df

### 610 Triangle Judgement

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = 'No'

    for i in range(len(triangle)):
        if (
            triangle.loc[i, 'x'] + triangle.loc[i, 'y'] > triangle.loc[i, 'z'] and
            triangle.loc[i, 'x'] + triangle.loc[i, 'z'] > triangle.loc[i, 'y'] and
            triangle.loc[i, 'y'] + triangle.loc[i, 'z'] > triangle.loc[i, 'x']
        ):
            triangle.loc[i, 'triangle'] = 'Yes'

    return triangle

##### 550) Game Play Analysis IV

activity = pd.DataFrame({
    "player_id": [1, 1, 2, 3, 3],
    "device_id": [2, 2, 3, 1, 4],
    "event_date": [
        "2016-03-01",
        "2016-03-02",
        "2017-06-25",
        "2016-03-02",
        "2018-07-03"
    ],
    "games_played": [5, 6, 1, 0, 5]
})
activity["event_date"] = pd.to_datetime(activity["event_date"])

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    tot_players = activity.player_id.nunique()

    activity["start_date"] = activity.groupby(by = "player_id", as_index = False)["event_date"].transform("min")
    activity["diff"] = activity["event_date"] - activity["start_date"]
    mask = (activity["diff"] == "1 days")
    log_back = activity[mask]["player_id"].nunique()

    return pd.DataFrame({"fraction": [round(log_back/tot_players, 2)]})

### print(gameplay_analysis(activity))

#### 1327. List the Products Ordered in a Period

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    mask_feb = orders['order_date'].dt.to_period("M") == "2020-02"
    df = orders[mask_feb].groupby(by = "product_id", as_index = False)['unit'].sum()

    mask_100 = (df.unit >= 100)
    df = df[mask_100]

    df = df.merge(products , on = "product_id", how = "left")

    return df[['product_name', 'unit']]

#### 1068. Product Sales Analysis I

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on = "product_id", how = "left")

    df = df[['product_name', 'year', 'price']]

    return df

### 1075. Project Employees I