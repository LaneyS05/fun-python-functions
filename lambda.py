school = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_school = sorted(school, key = lambda x: x[1])
print(sorted_school)

cubed = lambda num: num**3
print([cubed(i) for i in [3,6,9,2]])

even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

count = [num for num in range(101)]
print(count)

book = "The quick brown fox jumped over the fence."
my_dict = {word: len(word) for word in book.split()}
print(my_dict)