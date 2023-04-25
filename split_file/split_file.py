import os
import time
start_time = time.time()
def split_file(file_path,save_path,lines_per_file = 500000):
    file_name = os.path.basename(file_path)
    file_name=file_name[0:-4]
    smallfile = None
    last_file_count=0
    i = 0
    with open(file_path) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = f'{save_path}/{file_name}_{i}.txt'
                i = i + 1
                smallfile = open(small_filename, "w")
            smallfile.write(line)

        if smallfile:
            smallfile.close()
    with open(small_filename, "r") as last_file:
        for line in last_file:
            last_file_count = last_file_count + 1
    record_count=(i)*lines_per_file+last_file_count
    print("--- %s seconds ---" % (time.time() - start_time))
    return record_count