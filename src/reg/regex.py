from .date import DATE_REGEX
from .juusho import TODOFUKEN

'''{"keyname":,"key_regex":,"value_regex":}'''

KAKKO_REGEX="\(.*?\)"

"""NG,Domain"""
NG_DOMAIN_REGEX="www\.city\..*$|city\..*$|www\.town\.|town\.|www\.courts\.|biz\.plala\.or\.jp.*$"

"""REGEXes"""
ZIP_REGEX="〒?.?(?<!(\-|\(|\)))\d{3}.\d{4}"
TEL_AND_FAX_REGEX='[0０]\d{1,3}[^0-9０-９,]\d{1,5}[^0-9０-９,]\d{3,5}'
GET_BY_SYMBOLS=""
NEGATIVE_REGEX_ADDRESS="(?!の(?!ぞみ))(?!より)(?!近辺)(?!にて)(?!指令\d+号)(?!.*?徒歩)"
GET_EMAIL_REGEX="^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$"
GET_EMAIL_REGEX_B="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}"
GROUP_REGEX="グル.プ"
MKNAME_REMOVE_REGEX="^[０-９（）　]+$|"+"|".join([n[1] for n in TODOFUKEN])
ABOUT_LINK_NEGATIVE_REGEX="^.*\.(css|png|php|pdf|ico).*$"

MONEY_REGEX="([\d,，\.十百千万億兆￥]+)円?"
'''住所の最後を削る。例：福岡市中央区清川1-3-1\xa0TEL：092-526-8730\xa0FAX：092-526-8740→福岡市中央区清川1-3-1_事前にTEL_FAX_TRANSで変換してから使用する'''
CUT_ADDRESS_END="tel|fax|<"

"""LISTS"""
MKNAME_EXTRA_LIST=["大きな地図で見る","に至る","所\s*在\s*地?","住\s*所地?","連絡先","地図データ.*$","地図を表示",TEL_AND_FAX_REGEX,"ｔｅｌ","ｆａｘ","ａｄｄｒｅｓｓ","お問い合わせ","地図で確認する","地図",".*?Ｇｏｏｇｌｅマップ.*$","アクセス"]#すべて全角
TAG_VALUE_STRIP_SYMBOLS=["\u3000","<br>","\n","</br>","{{SPLIT}}"]
NEGATIVEWORDS_LEFT_COMMON=["\="]
NEGATIVEWORDS_RIGHT_COMMON=["を"]
NEGATIVEWORDS_DATE=["より","年以上","経緯"]
DAIHYOSHA_NEGATIVEWORDS=["tel","電話","挨拶","０","0","メッセ","紹介","あいさつ","略歴","メール","からの",".*?就任","ブログ","より","とする","組織","が","プロフ","の.*?です","教育","する","を","は"]
TEL_FAX_NG=["0123456789","[0]{6,12}","[1]{6,12}","[2]{6,12}","[3]{6,12}","[4]{6,12}","[5]{6,12}","[6]{6,12}","[7]{6,12}","[8]{6,12}","[9]{6,12}"]

"""TRANS"""
'''一旦半角に変換してキーワードを揃える→その後、REGEX'''
TEL_FAX_TRANS={"tel":"電\s*話\s*番\s*号|電\s*話|代表番号|T\s*E\s*L|t\s*e\s*l|T\s*e\s*l|Ｔ\s*Ｅ\s*Ｌ|ｔ\s*ｅ\s*ｌ|Ｔ\s*ｅ\s*ｌ|P\s*h\s*o\s*n\s*e|P\s*H\s*O\s*N\s*E|p\s*h\s*o\s*n\s*e|<.*?tel.*?>","fax":"ファックス|ファクス|ファクシミリ|ﾌｧｯｸｽ|ﾌｧｸｽ|ﾌｧｸｼﾐﾘ|F\s*A\s*X|f\s*a\s*x|F\s*a\s*x|Ｆ\s*Ａ\s*Ｘ|ｆ\s*ａ\s*ｘ|Ｆ\s*ａ\s*ｘ|<.*?fax.*?>"}
HTML_TRANS={**TEL_FAX_TRANS,**{"\n":"<br>|</br>"}}
RESULT_TRANS_DICT={"&nbsp;":"","\u2003":"","\x03":"","&gt;":"","\t":"","&lt":"","\u200b":"","\uf095":"","\ue911'":""}
OUTPUT_TRANS_DICT={"\u3000":" ",r"\\ｂ":"",r"\\b":"","\t":"","\xa0":"","\\":""}
NUM_ZEN_TO_HAN={"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9"}
TAGS_BASIC_TRANS={"<th":"<td","<dl":"<dd"}

