#	Hero Battle Game example in Ruby [following SoloLearn's Ruby Tutorial]
#	Author: Nikos-Nikitas
#	GitHub: nikosnikitas

#	Hero class with a name, hit points and attack power.
#	Checks if player is alive (hp > 0), if a player attacks,
#	and shows a player's information 

class Hero
	attr_accessor:name, :hp, :atk
	
	def initialize(n,h,a)
		@name = n
		@hp = h
		@atk = a
	end
	
	def inPlay
	
		@hp > 0
	
	end
	
	def attack(opponent)
	
		opponent.hp -= self.atk
	
	end
		#	this is called when a player is created
	def to_s
		"#{name}: HP: #{hp}, ATK: #{atk}"
	end

end
#	the battle where each player attacks eachother
def battle(p1,p2)
	while p1.inPlay && p2.inPlay
		p1.attack(p2)
		p2.attack(p1)
		show_status(p1,p2)
	end
	#	checking which player is in play
	if p1.inPlay
		puts"#{p1.name} Wins!!!"
	elsif p2.inPlay
		puts"#{p2.name} Wins!!!"
	else
		puts "It's a DRAW."
	end
end

#	showing the game status for each player
def show_status(*p)
	p.each{|x| puts x}
end

#	Printing "HERO STATS" and....
#	Let the game begin! Heroes initialize!!
puts "HERO STATS"

#random number of => 1 out of 100 for Health Points and => 1 out of 10 for attack power.
h1 = Hero.new("Hero 1", 1+rand(100), 1+rand(10))
h2 = Hero.new("Hero 2", 1+rand(100), 1+rand(10))

show_status(h1,h2)

# Ready Set BATTLE!
puts "BATTLE BEGINS!"
battle(h1,h2)
