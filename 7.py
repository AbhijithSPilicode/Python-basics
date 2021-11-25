Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#programme 7
" " "a b c d " " "
' a b c d  '
print("""a b c d""")
a b c d
print("""a.
b.
c.
d.""")
a.
b.
c.
d.
#multiline text above
#string
word="dhoni"
len(word)
5
len("dhoni")
5

#length of a string
word[0]
'd'
word[1]
'h'
word[2]
'o'
word[3]
'n'
word[4]
'i'
word[5]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    word[5]
IndexError: string index out of range
word[-1]
'i'
word[-2]
'n'
word[2:4]
'on'
#word[index of the beginning variable:index of ending variable+1]
c="python is a high level language"
c=[13:22]
SyntaxError: invalid syntax
c=[13:22]
SyntaxError: invalid syntax
c[13:22]
'igh level'
c[12:22]
'high level'
c[:22]
'python is a high level'
c[-8:-1]
'languag'
#slcing above
word[0:4:2]
'do'
word[0:5:2]
'doi'
word[0:3]
'dho'
c[-19:-9]
'high level'
c[-10:-20:-1]
'level hgih'
c[::-1]
'egaugnal level hgih a si nohtyp'
c[:-1]
'python is a high level languag'
word2='programming'
word2[::1]
'programming'
word2[::-1]
'gnimmargorp'
#reversing a string
"string methods"
'string methods'
word2=word2.upper()
word2
'PROGRAMMING'
#lowecase to uppercase
word2=word2.lower()
word2
'programming'
#uppercase to lower
d="        unstoppable mallu          "
d.lstrip()
'unstoppable mallu          '
d.rstrip()
'        unstoppable mallu'
d.strip()
'unstoppable mallu'
#to remove the spaces in a string


d.strip().upper()
'UNSTOPPABLE MALLU'
d,capitalize()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d,capitalize()
NameError: name 'capitalize' is not defined
word2.capitalize()
'Programming'
word2.startswith("pr")
True
word2.endswith("ng")
True
word2.startswith("as")
False
#first and last elements of string
type(True)
<class 'bool'>
