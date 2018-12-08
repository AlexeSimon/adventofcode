# Advent of code Year 2018 Day 4 solution
# Author = Alexe Simon
# Date = December 2018

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_as_lines = input.split('\n')

# Represents a guard and its habits (id, total minutes slept, minutes prefered)
class Guard:
    def __init__(self, id):
        self.id = id
        self.minutes_scores = list(0 for i in range(60)) # minutes from 00:00 to 00:59
        self.sleep_time = 0
        
    def update_sleep_stats(self, record_entry, minute_passed):
        for i in range(record_entry.minute, record_entry.minute + minute_passed):
            self.minutes_scores[i] += 1

# Used to hold records, simulates a priority list (sort items when added in chronological order)  
class RecordList(list):
    def __init__(self):
        super(RecordEntry)
    
    def add_record_entry(self, record_entry):
        i = 0
        while (i < len(self) and self[i] < record_entry):
            i += 1
        self.insert(i, record_entry)
    
    def compute_time_asleep(self):
        guards = {} # directory for improved searched
        on_duty = self[0].id # current guard
        guards[on_duty] = Guard(on_duty)
        sleeping = False
        i = 0
        while i < len(self)-1:
            if sleeping: # if he was sleeping
                minute_passed = self[i].minute_passed(self[i+1]) # we compute how much he slept
                guards[on_duty].sleep_time += minute_passed # we add it to his total sleep time
                guards[on_duty].update_sleep_stats(self[i], minute_passed) # we update his favorite minutes to sleep
            if self[i+1].action == 0: # change of guard
                on_duty = self[i+1].id
                sleeping = False
                if on_duty not in guards:
                    guards[on_duty] = Guard(on_duty)
            elif self[i+1].action == 1: # falls asleep
                sleeping = True
            else: # wakes up
                sleeping = False
            i += 1
        return guards

# Represents a record (year, month, ...)
class RecordEntry:
    def __init__(self, year, month, day, hour, minute, action):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        if action == "falls asleep":
            self.action = 1
            self.id = None
        elif action == "wakes up":
            self.action = 2
            self.id = None
        else:
            self.action = 0
            self.id = int(action[action.find("#")+1:action.rfind("begins")])
            
    def __lt__(self, other):
        if not self.year == other.year:
            return self.year < other.year
        if not self.month == other.month:
            return self.month < other.month
        if not self.day == other.day:
            return self.day < other.day
        if not self.hour == other.hour:
            return self.hour < other.hour
        if not self.minute == other.minute:
            return self.minute < other.minute
        return False
    
    def minute_passed(self, other):
        return other.minute - self.minute # This is a little hack : we know guards only sleep between 00:00 and 00:59 so we can simply substract them
    
    def __str__(self):
        return('[{0:4d}-{1:2d}-{2:2d} {3:2d}:{4:2d}] {5} started  action {6}'.format(self.year, self.month, self.day, self.hour, self.minute, self.id, self.action))
        
        
# We define actions as follow :
#   0 : begins shift (is awake)
#   1 : falls asleep
#   2 : wakes up

records = RecordList()
for line in input_as_lines:
    match = re.match("\[(?P<year>.+)\-(?P<month>.+)\-(?P<day>.+) (?P<hour>.+):(?P<minute>.+)\] (?P<action>.+)", line)
    records.add_record_entry(RecordEntry(int(match.group("year")), int(match.group("month")), int(match.group("day")), int(match.group("hour")), int(match.group("minute")), match.group("action")))

# if you want to print sorted records:
# with open((__file__.rstrip("code.py")+"output.txt"), 'w+') as output_file:
    # for record in records:
        # output_file.write(str(record)+"\n")

guards = list(records.compute_time_asleep().values())

# from here on everything is computed, and we simply search for the two guard*min combination

def get_max_index(list):
    best = list[0]
    best_index = 0
    for i in range(1, len(list)):
        if best < list[i]:
            best = list[i]
            best_index = i
    return best_index

best_sleeper_index = get_max_index([guard.sleep_time for guard in guards])
best_sleeper_minute = get_max_index(guards[best_sleeper_index].minutes_scores)

print("Part One : "+ str(best_sleeper_minute*guards[best_sleeper_index].id))

constant_sleeper_index = get_max_index([max(guard.minutes_scores) for guard in guards])
constant_sleeper_minute = get_max_index(guards[constant_sleeper_index].minutes_scores)

print("Part Two : "+ str(constant_sleeper_minute*guards[constant_sleeper_index].id))