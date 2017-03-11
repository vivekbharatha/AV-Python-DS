import sys
import re

def extract_names(filename):
	result = []
	file_ = open(filename, 'rU')
	fileText = file_.read()
	yearM = re.search(r'Popularity\sin\s(\d\d\d\d)', fileText)

	if not yearM:
		print("Couldn't find year")
		sys.exit(1)

	year = yearM.group(1)
	result.append(year)

	rankndNames = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fileText)
	namesRank = {}

	for v in rankndNames:
		(rank, male, female) = v
		if male not in namesRank:
			namesRank[male] = rank
		if female not in namesRank:
			namesRank[female] = rank

	sortedNames = sorted(namesRank.keys())
	for name in sortedNames:
		result.append(name + " " + namesRank[name])

	return result

def main():
	args = sys.argv[1:]

	if not args:
		print("usage: [--summaryfile] file [file ...]")
		sys.exit(1)	

	# Notice the summary flag and remove it from args if it is present.
	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]

	for fName in args:
		print(fName)
		result = extract_names(fName)
		result = "\n".join(result)
		print(result)

if __name__ == '__main__':
	main()
