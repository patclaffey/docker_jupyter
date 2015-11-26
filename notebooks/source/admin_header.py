from datetime import datetime, timedelta

def get_duration(time_delta):
    hr = int(( time_delta ).total_seconds()/3600) 
    minu = int ( ( ( time_delta ).total_seconds()/3600 % 1 ) * 60) 
    sec = int ((( ( time_delta ).total_seconds()/3600 % 1 ) * 60 % 1) * 60 ) 
    return "{:02}:{:02}:{:02}".format(hr,minu,sec)


def output_header(df, axes):
    
    if 'time' in df:
        start_time = df.time[0].to_datetime()
        end_time = df.time[-1].to_datetime()
    else:
        start_time = min(df.index)
        end_time = max(df.index)
        
    elapsed_time = end_time - start_time
    activity_time = timedelta( seconds= int( df.breaks[~df.breaks].count() ) )
    break_time = timedelta( seconds= int( df.breaks[df.breaks].count() ) )
    moving_time = timedelta( seconds= int( df.moving[df.moving].count() ) )
    non_moving_time = timedelta( seconds= int( df.moving[~df.moving].count() ) )

    distance = max(df.distance) - min(df.distance) 

    avg_speed_activity = (distance / activity_time.total_seconds()) * 3.6
    avg_speed_moving = (distance / moving_time.total_seconds()) * 3.6

    max_speed = df.speed.max()
    avg_speed = df.speed[~df.breaks].mean()

    max_heart_rate = df.heart_rate.max()
    avg_heart_rate = df.heart_rate[~df.breaks].median()

    max_cadence = df.cadence.max()
    avg_cadence = df.cadence[~df.breaks].median()

    start_day_date = datetime.strftime(start_time,'%A, %B %-d, %Y') 
    start_hr_min = datetime.strftime(start_time,'%H:%M' )
    end_hr_min = datetime.strftime(end_time,'%H:%M' )

    text_title = "Great Dublin Cycle - 100km Sportif"
    text_start_time = datetime.strftime(start_time,'%H:%M on %A, %B %-d, %Y') 
    text_headline_time = '{} to {} on {}'.format(start_hr_min, end_hr_min, start_day_date)
    text_elapsed_time = get_duration(elapsed_time)
    text_activity_time = get_duration(activity_time)
    text_break_time = get_duration(break_time)
    text_moving_time = get_duration(moving_time)
    text_distance = '{:.2f} km'.format( distance / 1000 )
    text_avg_speed_activity = '{:.1f} km/h'.format( avg_speed_activity )
    text_avg_moving_speed = '{:.1f} km/h'.format( avg_speed_moving )
    text_max_speed = '{:.1f} km/h'.format( max_speed ) 
    text_avg_heart_rate = '{:.0f} bpm'.format( avg_heart_rate )
    text_avg_cadence = '{:.0f} rpm'.format( avg_cadence )



    axes[0].set_axis_off()
    axes_a = axes[0]

    y_adjust = -.075
    axes_a.text(.5,.925 + y_adjust , text_title, fontsize=20, ha = 'center')
    axes_a.text(.5,.8 + y_adjust ,text_headline_time, fontsize=12, ha = 'center')


    axes_a.text(.15,.6 + y_adjust ,text_activity_time, fontsize=12, ha = 'center', weight='bold',)
    axes_a.text(.5,.6 + y_adjust ,text_avg_speed_activity, fontsize=12, ha = 'center', weight='bold',)
    axes_a.text(.85,.6 + y_adjust ,text_distance, fontsize=12, ha = 'center', weight='bold',)
    axes_a.text(.15,.525 + y_adjust ,'activity time', fontsize=8, ha = 'center', weight='bold',)
    axes_a.text(.5,.525 + y_adjust ,'avg speed', fontsize=8, ha = 'center', weight='bold',)
    axes_a.text(.85,.525 + y_adjust ,'distance', fontsize=8, ha = 'center', weight='bold',)

    axes_a.text(.15,.4 + y_adjust ,text_moving_time, fontsize=12, ha = 'center')
    axes_a.text(.5,.4 + y_adjust ,text_avg_moving_speed , fontsize=12, ha = 'center')
    axes_a.text(.85,.4 + y_adjust ,text_avg_heart_rate , fontsize=12, ha = 'center')
    axes_a.text(.15,.325 + y_adjust ,'moving time', fontsize=8, ha = 'center')
    axes_a.text(.5,.325 + y_adjust ,'avg moving speed', fontsize=8, ha = 'center')
    axes_a.text(.85,.325 + y_adjust ,'avg heart rate', fontsize=8, ha = 'center')

    axes_a.text(.15,.2 + y_adjust ,text_elapsed_time, fontsize=12, ha = 'center')
    axes_a.text(.5,.2 + y_adjust ,text_max_speed, fontsize=12, ha = 'center')
    axes_a.text(.85,.2 + y_adjust ,text_avg_cadence , fontsize=12, ha = 'center')
    axes_a.text(.15,.125 + y_adjust ,'elapsed time', fontsize=8, ha = 'center')
    axes_a.text(.5,.125 + y_adjust ,'max speed', fontsize=8, ha = 'center')
    axes_a.text(.85,.125 + y_adjust ,'avg cadence', fontsize=8, ha = 'center')
  

'''
print('{:<20}'.format('Start time:') + datetime.strftime(start_time,'%H:%M on %A, %B %-d, %Y') )
print('{:<20}'.format('End time:') + datetime.strftime(end_time,'%H:%M on %A, %B %-d, %Y') )
print('')

print ('{:<20}'.format('Elapsed time:') + '{}'.format( get_duration(elapsed_time) )   ) 
print ('{:<20}'.format('Distance:') + '{:.2f} km'.format( distance / 1000 )   ) 
print ('{:<20}'.format('Avg speed:') + '{:.1f} km/h'.format( avg_speed_activity )   ) 
print ('{:<20}'.format('Avg moving speed:') + '{:.1f} km/h'.format( avg_speed_moving )   ) 
print ('{:<20}'.format('Max speed:') + '{:.1f} km/h'.format( max_speed )   ) 
#print ('{:<20}'.format('Avg speed:') + '{:.1f} kph'.format( avg_speed )   ) 
print('')
print ('{:<20}'.format('Activity time:') + '{}'.format( get_duration(activity_time) )   ) 
print ('{:<20}'.format('Break time:') + '{}'.format( get_duration(break_time) )   ) 

print ('{:<20}'.format('Moving time:') + '{}'.format( get_duration(moving_time) )  )
print ('{:<20}'.format('Non-moving time:') + '{}'.format( get_duration(non_moving_time) )  )

print('')
print ('{:<20}'.format('Avg heart rate:') + '{:.0f} bpm'.format( avg_heart_rate )   ) 
print ('{:<20}'.format('Max heart rate:') + '{:.0f} bpm'.format( max_heart_rate )   ) 
print('')
print ('{:<20}'.format('Avg cadence:') + '{:.0f}'.format( avg_cadence )   ) 
print ('{:<20}'.format('Max cadence:') + '{:.0f}'.format( max_cadence )   ) 
'''
