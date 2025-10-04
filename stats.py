def get_num_words(book):
  words = book.split()
  return len(words)

def get_num_chars(book):
  lowercase_book = book.lower()
  chars = {}
  for char in lowercase_book:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1

  return chars

def get_sorted_num_chars(chars_dict):
  chars_list = []
  for char in chars_dict:
    if char.isalpha():
      chars_list.append({ "char": char, "num": chars_dict[char] })
  def sort_on(items):
    return items['num']
  chars_list.sort(reverse=True, key=sort_on)
  return chars_list