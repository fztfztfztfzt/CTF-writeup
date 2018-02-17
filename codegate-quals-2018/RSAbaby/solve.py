enc = 380838525806255337893946743050327173947433371586247814759050430578204300094635270877953690129762202769875996939276197842147224857220372679703619497806927398399795108952962442891905146440202908075035070979097412854358636621348531277713225298087614167276769631514565642627640343771883615641654535423058064397195504442204533423747451626752470200734177912209703945585196661670059908372263823148356525332391696830864610833871912286943309315368473809329884078356658600058695228563250424729883958206468130236010169302227516477051342268478958591705205358855157076547042386496593253499052139707216013118968009859098636706611794339780312391554420587540660796607687910531233690474314728367495027785278881971814489961127141923005420385579115964806930701533734013794866357390109761177291603859980361697959155126598284421792362843501361967548503757576918138895493498276658301936707818035503138088925361983300854592909022681075014994189523262500924039153521343614460622246152945716505290603455309333333560506091410274263241508522602811994582040578653226240563907254131889033343189265841619698442130035569880428826546382882121430886993470180883869383405219173399698928360778092640513571913940390199302310817294277155376000921294944591121246587133744

N =  523639805914061918270627443134741619704989339108811345591765650823383811679404400743730300288077320843234806116907796484315512386749183735427076044515394957782722144465236043561036957495670530886847413432636828661793513741180618385135095922719611444315861194066682307139969523206842728092440966461922557111209480112023032164065707216752568624317883094770784553451376502893748762652573604180632157059219119741129827017117558208565054860250853978397405747507844727903363351081745897472675235414693294079400158465019978970101063161094836772073302365997371679643083941089269169502839517043186914783290465318781726781533226599462066259256698885200843104424722505593942510854302401488139137362276492532699951880474157691347473741517183512613811731637427562990396497067805682564174185792379491573312640862381843195615293946630128509982267460922475624107750277459002662884836031305873522960659017891138316482378312004790485681371129328860344989214941450460756203906709954285455206483931555441550631622907560476932030275168094874500348941952385811045752980245084909805234648503736291123092594689494187215718382724496356220857628352007757197464098872772987476828030721472777531411032286344430474215475330008833588291692767417022829531866323051

g =  14511485561279877242490049924164262671564856980418706493772866848857612385453104346586350276227873984815502106112389832011566814347565705873657427101510533972939335373118027470906354834216983842099812965592939768854241417529908124711818216182341332507918374220901579987851767888710421089266081280013256600425746557269742268670300714949183260246617797156425767983027415373581836147225552931559016487193903056680274018867169067069164417868649729813464306199388375773268972224468436723728788928618254041886532217172217283880677562744928063668302190530092708676086756514664006766909499651097644447881334032649057611965077951245778537347658519214651268439995915614667939336569800565797702566887133370244643122543689011224353239395653153094885449557256699923700742653930928887024447374907536229536501931493386170594869542262576409686250950887746501725676758035668270309685358291271363775138099327895323451901829587908987436831617628346535627562925010698445652286450107659802164994355539623617745529876829000553355956755914526849056343372137493951531663650121127924626353148067965144997177441402726593083629261964699315644045714647617156724816370270635144953182744245498998992807987174252376199074131496163299914588620694929584594866873400406185502626180264465104468365933575409921644759774899908018217623256295871823903858740112075223018089096313796599554636163186830200265892525403238639070366999401808068998639590975305617369688731214141047568939908240058088089504343104889824160334560324387496383256518400827927341943755279126157377196722373876343583757261084975726106468397487366825775319965557539853162973895788663508023419482720093445137085452233528426725965549266605359644884153719762909553953900709890192728260024241748671796401590112629479273363064208874240854298225057415248756216847693518038319188675206377870041466557414694779134628404260587970

from gmpy2 import *
from Crypto.Util.number import *
import binascii
e = 65537
kp = pow(2,e*g,N)*pow(2,0xdeadbeef-1,N)
p = gcd(kp-1,N)
q = N//p
phi = (p-1)*(q-1)
d = inverse(e,phi)
flag = pow(enc,d,N)
print(binascii.unhexlify(hex(flag)[2:]))