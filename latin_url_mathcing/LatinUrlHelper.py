import unicodedata
import re
class LatinUrlHelper:

    def __init__(self, options):
        self.options = options
        self.alphanum_pattern = re.compile('[a-zA-Z0-9]')

    def match(self, text):
        a = self.get_only_alphanumerics(text)
        for key in self.options:
            if self.get_only_alphanumerics(key) == a:
                return key
        
    def build_url(self, text, keep_char_at = [], separator='-', to_ascii=False, lowercase=False):
        result = ''
        last_char_alphanum = False
        i = 0
        for char in text:
            if i in keep_char_at:
                if lowercase:
                    char = char.lower()
                result += char    
            elif separator and last_char_alphanum and (char == ' ' or char == '-'):
                result += separator
                last_char_alphanum = False
            elif char.isalnum():
                last_char_alphanum = True
                if 128 < ord(char) and to_ascii:
                    char = unicodedata.normalize('NFD', char)[0]
                if lowercase:
                    char = char.lower()
                result += char  
            i += 1
        return result

    def get_only_alphanumerics(self, text):
        result = ''
        for char in text:
            if char.isalnum():
                if ord(char) < 128:
                    result += char.lower()
                else:
                    result += unicodedata.normalize('NFD', char)[0].lower()
            
        return result