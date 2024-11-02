#type: ignore
from math import sqrt,factorial
from typing import overload
from builtins import range as builtin_range
import struct
_A='clamp'
def reverse_number(number):return int(str(number)[::-1])
def hypotenuse(a,b):return sqrt(a**2+b**2)
def quadratic_roots(a,b,c):return(-b+sqrt(b**2-4*a*c))/(2*a)
def check_perfect_number(number):
 A=number
 if A<1:return False
 B=0
 for C in range(1,A):
  if A%C==0:B+=C
 return B==A
def factorial_iterative(number):
 A=1
 for B in builtin_range(1,number+1):A*=B
 return A
def binomial_coefficient(n,k):return factorial(n)/(factorial(k)*factorial(n-k))
def calculate_combinations(n,k):return factorial(n)/(factorial(k)*factorial(n-k))
def generate_fibonacci_sequence(number):
 A=[1,1]
 for B in builtin_range(2,number):A.append(A[B-1]+A[B-2])
 return A
def check_armstrong_number(number):A=number;return sum(int(B)**len(str(A))for B in str(A))==A
def calculate_gcd(a,b):
 while b!=0:a,b=b,a%b
 return a
def factorial_recursive(number):
 A=number
 if A<0:raise ValueError('Input number must be non-negative.')
 if A<=1:return 1
 else:return A*factorial_recursive(A-1)
def fibonacci(n):
 if n<=0:return[]
 elif n==1:return[0]
 elif n==2:return[0,1]
 else:
  A=[0,1]
  while len(A)<n:B=A[-1]+A[-2];A.append(B)
  return A
def range(start,stop=None,step=1):
 C=step;B=stop;A=start
 if B is None:B=A;A=0
 if A>B and C>0 or A<B and C<0:C=-C
 return builtin_range(A,B,C)
def divide_by_power_of_2(int,divider):return int>>divider
def calculate_percentage(value,total):return int(value/total*100)
def get_pi(amount):
 A=amount
 if A==1:return 3
 elif A==0:return 0
 elif A<0:return float(return_like_a_thousand_digits_of_pi()[:A])
 else:return float(return_like_a_thousand_digits_of_pi()[:A+1])
def smaller(a,b):
 if a<b:return a
 else:return b
def bigger(a,b):
 if a>b:return a
 else:return b
