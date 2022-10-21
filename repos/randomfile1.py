while True :
     season = input("My chosen season is ... ")
     print("")
     if season == 'Summer':
         print("Destination 1.")
         print("")
         print("")
         print("Destination 2.")
         print("")
         print("")
         print("Destination 3.")
         print("")
         print("")
         print("Destination 4.")
         print("")
         print("")
     elif season == 'Autumn':
         print("Destination 1. NEW YORK, USA")
         print("It goes without saying that New York is a year-round destination, but the Big Apple is particularly appealing during autumn. Why? As cooler temperatures arrive, so do world-famous American holidays such as Halloween and Thanksgiving. And autumn really shows off its colours in Central Park, where more than 26,000 resident trees start to shed their leaves. Strolling through the foliage wearing a scarf, drinking a pumpkin spice latte? That’s definitely one to share with your Facebook feed.")
         print("")
         print("Destination 2. CAPE VERDE, AFRICA")
         print("Autumn doesn’t have to mean saying goodbye to the sun, as Cape Verde’s shores stay warm all year round. Temperatures sit in the high 20s from September to December, so you won’t have to travel far to squeeze in some last minute vitamin C. Enjoy long days on the beach in hotspots like Sal and Boa Vista, and have a go at watersports like surfing and kayaking. Away from the beach, make the most of Cape Verde’s mixture of cultural influences from Africa and Portugal by tucking into national dish Cachupa, or some of the island’s fresh fish.")
         print("")
         print("Destination 3. ICELAND")
         print("This is the best time of year to spot the world-famous northern lights, and you’ll get the chance to see them on our excursion included in a TUI holiday package. Our trips to Iceland run from November to March, and autumn is the best time to visit if you want to skip the heavy snowfall of the winter months. And, as the temperatures drop, you can warm up in the Blue Lagoon without having to climb out into the cold when you leave.")
         print("")
         print("Destination 4. THE BALEARICS, SPAIN")
         print("The Balearics hang on to the summer heat into the autumn, with temperatures averaging at 24C in October. You have four islands to choose from, including sleepy Formentera and party-central Majorca. But away from the beaches, the autumn months are the ideal time to explore the island’s hiking and cycling paths, and visit markets full of local produce fresh from the harvest. Autumn has fewer tourists, but keeps the summer heat – making it an ideal spot for a getaway.")
         print("")
     elif season == 'Winter':
          print("Destination 1.")
          print("Destination 1.")
          print("")
          print("")
          print("Destination 2.")
          print("")
          print("")
          print("Destination 3.")
          print("")
          print("")
          print("Destination 4.")
          print("")
          print("")
     else: 
       print("Destination 1.")
       print("")
       print("")
       print("Destination 2.")
       print("")
       print("")
       print("Destination 3.")
       print("")
       print("")
       print("Destination 4.")
       print("")
       print("")


     outcome = input("Are you happy with your destination?")
 
     if outcome == 'Yes':
      print("We are happy to hear it!")
     if outcome == 'No':
      print("How about looking at another season?")
     
     
    
     check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
     if check.upper() == "Y": #go back to the top
      continue    
     print("Bye...")
     break #exit