from stack import Array_stack

def test_match_html (raw):
	""" Return True if all HTML tags are properly match : False otherwise. """
	
	S = Array_stack.ArrayStack()
	j = raw.find('<')

	while j != -1:
		k = raw.find('>', j+1)
		if k == -1:
			return False
		tag = raw[j+1 : k]
		if not tag.startswith('/'):
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if tag[1:] != S.pop():
				return False

		j = raw.find('<',k+1)

	return S.is_empty()

if __name__ == '__main__' :
	print (test_match_html('<html> <body> <center> <h1> The little Boat </h1> </center> </body> </html>'))

