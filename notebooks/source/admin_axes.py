from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import dates
from pytz import common_timezones, all_timezones, timezone


tz_local = timezone('Europe/Dublin')

# requried for formating
def hours(x, pos):
    'The two args are the value and tick position'
    
    return '{:02d}:00'.format(int(x /3600))

def hours22(x, pos):
    'The two args are the value and tick position'
    
    return get_duration22(x)

def quarter_hours(x, pos):
    'The two args are the value and tick position'
    if x == 0:
        return ''
    elif x %  3600 == 0:
        return ''
    elif x %  1800 == 0:
        return '30'
    elif x  %  900 == 0:
        if x  %  3600  == 900:
            return '15'
        elif x  %  3600  == 2700:
            return '45'
        
def get_duration22(time_delta):
    hr = int(( time_delta )/3600) 
    minu = int ( ( ( time_delta )/3600 % 1 ) * 60) 
    sec = int ((( ( time_delta )/3600 % 1 ) * 60 % 1) * 60 ) 
    return "{:02}:{:02}:{:02}".format(hr,minu,sec)

#[ plot_control['axes_number'] ]

def wrap_axes(plot_axes_in):
    def new_plot_axes(df,  plot_control, axes):
        plot_axes_in( df,  plot_control, axes)  # old plot axes
        
        for label in axes.xaxis.get_ticklabels():
            label.set_rotation(0.0)
            label.set_horizontalalignment('center')
            label.set_color(plot_control['plot_color'])
        
        for label in axes.yaxis.get_ticklabels():
            label.set_color(plot_control['plot_color'])
        
        for tick in axes.xaxis.get_minor_ticks():
            tick.label.set_fontsize(7)
            tick.label.set_color(plot_control['plot_color'])

        axes.set_axis_bgcolor('linen')
        axes.set_title( plot_control['plot_title'], 
                                                  color= plot_control['plot_color'],
                                                 weight='normal',)
        axes.set_xlabel( plot_control['xlabel'], color= plot_control['plot_color'], )
        axes.set_ylabel( plot_control['ylabel'], color= plot_control['plot_color'],)
    
        if plot_control['ylimit_qty'] > 0:
            axes.set_ylim( 
                [ min( df[plot_control['column']][df[ plot_control['column']]>0 ] ) - plot_control['ylimit_qty'], 
                                            max(df[ plot_control['column'] ]) + plot_control['ylimit_qty'] ])
        
        if plot_control['show_avg']:
        
            if plot_control['column'] == 'speed':
                text_value_format = '{:.1f}'
                avg_value = df[df.moving == True ][plot_control['column']].mean()
            else:
                text_value_format = '{:.0f}'
                avg_value = df[df.moving == True ][plot_control['column']].median()
            
        
            max_value = df[ df.moving == True ][plot_control['column']].max()
        
            text_content = '{:<6}'.format('avg:') + text_value_format.format(avg_value) +\
                        ' ' + plot_control['units'] +   '\n' +\
                        '{:<6}'.format('max:') + text_value_format.format(max_value) +\
                        ' ' + plot_control['units']
            axes.axhline(avg_value, 
                        color= plot_control['plot_color'], ls = 'dotted')
            axes.text(.82, .07, text_content , family = 'monospace',
                style='normal', transform=axes.transAxes, color='white',
                bbox={'facecolor': plot_control['plot_color'] , 'color': plot_control['plot_color'] ,
                      'alpha':0.7, 'pad':5})
        
    return new_plot_axes
    
@wrap_axes
def plot_timeline( df, plot_control,axes ):

    df[ plot_control['column'] ].plot(ax=axes,  
                kind='area',color= plot_control['plot_color'] ,alpha = .7)    
    
    y_max = axes.get_ylim()[1]
    
    df[ 'breaks' ].apply(lambda y: y * y_max) .plot(ax=axes,  
                kind='area',color= 'lightgrey' ,alpha = 1.); 

    
    #format time labesl - show hour and minutes only
    axes.xaxis.set_major_locator( dates.MinuteLocator(byminute=0) )
    axes.xaxis.set_minor_locator( dates.MinuteLocator(byminute=[15,30 ,45]) )
    axes.xaxis.set_major_formatter(dates.DateFormatter('%H:%M', tz=tz_local))
    axes.xaxis.set_minor_formatter(dates.DateFormatter('%M', tz=tz_local))
    #axes[ plot_control['axes_number'] ].set_xlim((datetime(2015,9,13,6,0,0),datetime(2015,9,13,12,0,0 )))
    
    
def hours(x, pos):
    'The two args are the value and tick position'
    
    return '{:02d}:00'.format(int(x /3600))

def quarter_hours(x, pos):
    'The two args are the value and tick position'
    if x == 0:
        return ''
    elif x %  3600 == 0:
        return ''
    elif x %  1800 == 0:
        return '30'
    elif x  %  900 == 0:
        if x  %  3600  == 900:
            return '15'
        elif x  %  3600  == 2700:
            return '45'

@wrap_axes
def plot_time( df, plot_control,axes ):
    
    df[ plot_control['column'] ].plot(ax=axes,
                kind='area',color= plot_control['plot_color'] ,alpha = .7); 
    
    majorLocator   = MultipleLocator(3600)
    minorLocator   = MultipleLocator(900)
    formatter = FuncFormatter(hours)
    minor_formatter = FuncFormatter(quarter_hours)

    axes.xaxis.set_major_locator(majorLocator)
    axes.xaxis.set_minor_locator(minorLocator)
    axes.xaxis.set_minor_formatter(minor_formatter)
    axes.xaxis.set_major_formatter(formatter)

def kms(x, pos):
    'The two args are the value and tick position'
    return '{:.1f}'.format(x /1000)

@wrap_axes
def plot_distance( df, plot_control, axes ):
    
    df[ [ 'interval10', plot_control['column']]  ].groupby('interval10').mean().\
        plot(ax=axes,
        kind='area',color= plot_control['plot_color'] ,alpha = .7,
            legend=None); 
        
    formatter = FuncFormatter(kms)
    minorLocator   = MultipleLocator(5) 
    axes.xaxis.set_major_formatter(formatter)
    axes.xaxis.set_minor_formatter(formatter)