# encoding: utf-8
import glob
import os
f2 = open("ft2 — копия 9.txt", "a")
#import glob
for lst_dir in glob.glob('./hw1/*.txt'):
	lfile = open(lst_dir, 'r')
	lfile = lfile.read()
	c_lf=lfile.count("python")
	c_lf=str(c_lf)
	print(lst_dir)
	print(c_lf)
	f2.write(c_lf)
f2.close()
