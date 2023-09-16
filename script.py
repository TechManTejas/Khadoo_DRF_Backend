import sys
from utilities.resetproject import resetproject
from utilities.resetprojectwithsampledata import resetprojectwithsampledata

# Commands 
reset_project = 'resetproject'
reset_project_with_sample_data = 'resetproject-sampledata'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py", "[", reset_project, "|", reset_project_with_sample_data, "]")
    else:
        command = sys.argv[1]
        if command == reset_project:
            resetproject()
        elif command == reset_project_with_sample_data:
            resetprojectwithsampledata()
        else:
            print("Invalid command. Use", reset_project, "or", reset_project_with_sample_data)
