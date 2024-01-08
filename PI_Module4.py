#A few words about None: continued

#It's obvious that the strangeFunction function returns True when it's argument is even.
#What does it return otherwise?

#We use the following code to check it:
print(strange_function(2))
print(strange_function(1))

#This is what we see in the console:
True
None

#Don't be surprised next time you see None as a function result - it may be symptom of a subtle
#mistake inside the function.

