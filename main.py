import googletrans as gs
import Assets.Language
from Languages import *
import xml.sax as xml
from xml.dom.minidom import parse
import xml.dom.minidom
translater = gs.Translator()

# Make a list of optional languages
nameOfLanguages = [french, spanish, arabic, english, hindi, portuguese, russian, japanese,
                   german, korean]

xmlFile = xml.dom.minidom.parse("index.xml")
collection = xmlFile.documentElement


choicesToDo = ["Android studio Translations", "Text-translation"]
for i in range(0,2):
    print(str(i+1)+".",choicesToDo[i])
choiceMade = int(input("Enter your choice:-"))

for i in range(0,len(nameOfLanguages)):
    print(i+1,nameOfLanguages[i].name)
previousLanguageIndex = int(input("Enter the previous language of XML file"))
previousLanguage = nameOfLanguages[previousLanguageIndex]

for i in range(0, len(nameOfLanguages)):
    print(i+1, nameOfLanguages[i].name)
nextLanguageIndex = int(input("Enter the language to get of XML file"))
nextLanguage = nameOfLanguages[nextLanguageIndex]

resource = collection.getElementByTagName("resources")
strings = resource.getElementByTagName("string")
translatedStrings = []
for string in strings:
    text = string.childNodes[0]
    textTranslatedMap = translater.translate(text, src=previousLanguage.shortForm, dest=nextLanguage.shortForm)
    textTranslated = textTranslatedMap.text
    translatedStrings.append(textTranslated)


