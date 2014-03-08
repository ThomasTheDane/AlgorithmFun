def checkFermat(a,b,c,n):
	if (a**n) + (b**n) == c**n and n > 2:
		print "holy smokes, Fermat was wrong"
	else:
		print "No, that doesn't work"

def checkIfHasTrippleLetter(word):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for aLetter in alphabet:
		if (aLetter.lower()*3) in word:
			print word

def findTrippleLetterWords():
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		checkIfHasTrippleLetter(word)

def exercise53():
	checkFermat(2,2,2,2)

def exercise97():
	findTrippleLetterWords()

def main():
#	exercise53()
	exercise97()

if __name__ == '__main__':
	main()