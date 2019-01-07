import pyxel
import subprocess
import time
from Script.GUI.ClientGUI import ClientGUI

class TitleScreen:
    
    def __init__(self,GM):
        pyxel.init(160, 120, caption="Title Tank Game")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        self.GM = GM
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ENTER):
            # cmd = "python Script/networking/TCPServer.py"
            # try:
            #   subprocess.run(cmd.split())
            # except ConnectionResetError:
            self.GM.load()
            pyxel.quit()
        
        if pyxel.btnp(pyxel.KEY_A):
            self.GM.load()
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)

