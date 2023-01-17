from dhooks import Webhook
import time


from pystyle import Add, Anime, Colorate, Colors, Col, Center, System, Write
import marshal as marshal
import base64
import random 

System.Title('SDEER TOOL')
System.Size(57, 20)


banner1 = """

      
    
┌─┐┌┬┐┌─┐┌─┐┬─┐  ┌┬┐┌─┐┌─┐┬  
└─┐ ││├┤ ├┤ ├┬┘   │ │ ││ ││  
└─┘─┴┘└─┘└─┘┴└─   ┴ └─┘└─┘┴─┘


                      
"""




Anime.Fade(Center.Center(banner1),Colors.blue_to_red, Colorate.Vertical, interval=0.025, enter=True)


message = (Write.Input("que voulez-vous spammer", Colors.red_to_blue, interval=0.1255))
webhookurl = Webhook (Write.Input("Enter url webhook -> ", Colors.red_to_blue, interval=0.1255))
delay = int (Write.Input("Enter a delay", Colors.red_to_blue, interval=0.1255))


while True:
    time.sleep(delay)
    webhookurl.send(message)
    Write.Print("\n[+] Spammed Webhook", Colors.blue_to_white)
    
    

    
