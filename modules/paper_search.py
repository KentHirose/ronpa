import requests
from bs4 import BeautifulSoup
import urllib.parse

def search(query: str, n_papers: int = 20) -> list:
    """
    j-stage からクエリにヒットする論文をn個取得する

    Args:
        query (str): クエリ
        n_papers (int, optional): 取得する論文の数

    Returns:
        list: タイトル, URL, アブストラクトをまとめたリスト
    """
    quote = urllib.parse.quote(query)

    # url = ("https://www.jstage.jst.go.jp/result/global/-char/ja?fromPage=%2Fsearch%2Fglobal%2F_search%2F-char%2Fja&freeText=" + quote + "&item1=&word1=&cond1=&notCond1=&item2=&word2=&cond2=&notCond2=&item3=&word3=&cond3=&notCond3=&item4=&word4=&notCond4=&count=50&from=" + str(page_num) + "&order=&type=&license=&attribute=&languageType=ja&option=&yearfrom=&yearto=&category=&cdjournal=&favorite=&translate=&bglobalSearch=false&sortby=1&showRecodsH=50&showRecords=20")
    url = ("https://www.jstage.jst.go.jp/result/global/-char/ja?fromPage=%2Fsearch%2Fglobal%2F_search%2F-char%2Fja&freeText=" + quote + "&item1=&word1=&cond1=&notCond1=&item2=&word2=&cond2=&notCond2=&item3=&word3=&cond3=&notCond3=&item4=&word4=&notCond4=&count=50&from=&order=&type=&license=&attribute=&languageType=ja&option=&yearfrom=&yearto=&category=&cdjournal=&favorite=&translate=&bglobalSearch=false&sortby=1&showRecodsH=50&showRecords=20")
    res = requests.get(url + query)
    # print(url)
    
    #HTMLからBeautifulSoupオブジェクトを作る
    soup = BeautifulSoup(res.text, "html.parser") 
    # 検索結果のタイトルとリンクのBSオブジェクトを取得
    title_url_element = soup.select('#search-resultslist-wrap > ul > li > .searchlist-title > a')

    # abstractのBSオブジェクトを取得
    abstract_element = []
    for q in range(50):
        abstract_element.append(soup.select("#search-resultslist-wrap > ul > li:nth-of-type("+ str(q+1) + ") > div.showabstractbox.content > div.inner-content.abstract"))
    # abst_listにabstを追加、abstがない場合はタイトルを追加
    for w in range(len(abstract_element)):
        if abstract_element[w] == []:
            abstract_element[w] = [title_url_element[w].get_text()]
    abstract_element = sum(abstract_element, [])

    # title,url,abstをlistに入れる
    search_results_list = []
    for e in range(n_papers):
        # タイトルのテキスト部分のみ取得
        title = title_url_element[e].get_text() 
        # リンクのみを取得し、余分な部分を削除する
        url = title_url_element[e].get('href').replace('/url?q=','')
        # abstractのテキスト部分のみ取得
        if type(abstract_element[e]) != str:
            abstract = abstract_element[e].get_text().replace("\n","").replace("\t","").replace("抄録全体を表示","")
        else:
            abstract = abstract_element[e]
        search_results_list.append([title, url, abstract])

    return list(zip(*search_results_list))