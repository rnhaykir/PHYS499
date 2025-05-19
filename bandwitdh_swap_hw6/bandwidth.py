def max_bandwidth(intervals):
    """
    l = start
    r = end
    b = bandwidth
    
    """
    events = []
    for (l, r, b) in intervals:
        events.append((l, b))
        events.append((r, -b))
    
    # Sort events by time - O(n log n)
    events.sort()
    
    current_band = 0
    max_band = 0
    max_time = 0
    
    for i in range(len(events)-1):
        time, change = events[i]
        next_time, _ = events[i+1]
        current_band += change
        
        if current_band >= max_band:
            max_band = current_band
            max_time = (time + next_time) / 2.0
            
            if i < len(events) - 1:
                next_time = events[i+1][0]
                if time < next_time:
                    max_time = (time + next_time) / 2.0
                else:
                    max_time = time
            else:
                max_time = time

    return max_time, max_band