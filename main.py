import xml.etree.ElementTree as ET

from googletrans import Translator

from Languages import *

translator = Translator()

# Make a list of optional languages
nameOfLanguages = [french, spanish, arabic, english, hindi, portuguese, russian, japanese,
                   german, korean]


tree = ET.parse('index.xml')
rootTree = tree.getroot()


choicesToDo = ["Android studio Translations", "Text-translation"]
for i in range(0,2):
    print(str(i+1)+".", choicesToDo[i])
choiceMade = int(input("Enter your choice:- "))
if choiceMade == 1:

    for i in range(0,len(nameOfLanguages)):
        print(i+1,nameOfLanguages[i].name)
    previousLanguageIndex = int(input("Enter the previous language of XML file "))
    previousLanguage = nameOfLanguages[previousLanguageIndex]

    for i in range(0, len(nameOfLanguages)):
        print(i+1, nameOfLanguages[i].name)
    nextLanguageIndex = int(input("Enter the language to get of XML file "))
    nextLanguage = nameOfLanguages[nextLanguageIndex]

    for string in rootTree.findall('string'):
        translatedText = translator.translate(string.text
                                              , src=previousLanguage.shortForm, dest=nextLanguage.shortForm)
        print(translatedText.text)
        string.text = str(translatedText.text)

    tree.write('strings-'+str(nextLanguage.shortForm)+'.xml')

elif choiceMade == 2:
    for i in range(0,len(nameOfLanguages)):
        print(i+1,nameOfLanguages[i].name)
    previousLanguageIndex = int(input("Enter the previous language of XML file "))
    previousLanguage = nameOfLanguages[previousLanguageIndex]

    for i in range(0, len(nameOfLanguages)):
        print(i+1, nameOfLanguages[i].name)
    nextLanguageIndex = int(input("Enter the language to get of XML file "))
    nextLanguage = nameOfLanguages[nextLanguageIndex]

    textToTranslate = input("Enter the word to translate ")
    srce = previousLanguage.shortForm
    deste = nextLanguage.shortForm
    translatedText = translator.translate(textToTranslate, src=srce, dest=deste)
    print(translatedText.text)


else:
    quit()

