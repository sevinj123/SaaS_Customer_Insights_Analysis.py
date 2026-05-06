# 1.#"Imagine your Excel file has some empty cells (e.g., missing car mileage). 
# # In this case, the program may throw an error when running calculations".
# import pandas as pd
# df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
# #print(df.isnull().sum().sum()) #the second sum() is summarizing how many index are there
# #print(df.isnull().sum())
# #if I want to fill empty rows, i should use fillna()/ we can use words inside of () to add something
# df['Support_Tickets'] = df['Support_Tickets'].fillna(2)
# print(df)



# #2. To avoid misleading results, we fill missing login days with the average instead of zero.
# # This ensures that empty cells don't skew our analysis by showing "0 days" (logged in today).
# import pandas as pd
# df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
# df['Last_Login_Days'] = df['Last_Login_Days'].fillna(df['Last_Login_Days'].mean())
# print(df)



# #3. if I want to filter my customers, how royal they are/ than...
# import pandas as pd
# df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
# def monthly_fee(fee):
#     if fee > 70.99:
#         return 'Loyal Customer'
#     elif fee > 50:
#         return 'Medium Customer'
#     else:
#         return 'Low Customer'
# print(df['Monthly_Fee'].apply(monthly_fee)) #this is apply(monthly_fee) - the name of function




# #4. # Filtering users who are on the Premium plan AND have more than 3 support tickets
# # to offer them a special discount for customer retention.
# import pandas as pd
# df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
# customers=df[(df['Plan_Type'] == 'Premium') & (df['Support_Tickets'] >= 3)]
# print(customers)



# #5. "Show the average amount paid by both 'Active' and 'Churned' "
# #"customers in each country in a single table."
# import pandas as pd
# df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
# customers=df.groupby('Status')['Monthly_Fee'].mean()
# print(customers)
#if I want to write this code by using PIVOT Table

import pandas as pd
df=pd.read_excel('Python-pandas/SaaS-Metrics.xlsx')
#report = df.pivot_table( index = 'Status' , values = 'Monthly_Fee' , aggfunc='mean') # if i want to see countries
#report = df.pivot_table(index = 'Country' , columns = 'Status' , values = 'Monthly_Fee', aggfunc = ['mean' , 'count']) #there some NAN function are ready to remove so..
report = df.pivot_table(index = 'Country' , columns = 'Status' , values = 'Monthly_Fee', aggfunc = ['mean' , 'count'])
#print(report) if i want to add them to new excel
report.to_excel('Python-pandas/SaaS-Metrics_analys.xlsx')