def return_like_a_thousand_digits_of_pi():return'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525720106548586327886593615338182796823030195203530185296899577362259941389124972177528347913151557485724245415069595082953311686172785588907509838175463746493931925506040092770167113900984882401285836160356370766010471018194295559619894676783744944825537977472684710404753464620804668425906949129331367702898915210475216205696602405803815019351125338243003558764024749647326391419927260426992279678235478163600934172164121992458631503028618297455570674983850549458858692699569092721079750930295532116534498720275596023648066549911988183479775356636980742654252786255181841757467289097777279380008164706001614524919217321721477235014144197356854816136115735255213347574184946843852332390739414333454776241686251898356948556209921922218427255025425688767179049460165346680498862723279178608578438382796797668145410095388378636095068006422512520511739298489608412848862694560424196528502221066118630674427862203919494504712371378696095636437191728746776465757396241389086583264599581339047802759009946576407895126946839835259570982582262052248940772671947826848260147699090264013639443745530506820349625245174939965143142980919065925093722169646151570985838741059788595977297549893016175392846813826868386894277415599185592524595395943104997252468084598727364469584865383673622262609912460805124388439045124413654976278079771569143599770012961608944169486855584840635342207222582848864815845602850601684273945226746767889525213852254995466672782398645659611635488623057745649803559363456817432411251507606947945109659609402522887971089314566913686722874894056010150330861792868092087476091782493858900971490967598526136554978189312978482168299894872265880485756401427047755513237964145152374623436454285844479526586782105114135473573952311342716610213596953623144295248493718711014576540359027993440374200731057853906219838744780847848968332144571386875194350643021845319104848100537061468067491927819119793995206141966342875444064374512371819217999839101591956181467514269123974894090718649423196156794520809514655022523160388193014209376213785595663893778708303906979207734672218256259966150142150306803844773454920260541466592520149744285073251866600213243408819071048633173464965145390579626856100550810665879699816357473638405257145910289706414011097120628043903975951567715770042033786993600723055876317635942187312514712053292819182618612586732157919841484882916447060957527069572209175671167229109816909152801735067127485832228718352093539657251210835791513698820914442100675103346711031412671113699086585163983150197016515116851714376576183515565088490998985998238734552833163550764791853589322618548963213293308985706420467525907091548141654985946163718027098199430992448895757128289059232332609729971208443357326548938239119325974636673058360414281388303203824903758985243744170291327656180937734440307074692112019130203303801976211011004492932151608424448596376698389522868478312355265821314495768572624334418930396864262434107732269780280731891544110104468232527162010526522721116603966655730925471105578537634668206531098965269186205647693125705863566201855810072936065987648611791045334885034611365768675324944166803962657978771855608455296541266540853061434443185867697514566140680070023787765913440171274947042056223053899456131407112700040785473326993908145466464588079727082668306343285878569830523580893306575740679545716377525420211495576158140025012622859413021647155097925923099079654737612551765675135751782966645477917450112996148903046399471329621073404375189573596145890193897131117904297828564750320319869151402870808599048010941214722131794764777262241425485454033215718530614228813758504306332175182979866223717215916077166925474873898665494945011465406284336639379003976926567214638530673609657120918076383271664162748888007869256029022847210403172118608204190004229661711963779213375751149595015660496318629472654736425230817703675159067350235072835405670403867435136222247715891504953098444893330963408780769325993978054193414473774418426312986080998886874132604721569516239658645730216315981931951673538129741677294786724229246543668009806769282382806899640048243540370141631496589794092432378969070697794223625082216889573837986230015937764716512289357860158816175578297352334460428151262720373431465319777741603199066554187639792933441952154134189948544473456738316249934191318148092777710386387734317720754565453220777092120190516609628049092636019759882816133231666365286193266863360627356763035447762803504507772355471058595487027908143562401451718062464362679456127531813407833033625423278394497538243720583531147711992606381334677687969597030983391307710987040859133746414428227726346594704745878477872019277152807317679077071572134447306057007334924369311383504931631284042512192565179806941135280131470130478164378851852909285452011658393419656213491434159562586586557055269049652098580338507224264829397285847831630577775606888764462482468579260395352773480304802900587607582510474709164396136267604492562742042083208566119062545433721315359584506877246029016187667952406163425225771954291629919306455377991403734043287526288896399587947572917464263574552540790914513571113694109119393251910760208252026187985318877058429725916778131496990090192116971737278476847268608490033770242429165130050051683233643503895170298939223345172201381280696501178440874519601212285993716231301711444846409038906449544400619869075485160263275052983491874078668088183385102283345085048608250393021332197155184306354550076682829493041377655279397517546139539846833936383047461199665385815384205685338621867252334028308711232827892125077126294632295639898989358211674562701021835646220134967151881909730381198004973407239610368540664319395097901906996395524530054505806855019567302292191393391856803449039820595510022635353619204199474553859381023439554495977837790237421617271117236434354394782218185286240851400666044332588856986705431547069657474585503323233421073015459405165537906866273337995851156257843229882737231989875714159578111963583300594087306812160287649628674460477464915995054973742562690104903778198683593814657412680492564879855614537234786733039046883834363465537949864192705638729317487233208376011230299113679386270894387993620162951541337142489283072201269014754668476535761647737946752004907571555278196536213239264061601363581559074220202031872776052772190055614842555187925303435139844253223415762336106425063904975008656271095359194658975141310348227693062474353632569160781547818115284366795706110861533150445212747392454494542368288606134084148637767009612071512491404302725386076482363414334623518975766452164137679690314950191085759844239198629164219399490723623464684411739403265918404437805133389452574239950829659122850855582157250310712570126683024029295252201187267675622041542051618416348475651699981161410100299607838690929160302884002691041407928862150784245167090870006992821206604183718065355672525325675328612910424877618258297651579598470356222629348600341587229805349896502262917487882027342092222453398562647669149055628425039127577102840279980663658254889264880254566101729670266407655904290994568150652653053718294127033693137851786090407086671149655834343476933857817113864558736781230145876871266034891390956200993936103102916161528813843790990423174733639480457593149314052976347574811935670911013775172100803155902485309066920376719220332290943346768514221447737939375170344366199104033751117354719185504644902636551281622882446257591633303910722538374218214088350865739177150968288747826569959957449066175834413752239709683408005355984917541738188399944697486762655165827658483588453142775687900290951702835297163445621296404352311760066510124120065975585127617858382920419748442360800719304576189323492292796501987518721272675079812554709589045563579212210333466974992356302549478024901141952123828153091140790738602515227429958180724716259166854513331239480494707911915326734302824418604142636395480004480026704962482017928964766975831832713142517029692348896276684403232609275249603579964692565049368183609003238092934595889706953653494060340216654437558900456328822505452556405644824651518754711962184439658253375438856909411303150952617937800297412076651479394259029896959469955657612186561967337862362561252163208628692221032748892186543648022967807057656151446320469279068212073883778142335628236089632080682224680122482611771858963814091839036736722208883215137556003727983940041529700287830766709444745601345564172543709069793961225714298946715435784687886144458123145935719849225284716050492212424701412147805734551050080190869960330276347870810817545011930714122339086639383395294257869050764310063835198343893415961318543475464955697810382930971646514384070070736041123735998434522516105070270562352660127648483084076118301305279320542746286540360367453286510570658748822569815793678976697422057505968344086973502014102067235850200724522563265134105592401902742162484391403599895353945909440704691209140938700126456001623742880210927645793106579229552498872758461012648369998922569596881592056001016552563756'
def fast_inverse_sqrt(x):C=1.5;A=x;D=struct.pack('f',A);B=struct.unpack('i',D)[0];B=1597463007-(B>>1);E=struct.pack('i',B);A=struct.unpack('f',E)[0];A=A*(C-.5*x*A*A);return A
def tetration(base,exponent):
 A=exponent
 if A==0:return 1
 B=base
 while A>1:B=base**B;A-=1
 return B
