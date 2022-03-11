import time, random

#Initialise the list from 1-90
tambola_list = list(range(1,91))
print(tambola_list)

# Shuffle the list
print("After shuffling of list")
random.shuffle(tambola_list)
print(tambola_list)

phrases = ['Zero', 'Son of Gun','You and me', 'Buy 2 get 1 free', 'Aar ya paar- number 4','Hum Panch','In a fix',' Lucky for all',' one fat major', ' U are mine','Dus numbari ','Those beautiful legs'
  ,' one doz number',' Lucky for some','Valentines','Independence',' Sweet 16',' Not so sweet',' Voting age', 'Last of the teens'
,'Blind one score','marriageable age','Two little ducks',' You & me','Two doz number', 'Silver Jublee',' Bole mere lips I love 26'

, 'A black raven', 'Out on a date','Rise & shine','Don’t play dirty',' Baskin Robin’s',' Binaca smile','All the three’s','Lions roar'

 ,'A flirty wife','Chatis ka Aankda',' Lime & Lemon','Me & my fat mate','Watch your waist line','Men get naughty at ',' Kiss and run'

 ,'Bharat chodo ',' Climb a tree',' Dil ke chor','Half way thru','Choke, chake maro','Independence','U are not late','Marooning Line'

,'Golden Jubliee','Auspicious','Pack of the cards','Pack with joker','House of bamboo door','All the fives','Whisky, Beer do not mix'

 ,'Banegi baat at panch aur saat','Retirement age','Do I hear a line at 59','3 Score','Done- dana-dan done'

 ,'Over haul is due','Kisses come free','Hardcore','Harem of wives','All the 6’s click 66','Haath mein haath 6 aur 7'

 ,'Mota seth',' ulta pulta',' Lucky Blind','Setting sun','A different view','Savitriji',' Still want more','Diamond jubilee'

 ,'Run out of tricks','thanda lemon','Wipe the slate','Old and senile','Blind 4 score','Said and done','Down with flu'

 ,'Grandma’s age','Haggard and bored','Still alive','Pick up a walking stick',' Nearing heaven',' Two fat majors'

,'Penultimate','Top of the house blind 90']

#Traverse the list with phrases
for number in tambola_list:
    print(phrases[number],"--->",number)
    time.sleep(5)