"""DELETE_SYMBOLS"""
DELETE_SPACES="　| "
DELETE_BRECKETS="\(.*?\)|（.*?）"

"""main関数内"""
GET_LINKS={"key_regex":"概要|会社案内|会社紹介|企業情報|会社情報|事務所案内|学校情報|運営会社|特定商取引法|法人|問い合わせ|連絡先|アクセス|about|company|kaisya|profile|gaiyo|contact"}

"""info関数内
key_regex=取得時の辞書のキーの正規表現、value_regex=取得時の辞書の値の正規表現、multi=複数取得、negative_regex=除外したい値の正規表現、p=値の最大文字数"""

D_JUUSHO={"keyname":"住所","limit_length":50,"key_regex":"本社|本店所在地|支社|本部|所在地|事業所|事業部|営業所|出張所|事務所|工場|倉庫|支店|OFFICE|本店|店|ショ.ル.ム|モデルハウス|物流センタ.","zenkaku":True}#市区郡のあとに、のが付くのはのぞみのみ(2022/4/6)

D_DAIHYOSHA={"keyname":"D_DAIHYOSHA","key_regex":"代表取締役社長|代表取締役会長|最高経営責任者|取締役社長|取締役会長|代表取締役|代表者名|代表社員|代表者|責任者|理事長|園長|校長|院長|社長|ＣＥＯ","value_regex":"^(?!.*(代表|園長|校長|院長|社長|取締|fax|tel|\d)).*$","limit_length":50,"negativewords_left":["tel","電話"],"negativewords_right":DAIHYOSHA_NEGATIVEWORDS,"strip_symbols":True}
D_TANTOUSHA={"keyname":"D_TANTOUSHA","key_regex":"役員|部長|専務|常務|監査役|取締役","negativewords_left":NEGATIVEWORDS_LEFT_COMMON+["代表"],"value_regex":"^(?!.*(取締役)).*$","negativewords_right":DAIHYOSHA_NEGATIVEWORDS+["社長","会長"],"strip_symbols":True}
D_REGISTERNO={"keyname":"D_REGISTERNO","key_regex":"登録番号|免許|登録認可|一級建築士事務所登録|資格|耐震対策|届出","strip_symbols":True,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":["普通(自動車)?(運転)?免許"],"limit_length":50,"delete_symbols":DELETE_SPACES,"get_by_tags":True}
D_LICENSE={"keyname":"D_LICENSE","key_regex":"有資格者|資格取得者","strip_symbols":True,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"limit_length":50,"delete_symbols":DELETE_SPACES,"get_by_tags":True}
D_SALES={"keyname":"D_SALES","key_regex":"売上高|年商","option_regex":DATE_REGEX,"value_regex":MONEY_REGEX+"?","negativewords_left":NEGATIVEWORDS_LEFT_COMMON+["グル.プ"],"delete_symbols":DELETE_SPACES,"strip_symbols":True}
D_AUTH={"keyname":"D_AUTH","key_regex":"ISO","value_regex":"\d+","strip_symbols":True}
D_SHIHONKIN={"keyname":"D_SHIHONKIN","key_regex":"資本金|出資金","value_regex":MONEY_REGEX,"negativewords_value":["グル.プ","設立","創業"],"negativewords_left":NEGATIVEWORDS_LEFT_COMMON+["グル.プ","設立","創業","増資"],"negativewords_right":["グル.プ","設立","創業","増資"],"delete_symbols":"|".join([DELETE_SPACES,DELETE_BRECKETS]),"look_ahead":DATE_REGEX,"strip_symbols":True}
D_SOUGYO={"keyname":"D_SOUGYO","key_regex":"創業","negativewords_right":"経緯","limit_length":50,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":NEGATIVEWORDS_DATE,"value_regex":DATE_REGEX,"delete_symbols":"|".join([DELETE_SPACES,DELETE_BRECKETS]),"strip_symbols":True}
D_SETSURITSU={"keyname":"D_SETSURITSU","key_regex":"設立年月日|会社設立|法人設立|設立日|設立|開設","limit_length":50,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":NEGATIVEWORDS_DATE,"value_regex":DATE_REGEX,"delete_symbols":"|".join([DELETE_SPACES,DELETE_BRECKETS]),"strip_symbols":True}
D_SOUSETSU={"keyname":"D_SOUSETSU","key_regex":"創設","limit_length":50,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":NEGATIVEWORDS_DATE,"value_regex":DATE_REGEX,"delete_symbols":"|".join([DELETE_SPACES,DELETE_BRECKETS]),"strip_symbols":True}
D_SOURITSU={"keyname":"D_SOURITSU","key_regex":"創立","limit_length":50,"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":NEGATIVEWORDS_DATE,"value_regex":DATE_REGEX,"delete_symbols":"|".join([DELETE_SPACES,DELETE_BRECKETS]),"strip_symbols":True}
D_JUGYOIN={"keyname":"D_JUGYOIN","key_regex":"従業員|社員数|従業員数|所員数|職員数","option_regex":".*?[\d,]+(人|名)","value_regex":"[\d,]+(人|名)","sum":{"unit_ahead":"計","unit_behind":"名"},"negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"limit_length":50,"delete_symbols":DELETE_SPACES,"strip_symbols":True}
D_CARS={"keyname":"D_CARS","key_regex":"車両台数|保有車両","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"delete_symbols":DELETE_SPACES,"strip_symbols":True,"get_by_tags":True}
D_CAPACITY={"keyname":"D_CAPACITY","key_regex":"定員","value_regex":"[\d,]+(人|名)","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"delete_symbols":DELETE_SPACES,"strip_symbols":True}
D_KESSAN={"keyname":"D_KESSAN","key_regex":"決算期?","value_regex":"^(?!.*～).*?月(\d{1,2}日)","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True}
D_OWNBANK={"keyname":"D_OWNBANK","key_regex":"取引銀行|主要取引銀行|取引先銀行|取引金融機関","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True,"get_by_tags":True}
D_MAINCUSTOMERS={"keyname":"D_MAINCUSTOMERS","key_regex":"主要取引先|取引先|受注先|納入先","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":["銀行","金融機関"],"limit_length":255,"strip_symbols":True,"get_by_tags":True}
D_MAINSUPLIERS={"keyname":"D_MAINSUPLIERS","key_regex":"主要仕入先|仕入先|主要取引メ.カ.|取り?扱いメ.カ.","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":["銀行","金融機関"],"limit_length":255,"strip_symbols":True,"get_by_tags":True}
D_EXPLANATION={"keyname":"D_EXPLANATION","key_regex":"事業内容|事業概要|業務内容|事業目的","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"get_by_tags":True,"strip_symbols":True}
D_HOJINNAME={"keyname":"D_HOJINNAME","key_regex":"会社名|商号|社名|法人名|名称|販売業者|業者名|屋号|運営|経営主体","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"negativewords_right":NEGATIVEWORDS_RIGHT_COMMON+["責任者"],"strip_symbols":True}
D_PARTNERSHIP={"keyname":"D_PARTNERSHIP","key_regex":"業務提携","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"limit_length":255,"strip_symbols":True,"get_by_tags":True}
D_SUBCONTRACTING={"keyname":"D_SUBCONTRACTING","key_regex":"業務委託先","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True,"get_by_tags":True}
D_GROUPCAMPANIES={"keyname":"D_GROUPCAMPANIES","key_regex":"関連会社|関連法人|グループ会社|子会社|親会社|協力会社","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True,"get_by_tags":True}
D_DANTAI={"keyname":"D_DANTAI","key_regex":"加盟団体|所属団体|加入団体","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True,"get_by_tags":True}
D_INSURANCE={"keyname":"D_INSURANCE","key_regex":"加入保険|保険会社","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True,"get_by_tags":True}
D_HOSHOKYOKAI={"keyname":"D_HOSHOKYOKAI","key_regex":"保証協会","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"strip_symbols":True}
D_ITEMS={"keyname":"D_ITEMS","key_regex":"営業.目|取扱商品","negativewords_left":NEGATIVEWORDS_LEFT_COMMON,"get_by_tags":True,"strip_symbols":True}
D_ITEMSBUILDING={"keyname":"D_ITEMSBUILDING","key_regex":"取扱物件","negativewords_left":NEGATIVEWORDS_LEFT_COMMON}



'''get_extra_d関数内'''
TEMP_TO_DICT={"tel":"D_TEL","fax":"D_FAX","":"D_TEL_or_FAX","tel、fax":"D_TEL_and_FAX"}

"""CATEGORIZE"""
LINKS_CATEGORIZE={"D_CONTACT":"^(?!.*mailto).*?(contact|問い合わせ)","D_FACEBOOK":"facebook.com","D_TWITTER":"twitter.com","D_LINEBIZ":"linebiz.com","D_YOUTUBE":"youtube.com","D_INSTAGRAM":"instagram.com"}
ADDRESS_CATEGORIZE={"D_JUUSHO":"","D_BUILDINGDB":"^(?!.*("+"|".join([D_SALES["key_regex"],D_SHIHONKIN["key_regex"]])+")).*?(\dL?DK|物件(?!に)|分譲|間取|入居|土地|売地|売約|見学会|一戸建|中古住宅|新築|万円)","D_TRANSFER":"移転|創業|地番変更|開設|設立|変更"}
