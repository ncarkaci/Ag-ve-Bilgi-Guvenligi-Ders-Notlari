#-*-coding:utf-8-*-
input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

f = open('ngramtest.txt')
input = f.readline().split()
while input != "":
	#[s.strip().split() for s in data_string.splitlines()]
	input_list.append(f.readline().decode('utf-8').lower().split())
	print input_list
def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

#print find_ngrams(input_list,5)