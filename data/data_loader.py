import csv
from assignment import Assignment


class DataLoader:

    def __init__(self):
        pass

    def load_data(self, data):

        # assignments = []
        
        with open(data, 'r') as file:
            classes = csv.DictReader(file)

            for line in classes:
                Assignment.assignments.append(Assignment(line['program'], line['project'], line['start_date'], line['end_date'], line['trainer'], line['room']))
        
        # return assignments