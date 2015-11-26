#from admin_garmin import get_file_path
input_file = 'activity_898238015_30.csv'
output_file = 'activity_898238015_40.csv'




import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.ticker import FuncFormatter, MultipleLocator

import xml.etree.ElementTree as etree 
from datetime import datetime, timedelta
import os
import json
import pandas as pd
import numpy as np
from pytz import common_timezones, all_timezones, timezone





def get_file_path(file_name):
    input_dir = os.path.join("/", "opt","jupyter","data","csv" )
    input_file_path = os.path.join(input_dir , file_name)
    return input_file_path




input_file_path = get_file_path(input_file)
output_file_path = get_file_path(output_file)


# Load data file into a Pandas data frame for inspection
df = pd.read_csv(input_file_path, index_col = 'time',  parse_dates=True)

# Define and set data source time zone
tz_source = 'UTC'
# Set timezone in our data frame
df = df.tz_localize( tz_source )

# Convert to local time zone - Dublin, Ireland
tz_local = timezone('Europe/Dublin')
df = df.tz_convert(tz_local  )


df_moving = df[df.moving].copy()
df_moving = df_moving.reset_index()
df_moving['interval10'] = df_moving.distance.apply(lambda x: (int (x / 10) + 1) * 10 )


