def reverse_string(s):
    return s[::-1]
  
def to_uppercase(s):
    return s.upper()
  
def to_lowercase(s):
    return s.lower()
  
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
  
def remove_spaces(s):
    return s.replace(" ", "")
  
def count_characters(s):
    return len(s)