def hexation(base,exponent):
 A=exponent
 if A==0:return 1
 B=base
 while A>1:B=tetration(base,B);A-=1
 return B
def round_with_precision(number,digits=0):A=10**digits;B=int(number*A)/A;return B
def find_divisors(x):
 A=[]
 for B in builtin_range(1,x+1):
  if x%B==0:A.append(B)
 return A
class Vector:
 def __init__(A,*B):A.components=list(B)
 def __repr__(A):return f"Vector{tuple(A.components)}"
 def __len__(A):return len(A.components)
 def __getitem__(A,index):return A.components[index]
 def __eq__(B,other):
  A=other
  if not isinstance(A,Vector):return False
  return B.components==A.components
 def __add__(A,other):
  B=other
  if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for addition.')
  C=[A+B for(A,B)in zip(A.components,B.components)];return Vector(*C)
 def __sub__(A,other):
  B=other
  if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for subtraction.')
  C=[A-B for(A,B)in zip(A.components,B.components)];return Vector(*C)
 def dot(A,other):
  B=other
  if len(A)!=len(B):raise ValueError('Vectors must have the same dimension for dot product.')
  return sum(A*B for(A,B)in zip(A.components,B.components))
 def magnitude(A):return sqrt(sum(A**2 for A in A.components))
 def normalize(A):
  B=A.magnitude()
  if B==0:raise ValueError('Cannot normalize a zero vector.')
  return Vector(*[A/B for A in A.components])
def bottom_clamp(min,value):A=value;return A if A>min else min
def top_clamp(max,value):A=value;return A if A<max else max
@overload
def clamp(min,max,value):0
@overload
def clamp(min,max,value):0
def clamp(min,max,value):
 A=value
 if A<min:return min
 elif A>max:return max
 else:return A
def sign(x):return 1 if x>0 else-1 if x<0 else 0
def is_number_similar(a,b,similarity):return abs(a-b)<=similarity
__all__=['reverse_number','hypotenuse','quadratic_roots','check_perfect_number','factorial_iterative','binomial_coefficient','calculate_combinations','generate_fibonacci_sequence','check_armstrong_number','calculate_gcd','factorial_recursive','fibonacci','range','divide_by_power_of_2','calculate_percentage','get_pi','smaller','bigger','return_like_a_thousand_digits_of_pi','fast_inverse_sqrt','tetration','hexation','round_with_precision','find_divisors','Vector','bottom_clamp','top_clamp',_A,_A,_A,'sign','is_number_similar']