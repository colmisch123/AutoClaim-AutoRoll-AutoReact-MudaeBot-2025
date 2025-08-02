import discum
import json
import time
import requests
import Vars
from discum.utils.slash import SlashCommander

botID = '432610292342587392' 
auth = {'authorization' : Vars.token}
bot = discum.Client(token = Vars.token, log=False)
url = (f'https://discord.com/api/v8/channels/{Vars.channelId}/messages')
claimed = '❤️'
unclaimed = '🤍'
kakera = '💎'
emoji='👍'

# This function is the outer layer to the rolling. It uses rollFunction() to do most of the heavy lifting.
def simpleRoll():

    print (time.strftime("Rolling at %H:%M - %d/%m/%y",time.localtime()))

    #Place any extra text commands you want to run here. 
    if(Vars.Extras):
        print('\nTrying to roll Pokeslot')
        requests.post(url=url , headers = auth, data = {'content' : '$p'})
        time.sleep(3)
        requests.post(url=url , headers = auth, data = {'content' : '$us 20'})
        time.sleep(3)
        requests.post(url=url , headers = auth, data = {'content' : '$us 20'})
        time.sleep(3)
        requests.post(url=url , headers = auth, data = {'content' : '$dk'})
        time.sleep(3)
        requests.post(url=url , headers = auth, data = {'content' : '$daily'})
        time.sleep(3)
        #requests.post(url=url , headers = auth, data = {'content' : '$rt'})
        #time.sleep(3)

    rollFunction()
        
    if Vars.reRoll:
        time.sleep(2)
        requests.post(url=url , headers = auth, data = {'content' : '$rolls'})
        time.sleep(2)
        rollFunction()

    print('Rolling ended')

# This function is used exclusively for debugging purposes, it is not used in the main code. 
def flatten_print(nested_list, layer=1):
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, dive into it with an increased layer
            flatten_print(element, layer + 1)
        else:
            if isinstance(element, str):
                print(f'Layer {layer}: "{element}"')
            else:
                print(f"Layer {layer}: {element}")

# Main rolling function
def rollFunction():

    #These variables help control the main loop to prevent it from rolling forever
    continueRolling = True
    x = 0
    i = 1
    
    isSoulmate = False
    
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])

    while continueRolling == True or x < 4:

        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data = rollCommand)
        time.sleep(1.8)
        r = requests.get(url , headers = auth )
        jsonCard = json.loads(r.text)

        #Loop ending chunk
        if (len(jsonCard[0]['content']) != 0):
            x += 1  
            continueRolling = False
            continue
        
        idMessage = (jsonCard[0]['id'])
        try:
            cardName = (jsonCard[0]['embeds'][0]['author']['name'])
            cardSeries = (jsonCard[0]['embeds'][0]['description']).replace('\n', '**').split('**')[0]
            cardPower = int((jsonCard[0]['embeds'][0]['description']).split('**')[1])
        except IndexError:
            cardName = 'null'
            cardSeries = 'null'
            cardPower = 0
        except KeyError:
            cardName = 'null'
            cardSeries = 'null'
            cardPower = 0
        except ValueError:
            cardPower = 0
        if not 'footer' in jsonCard[0]['embeds'][0] or not 'icon_url' in jsonCard[0]['embeds'][0]['footer']:
            print(i,' - '+unclaimed+' ---- ',cardPower,' - '+cardName+' - '+cardSeries)
            if ((cardPower >= Vars.minimumClaimValue and Vars.claimAnyone) or cardName in Vars.desiredCharacters or cardSeries in Vars.desiredSeries):
                print('Trying to Claim '+ cardName)
                r= requests.put(f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/{emoji}/%40me',headers=auth)
        else: 
            print(i,' - '+claimed+' ---- ',cardPower,' - '+cardName+' - '+cardSeries)
        #This if statement fixes the bot breaking on already owned cards that don't have a kakera react, but it can occasionally cause weird printing outputs
        if jsonCard[0]['components'] != []:
            cardsKakera = (jsonCard[0]['components'][0]['components'][0]['emoji']['name'])

            if "chaoskey" in jsonCard[0]['embeds'][0]['description']:
                isSoulmate = True
            else:
                isSoulmate = False
                
            components = jsonCard[0]["components"][0]['components']

            ### Printing function for debugging purposes ###
            # Uncomment the code block below to get much more detailed information with each character roll. 
            # If you intend to implement your own functionality to this script, I highly recommended getting the data structures of the cards from this function. 
            
            # if jsonCard[0]["components"][0] != None: 
                # flatten_print(jsonCard)
                # print(f'jsonCard[0]["components"][0]: {jsonCard[0]["components"][0]}')
                #if components[0] != []:
                   # print(f"Components[0]: {components[0]}")
            # print(f"cardsKakera: {cardsKakera} \n components: {components}")

        else:
            components = jsonCard[0]["components"]
        for index in range(len(components)):
            try:
                cardsKakera = components[index]['emoji']['name']
                if (cardsKakera in Vars.soulmateKakeras and isSoulmate) or (cardsKakera in Vars.anycardKakeras):
                    x -= 1 
                    print(kakera+' - '+kakera+' - Trying to react to '+ cardsKakera + ' of '+ cardName)
                    bot.click(jsonCard[0]['author']['id'], channelID =jsonCard[0]['channel_id'], guildID = Vars.serverId, messageID=jsonCard[0]['id'], messageFlags=jsonCard[0]['flags'], data={'component_type': 2, 'custom_id': components[index]['custom_id']})
                    time.sleep(0.5)

            except IndexError:
                cardsKakera = 'null'
        i += 1
        isSoulmate = False