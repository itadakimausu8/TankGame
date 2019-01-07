from Script.GUI.ClientGUI import ClientGUI
from Script.GUI.TitleScreen import TitleScreen
from Script.GameManager import GameManager

GM = GameManager()
TitleScreen(GM)
ClientGUI(GM)