import requests as C;A=C.get('https://raw.githubusercontent.com/Miner3DGaming/TGE/main/installer/install_tge_installer.py');A.raise_for_status();B=open('\\'.join(__file__.split('\\')[:-1])+'/install_tge_installer.py','w');B.write(A.text);B.close()