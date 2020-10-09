import os
import re

# Set up environment variables
base_dir = 'C:\\Users\\bkao0\\Documents\\GitHub\\data-engineering-coding-challenge'
data_dir = os.path.join(base_dir, 'dataset')
output_dir = os.path.join(base_dir, 'output')

logpath = os.path.join(output_dir,'logs.txt')
log_fp = open(logpath, "w+")

# Generate doc file list
doc_list = os.listdir(data_dir)
# Loop through all doc files
words_dict = {}
for doc in doc_list:
    filepath = os.path.join(data_dir, doc)
    total_lines = 0
    empty_lines = 0
    #print(filepath)
    log_fp.write('%s\n' % filepath)
    with open(filepath) as in_fp:
        line = in_fp.readline()
        while line:
            total_lines = total_lines + 1
            line = line.strip()
            #print('|{}|'.format(line))
            if line != '':
                #log_fp.write('%s\n' % line)
                words = re.sub("[^\w]", " ",  line).split()
                #words2 = re.split('; |, |\*|\n', line)
                for w in words:
                    if w == 's':
                        continue
                    if w.isdigit():
                        continue
                    if w in words_dict:
                        val = words_dict.get(w)
                        if int(doc) not in val:
                            val.append(int(doc))
                            words_dict[w] = val
                    else:
                        words_dict[w] = [int(doc)]
                #print('words = {}'.format(words))
                #print(words_dict)
                #log_fp.write('%s\n' % str(words))
                #log_fp.write('%s\n' % str(words_dict))
            else:
                empty_lines = empty_lines + 1
            #if total_lines == 10:
            #    break
            line = in_fp.readline()    
    in_fp.close()

    #print('filepath = {}, total_lines = {}, empty_lines = {}'.format(filepath, total_lines, empty_lines))
    log_fp.write('filepath = %s total_lines = %d, empty_lines = %d' % (filepath, total_lines, empty_lines))
log_fp.close()

# Write word dictionary to file in the format word, id of docs
outpath = os.path.join(output_dir,'words_dictionary')
out_fp = open(outpath, "w+") 
# Sort words_dict by key
sorted_words_dict = dict(sorted(words_dict.items()))
for k in list(sorted_words_dict.keys()):
    v = sorted_words_dict[k]
    new_v = sorted(v)     # sort list in words_dict value
    #sorted_words_dict[k] = new_v      # If sorted_words_dict will be referred later the value can be updated. Otherwise skip it.
    out_fp.write('%s %s\n' % (k, new_v))
out_fp.close()


