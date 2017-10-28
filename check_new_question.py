import config
import SakitoScrap
import slackweb

def main():
  sakitoScrap = SakitoScrap.SakitoScrap(config.sakito['email'], config.sakito['password'])
  questionList = sakitoScrap.checkNewQuestion()

  #新規アンケートがあればslackに通知を送る
  if(not len(questionList) == 0):
    slackUrl = config.slack['webhooksUrl']
    sendText = '新規アンケートが追加されました。\n'
    for test in questionList:
      sendText = sendText + '・' + test + '\n'
    slack = slackweb.Slack(url=slackUrl)
    slack.notify(text=sendText, username='sakitobot')

if __name__ == '__main__':
  main()
