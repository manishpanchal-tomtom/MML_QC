import os
from DB import mml_ext

# User parameters #
country = 'IND'
project_name = 'TBTRestrMSFT'
start_date = '2021-09-15'
end_date = '2021-09-16'

# Calling MML_DB function to get data
data = mml_ext(country, project_name, start_date, end_date)

print(data)
