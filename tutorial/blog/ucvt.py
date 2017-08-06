#!/bin/sh
#import language_check

import re,math
from nltk import sent_tokenize, word_tokenize,RegexpParser
from string import punctuation
from nltk.corpus import stopwords
#from nltk.tag.stanford import StanfordPOSTagger
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tag.perceptron import PerceptronTagger
#from nltk.tag.hunpos import HunposTagger
import os.path


from collections import Counter



tagger1=PerceptronTagger()
porter_stemmer = PorterStemmer()
#path_to_model = r"D:\stanford-postagger\models\english-bidirectional-distsim.tagger"
#path_to_jar = r"D:\stanford-postagger\stanford-postagger.jar"
#tagger=StanfordPOSTagger(path_to_model, path_to_jar)
v1="Errors and suggestions:\n"
#tool = language_check.LanguageTool('en-US')

#path_to_model = "~/uca/tutorial/blog/english.model"
#path_to_bin="~/uca/tutorial/blog/hunpos-tag.exe"
#script_dir = os.path.dirname(__file__)

#path1=os.path.join(path_to_model)
#path2=os.path.join(path_to_bin)
#tagger = HunposTagger(path1,path2)
tagger=PerceptronTagger()
WORD = re.compile(r'\w+')


from math import*
 
def get_cosine(vec1, vec2):
     
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator


def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)    




def propernouncheck(a):
    #print(path1)
    if len(a)<0:
        return
    sent=sent_tokenize(a)
    for s in sent:
        tokens=word_tokenize(s)
        tagged=tagger.tag(tokens)
        for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
        b=[tagged[0][0].lower()]
        c=tagger.tag(b)
        if c[0][1]=="NN" or c[0][0]=="system":
            tagged[0]=(tagged[0][0],"NN")
        p=[w for w,p in tagged if p in ["NNP'","NNPS'"]]
        if p:
        #print(p)
            global v1
            v1=v1+"</br><b>"+str(p)+"</b>Please remove these proper nouns.\n</br>"
        #print(" : Please remove these proper nouns")

def synonymcheck(a):
    a=a.lower()
    if len(a)<0:
        return
    a=''.join(c for c in a if c not in punctuation)
    tokens=word_tokenize(a)
    tagged=tagger1.tag(tokens)
    p=[w for w,p in tagged if p in ['NN']]
    for words in p:
        syn = wn.synsets(words)
        if syn:
            res=syn[0].lemma_names()
            for snms in res:
                if snms in p and snms!=words:
                    p[:] = (value for value in p if value != words)
                    p[:] = (value for value in p if value != snms)
                    global v1
                    v1=v1+"\n</br><b>"+str(words)+"</b> "+str(snms)+"These might be synonyms.\n</br>"


def pronouncheck(a):
    if len(a)<0:
        return
    a=''.join(c for c in a if c not in punctuation)
    tokens=word_tokenize(a)
    tagged=tagger1.tag(tokens)
    p=[w for w,p in tagged if p=='PRP']
    if p:
        global v1
        v1=v1+"</br><b>"+str(p)+"</b>Please remove these personal pronouns.\n</br>"
        #print(p)
        #print(" :Please remove these personal pronouns")


def tensecheck(a):
    if len(a)<0:
        return
    a=''.join(c for c in a if c not in punctuation)
    tokens=word_tokenize(a)
    tagged=tagger1.tag(tokens)
    l=["VBD","MD","RB","RBR","JJS","CC","RBS"]
    p=[w for w,p in tagged if p in l]
    if p:
        global v1
        v1=v1+"</br><b>"+str(p)+"</b>"+"</br>Please improve tenses,conjunctions and/or adverbs.</br>\n"
        #print(p)
        #print(" :Please improve tenses and/or adverbs")


def tensecheck1(a):
    if len(a)<0:
        return
    a=''.join(c for c in a if c not in punctuation)
    tokens=word_tokenize(a)
    tagged=tagger1.tag(tokens)
    l=["VBD","MD","RB","RBR","JJS","CC","RBS"]
    p=[w for w,p in tagged if p in l]
    if p:
        global v1
        v1=v1+"</br><b>"+str(p)+"</b>"+"</br>Please improve tenses,conjunctions and/or adverbs.</br>\n"


def declcheck(a):
    if len(a)<0:
        return
    tokens=word_tokenize(a)
    l=["?","!",";"]
    p=[w for w in tokens if w in l]
    if p:
        global v1
        v1=v1+"</br><b>"+str(p)+"</b>"+"Please write only declarative sentences.</br>\n"

