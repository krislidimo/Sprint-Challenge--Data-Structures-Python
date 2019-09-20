import time

start_time = time.time()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Sorting one of the name arrays using dictionaries
# {a: [Alice, Alex ...]
#  b: [Bob ...........]
#  c: [...............]}
sorted_names_2 = {letter:[] for letter in alphabet}
for letter in sorted_names_2:
	sorted_names_2[letter] = [name for name in names_1 if letter == name[0].lower()]

duplicates = []
for name_1 in names_1:
  first_letter = name_1[0].lower()
  # Search is narrowed based on first_letter of the name
  if name_1 in sorted_names_2[first_letter]:
    duplicates.append(name_1)

  # for name_2 in sorted_names_2[first_letter]:
  #   if name_1 == name_2:
  #     duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print('done')

# Original implementation: O(n^2)
# New implementation: O(n log n)