import random

quantity = ["single", "plural"]
verb_tense = ["past", "present", "future"]

def main():
    #Creat a loop to creat a sentence in singula and plural with all verb-tenses
    for tense in verb_tense:
        sentence = make_sentence(quantity[0], tense)
        print(str.capitalize(sentence))
    for tense in verb_tense:
        sentence = make_sentence(quantity[1], tense)
        print(sentence)


def get_determiner(quantity):
    #If quantity is 1, this function will return aeterminer for a single noun. Otherwise thisfunction will return a determiner for a plural noun.
    if quantity == 1:
      words = ["a", "one", "the"]
    else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
        #an integer that determines if the returned noun is single or plural.
    if quantity == 1:
      words = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
    else:
      words = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
  # Randomly choose and return a noum.
    word = random.choice(words)
    return word
     
def get_verb(quantity, tense):
    #Return a randomly chosen verb. If tense is "past",this function will return one of these ten verbs
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words =["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words =["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words =["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def make_sentence(quantity, tense):
   #execute de tree def that retur a determine, a noun amd a verb.
   determine = get_determiner(quantity)
   noun = get_noun(quantity)
   verb = get_verb(quantity, tense)
   prepositional_phrase = get_preposition_phrase(quantity)
   #Create a sentence based the values above
   return(str.capitalize(f'{determine} {noun} {verb} {prepositional_phrase}.'))

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
    
    preposition = random.choice(prepositions)
    return preposition

def get_preposition_phrase(quantity):
   noun = get_noun(quantity)
   determiner = get_determiner(quantity)
   preposition = get_preposition()

   preposition_frase = (f'{preposition} {determiner} {noun}')
   return preposition_frase
   

main()