def postcheck(a):
    if len(a)<0:
        return
    #matches=tool.check(a)
    #if len(matches)>0 :
        #for m in matches:
             
            #if not str(m.ruleId) =="MORFOLOGIK_RULE_EN_US" and not str(m.ruleId)=='A_INFINITVE' and not str(m.ruleId)=='SENTENCE_FRAGMENT' and not str(m.ruleId)=='ENGLISH_WORD_REPEAT_BEGINNING_RULE' and not str(m.ruleId)=='COMMA_PARENTHESIS_WHITESPACE' and not str(m.ruleId)=='WHITESPACE_RULE':
                #global v1
                #v1=v1+"</br>Check grammar: "+str(m.ruleId)+" "+str(m.replacements)+"\n</br>"
                #print(str(m.ruleId)+" "+str(m.replacements)+"\n")
    
    propernouncheck(a)
    pronouncheck(a)



def precheck(a):
    if len(a)<0:
        return
    #matches=tool.check(a)
    #if len(matches)>0 :
        #for m in matches:
            #if not str(m.ruleId) =="MORFOLOGIK_RULE_EN_US" and not str(m.ruleId)=='A_INFINITVE' and not str(m.ruleId)=='SENTENCE_FRAGMENT' and not str(m.ruleId)=='ENGLISH_WORD_REPEAT_BEGINNING_RULE' and not str(m.ruleId)=='COMMA_PARENTHESIS_WHITESPACE' and not str(m.ruleId)=='WHITESPACE_RULE':
                #global v1
                #v1=v1+"</br>Check grammar: "+str(m.ruleId)+" "+str(m.replacements)+"\n</br>"
                #print(str(m.ruleId)+" "+str(m.replacements)+"\n")
    #checkpassive(a)
    propernouncheck(a)
    pronouncheck(a)
    



        
def guicheck(a):
    a=a.lower()
    if len(a)<0:
        return
    tokens=word_tokenize(a)
    p=[w for w in tokens]
    gui={"checkbox", "radio button","radiobutton", "dropdown list","dropdownlist", "list box","listbox", "button", "toggle", "text field","textfield" ,"datefield","date field","breadcrumb", "slider", "search field","pagination","slider","tag","icon"}
    for a in p:
        if a in gui:
            global v1
            v1=v1+"</br>"+str(a)+"</br> <b>GUI elements not allowed.</b>\n</br>"
            #print(a+" : gui not allowed")
        
def nfrcheck(a):
    a=a.lower()
    if len(a)<0:
        return
    tokens=word_tokenize(a)
    p=[w for w in tokens]
    gui={"performance", "security","scalable","scalability","availability","regulatory","manageable", "manageability","environmental", "integrity","usable","usability","interoperable","interoperability"}
    for a in p:
        if a in gui:
            global v1
            v1=v1+str(a)+"</br> <b>Non functional requirements not allowed.</b>\n</br>"
            #print(a+" : gui not allowed")



def compare(s1,s2):
     
    s1=s1.lower()
    if len(s1)<0:
        return
    s1=''.join(c for c in s1 if c not in punctuation)
    tokens=word_tokenize(s1)
    tagged=tagger.tag(tokens)
    for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
    p1=[w for w,p in tagged if p in ["NN"]]
    print(str(p1)+"mayank")
    s2=s2.lower()
    if len(s2)<0:
        return
    s2=''.join(c for c in s2 if c not in punctuation)
    tokens1=word_tokenize(s2)
    tagged1=tagger.tag(tokens1)
    for x in range(len(tagged1)):
            tagged1[x]=(tagged1[x][0],str(tagged1[x][1]))
    p2=[w for w,p in tagged1 if p in ["NN"]]
    print(str(p2)+"laddha")
    gg=False
    for e in p1:
         if e in p2:
              gg=True
    if gg is False:
         global v1
         v1=v1+"</br><b>Alternate flow sentence </b>"+s1+".<b> and basic flow sentence: </b>"+s2+".<b> do not match.</b></br>"
          
         


