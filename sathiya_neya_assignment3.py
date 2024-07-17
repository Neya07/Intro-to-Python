#%%
#1
def is_palindrome(word):

    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word 
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrome("racecar")) 
print(is_palindrome("python"))

# %%
#2
class Rectangle:
    def area(l, w):
        return l*w
    def perimeter(l,w):
        return 2*l+2*w

l = 3
w = 4

area = Rectangle.area(l,w)
perimeter = Rectangle.perimeter(l,w)
print("Length:",l,"Width:",w,"Area:",area,"Perimeter:",perimeter)

# %%
#3
def count_words(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

sentence = "hello world, hello python"
print(count_words(sentence))

# %%
