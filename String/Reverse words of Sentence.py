def reverseWords(sentence):
        reverse_char_list = sentence.split()
        reverse_char_list = reverse_char_list[::-1]
        string_word = ""
        for word in reverse_char_list:
            string_word += word
            string_word += " "
        return string_word.strip()

print(reverseWords('the sky is blue'))
#output : blue is sky the