def comparecs1(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return
    ls1 = re.sub("[^a-zA-Z]", " ", s1)
    ls2 = re.sub("[^a-zA-Z]", " ", s2)
    vector1 = text_to_vector(ls1)
    vector2 = text_to_vector(ls2)
    cosine = get_cosine(vector1, vector2)
    print(cosine)
    if cosine<0.6:
        global v1
        v1=v1+"There is a mismatch between requirements and use case description.\n</br>"
        

def comparecs2(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return
    ls1 = re.sub("[^a-zA-Z]", " ", s1)
    ls2 = re.sub("[^a-zA-Z]", " ", s2)
    vector1 = text_to_vector(ls1)
    vector2 = text_to_vector(ls2)
    cosine = get_cosine(vector1, vector2)
    if cosine<0.6:
        return False
    return True

        



def compare1(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return
    ls1 = re.sub("[^a-zA-Z]", " ", s1)
    ls2 = re.sub("[^a-zA-Z]", " ", s2)
    words1 = ls1.lower().split()
    words2 = ls2.lower().split()
    stops = set(stopwords.words("english"))
    m1 = [w for w in words1 if not w in stops]
    m2 = [w for w in words2 if not w in stops]
    for i in range(len(m1)):
        m1[i] = porter_stemmer.stem(m1[i])
    for i in range(len(m2)):
        m2[i] = porter_stemmer.stem(m2[i])
    aset=set(m1)
    bset=set(m2)
    inter=aset.intersection(bset)
    unio=aset.union(bset)
    jsim=len(inter)/len(unio)
    if jsim < 0.3 :
        global v1
        v1=v1+"There is a mismatch between requirements and use case description.\n</br>"


def compare2(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return True
    ls1 = re.sub("[^a-zA-Z]", " ", s1)
    ls2 = re.sub("[^a-zA-Z]", " ", s2)
    words1 = ls1.lower().split()
    words2 = ls2.lower().split()
    stops = set(stopwords.words("english"))
    m1 = [w for w in words1 if not w in stops]
    m2 = [w for w in words2 if not w in stops]
    for i in range(len(m1)):
        m1[i] = porter_stemmer.stem(m1[i])
    for i in range(len(m2)):
        m2[i] = porter_stemmer.stem(m2[i])
    aset=set(m1)
    bset=set(m2)
    inter=aset.intersection(bset)
    unio=aset.union(bset)
    jsim=len(inter)/len(unio)
    if jsim < 0.36 :
        return False
    return True

def compare3(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return True
    ls1 = re.sub("[^a-zA-Z]", " ", s1)
    ls2 = re.sub("[^a-zA-Z]", " ", s2)
    words1 = ls1.lower().split()
    words2 = ls2.lower().split()
    stops = set(stopwords.words("english"))
    m1 = [w for w in words1 if not w in stops]
    m2 = [w for w in words2 if not w in stops]
    for i in range(len(m1)):
        m1[i] = porter_stemmer.stem(m1[i])
    for i in range(len(m2)):
        m2[i] = porter_stemmer.stem(m2[i])
    aset=set(m1)
    bset=set(m2)
    inter=aset.intersection(bset)
    unio=aset.union(bset)
    jsim=len(inter)/len(unio)
    if jsim < 0.36 :
        return False
    return True

def completeness(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return
    comparecs1(s1,s2)
    sent1=sent_tokenize(s1)
    sent2=sent_tokenize(s2)
    for w in range(len(sent1)):
        flag=False
        for w1 in range(len(sent2)):
            a=compare3(sent1[w],sent2[w1])
            print(a)
            if a is True:
                flag=True
        if flag is False:
             global v1
             v1=v1+"</br>"+"</br>"+"</br>"+sent1[w]+" </br><b>This information has not been shown in the use case description.</b></br></br>"
            
    
def completeness1(s1,s2):
     if len(s1)==0 or len(s2)==0:
        return
     sent1=sent_tokenize(s1)
     sent2=sent_tokenize(s2)
     prev=-1
     for w in range(len(sent1)):
        for w1 in range(len(sent2)):
            a=comparecs2(sent1[w],sent2[w1])
            print(a)
            if comparecs2(sent1[w],sent2[w1]) is True and  w1<prev:
                print(sent1[w]+" "+sent2[w1])
                global v1
                v1=v1+"There is an error in the ordering of the sentences in basic flow.</br>"
                return
            else:
                prev=w1
     

        
def checkpassive(a):
    if len(a)<1:
        return
    tokens=word_tokenize(a)
    tagged=tagger1.tag(tokens)
    chunkGram=r"""Error: {<VBZ><VBN>} """
    chunkparser=RegexpParser(chunkGram)
    chunked=chunkparser.parse(tagged)
    w=[k for k in chunked.subtrees(filter=lambda x: x.label()=='Error')]
    #print(bool(w))
    for i in chunked.subtrees(filter=lambda x: x.label() == 'Error'):
        print(str(i)+" Passive voice is there avoid it.\n</br>")
        global v1
        v1=v1+"</br>"+str(i)+":</br><b>Passive voice is there avoid it.</b>\n</br>"
    


def checkifelse(a):
     sent=sent_tokenize(a)
     global v1
     for s in sent:
          s=s.lower()
          if not s.startswith("if"):
               if not s.startswith("extends"):
                    v1=v1+"</br>"+s+"<b>The given alternate flow sentence does not start with if.</b>"
     for s in sent:
          s=s.lower()
          if not "then" in s :
               if not s.startswith("extends"):
                    v1=v1+"</br>"+s+" <b>The given alternate flow sentence does not contain then.</b>"
               



def checkstruct(a):
    global v1
    #matches=tool.check(a)
    a=a.lower()
    if len(a)<1:
        return
    tokens=word_tokenize(a)
    if "extends" in tokens:
        v1=v1+"</br><b>Do not use extends in basic flow.</b>\n</br>"
    if len(tokens)==0:
        return
    tagged=tagger.tag(tokens)
    for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
    vn=["access","ache","act","address","aim","alert","answer","arrest","attack","auction",
"back","bail","balance","balloon","ban","bandage","bank","bare","bargain","battle","beam","bear","beat","bend","benefit","blame","blast","bleach","block","bloom","blow","board","bomb","bother","bounce","bow","box","bread","break","breed","broadcast","browse","brush","bump","burn","buy","cake","call","camp","care","catch","cause","challenge","change","chant","charge","cheat","check","cheer","chip","claim","clip","cloud","clue","coach","color","comb","comfort","contrast","control","cook","coop","copy","cost","count","cover","crack","crash","crate","credit","crush","cure","curl","curve","cut","cycle","dam","damage","dance","delay","delight","demand","dislike","display","dive","doubt","drain","draw","drink","drive","duck","deal","decay","decrease","design","dial","die","divorce","dock","double","dream","dress","drill","dump","dust","dye","echo","email","end","escape","esteem","estimate","exchange","excuse","exhibit","experience","eye","face","fall","favor","fax","fear","feel","fight","file","fill","film","finish","fish","fix","flap","flash","float","flood","floss","flow","flower","fly","fold","fool","force","form","frame","freeze","frown","function","garden","gaze","gel","glue","grate","grease","grill","grimace","grin","grip","guarantee","guard","guess","guide","hammer","hand","handle","harm","harness","hate","head","heap","heat","help","hide","highlight","hike","hit","hold","hop","hope","hose","hug","humor","hunt","hurry","ice","impact","inch","increase","influence","insult","interest","iron",
    "jail",
    "jam",
    "joke",
    "judge",
    "jump",
    "keep",
    "kick",
    "knit",
    "knock",
    "knot",
    "label",
    "land",
    "last",
    "laugh",
    "lead",
    "leap",
    "level",
    "license",
    "lie",
    "lift",
    "light",
    "limit",
    "link",
    "load",
    "loan",
    "lock",
    "look",
    "love",
    "mail",
    "make",
    "man",
    "march",
    "mark",
    "match",
    "mate",
    "matter",
    "mean",
    "measure",
    "milk",
    "mind",
    "mine",
    "miss",
    "mistake",
    "moor",
    "move",
    "mug",
    "nail",
    "name",
    "need",
    "nest",
    "notch",
    "note",
    "notice",
    "number",
    "object",
    "offer",
    "oil",
    "order",
    "pack",
    "pad",
    "paddle",
    "paint",
    "park",
    "part",
    "pass",
    "paste",
    "pause",
    "pat",
    "pay",
    "pedal",
    "peel",
    "pelt",
    "permit",
    "phone",
    "photograph",
    "pick",
    "pine",
    "place",
    "plan",
    "plane",
    "plant",
    "play",
    "plow",
    "plug",
    "point",
    "poke",
    "pop",
    "post",
    "practice",
    "praise",
    "present",
    "process",
    "produce",
    "promise",
    "protest",
    "pull",
    "pump",
    "punch",
    "question",
    "quilt",
    "quiz",
    "race",
    "rain",
    "raise",
    "rant",
    "rate",
    "reach",
    "reason",
    "record",
    "reign",
    "rent",
    "repair",
    "reply",
    "report",
    "request",
    "rhyme",
    "ring",
    "riot",
    "risk",
    "rock", 
    "roll",
    "row",
    "ruin",
    "rule",
    "run",
    "sail",
    "sand",
    "saw",
    "scare",
    "scratch",
    "screw",
    "search",
    "season",
    "sense",
    "shampoo",
    "shape",
    "share",
    "shelter",
    "shock",
    "shop",
    "show",
    "sign",
    "signal",
    "silence",
    "sin",
    "sip",
    "skate",
    "sketch", 
    "ski",
    "slice",
    "slide",
    "slip",   
    "smell",
    "smile",
    "smirk",
    "smoke",
    "snack",
    "snow",
    "sound",
    "span",
    "spot",
    "spray",
    "sprout",
    "squash",
    "stain",
    "stamp",
    "stand",
    "star",
    "start",
    "state",
    "steer",
    "step",
    "sting",
    "stop",
    "store",
    "storm", 
    "stress",
    "strip",
    "stroke",
    "struggle",
    "study",
    "stuff",
    "stunt",
    "suit",
    "supply",
    "support",
    "surf",
    "surprise",
    "swap",
    "swing",
    "swivel",
    "tack",
    "talk",
    "taste",
    "tear",
    "tease",
    "telephone",
    "test",
    "thunder",
    "thought",
    "tick",
    "tie",
    "time",
    "tip",
    "tire",
    "toast",
    "touch",
    "tour",
    "tow",
    "trace",
    "track",
    "trade",
    "train",
    "transport",
    "trap",
    "travel",
    "treat",
    "trick",
    "trim",
    "trust",
    "tug",
    "turn",
    "twist",
    "type",
    "upstage",
    "use",
    "vacuum",
    "value",
    "view",
    "visit",
    "voice",
    "vote",
    "walk",
    "waltz",
    "wake",
    "watch",
    "water",
    "wave",
    "wear",
    "whip",
    "whisper",
    "whistle",
    "wick",
    "wink", 
    "wire",
    "wish",
    "work",
    "worry",
    "wrap",
    "wreck",
    "yawn",
    "yield",]        
    
    for x in range(len(tagged)):
            if tagged[x][0] in vn:
                tagged[x]=(tagged[x][0],"VB")
    print(tagged)
    print(tokens[0].lower())
    sstring=""
    ab=True
    for x in range(len(tagged)):
         sstring=sstring+tagged[x][1]
    if not re.search(r"^(DTNNVBZ|NNVBZ|DTNNNNS|NNNNS)",sstring):
        v1=v1+"</br><b>Basic Flow:</b> Plaese check this sentence for structure:"+" "+a+"</br>"
        ab=False
    print("mayank laddha"+sstring)
    #if len(matches)>0 :
        #for m in matches:
            #if not str(m.ruleId) =="MORFOLOGIK_RULE_EN_US" and not str(m.ruleId)=='A_INFINITVE' and not str(m.ruleId)=='SENTENCE_FRAGMENT' and not str(m.ruleId)=='ENGLISH_WORD_REPEAT_BEGINNING_RULE' and not str(m.ruleId)=='COMMA_PARENTHESIS_WHITESPACE' and not str(m.ruleId)=='WHITESPACE_RULE':
                #v1=v1+"<b></br>Basic Flow Check grammar:</b></br> "+a+str(m.ruleId)+" "+str(m.replacements)+"</br>"
                #print(str(m.ruleId)+" "+str(m.replacements)+"\n")
    p=[p for w,p in tagged]
    t=True
    if tokens[0].lower() is not "includes":
        chunkGram=r"""Error: {<DT>?<NN><VBZ>?<NNS>?<DT>?} """
        chunkparser=RegexpParser(chunkGram)
        chunked=chunkparser.parse(tagged)
        w=[k for k in chunked.subtrees(filter=lambda x: x.label()=='Error')]
        t=bool(w)
    if tokens[0].lower() is  "includes":
        chunkGram=r"""Error: {<VBZ><VB>} """
        chunkparser=RegexpParser(chunkGram)
        chunked=chunkparser.parse(tagged)
        u=[k for k in chunked.subtrees(filter=lambda x: x.label()=='Error')]
        t=bool(u)
    if not t and ab is True:
        v1=v1+"</br><b>Basic Flow:</b> Plaese check this sentence for structure:"+" "+a+"</br>"
        

def checkstruct1(a):
    global v1
    matches=tool.check(a)
    a=a.lower()
    if len(a)<1:
        return
    tokens=word_tokenize(a)
    if "includes" in tokens:
        v1=v1+"</br><b>Do not use includes in alternate flow.</b></br>"        
    if len(tokens)==0:
        return
    tagged=tagger.tag(tokens)
    for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
    
    #if len(matches)>0 :
        #for m in matches:
            #if not str(m.ruleId) =="MORFOLOGIK_RULE_EN_US" and not str(m.ruleId)=='A_INFINITVE' and not str(m.ruleId)=='SENTENCE_FRAGMENT' and not str(m.ruleId)=='ENGLISH_WORD_REPEAT_BEGINNING_RULE' and not str(m.ruleId)=='COMMA_PARENTHESIS_WHITESPACE' and not str(m.ruleId)=='WHITESPACE_RULE':
                #v1=v1+"</br><b>Alternate flow: check grammar</b> "+str(m.ruleId)+" "+str(m.replacements)+"\n</br>"
                #print(str(m.ruleId)+" "+str(m.replacements)+"\n</br>")



def pfinal():
    global v1
    #print(v1)
    return v1

def pinit():
    global v1
    v1=""


def sentstructure(b):
    #a=m1=T.get("1.0",'end-1c')
    sent=sent_tokenize(b)
    propernouncheck(b)
    tensecheck(b)
    checkpassive(b)
    pronouncheck(b)
    guicheck(b)
    nfrcheck(b)
    declcheck(b)
    synonymcheck(b)
    for s in sent:
        checkstruct(s)


def sentstructure1(b):
    #a=m1=T.get("1.0",'end-1c')
    sent=sent_tokenize(b)
    propernouncheck(b)
    #tensecheck(b)
    #checkpassive(b)
    pronouncheck(b)
    guicheck(b)
    nfrcheck(b)
    declcheck(b)
    synonymcheck(b)
    for s in sent:
        checkstruct1(s)





def checkname(b):
    b=b.lower()
    global v1
    #a=m2=T3.get("1.0",'end-1c')
    tokens=word_tokenize(b)
    if len(tokens) is 0:
        return
    tagged= tagger.tag(tokens)
    vn=["access","ache","act","address","aim","alert","answer","arrest","attack","auction",
"back","bail","balance","balloon","ban","bandage","bank","bare","bargain","battle","beam","bear","beat","bend","benefit","blame","blast","bleach","block","bloom","blow","board","bomb","bother","bounce","bow","box","bread","break","breed","broadcast","browse","brush","bump","burn","buy","cake","call","camp","care","catch","cause","challenge","change","chant","charge","cheat","check","cheer","chip","claim","clip","cloud","clue","coach","color","comb","comfort","contrast","control","cook","coop","copy","cost","count","cover","crack","crash","crate","credit","crush","cure","curl","curve","cut","cycle","dam","damage","dance","delay","delight","demand","dislike","display","dive","doubt","drain","draw","drink","drive","duck","deal","decay","decrease","design","dial","die","divorce","dock","double","dream","dress","drill","dump","dust","dye","echo","email","end","escape","esteem","estimate","exchange","excuse","exhibit","experience","eye","face","fall","favor","fax","fear","feel","fight","file","fill","film","finish","fish","fix","flap","flash","float","flood","floss","flow","flower","fly","fold","fool","force","form","frame","freeze","frown","function","garden","gaze","gel","glue","grate","grease","grill","grimace","grin","grip","guarantee","guard","guess","guide","hammer","hand","handle","harm","harness","hate","head","heap","heat","help","hide","highlight","hike","hit","hold","hop","hope","hose","hug","humor","hunt","hurry","ice","impact","inch","increase","influence","insult","interest","iron",
    "jail",
    "jam",
    "joke",
    "judge",
    "jump",
    "keep",
    "kick",
    "knit",
    "knock",
    "knot",
    "label",
    "land",
    "last",
    "laugh",
    "lead",
    "leap",
    "level",
    "license",
    "lie",
    "lift",
    "light",
    "limit",
    "link",
    "load",
    "loan",
    "lock",
    "look",
    "love",
    "mail",
    "make",
    "man",
    "march",
    "mark",
    "match",
    "mate",
    "matter",
    "mean",
    "measure",
    "milk",
    "mind",
    "mine",
    "miss",
    "mistake",
    "moor",
    "move",
    "mug",
    "nail",
    "name",
    "need",
    "nest",
    "notch",
    "note",
    "notice",
    "number",
    "object",
    "offer",
    "oil",
    "order",
    "pack",
    "pad",
    "paddle",
    "paint",
    "park",
    "part",
    "pass",
    "paste",
    "pause",
    "pat",
    "pay",
    "pedal",
    "peel",
    "pelt",
    "permit",
    "phone",
    "photograph",
    "pick",
    "pine",
    "place",
    "plan",
    "plane",
    "plant",
    "play",
    "plow",
    "plug",
    "point",
    "poke",
    "pop",
    "post",
    "practice",
    "praise",
    "present",
    "process",
    "produce",
    "promise",
    "protest",
    "pull",
    "pump",
    "punch",
    "question",
    "quilt",
    "quiz",
    "race",
    "rain",
    "raise",
    "rant",
    "rate",
    "reach",
    "reason",
    "record",
    "reign",
    "rent",
    "repair",
    "reply",
    "report",
    "request",
    "rhyme",
    "ring",
    "riot",
    "risk",
    "rock", 
    "roll",
    "route",    
    "row",
    "ruin",
    "rule",
    "run",
    "sail",
    "sand",
    "saw",
    "scare",
    "scratch",
    "screw",
    "search",
    "season",
    "sense",
    "shampoo",
    "shape",
    "share",
    "shelter",
    "shock",
    "shop",
    "show",
    "sign",
    "signal",
    "silence",
    "sin",
    "sip",
    "skate",
    "sketch", 
    "ski",
    "slice",
    "slide",
    "slip",   
    "smell",
    "smile",
    "smirk",
    "smoke",
    "snack",
    "snow",
    "sound",
    "span",
    "spot",
    "spray",
    "sprout",
    "squash",
    "stain",
    "stamp",
    "stand",
    "star",
    "start",
    "state",
    "steer",
    "step",
    "sting",
    "stop",
    "store",
    "storm", 
    "stress",
    "strip",
    "stroke",
    "struggle",
    "study",
    "stuff",
    "stunt",
    "suit",
    "supply",
    "support",
    "surf",
    "surprise",
    "swap",
    "swing",
    "swivel",
    "tack",
    "talk",
    "taste",
    "tear",
    "tease",
    "telephone",
    "test",
    "thunder",
    "thought",
    "tick",
    "tie",
    "time",
    "tip",
    "tire",
    "toast",
    "touch",
    "tour",
    "tow",
    "trace",
    "track",
    "trade",
    "train",
    "transport",
    "trap",
    "travel",
    "treat",
    "trick",
    "trim",
    "trust",
    "tug",
    "turn",
    "twist",
    "type",
    "upstage",
    "use",
    "vacuum",
    "value",
    "view",
    "visit",
    "voice",
    "vote",
    "walk",
    "waltz",
    "wake",
    "watch",
    "water",
    "wave",
    "wear",
    "whip",
    "whisper",
    "whistle",
    "wick",
    "wink", 
    "wire",
    "wish",
    "work",
    "worry",
    "wrap",
    "wreck",
    "yawn",
    "yield",]
    for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
            if tagged[x][0] in vn:
                tagged[x]=(tagged[x][0],"VB")
            if x>0 and tagged[x][0] in vn:
                tagged[x]=(tagged[x][0],"NN")    
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
    p=[p for w,p in tagged]
    
    if len(p)>2:
        global v1
        v1=v1+" </br><b>Use case Name:</b> Please consider shorter use case name.\n</br>"
        return
    if len(p)>0 and p[0] is not None and p[0]!="VB":
        v1=v1+" </br><b>Use case Name:</b> Please try to use base form of a verb at the beginning.</br>"
    if len(p)>1 and p[-1] is not None:
        if p[-1]=="NNS" or p[-1]=="NN":
            return
        else:
            v1=v1+" </br>Use case Name: Please try to use a noun at the end.\n</br>"

def ccc(b):
    b=b.lower()
    global v1
    #a=m3=T4.get("1.0",'end-1c')
    tokens=word_tokenize(b)
    tagged=tagger.tag(tokens)
    vn=["access","ache","act","address","aim","alert","answer","arrest","attack","auction",
"back","bail","balance","balloon","ban","bandage","bank","bare","bargain","battle","beam","bear","beat","bend","benefit","blame","blast","bleach","block","bloom","blow","board","bomb","bother","bounce","bow","box","bread","break","breed","broadcast","browse","brush","bump","burn","buy","cake","call","camp","care","catch","cause","challenge","change","chant","charge","cheat","check","cheer","chip","claim","clip","cloud","clue","coach","color","comb","comfort","contrast","control","cook","coop","copy","cost","count","cover","crack","crash","crate","credit","crush","cure","curl","curve","cut","cycle","dam","damage","dance","delay","delight","demand","dislike","display","dive","doubt","drain","draw","drink","drive","duck","deal","decay","decrease","design","dial","die","divorce","dock","double","dream","dress","drill","dump","dust","dye","echo","email","end","escape","esteem","estimate","exchange","excuse","exhibit","experience","eye","face","fall","favor","fax","fear","feel","fight","file","fill","film","finish","fish","fix","flap","flash","float","flood","floss","flow","flower","fly","fold","fool","force","form","frame","freeze","frown","function","garden","gaze","gel","glue","grate","grease","grill","grimace","grin","grip","guarantee","guard","guess","guide","hammer","hand","handle","harm","harness","hate","head","heap","heat","help","hide","highlight","hike","hit","hold","hop","hope","hose","hug","humor","hunt","hurry","ice","impact","inch","increase","influence","insult","interest","iron",
    "jail",
    "jam",
    "joke",
    "judge",
    "jump",
    "keep",
    "kick",
    "knit",
    "knock",
    "knot",
    "label",
    "land",
    "last",
    "laugh",
    "lead",
    "leap",
    "level",
    "license",
    "lie",
    "lift",
    "light",
    "limit",
    "link",
    "load",
    "loan",
    "lock",
    "look",
    "love",
    "mail",
    "make",
    "man",
    "march",
    "mark",
    "match",
    "mate",
    "matter",
    "mean",
    "measure",
    "milk",
    "mind",
    "mine",
    "miss",
    "mistake",
    "moor",
    "move",
    "mug",
    "nail",
    "name",
    "need",
    "nest",
    "notch",
    "note",
    "notice",
    "number",
    "object",
    "offer",
    "oil",
    "order",
    "pack",
    "pad",
    "paddle",
    "paint",
    "park",
    "part",
    "pass",
    "paste",
    "pause",
    "pat",
    "pay",
    "pedal",
    "peel",
    "pelt",
    "permit",
    "phone",
    "photograph",
    "pick",
    "pine",
    "place",
    "plan",
    "plane",
    "plant",
    "play",
    "plow",
    "plug",
    "point",
    "poke",
    "pop",
    "post",
    "practice",
    "praise",
    "present",
    "process",
    "produce",
    "promise",
    "protest",
    "pull",
    "pump",
    "punch",
    "question",
    "quilt",
    "quiz",
    "race",
    "rain",
    "raise",
    "rant",
    "rate",
    "reach",
    "reason",
    "record",
    "reign",
    "rent",
    "repair",
    "reply",
    "report",
    "request",
    "rhyme",
    "ring",
    "riot",
    "risk",
    "rock", 
    "roll",
    "row",
    "ruin",
    "rule",
    "run",
    "sail",
    "sand",
    "saw",
    "scare",
    "scratch",
    "screw",
    "search",
    "season",
    "sense",
    "shampoo",
    "shape",
    "share",
    "shelter",
    "shock",
    "shop",
    "show",
    "sign",
    "signal",
    "silence",
    "sin",
    "sip",
    "skate",
    "sketch", 
    "ski",
    "slice",
    "slide",
    "slip",   
    "smell",
    "smile",
    "smirk",
    "smoke",
    "snack",
    "snow",
    "sound",
    "span",
    "spot",
    "spray",
    "sprout",
    "squash",
    "stain",
    "stamp",
    "stand",
    "star",
    "start",
    "state",
    "steer",
    "step",
    "sting",
    "stop",
    "store",
    "storm", 
    "stress",
    "strip",
    "stroke",
    "struggle",
    "study",
    "stuff",
    "stunt",
    "suit",
    "supply",
    "support",
    "surf",
    "surprise",
    "swap",
    "swing",
    "swivel",
    "tack",
    "talk",
    "taste",
    "tear",
    "tease",
    "telephone",
    "test",
    "thunder",
    "thought",
    "tick",
    "tie",
    "time",
    "tip",
    "tire",
    "toast",
    "touch",
    "tour",
    "tow",
    "trace",
    "track",
    "trade",
    "train",
    "transport",
    "trap",
    "travel",
    "treat",
    "trick",
    "trim",
    "trust",
    "tug",
    "turn",
    "twist",
    "type",
    "upstage",
    "use",
    "vacuum",
    "value",
    "view",
    "visit",
    "voice",
    "vote",
    "walk",
    "waltz",
    "wake",
    "watch",
    "water",
    "wave",
    "wear",
    "whip",
    "whisper",
    "whistle",
    "wick",
    "wink", 
    "wire",
    "wish",
    "work",
    "worry",
    "wrap",
    "wreck",
    "yawn",
    "yield",]        
    for x in range(len(tagged)):
            tagged[x]=(tagged[x][0],str(tagged[x][1]))
            if tagged[x][0] in vn:
                tagged[x]=(tagged[x][0],"VB")
    p=[p for w,p in tagged]
    w=[w for w,p in tagged]
    if len(p)>1:
        global v1
        v1=v1+"</br><b>Actor name</b>:Please consider shorter actor name.\n</br>"
    if len(p)>0 and p[0] is not None and 'ing' in w[0]:
        v1=v1+"</br><b>Actor name</b>:Please use a noun for actor name.\n</br>"
    if len(p)>0 and p[0] is not None and p[0]!="NN":
        v1=v1+"</br><b>Actor name</b>:Please use a noun for actor name.\n</br>"
    
def ccc1(b):
    if len(b)==0:
        return
    b=b.lower()
    a=b.split(",")
    for s in a:
        ccc(s)



def checkactors(b,a):
    if len(a)==0 or len(b)==0:
        return
    b=b.lower()
    t=b.split(",")
    print(str(t)+"paaji")
    sent=sent_tokenize(a)
    p=[]
    k=[]
    bo=False
    global v1
    for s in sent:
        for a in t:
             if a in s:
                  k.append(a)
        if len(k)>1:
             print(k)
             bo=True
             v1=v1+"<b>Basic flow:</b>Possible actor to actor interaction.\n</br>"
        k=[]     
        s=s.lower()
        tokens=word_tokenize(s)
        tagged=tagger.tag(tokens)
        for x in range(len(tagged)):
            if x<2 and str(tagged[x][1])=="NN":
                p.append(str(tagged[x][0]))
    print(p)            
    if len(t)>0 :
        for g in t:
            if g not in p:
                print(g)
                if bo is False:
                     v1=v1+"<b>Basic flow:</b>You have used actors other than mentioned.\n</br>"
        
    


def checkactors2(b,a):
    if len(a)==0 or len(b)==0:
        return
    b=b.lower()
    t=b.split(",")
    sent=sent_tokenize(b)
    p=[]
    for s in sent:
        tokens=word_tokenize(a)
        tagged=tagger.tag(tokens)
        for x in range(len(tagged)):
            if x<2 and str(tagged[x][1])=="NN":
                p.append(str(tagged[x][0]))
        for g in p:
            if g not in t:
                global v1
                v1=v1+"<b>Requirements:</b> You have used actors other than mentioned.\n</br>"
