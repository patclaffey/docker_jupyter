
from admin_garmin import *
from admin_axes import *
from admin_header import *
from admin_segments import *

# full activity level
sum_metrics = get_metrics(df,"Summary")

def summary_view(view_type):
    
    if view_type in ['time','distance']:
        df_name = df_moving
    else:
        df_name = df
        
    view_description, view_xlabel, view_procedure, view_units = get_view_properties(view_type)

    fig, axes = plt.subplots(nrows=5, ncols=1,  figsize=(14, 16))

    create_header(axes[0], sum_metrics, "Summary Level - Great Dublin Cycle, 100km Sportif", view_description)

    plot_control = get_plot_controls('speed',activity_xlabel = '')
    view_procedure(df_name, plot_control, axes[1])

    plot_control = get_plot_controls('heart_rate',activity_xlabel = '')
    view_procedure(df_name, plot_control, axes[2])

    plot_control = get_plot_controls('altitude',activity_xlabel = '')
    view_procedure(df_name, plot_control, axes[3])

    plot_control = get_plot_controls('cadence',activity_xlabel = view_xlabel)
    view_procedure(df_name, plot_control, axes[4])

    fig.savefig('summary.png', bbox_inches='tight')


sub = create_segments(df)
session_metrics = []
session_metrics.append(get_metrics(sub[0],"Session 1 - Clontarf to SmithField"))
session_metrics.append(get_metrics(sub[1],"Session 2 - Smithfield to Garristown"))
session_metrics.append(get_metrics(sub[2],"Session 3 - Garristown to Smithfield"))


def session_overview(view_type, column_name):
    view_description, view_xlabel, view_procedure, view_units = get_view_properties(view_type)
        
    fig, axes = plt.subplots(nrows=6, ncols=1,  figsize=(14, 21))

    #Speed over distance for sub-activity 1

    create_header(axes[0], session_metrics[0], session_metrics[0]['title'], view_description)
    plot_control = get_plot_controls(column_name, 
                                 activity_xlabel = view_xlabel,)
    view_procedure(sub[0], plot_control, axes[1])

    #Speed over distance for sub-activity 2

    create_header(axes[2], session_metrics[1], session_metrics[1]['title'], view_description)
    plot_control = get_plot_controls(column_name, 
                                 activity_xlabel = view_xlabel,)
    view_procedure(sub[1], plot_control, axes[3])

    #Speed over distance for sub-activity 3

    create_header(axes[4], session_metrics[2], session_metrics[2]['title'], view_description)
    plot_control = get_plot_controls(column_name, 
                                 activity_xlabel = view_xlabel,)
    view_procedure(sub[2], plot_control, axes[5])
  

def session_detail(view_type, session_num):    
    view_description, view_xlabel, view_procedure, view_units = get_view_properties(view_type)

    fig, axes = plt.subplots(nrows=5, ncols=1,  figsize=(14, 20))
    sub_activity_number =  session_num - 1

    create_header(axes[0], session_metrics[sub_activity_number], 
              session_metrics[sub_activity_number]['title'], view_description)

    plot_control = get_plot_controls('speed',activity_xlabel = '')
    view_procedure(sub[sub_activity_number], plot_control, axes[1])

    plot_control = get_plot_controls('heart_rate',activity_xlabel = '')
    view_procedure(sub[sub_activity_number], plot_control, axes[2])

    plot_control = get_plot_controls('altitude',activity_xlabel = '')
    view_procedure(sub[sub_activity_number], plot_control, axes[3])

    plot_control = get_plot_controls('cadence',activity_xlabel = view_xlabel)
    view_procedure(sub[sub_activity_number], plot_control, axes[4])
    
def detail_heading(start_distance, end_distance, title, units):
    return 'Zoom {} to {}{} - {}'.format(start_distance, end_distance,units, title)


