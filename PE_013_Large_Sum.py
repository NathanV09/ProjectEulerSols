def get_sum(filename):
    with open(filename) as f:
        tot_sum=0
        for line in f:
            line=int(line)
            tot_sum+=line
    return tot_sum
print get_sum("PE_013_Data.txt")