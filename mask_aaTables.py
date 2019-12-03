from sys import argv
import os

aaCount_dir = argv[1]
min_count_cutoff = argv[2]
position_mapping_file_name = argv[3]


zero_list = []
keep_list = []
nMA_pos_list = []

for file in os.listdir(aaCount_dir):
	if(file.endswith('_aaCount_table.txt')):
		for i, l in enumerate(open(aaCount_dir + '/' + file, 'U')):
			if i > 0:
				l = l.split('\t')
				pos = l[0]
				tmp_freq_list = l[3:]
				tmp_freq_list = [int(x) for x in tmp_freq_list]
				if(sum(tmp_freq_list) < int(min_count_cutoff)):
					zero_list.append(pos)
				else:
					keep_list.append(pos)

for file in os.listdir(aaCount_dir):
	if(file.endswith('_aaCount_table.txt')):
		sample_name = file.split('_aaCount_table.txt')[0]
		
		masked_aaCount_table = open(sample_name + '_masked_aaCount_table.txt', 'w')
		pos_counter = 0
		for i,l in enumerate(open(aaCount_dir + '/' + file, 'U')):
			if i == 0:
				masked_aaCount_table.write(l)
				masked_aaCount_table.write('\n')
			elif i > 0:
				split_l = l.split('\t')
				pos = split_l[0]
				if pos in keep_list:
					pos_counter += 1
					nMA_pos_list.append(i)
					out_line = pos + '\t' + '\t'.join(split_l[1:])
					masked_aaCount_table.write(str(pos_counter) + '\t' + '\t'.join(split_l[1:]))
		masked_aaCount_table.close()

for file in os.listdir(aaCount_dir):
	if(file.endswith('_aaFreq_table.txt')):
		sample_name = file.split('_aaFreq_table.txt')[0]
		masked_aaFreq_table = open(sample_name + '_masked_aaFreq_table.txt', 'w')
		pos_counter = 0
		for i,l in enumerate(open(aaCount_dir + '/' + file, 'U')):
			if i == 0:
				masked_aaFreq_table.write(l + '\n')
			elif i > 0:
				split_l = l.split('\t')
				pos = split_l[0]
				if pos in keep_list:
					pos_counter += 1
					masked_aaFreq_table.write(str(pos_counter) + '\t' + '\t'.join(split_l[1:]))
		masked_aaFreq_table.close()



mapping_out = open(position_mapping_file_name, 'w')
mapping_out.write('nMA_position\trenumbered_position\n')

for i,pos in enumerate(keep_list):
	mapping_out.write(pos + '\t' + str(i + 1) + '\n')
mapping_out.close()
		
					
				


