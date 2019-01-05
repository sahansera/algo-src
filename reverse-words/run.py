'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

'''
def reverse_words(s):
	str_arr = s.split()
	str_out = ''
	for str in str_arr:
		str_out = str_out + "".join(reversed(str))
		str_out = str_out + ' '
	print(str_out[1:len(str_out)-1])

reverse_words('Let\'s take LeetCode contest')
