import argparse
from markov_gen import MarkovGenerate

parser = argparse.ArgumentParser(description = "Generate a random sentence.")
parser.add_argument("-filename", metavar = "F", type = str,
	help = "The training corpus.", required = True)
parser.add_argument("-order", type = int, help = "The order of the Markov generator to be built.", 
	default = 1)
parser.add_argument("-limit", type = int, help = "Length of the sentence to be formed", 
	default = 20)

if __name__ == "__main__":
	try:
		args = parser.parse_args()
		markov = MarkovGenerate(args.filename, args.order)
		print markov.generate(args.limit)
	except IOError:
		print "File not found or text in file is of an incorrect format."

