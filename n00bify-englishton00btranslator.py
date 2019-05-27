'''Description

The internet is a very confounding place for some adults. Tom has just joined an online forum and is trying to fit in
with all the teens and tweens. It seems like they're speaking in another language! Help Tom fit in by translating
his well-formatted English into n00b language.
The following rules should be observed:
- "to" and "too" should be replaced by the number 2, even if they are only part of a word (E.g. today = 2day);
- Likewise, "for" and "fore" should be replaced by the number 4;
- Any remaining double o's should be replaced with zeros (E.g. noob = n00b);
- "be", "are", "you", "please", "people", "really", "have", and "know" should be changed to "b", "r", "u", "plz",
"ppl", "rly", "haz", and "no" respectively (even if they are only part of the word);
- When replacing words, always maintain case of the first letter unless another rule forces the word to all caps;
- The letter "s" should always be replaced by a "z", maintaining case;
- "LOL" must be added to the beginning of any input string starting with a "w" or "W";
- "OMG" must be added to the beginning (after LOL, if applicable,) of a string 32 characters or longer;
- All evenly numbered words must be in ALL CAPS (Example: Cake is very delicious. becomes Cake IZ very DELICIOUZ);
- If the input string starts with "h" or "H", the entire output string should be in ALL CAPS;
- Periods ( . ), commas ( , ), and apostrophes ( ' ) are to be removed;
- A question mark ( ? ) should have more question marks added to it, equal to the number of words2 in the sentence
(Example: Are you a foo? has 4 words, so it would be converted to r U a F00????);
- Similarly, exclamation points ( ! ) should be replaced by a series of alternating exclamation points and the number 1,
equal to the number of words2 in the sentence (Example: You are a foo! becomes u R a F00!1!1).
Characters should be counted After: any word conversions, adding additional words, and removing punctuation.
Excluding: All punctuation and any 1's added after exclamation marks ( ! ). Character count includes spaces.
For the sake of this kata, "words" are simply a space-delimited substring, regardless of its characters. Since
the output may have a different number of words than the input, words should be counted based on the output string.
The incoming string will be punctuated properly, so punctuation does not need to be validated.'''


def n00bify(text):
    nooblist = list()
    noobdict = {'too':'2', 'fore':'4', 'be':'b', 'are':'r',
                'you':'u', 'please':'plz', 'people':'ppl',
                'really':'rly', 'have':'haz', 'know':'no',
                's':'z', '.':'', ',':'', '\'':''}
    rest = {'to':'2', 'oo':'00', 'for':'4', 's':'z'}
    for i in text.split():
        for word in noobdict.keys():
            lowcase = i.lower()
            if word in lowcase:
                n = lowcase.index(word)
                if i[n].isupper():
                    i = i.replace(i[n:n+len(word)], noobdict[word].upper())
                else:
                    i = i.replace(i[n:n+len(word)], noobdict[word])
        for word in rest.keys():
            if word in lowcase:
                n = lowcase.index(word)
                if i[n].isupper():
                    i = i.replace(i[n:n+len(word)], rest[word].upper())
                else:
                    i = i.replace(i[n:n+len(word)], rest[word])
        nooblist.append(i)
    if text.startswith(('w','W')):
        nooblist.insert(0, 'lol')
    noobstr = ' '.join(nooblist)
    if len(noobstr) - noobstr.count('?') - noobstr.count('!')> 31:
        if noobstr.startswith('lol'):
            nooblist.insert(1, 'omg')
        else:
            nooblist.insert(0, 'omg')
    noobwpunc = list()
    for j in range(len(nooblist)):
        if j % 2 != 0 or nooblist[j] == 'omg' or nooblist[j] == 'lol':
            nooblist[j] = nooblist[j].upper()
        wordwpunc = str()
        for k in nooblist[j]:
            if k is '!':
                k = '!1'*(len(nooblist)//2) + '!'*(len(nooblist)%2)
            elif k is '?':
                k = '?' * len(nooblist)
            wordwpunc += k
        noobwpunc.append(wordwpunc)
    return (' '.join(noobwpunc)).upper() if text.startswith(('h', 'H')) else ' '.join(noobwpunc)

print(n00bify('Let\'S eat, Grandma!'))  # LetZ EAT Grandma!1!
print(n00bify('Before I knew it for people were looking for you!'))  # OMG B4 I KNEW it 4 ppl WERE l00king 4
                                                                     # u!1!1!1!1!1!