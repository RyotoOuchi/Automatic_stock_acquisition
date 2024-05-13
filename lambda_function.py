import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 株価サイト取得 対象のURLを入力してください。
    #※https://finance.yahoo.co.jpから
    url="https://finance.yahoo.co.jp"
    response=requests.get(url)
    response.text

    # BeautifulSoupにて加工できるように変換
    html=BeautifulSoup(response.text,"html.parser")

    # 必要情報を抽出
    LiloClubStockPrice=html.find_all("div",attrs={"class":"_1nb3c4wQ"})[0]
    date=LiloClubStockPrice.find_all("time")[0].text
    today=LiloClubStockPrice.find_all("span",attrs={"class":"_3rXWJKZF"})[0].text
    howmany=LiloClubStockPrice.find_all("span",attrs={"class":"_3rXWJKZF"})[1].text
    percent=LiloClubStockPrice.find_all("span",attrs={"class":"_3rXWJKZF"})[2].text

    # 送信メッセージ
    message="""
    {}の株価！
    今日の株価は「{}」！
    前日から「{}」円「{}％」！
    今日も頑張りましょうᕙ( 'ω')ᕗﾑｷｯ""".format(date,today,howmany,percent)

    # lineのトークンとURLを変数に代入 
    #※notifyから取得してください。 
    tokun=""
    url="https://notify-api.line.me/api/notify"

    # lineに送る情報
    auth={"Authorization":"Bearer"+ ' ' + tokun}
    conternt={"message":message}
    requests.post(url,headers=auth,data=conternt)
