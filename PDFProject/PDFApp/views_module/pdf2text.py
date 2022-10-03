from PyPDF2 import PdfFileReader
import re
def pdf_to_text(file_path):

    text=""
    with open(file_path, "rb") as input:
        reader = PdfFileReader(input)
        # 指定のページのデータを読み込む
        for i in range(0,reader.getNumPages()):
            page = reader.getPage(i)
            text+=page.extractText()

    kari_text = text.split("\n")

    new_text=[]
    text_cnt=0
    for i,sentence in enumerate(kari_text):
        sentence =re.sub('\x0f','',sentence)
        sentence =re.sub(' ,',', ',sentence)
        #print(sentence,i)
        if text_cnt==0:
            
            if len(sentence.split(' '))<5:
                new_text.append(sentence)
                text_cnt=0
                continue
            else:
                new_text.append(sentence)
                text_cnt=1
                continue
        
        else:
            
            if sentence[-1]=="-":
                new_text[-1]+=(sentence[:-1])
                
            elif sentence[-1]==".":
                new_text[-1]+=(sentence)
                text_cnt=0
            
            elif len(sentence.split(' '))<5:
                if new_text[-1][-1]==".":
                    new_text.append(sentence)
                    text_cnt=0
                else:
                    new_text[-1]+=(' '+sentence+' ')
                
            else:
                new_text[-1]+=(sentence+' ')
                
    new_text_1=[]
    word_cnt=[]
    for i,sentence in enumerate(new_text):
        if '. ' in sentence:
            for sent in (sentence.split('. ')):
                if sent[-1]!=".":
                    new_text_1.append(sent+'.')
                    word_cnt.append(len(new_text_1[-1].split(' ')))
                else:
                    new_text_1.append(sent)
                    word_cnt.append(len(new_text_1[-1].split(' ')))
        else:
            new_text_1.append(sentence)
            word_cnt.append(len(sentence.split(' ')))

    return(new_text_1,word_cnt)