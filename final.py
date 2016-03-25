import codecs
import sys
import csv
import os

def find_unicodes():
	file = codecs.open("/home/akanksha/ocr/abc1.txt", "r", "utf-8")
	for line in file:
		for words in line:
			for characters in words:
				print (characters)	
				print (ord(characters))
				with open("uni_code.txt", "a") as uni_file:
					uni_file.write(str(ord(characters)))
					uni_file.write("\n")
	file.close()
	return

def compare_csv():
	with open("/home/akanksha/ocr/uni_code.txt", "r") as text:
		for line in text:
			with open('braille_array1.csv', 'r') as file:
				reader = csv.reader(file)
				array = [row[1] for row in reader if row[0].lstrip().rstrip() == line.lstrip().rstrip()]
	            	string = ','.join(array) 
	            	print string
	            	with open("br_array.txt", "a") as array_file:
					array_file.write(str(string))
					array_file.write(',')
	return
					
def truncate():
	with open("br_array1.txt", "a") as array_file:
		array_file.seek(-2, os.SEEK_END)
		array_file.truncate()
	return

find_unicodes()
compare_csv()
truncate