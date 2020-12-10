
def find_num_paths(right_path,left_path):
    if(right_path==0)or(left_path==0):
        return 1
        return find_num_paths(right_path -1, left_path)+ find_num_paths(right_path,left_path -1)
