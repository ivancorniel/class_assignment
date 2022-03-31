class Assignment:

    assignments = []
    conflicts = []

    def __init__(self, program, project, start_date, end_date, trainer, room):
        self.program = program
        self.project = project
        self.start_date = start_date
        self.end_date = end_date
        self.trainer = trainer
        self.room = room
        Assignment.assignments.append(self)
        self.find_conflicts()

    def find_conflicts(self):
        for i in Assignment.assignments:
            if self.program == i.program and self.project == i.project and self.start_date == i.start_date:
                if self.trainer == i.trainer:
                    if self.start_date < i.end_date and self.end_date >= i.start_date:
                        Assignment.conflicts.append(f'{self.trainer} assigned to {self.program} {self.project} {self.start_date} and  {i.program} {i.project} {i.start_date} in conflict')
                if self.room == i.room:
                    if self.start_date < i.end_date and self.end_date >= i.start_date:
                        Assignment.conflicts.append(f'{self.room} assigned to {self.program} {self.project} {self.start_date} and  {i.program} {i.project} {i.start_date} in conflict')

        return Assignment.assignments, Assignment.conflicts

    def __repr__(self) -> str:
        return self.program + ' ' + self.project + ' ' + self.start_date
