import sys

from stats import word_count, frequency, sort
def get_book_text(path):
  with open(path) as f:
    return f.read()


if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
else: 
  path = sys.argv[1]

def main(path):
  text = get_book_text(path)
  wc = word_count(text)
  count = frequency(text)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}")
  print("----------- Word Count ----------")
  print(f"Found {wc} total words")
  print("--------- Character Count -------")
  for item in sort(count):
    ch = item["char"]
    val = item["num"]
    if ch.isalpha():
      print(f"{ch}: {val}")
  print("============= END ===============")

main(path)




