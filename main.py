import sys
from assignment import Assignment
from data import DataLoader

def main():
    
    data = DataLoader()
    
    data.load_data(sys.argv[1])

    conflicts = Assignment.conflicts

    for i in conflicts:
        print(i)

if __name__ == '__main__':
    main()