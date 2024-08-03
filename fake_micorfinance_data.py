import random as rd
import string as st
import pandas as pd
import numpy as np

max_lim = 15000
savings= [round(rd.random()*1500,2) for fig in range(max_lim)]
status = [rd.choice(['active','passive','active']) for i in range(max_lim)]
gender = [rd.choice(['W','M','M','W','W']) for i in range(max_lim)]

def age(max_lim, mini_age= 21, maxi_age = 51,mini = 1, maxi = 15):
    possible_ages = [e for e in range(mini_age,maxi_age,1)]
    possible_ages_count= len(possible_ages)
    while len(possible_ages) <= max_lim:
        for i in range(possible_ages_count):
            possible_ages = possible_ages + [possible_ages[i]]*rd.randint(mini,maxi)
    possible_ages = possible_ages[:max_lim]
    return possible_ages

def profession(max_lim,mini = 1, maxi = 15):
    profs = ['Prof','School Teacher', 'Student', 'Taxi Driver', 'Farmer', 'Barber', 'Student','Buyam Sellam','Business']
    profs_count= len(profs)
    while len(profs) <= max_lim:
        for i in range(profs_count):
            profs = profs + [profs[i]]*rd.randint(mini,maxi)
    profs = profs[:max_lim]
    return profs

def location(max_lim,mini = 1, maxi = 15):
    locs = ['Bamenda','Tiko', 'Buea', 'Limbe', 'Banso', 'Bali', 'Mutengene','Baffousam','Kumba', 'Bambili']
    locs_count= len(locs)
    while len(locs) <= max_lim:
        for i in range(locs_count):
            locs = locs + [locs[i]]*rd.randint(mini,maxi)
    locs = locs[:max_lim]
    return locs

def customer(id: int, max_lim, char_type = st.ascii_letters, mini = 1, maxi = 15, sample_size = 15) -> list:
    ref = set()
    join = ''.join
    ref_user = ref.add
    while len(ref) < max_lim:
        token = join(rd.choices(char_type, k = id))
        ref_user(token)
    all_ids = list(ref)
    referenced_users = rd.sample(all_ids,sample_size)
    referenced_users.append('None')
    referenced_users_count = len(referenced_users)
    while len(referenced_users) <= max_lim:
        for i in range(referenced_users_count):
            referenced_users = referenced_users + [referenced_users[i]]*rd.randint(mini,maxi)
    referenced_users = referenced_users[:max_lim]
    for i in range(max_lim):
        if referenced_users[i] == all_ids[i]:
            referenced_users[i] = 'None'
    return all_ids, referenced_users

def create_random_repetitive_dates(start_date, end_date, freq, max_lim, min_repeat, max_repeat):
    # Generate the initial sequence of dates
    date_range = pd.date_range(start=start_date, end=end_date, freq=freq)
    
    # Repeat each date a random number of times
    repeated_dates = []
    for date in date_range:
        repeat_count = np.random.randint(min_repeat, max_repeat + 1)
        repeated_dates.extend([date] * repeat_count)
    
    # Convert to a DataFrame
    repeated_dates = rd.choices(repeated_dates,k=max_lim)
    repeated_dates = [dates for dates in repeated_dates]
   
    return repeated_dates

# Parameters
start_date = '01.01.2023' #'2023-01-01'
end_date = '26.06.2024'  #2024-06-10'
frequency = 'D'  # Daily frequency
min_repeat = rd.randint(3,5)  
max_repeat = rd.randint(11,15) 

# Generate the random repetitive sequence of dates
random_repetitive_dates = create_random_repetitive_dates(start_date, end_date, frequency,max_lim, min_repeat, max_repeat)


customer = customer(id=6,max_lim=max_lim)
age = age(max_lim=max_lim)
profession = profession(max_lim=max_lim)
location = location(max_lim=max_lim)

customers = {"registration":random_repetitive_dates,"refered_users":customer[0],"referenced_users":customer[1],
             "gender":gender,"age":age, "profession":profession,"location":location,"status":status,"savings":savings}
customers = pd.DataFrame(customers)

file_path = 'customer_data.csv'
customers.to_csv(file_path, index=False)

print(f'DataFrame written to CSV file at: {file_path}') 

