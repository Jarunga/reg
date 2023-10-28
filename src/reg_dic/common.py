VERBOSE_NAME={'D_JUUSHO':'住所','D_DAIHYOSHA':'代表者','D_TANTOUSHA':'担当者','D_REGISTERNO':'登録番号','D_LICENSE':'有資格者',
              'D_SALES':'売上高','D_AUTH':'認証','D_SHIHONKIN':'資本金','D_SOUGYO':'創業年月','D_SETSURITSU':'設立年月',
              'D_SOUSETSU':'創設年月','D_SOURITSU':'創立年月','D_JUGYOIN':'従業員','D_CARS':'車両台数','D_CAPACITY':'定員',
              'D_KESSAN':'決算期','D_OWNBANK':'取引銀行','D_MAINCUSTOMERS':'主要取引先','D_MAINSUPLIERS':'主要仕入先',
              'D_EXPLANATION':'事業内容','D_HOJINNAME':'法人名','D_PARTNERSHIP':'業務提携','D_SUBCONTRACTING':'業務委託先',
              'D_GROUPCAMPANIES':'関連会社','D_DANTAI':'加盟団体','D_INSURANCE':'加入保険','D_HOSHOKYOKAI':'保証協会',
              'D_ITEMS':'営業品目','D_ITEMSBUILDING':'取扱物件'}

COLUMNS_VERBOSE_NAME={'hojinno':'法人番号','kensetsuno':'建設業許可番号','kyokatype':'許可区分','hojinname':'法人名',
                      'hojinkana':'法人名カナ','honjineng':'法人名英語','hontenjuusho':'本店所在地',
                      'kcd':'都道府県番号','cd':'自治体コード','pcd':'郵便番号','adr4':'それ以降の住所',
                      'mailaddress':'メールアドレス','tel':'電話番号','fax':'FAX番号','name':'名称','href':'取得元URL','setsuritsu':'設立',
                      'daihyoshaname':'代表者名','shihonkin':'資本金','jugyoin':'従業員数','homepage':'ホームページ','getdate':'情報取得日',
                      'sales':'売上','tantousha_name':'担当者名','category':'業種','juusho':'住所','adr1':'都道府県名',
                      'dainame':'大分類','chuname':'中分類','shoname':'小分類','sainame':'細分類'}

SYMBOLS='[!"\'#$%&\'\\\\()*+,./:;<=>?@[\\]^_`{|}~「」［］〔〕“”〈〉『』《》【】●■◇◆□◉＆＊※：・（）／＄＃→＠。、？！｀＋￥％　 \xa0\t\u202F\u00A0]'

HYPHENS='-−－﹣−‐⁃‑‒–—﹘―⎯⏤ーｰ─━－-'#全角に直すべき？？

KOBUKISHU = str.maketrans(
    "⺃⺅⺉⺋⺎⺏⺐⺒⺓⺔⺖⺘⺙⺛⺟⺠⺡⺢⺣⺦⺨⺫⺬⺭⺱⺲⺹⺾⻁⻂⻃⻄⻍⻏⻑⻒⻖⻘⻟⻤⻨⻩⻫⻭⻯⻲⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕戶黑",
    "乚亻刂㔾兀尣尢巳幺彑忄扌攵旡母民氵氺灬丬犭罒示礻罓罒耂艹虎衤覀西辶阝長镸阝青飠鬼麦黄斉歯竜亀一丨丶丿乙亅二亠人儿入八冂冖冫几凵刀力勹匕匚匸十卜卩厂厶又口囗土士夂夊夕大女子宀寸小尢尸屮山巛工己巾干幺广廴廾弋弓彐彡彳心戈戸手支攴文斗斤方无日曰月木欠止歹殳毋比毛氏气水火爪父爻爿片牙牛犬玄玉瓜瓦甘生用田疋疒癶白皮皿目矛矢石示禸禾穴立竹米糸缶网羊羽老而耒耳聿肉臣自至臼舌舛舟艮色艸虍虫血行衣襾見角言谷豆豕豸貝赤走足身車辛辰辵邑酉釆里金長門阜隶隹雨靑非面革韋韭音頁風飛食首香馬骨高髟鬥鬯鬲鬼魚鳥鹵鹿麥麻黃黍黒黹黽鼎鼓鼠鼻齊齒龍龜龠戸黒",
)
