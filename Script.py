# %%
pip install randomuser

# %%
from randomuser import RandomUser

# %%
pip install pandas

# %%
from randomuser import RandomUser
from pandas import pandas
r = RandomUser()
some_list = r.generate_users(10)
some_list

name = r.get_full_name()
for user in some_list:
    print (user.get_full_name()," ",user.get_email(), user.get_nat(), user.get_picture())

# %%
from randomuser import RandomUser
from pandas import pandas
r = RandomUser()
some_list = r.generate_users(10)
some_list

name = r.get_full_name()

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pandas.DataFrame(users) 

get_users()
df1 = pandas.DataFrame(get_users())      


