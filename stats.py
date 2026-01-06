def word_count(text):
  words = text.split()
  return len(words)

def frequency(text):
  frequency = {}
  letters = text.lower()
  for letter in letters:
    if letter in frequency:
      frequency[letter] += 1
    else:
      frequency[letter] = 1
  return frequency

def sort_on(dicti):
  return dicti["num"]

def sort(report_dict):
  report = []
  for ch in report_dict:
    entry = {
      "char": ch,
      "num": report_dict[ch],
    }
    report.append(entry)
  report.sort(reverse = True, key=sort_on)
  return report


  
    
