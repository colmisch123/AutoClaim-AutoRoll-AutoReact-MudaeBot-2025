token = '' #Put your discord token in this string
channelId = '' #Copy the id of the text channel you want to auto-roll for this string      
serverId = '' #Copy the id of the server you want to auto-roll in for this string    

rollCommand = 'ha' # ha, wa, hg, wg, h, w, ma, mg, m depending on what you want to roll for

soulmateKakeras = ['kakeraP','kakeraR','kakeraW', 'kakeraL'] # Kakera reacts you only want to happen on soulmates (half react cost)
anycardKakeras = ['kakeraP', 'kakeraW', 'kakeraL'] # Kakera reacts you want on any card

desiredSeries = ['Haikyuu!!', 'Jujutsu Kaisen', 'Death Note', 'Berserk'] # Autoclaim any characters from these series if they appear (case sensitive)
desiredCharacters = ['Monkey D. Luffy', 'Gon Freecss', 'Jotaro Kujo'] # Input names of characters you want autoclaimed (case sensitive)
repeatMinute = '25' # Choose minute on which function repeats 0-59. '25' would have the function repeat at 12:25 pm, 1:25 pm, 2:25 pm etc.
Extras = True # Check Function.py line 23 to see greater details on how this is used. It includes extra text functions like $p, $us 20, $dk, $daily, $rt. Feel free to modify this depending on what you want.
reRoll = False # Automatically uses '$rolls' command at the end of a rolling session and starts over. 

claimAnyone = False # Set this to true if you just want to grow your collection, and claim whoever is available. 
minimumClaimValue = 500 # Use this to set a minimum value for whoever gets autoclaimed. Note that this value will be overriden if a character is in desiredSeries or desiredCharacters list. 
