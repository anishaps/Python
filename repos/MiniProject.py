print ("Welcome to Hello World! The key to discovering your next holiday destination.")
print ("To get started, please choose which season you would like to travel in...")
print ("")
print ("Summer e.g. June, July and August")
print ("Autumn e.g. September, October and November")
print ("Winter e.g. December, January and February")
print ("Spring e.g. March, April and May")
print ("")

while True :
     season = input("Your chosen season is ... ")
     print("")
     if season == 'Summer':
         print("Here are 4 incredible summer holiday ideas!")
         print("")
         print("Destination 1. MAUI, HAWAII USA")
         print("Maui has a 30 miles stretch filled with beautiful beaches with crystal clear waters. The general vibe of Maui is very relaxed and laid back. You can simply chill and explore the local culture which is full of stories and mythology. Maui is a paradise on earth. You can enjoy great food, chilled-out music, beautiful landscape, and water sports to make your vacation a memorable one.")
         print("")
         print("Destination 2. NEW ZEALAND")
         print("It’s one of the most scenic and beautiful destinations in the world owing to the majestic landscapes that appear to be from another planet altogether! It’s also the perfect place for adventure seekers, nature lovers, honeymooners, photographers, birdwatchers, and those inspired to visit simply by the famous Hollywood movies that were shot here!")
         print("")
         print("Destination 3. AMALFI COAST, ITALY")
         print("Considered to be the coastal gem of Italy, the Amalfi Coast is a true manifestation of nature’s beauty. With its picturesque landscape, coastal peaks, dense forests, and pastel buildings on the cliff, the Amalfi Coast shine bright like a star in the night and comes alive with first ray of the sun.")
         print("")
         print("Destination 4. KERALA, INDIA")
         print("Kerala is a name which needs no introduction to travelers across the world. Being a perfect blend of hill stations, tea plantations, backwaters, and beaches, this tropical paradise of Kerala serves as one of the best holiday destinations in South India.")
         print("")
     elif season == 'Autumn':
         print("Check out these 4 autumn holiday destinations...")
         print("")
         print("Destination 1. NEW YORK, USA")
         print("It goes without saying that New York is a year-round destination, but the Big Apple is particularly appealing during autumn. Why? As cooler temperatures arrive, so do world-famous American holidays such as Halloween and Thanksgiving. And autumn really shows off its colours in Central Park, where more than 26,000 resident trees start to shed their leaves. Strolling through the foliage wearing a scarf, drinking a pumpkin spice latte? That’s definitely one to share with your Facebook feed.")
         print("")
         print("Destination 2. CAPE VERDE")
         print("Autumn doesn’t have to mean saying goodbye to the sun, as Cape Verde’s shores stay warm all year round. Enjoy long days on the beach in hotspots like Sal and Boa Vista, and have a go at watersports like surfing and kayaking. Away from the beach, make the most of Cape Verde’s mixture of cultural influences from Africa and Portugal by tucking into national dish Cachupa, or some of the island’s fresh fish.")
         print("")
         print("Destination 3. ICELAND")
         print("This is the best time of year to spot the world-famous northern lights, and you’ll get the chance to see them on our excursion included in a TUI holiday package. Our trips to Iceland run from November to March, and autumn is the best time to visit if you want to skip the heavy snowfall of the winter months. And, as the temperatures drop, you can warm up in the Blue Lagoon without having to climb out into the cold when you leave.")
         print("")
         print("Destination 4. THE BALEARICS, SPAIN")
         print("The Balearics hang on to the summer heat into the autumn, with temperatures averaging at 24C in October. You have four islands to choose from, including sleepy Formentera and party-central Majorca. But away from the beaches, the autumn months are the ideal time to explore the island’s hiking and cycling paths, and visit markets full of local produce fresh from the harvest. Autumn has fewer tourists, but keeps the summer heat – making it an ideal spot for a getaway.")
         print("")
     elif season == 'Winter':
          print("Whether you're looking for snow or sun, here are some great winter travel ideas!")
          print("")
          print("Destination 1. MAURITIUS")
          print("Its beaches are still potted tropical paradises, and here you can rent a car and go exploring to find your own deserted cove, drive or hike up into its rainforested hills, take a boat out and go snorkelling or dive in its extraordinary underwater world. It has some of the finest beach hotels in the world, and you can find little boutique hotels right on the beach, too. Perhaps the best months to go to Mauritius are October and November, when it's hot but not too hot, and at its driest.")
          print("")
          print("Destination 2. THAILAND")
          print("The islands of Thailand are the stuff of castaway fantasies. White sand, rustic-chic beach shacks, a hammock gently swaying between two palm trees as a turquoise sea laps at the shore… There are dozens to choose from, and each offers something quite different, from the super-spas of Koh Samui to barefoot beach-bum in Koh Lipe, while Koh Lanta remains quietly chilled out with lovely places to stay on beaches that stretch for miles.")
          print("")
          print("Destination 3. LAPLAND, FINLAND")
          print("Lapland pulls out all the stops over the festive period, so there’s nowhere better to get into the Christmas spirit. Known as Santa Claus’ homeland, this country dishes up the stuff of fairytales – like snow-dusted forests, cosy log cabins, and a population that’s made up of more reindeer than people.")
          print("")
          print("Destination 4. MEXICO")
          print("Mexico's Yucatán Peninsula, on the Atlantic Coast, has a magical mix of ancient and buzzy-right-now cultures. Swim in its green ceynotes, discover temples, salute the sun beneath the glitterball gods with fashionistas on the beach in Tulum. Mix it up in colonial Mérida. Go barefoot on Isla Holbox. The best time to come is during Britain's darkest months.")
          print("")
     else: 
       print("Fancy an Easter getaway, look no further...")
       print("")
       print("Destination 1. TOKYO, JAPAN")
       print("Splurge on a long-haul trip to Tokyo, where thousands of cherry trees, or sakura, burst into bloom each spring and mark the end of winter. There’s a ritual to enjoying the blossoms, known as hanami (literally, ‘looking at flowers’): To make like a local, pick up a seasonal bento box from a supermarket and head to a park for an al fresco lunch under the branches.")
       print("")
       print("Destination 2. FLORIDA, USA")
       print("It's one of the best places to go on holiday in Spring for beach breaks or outdoor adventures, with long sunny days and warm-but-not-hot weather – just right for tailing alligators through the mangroves or galloping around a cattle ranch, cruising around Miami's art district or having a classic family beach holiday on the Gulf of Mexico.")
       print("")
       print("Destination 3. PARIS, FRANCE")
       print("Who doesn't love Paris in the springtime, when the city is warming up and the trees around the Tuileries are in blossom. When we can sit out beside the Canal Saint-Martin and smoke Gauloises, or stroll a long, golden-evening stroll along the Seine, hand in hand with someone else who loves Paris in the springtime. ")
       print("")
       print("Destination 4. ZERMATT, SWITZERLAND")
       print("While things are hotting up down at the coast, up in the mountains it's still ice-cool. A spring ski break is a brilliant thing, especially for people who are more concerned with the après ski than the quality of the powder.  Zermatt is one of the best ski resorts in April – it's high enough that there's still plenty of snow and open all year round, plus it's quieter and cheaper than in high season.")
       print("")


     outcome = input("Are you happy with your destinations? ")
     print("")
 
     if outcome == 'Yes':
      print("Amazing!")
     if outcome == 'yes':
      print("Excellent!")
     if outcome == 'No':
      print("That's a shame! You can always explore another season...")
     if outcome == 'no':
      print("That's a shame! You can always explore another season...")
     else:
        print("")
     
     print("")
    
     check = input("Would you like to leave Hello World! or take another trip? Enter Y to find another destination or press N to exit Hello World!: ")
     if check.upper() == "Y": 
      continue    
     print("Goodbye World!")
     break 