def session_zoom(view_type, session_num, start_distance, end_distance):
    
    view_description, view_xlabel, view_procedure, view_units = get_view_properties(view_type)
    sub_activity_number = session_num - 1

    session_title = session_metrics[sub_activity_number]['title']
    detail_title = detail_heading(start_distance, end_distance, session_title, view_units)


    df_seg = sub[sub_activity_number]

    if view_type == 'distance':
        df_seg =  df_seg[((df_seg.distance > start_distance*1000) & (df_seg.distance < end_distance*1000))]
    elif view_type == 'time':
        df_seg = df_seg[int(start_distance*60.0): int(end_distance*60.0)]

    fig, axes = plt.subplots(nrows=5, ncols=1,  figsize=(14, 16))

    ses_metrics = get_metrics(df_seg,detail_title)

    create_header(axes[0], ses_metrics, ses_metrics['title'],view_description)

    plot_control = get_plot_controls('speed',activity_xlabel = '', activity_ylimit_qty=5)
    view_procedure(df_seg, plot_control, axes[1])

    plot_control = get_plot_controls('heart_rate',activity_xlabel = '')
    view_procedure(df_seg, plot_control, axes[2])

    plot_control = get_plot_controls('altitude',activity_xlabel = '')
    view_procedure(df_seg, plot_control, axes[3])

    plot_control = get_plot_controls('cadence',activity_xlabel = view_xlabel)
    view_procedure(df_seg, plot_control, axes[4])
    
    
def gen_list(start, end, div,view_type):
    
    if view_type == 'distance':
        multiplier = 1000
    elif view_type == 'time':
        multiplier = 60
        
    step = (end - start)* multiplier  /div
    for i in range(div):
        from_value = start*multiplier + i * step 
        to_value = start*multiplier +  i * step + step
        
        if view_type == 'time':
            yield (int(from_value), int(to_value) )
        else:
            yield (from_value, to_value)
        #yield (start*multiplier + i * step, start*multiplier +  i * step + step)
        

def get_list(start, end, div, view_type):
    list_dist = []
    for i in gen_list(start, end, div,view_type):
        list_dist.append(i)
    return list_dist


def session_detail_zoom(view_type, session_num, column_name, start_distance, end_distance, divs):
    view_description, view_xlabel, view_procedure, view_units = get_view_properties(view_type)
    sub_activity_number = session_num - 1

    session_title = session_metrics[sub_activity_number]['title']
    detail_title = detail_heading(start_distance, end_distance, session_title, view_units)


    df_seg = sub[sub_activity_number]

    if view_type == 'distance':
        df_seg =  df_seg[((df_seg.distance > start_distance*1000) & (df_seg.distance < end_distance*1000))]
    #elif view_type == 'time':
    #    df_seg = df_seg[int(start_distance*60.0): int(end_distance*60.0)]

    if view_type == 'time':
        ses_metrics = get_metrics(df_seg[int(start_distance*60.0): int(end_distance*60.0)],detail_title)
    else:
        ses_metrics = get_metrics(df_seg,detail_title)

    list_dist = get_list(start_distance , end_distance, divs, view_type)
    plot_qty = len(list_dist)

    fig, axes = plt.subplots(nrows= plot_qty+1, ncols=1,  figsize=(14, 16))
    create_header(axes[0], ses_metrics, ses_metrics['title'],view_description)

    plot_control = get_plot_controls( column_name ,activity_xlabel = '', activity_ylimit_qty=5)
    #view_procedure(df_seg, plot_control, axes[1])
    for plot_num in range( 0, plot_qty ):
        if view_type == 'distance':
            plot_distance(df_seg[((df_seg.distance > list_dist[plot_num][0]) & (df_seg.distance < list_dist[plot_num][1]))]
             , plot_control, axes[plot_num + 1])
        elif view_type == 'time':
            plot_time( df_seg[ list_dist[plot_num][0]: list_dist[plot_num][1] ], plot_control, axes[plot_num + 1])
