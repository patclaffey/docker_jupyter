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


def get_plot_controls(activity_variable, **kwargs):
    
    if activity_variable == 'heart_rate':
        activity_column = activity_variable
        activity_title = kwargs['activity_title'] if 'activity_title' in kwargs else 'Heart Rate'
        activity_color = kwargs['activity_color'] if 'activity_color' in kwargs else 'red'
        activity_ylimit_qty = kwargs['activity_ylimit_qty'] if 'activity_ylimit_qty' in kwargs else 10
        activity_units = kwargs['activity_units'] if 'activity_units' in kwargs else 'bpm'
        activity_xlabel = kwargs['activity_xlabel'] if 'activity_xlabel' in kwargs else  ''
        activity_ylabel = kwargs['activity_ylabel'] if 'activity_ylabel' in kwargs else 'Beats per Minute'
        activity_show_avg = kwargs['activity_show_avg'] if 'activity_show_avg' in kwargs else True
    elif activity_variable == 'speed':
        activity_column = activity_variable
        activity_title = kwargs['activity_title'] if 'activity_title' in kwargs else 'Speed'
        activity_color = kwargs['activity_color'] if 'activity_color' in kwargs else 'blue'
        activity_ylimit_qty = kwargs['activity_ylimit_qty'] if 'activity_ylimit_qty' in kwargs else 0
        activity_units = kwargs['activity_units'] if 'activity_units' in kwargs else 'km/h'
        activity_xlabel = kwargs['activity_xlabel'] if 'activity_xlabel' in kwargs else  ''
        activity_ylabel = kwargs['activity_ylabel'] if 'activity_ylabel' in kwargs else 'Kilometers per Hour'
        activity_show_avg = kwargs['activity_show_avg'] if 'activity_show_avg' in kwargs else True
    elif activity_variable == 'cadence':
        activity_column = activity_variable
        activity_title = kwargs['activity_title'] if 'activity_title' in kwargs else 'Cadence'
        activity_color = kwargs['activity_color'] if 'activity_color' in kwargs else 'black'
        activity_ylimit_qty = kwargs['activity_ylimit_qty'] if 'activity_ylimit_qty' in kwargs else 0
        activity_units = kwargs['activity_units'] if 'activity_units' in kwargs else 'rpm'
        activity_xlabel = kwargs['activity_xlabel'] if 'activity_xlabel' in kwargs else  ''
        activity_ylabel = kwargs['activity_ylabel'] if 'activity_ylabel' in kwargs else 'Revolutions per Minute'
        activity_show_avg = kwargs['activity_show_avg'] if 'activity_show_avg' in kwargs else True
    elif activity_variable == 'altitude':
        activity_column = activity_variable
        activity_title = kwargs['activity_title'] if 'activity_title' in kwargs else 'Altitude'
        activity_color = kwargs['activity_color'] if 'activity_color' in kwargs else 'green'
        activity_ylimit_qty = kwargs['activity_ylimit_qty'] if 'activity_ylimit_qty' in kwargs else 10
        activity_units = kwargs['activity_units'] if 'activity_units' in kwargs else 'metres'
        activity_xlabel = kwargs['activity_xlabel'] if 'activity_xlabel' in kwargs else  ''
        activity_ylabel = kwargs['activity_ylabel'] if 'activity_ylabel' in kwargs else 'Metres'
        activity_show_avg = kwargs['activity_show_avg'] if 'activity_show_avg' in kwargs else False
    
        
    plot_control = {'column':activity_column,  'plot_color':activity_color, 'show_avg': activity_show_avg,
                'units':activity_units, 'plot_title':activity_title, 'xlabel': activity_xlabel,
                'ylabel':activity_ylabel, 'ylimit_qty':activity_ylimit_qty}
    
    
    return plot_control


