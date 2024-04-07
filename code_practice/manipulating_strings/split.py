#Declares string_one and initialises its value
string_one = ",H,e,l,l,o, ,W,o,r,l,d,!,"
#Splits string_one into a list without the delimiter ",", recombines the list back into a string and stores
#that new string in string_one
string_one = "".join(string_one.split(","))
#Outputs the new value of string_one which is "Hello World!"
print(string_one)

#Declares string_two and initialises its value
string_two = "@H@.e@l@lo@. @W@.o@r@l.@d@!@."
#Splits string_two into a list without the delimiter "@", recombines the list back into a string and stores
#that new string in string_two
string_two = "".join(string_two.split("@"))
#Outputs the new value of string_two "H.ello. W.orl.d!."
print(string_two)
#Splits string_two into a list without the delimiter ".", recombines the list back into a string and stores
#that new string in string_two
string_two = "".join(string_two.split("."))
#Outputs the new value of string_two "Hello World!"
print(string_two)

#Declares string_three and initialises its value
string_three = "!!T##!$*%*$h!i%**!!s!!##! !$is #%%*##t!*!!**!%$h##!i!r#$#$**%##!d$! !s!$t*%*!r#$#%!i!#%#n$$!g!**!##!"
#Splits string_three into a list without the delimiter "!", recombines the list back into a string and stores
#that new string in string_three
string_three = "".join(string_three.split("!"))
#Outputs the new value of string_three "T##$*%*$hi%**s## $is #%%*##t***%$h##ir#$#$**%##d$ s$t*%*r#$#%i#%#n$$g**##"
print(string_three)
#Splits string_three into a list without the delimiter "#", recombines the list back into a string and stores
#that new string in string_three
string_three = "".join(string_three.split("#"))
#Outputs the new value of string_three "T$*%*$hi%**s $is %%*t***%$hir$$**%d$ s$t*%*r$%i%n$$g**"
print(string_three)
#Splits string_three into a list without the delimiter "$", recombines the list back into a string and stores
#that new string in string_three
string_three = "".join(string_three.split("$"))
#Outputs the new value of string_three "T*%*hi%**s is %%*t***%hir**%d st*%*r%i%ng**"
print(string_three)
#Splits string_three into a list without the delimiter "%", recombines the list back into a string and stores
#that new string in string_three
string_three = "".join(string_three.split("%"))
#Outputs the new value of string_three "T**hi**s is *t***hir**d st**ring**"
print(string_three)
#Splits string_three into a list without the delimiter "*", recombines the list back into a string and stores
#that new string in string_three
string_three = "".join(string_three.split("*"))
#Outputs the new value of string_three "This is third string"
print(string_three)
