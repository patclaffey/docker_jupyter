def define_segments(df):
    initial_value = df.iloc[:1].breaks.values[0]
    last_value = initial_value
    start_loc = 0
    
    for loc, val in enumerate(df.breaks):
        if val != last_value:
            #print('value of iloc is ' + str(loc))
            
            yield (start_loc,loc - 1,last_value)
            last_value = val
            start_loc = loc
    yield (start_loc,loc, val)
    
    



def create_segments(df):
    seg = []
    for i in define_segments(df):
        if ~i[2]:
            df_seg = df.iloc[i[0]:i[1]+1].copy()
            df_seg = df_seg.reset_index()
            initial_distance = df_seg.iloc[0:1].distance.values[0]
            df_seg['distance'] = df_seg.distance.apply(lambda x: x - initial_distance)
            df_seg['interval10'] = df_seg.distance.apply(lambda x: (int (x / 10) + 1) * 10 )
            seg.append(df_seg)
    return seg
