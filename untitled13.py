

import time
import random
print('Piling resources')
time.sleep(2)
print('Getting resources ready')
time.sleep(1)
print('Loading')
time.sleep(0.5)
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
print(' ')
print('NLTK resource locked and loaded')
time.sleep(2)
print(' ')
!pip install deep-translator
from textblob import TextBlob
from deep_translator import GoogleTranslator
print('')
print('TextBlob loaded')
time.sleep(2)
print('All resources loaded')
time.sleep(1)
print('ready')
print('loading')
time.sleep(0.4)
print('loading.')
time.sleep(0.4)
print('loading..')
time.sleep(0.4)
print('loading...')
time.sleep(0.4)
print('loading..')
time.sleep(0.4)
print('loading.')
time.sleep(0.4)
print('loading')
time.sleep(0.4)
print('ready')
time.sleep(1)
print('     .     ')
time.sleep(1)
print(' .      .                 .')
time.sleep(1)
print('            . ')
time.sleep(1)
print('               .     ')
time.sleep(1)
print('                 .')
time.sleep(1)
print('                          .     ')
class f:
    def __init__(self):
        # Dictionary of common 'gotchas' - you can paste accented words here!
        self.rules = {
    # --- People & Basics ---
    "fille": "🔴 Feminine: 'girl' (Agreement: adds -e)",
    "garçon": "🔵 Masculine: 'boy' (Watch for the 'ç')",
    "ami": "🔵 Masculine: 'friend' (Add -e for a female friend: amie)",
    "professeur": "🔵 Masculine: 'teacher' (Usually stays masc. in school)",

    # --- Objects (Commonly tested) ---
    "stylo": "🔵 Masculine: 'pen'",
    "crayon": "🔵 Masculine: 'pencil'",
    "cahier": "🔵 Masculine: 'notebook'",
    "livre": "🔵 Masculine: 'book'",
    "chaise": "🔴 Feminine: 'chair'",
    "table": "🔴 Feminine: 'table'",
    "porte": "🔴 Feminine: 'door'",
    "fenêtre": "🔴 Feminine: 'window'",

    # --- Places ---
    "école": "🔴 Feminine: 'school' (Starts with vowel, use l'école)",
    "maison": "🔴 Feminine: 'house'",
    "classe": "🔴 Feminine: 'class/classroom'",

    # --- Sneaky Irregular Verbs ---
    "être": "⚠️ Irregular Verb: 'To be' (suis, es, est, sommes, êtes, sont)",
    "avoir": "⚠️ Irregular Verb: 'To have' (ai, as, a, avons, avez, ont)",
    "aller": "⚠️ Irregular Verb: 'To go' (vais, vas, va, allons, allez, vont)",
    "faire": "⚠️ Irregular Verb: 'To do/make' (fais, fais, fait, faisons, faites, font)",
    "vouloir": "⚠️ Irregular Verb: 'To want' (veux, veux, veut...)"
  }

    def analyzer(self, translated_text):
        # We lowercase it so 'Être' and 'être' both trigger the rule
        words = translated_text.lower().split()

        for word in words:
            if word in self.rules:
                print(f"💡 MEMORY RECALL: {self.rules[word]}")

    def translator(self, sentence):
        try:
            # Your existing translation logic
            translator = GoogleTranslator(source='en', target='fr')
            translated_text = translator.translate(sentence)

            print(f"English: {sentence}")
            print(f"French: {translated_text}")

            # This checks the translated text against your 'cheat' rules
            self.analyzer(translated_text)

        except Exception as e:
            print(f"Session ended: {e}")

    def categoriser(self, sentence):
      text = sentence
      blob = TextBlob(text)

      categorized_words = {}
      for word, pos in blob.tags:
          if pos == 'NN':
              categorized_words[word] = 'Noun, singular or mass (a word that refers to a person, place, or thing), typically called NN formally'
          elif pos == 'NNP':
            categorized_words[word] = 'Proper Noun, Singular'
          elif pos == 'CC':
            categorized_words[word] = 'Simply means Conjunctions/ transitive verb.'
          else:
              categorized_words[word] = pos
      print(categorized_words)
language = f()
def mains():
  while True:
    try:
      r = random.randint(150, 999)
      print(f'welcome user {r}')
      print("-----MENU-----")
      print("1. english to french")
      print("2. Categorizer for parts of speech(english)")
      print("3. Exit")
      choice = int(input("Type in your choice(1-3):"))
      if choice == 3:
        print(f'byr user {r}, nice to meet you')
        break
      elif choice == 1:
        sentence = input("Type in sentence to be converted")
        language.translator(sentence)
        print('')
      elif choice == 2:
        sentence = input("Type in sentence to be categorised:")
        language.categoriser(sentence)
        print('')
      else:
        print('Option not found')
    except ValueError:
      print('hahaha, caught you, anyways use real numbers when picking choice/option')
      print('')
    except Exception as e :
      print(f'On no, an error occured {e}')
mains()
