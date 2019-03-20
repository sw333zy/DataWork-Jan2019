#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = '''A CerTaiN kING HaD a bEaUtIFul gaRDEn, ANd IN THe GarDen StooD A trEewhICH 
bORe GoLDeN ApPlEs. THesE aPples WerE alwAyS CoUntEd, aNd abOuTtHE TiMe WheN tHEY BEgAn 
tO grow RipE IT wAs foUND THat EVeRY NIgHT ONEOF THeM Was gOne. thE kiNg bECAMe veRy ANGRy 
at thiS, aND ORDEred theGarDEneR TO KEeP WAtch ALL NIgHT uNDER the tREE. tHE gardener sEt 
hIsELdEsT SoN to WATCH; buT ABout TweLve Oâ€™clOCK He fELL ASlEEp, And inthe morNIng aNOTheR 
Of thE aPPLes Was mIssinG. tHEn THE sECONd Son waSoRdERED to waTch; aNd AT mIDniGhT he tOO FELl
ASleEP, aND iN thE mOrNIngANoThER AppLE WaS gOne . TheN THe thIrd Son oFfeREd tO KeEp wATCh; 
buTthE garDENer At First WoULd NoT LET Him, FOr fEaR sOMe HArM ShOuLD cOMETo hIM: hoWeveR, 
at lAST hE coNSEnteD, AND tHE YouNg MAN laID HimSELfuNDER tHE tREe TO wAtch. AS tHE clocK STRuCk
tweLvE He Heard A rustlinGNoISe IN ThE aIr, And a biRd CAME FlYing ThAt was Of PUre gOLd; AND 
asIT WAs SNApPING At onE oF ThE aPpleS wIth iTS BeaK, tHE GArDEnerâ€™S sonjUMpED UP And SHOT AN
aRrOw at iT. But THE arrOw DID thE BiRD nO HaRm;ONlY iT dRoPPEd a GoLDEn FEather FROM iTS tAiL,
aND THEN FLEw AwaY.the gOLdEN FEAthER WAS bRoUght to THe KinG IN THE MOrNING, AnD aLL ThEcOunCil
WAs called TogETHER. EVERYoNE aGREed ThAt it wAS wORth MoRe THAnaLl The weAltH Of tHE kIngDOm: 
But THE KiNg sAID, â€ ̃One FeatHeR Is Of NOuse tO me, I MusT HaVE ThE wHOLE BIRD .'''


# In[2]:


print(text)


# In[3]:


# Clean text from punctuation
for char in '-.,\n;:':
    text=text.replace(char,' ')
# then make lower case
text = text.lower()


# In[4]:


print(text)


# In[5]:


# use split for a list of words delimited by whitespace, newlines, etc
textlist = text.split()


# In[6]:


print(textlist)


# In[13]:


#collections method
from collections import Counter
Counter(textlist).most_common()


# In[8]:


#dictionary and loop
d = {}
# count number of times each word comes up in list in dictionary
for word in textlist: 
    d[word] = d.get(word, 0) + 1


# In[9]:


word_freq = []
for key, value in d.items():
    word_freq.append((value, key))


# In[10]:


word_freq.sort(reverse=True) 
print(word_freq)


# In[11]:


print("There are a total of {} words.".format(len(textlist)))
print("And {} unique words.".format(len(word_freq)))


# In[ ]:




