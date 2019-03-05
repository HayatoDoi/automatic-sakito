import config
import SakitoScrap

def main():
  sakitoScrap = SakitoScrap.SakitoScrap(config.sakito['email'], config.sakito['password'])

  while sakitoScrap.getBonusPoint() > 0:
    sakitoScrap.bonusGacha()

if __name__ == '__main__':
  main()
