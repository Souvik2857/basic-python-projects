from spellchecker import SpellChecker
class spellcheckerapp:
    def __init__(self):
        self.spell=SpellChecker()
    def correct_text(self,text):
        words=text.split()
        corrected_words=[]
        for word in words:
            corrected_word=self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"correcting the {word} to {corrected_word}")
                corrected_words.append(corrected_word)
        
        return ' '.join(corrected_words)
    def run(self):
        print("Welcome to spell checker.....")
        while True:
            text=input("Enter text to correct or (type exit to close the programme)\n")
            if text.lower()=="exit":
                print("Closing the programme........")
                break
            corrected_text=self.correct_text(text)
            print(f"Corrected text:{corrected_text}") 
if __name__=="__main__":
    spellcheckerapp().run()
