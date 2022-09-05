import requests
from bs4 import BeautifulSoup
import urllib.parse
from tours import lang_judg

def search(
    query: str,
    n_papers: int,
    doc_type: list,
    category: list,
    option: bool,
    order_input: int,
    document_type_list: list,
    category_list: list,
) -> list:
    """
    j-stage からクエリにヒットする論文をn個取得する
    """
    quote = urllib.parse.quote(query)
    document_type = ""
    cat_text = ""
    for i in doc_type:
        document_type += document_type_list[i]
    for w in category:
        cat_text += category_list[w]

    document_type = document_type.lstrip("%2C")
    cat_text = cat_text.lstrip("%2C")

    if option:
        option = "0"
    else:
        option = ""

    order = str(order_input + 1)
    url = ("https://www.jstage.jst.go.jp/result/global/-char/ja?fromPage=%2Fsearch%2Fglobal%2F_search%2F-char%2Fja&freeText=" + str(quote) + "&item1=&word1=&cond1=&notCond1=&item2=&word2=&cond2=&notCond2=&item3=&word3=&cond3=&notCond3=&item4=&word4=&notCond4=&count=50&from=&order=" + str(order) + "&type=" + str(document_type) + "&license=&attribute=&languageType=ja&option=" + str(option) + "&yearfrom=&yearto=&category=" + str(cat_text) + "&cdjournal=&favorite=&translate=&bglobalSearch=false&sortby=1&showRecodsH=50&showRecords=20")
    res = requests.get(url + query)

    #HTMLからBeautifulSoupオブジェクトを作る
    soup = BeautifulSoup(res.text, "html.parser") 
    # 検索結果のタイトルとリンクのBSオブジェクトを取得
    title_url_element = soup.select('#search-resultslist-wrap > ul > li > .searchlist-title > a')

    # abstractのBSオブジェクトを取得
    search_results_list = []
    for q in range(n_papers):
        title = title_url_element[q].get_text() 
        url = title_url_element[q].get('href').replace('/url?q=','')

        check = lambda a: a[0].get_text().replace("\n","").replace("\t","").replace("抄録全体を表示","") if( len(a)== 1) else "None"
        abstract_check =lambda a: a[0].get_text().replace("\n","").replace("\t","").replace("抄録全体を表示","") if( len(a)== 1) else title_url_element[q].get_text()

        abstract=abstract_check(soup.select("#search-resultslist-wrap > ul > li:nth-of-type("+ str(q+1) + ") > div.showabstractbox.content > div.inner-content.abstract"))
        author=check(soup.select("#search-resultslist-wrap > ul > li:nth-of-type("+ str(q+1) + ") > div.searchlist-authortags.customTooltip"))
        additional=check(soup.select("#search-resultslist-wrap > ul > li:nth-of-type("+ str(q+1) + ") > div.searchlist-additional-info"))
        
        search_results_list.append([title, url, abstract, author, additional])
    
    print("result_got\t",len(search_results_list))

    all_info = list(zip(*search_results_list))
    result = lang_judg(all_info)

    return result