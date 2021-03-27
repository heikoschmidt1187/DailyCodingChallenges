#!/bin/bash
"""
Given an array of time intervals (start, end) for classroom lectures (possibly 
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from queue import PriorityQueue

def min_rooms(intervals):
    length = len(intervals)

    # edge cases
    if length == 0:
        return 0

    # only one meeting fits one room
    if length == 1:
        return 1
    
    # sort by start time
    for i in range(0, length - 1, 1):
        if intervals[i][0] > intervals[i+1][0]:
            intervals[i], intervals[i+1] = intervals[i+1], intervals[i]

    # calculate rooms
    rooms = 1
    q = PriorityQueue(maxsize=length)
    q.put(intervals[0][1])
    
    for i in range(1, length, 1):
        temp = q.get()
        q.put(temp)

        if intervals[i][0] < temp:
            rooms += 1
        else:
            q.get()

        q.put(intervals[i][1])

    return rooms

if __name__ == '__main__':
    intervals = [(30, 75), (0, 50), (60, 150)]
    print('Rooms: ', min_rooms(intervals))