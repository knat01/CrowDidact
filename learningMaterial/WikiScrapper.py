import wikipedia

def wiki(search):
    if wikipedia.search(search) == None:
        wiki_recommend = wikipedia.suggest(search)
        return (wikipedia.summary(wiki_recommend))
    else:
        return(wikipedia.summary(search))