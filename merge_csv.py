import csv
def merge_csv(csv_list, output_path):
	#list of all field names
	fieldnames = list()
	for file in csv_list:
		with open(file, 'r') as input_csv:
			fn = csv.DictReader(input_csv).filenames
			fieldnames.extend(x for x in fn if x not in fieldnames)
			
	with open(output_path, 'w', newline ='') as output csv:
		writer = csv.DictWriter(output_csv, fieldnames = fieldnames)
		writer.writerheader()
		for file in csv_list:
			with open(fil, 'r') as input_csv:
				reader = csv.DictReader(input_csv)
				for row in reader:
					writer.writerow(row)
