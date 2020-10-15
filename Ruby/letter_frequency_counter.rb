#	Letter Frequency Counter in Ruby [ following SoloLearn's course ]
#	Author: Nikos-Nikitas
#	GitHub: nikosnikitas

#	the text we'll use

myText = "This is a sample text. Ruby counts the letters of this"

#	converting the letters to downcase

myText.downcase!

#	frequency of letters goes in this hash. its default value is 0.
#	so any key that doesn't have a value will be 0.

frequency = {}

frequency.default = 0

#	iterating over each letter (character) in the text
#	and calculating its value +1 every time we see each letter

myText.each_char{|char| frequency[char] += 1}

#	making a range of all letters in the alphabet 
#	and printing their frequencies

("a".."z").each{|x| puts "#{x}: #{frequency[x]}"}
