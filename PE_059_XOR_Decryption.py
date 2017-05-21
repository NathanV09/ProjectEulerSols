import _csv
with open("PE_59_Data.txt",'r') as f:
    data=list(_csv.reader(f, delimiter=","))
