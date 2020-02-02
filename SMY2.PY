#importing libraries
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import bs4 as BeautifulSoup
import urllib.request  

'''
import pytesseract as tess
import re
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image





img = Image.open('samplefir.txt_2.png')
paragraphs = tess.image_to_string(img)

'''
paragraphs='I am elder brother of Anurag tewari, IAS, 2019 batch Indore who was found in mysterious0 condition       on 02nd september  2019 morning he was murder. He was an honest officer and gets transferred around 7 to 8 times in his 10 years of carrier. At present he was posted  as Commissioner food and civil supply. During Discussion he told me that he  was working on some file which can expose a big scam and to many of Indore. He was pressurized to sign some paper which he don’t want to sign, thats’y  some unknown people were making pressure on him. He was under tremendous pressure from last few monthsand he also inform 2 months back that he is under life threst. Therefore, it is requested to kindly investigatethe issue for his mysterious death on 2nd september and file a report under section 302against unknown Regards, Mayank tewari. Wildlife Forensic Laboratory, Medical Sciences Building, University of Leicester, LE1 9HN. Position of victim On laboratory floor, in a pool of blood, with an obvious head wound. Possible murder weapon(s) Broken glass 1L bottle of ‘DNA Extraction Buffer’ found on floor near victim covered in blood. Initial coroner’s findings Time of death Estimated from liver temperature measurements to be between 8.00 and 10.00 pm on 11/09/06. Cause of death Blunt force trauma to the head. Background information Last known movements of the victim was working late in the laboratory on the evening of 11/09/06. She was last seen by her laboratory technician, Jim Johnson, who left the building at 6.30 pm, confirmed by the building’s CCTV cameras. A reliable alibi has also been provided for the estimated time of the victim’s death When and where was the victim found? The body was found at 7.15 am in the laboratory on 12/09/06 by Jade Flowers, the cleaner. She has been excluded from investigations as she has a confirmed alibi for the estimated time of the victim’s death. Additional information An unidentified individual wearing a pulled-up ‘hoodie’ was seen, by CCTV, entering the building at 7.55 pm on 11/09/06. Work: Current case – the analysis of parrot DNA to assess whether birds on sale in a local pet shop, The Bird Cage, were supplied by a local breeder or illegally imported into the UK. Old case(s) – threatening phone calls were received on 04/09/06 from a Kevin Black. Mr Black was convicted of the theft of a number of rare bird eggs in May 2005 after expert evidence provided by Dr Jones.On October 5, Pushpa Bhalotia, a 39-year-old housewife of a renowned industrialist family residing in West Burdwan’s Raniganj block was found burnt in her in-law’s house on October 5 of this year. When she was brought to a private hospital in Durgapur, the doctors declared her dead. However, the post-mortem report turned the case upside down and added enough doubts over the theory that this was a case of suicide. The doctors conducting the post-mortem found a bullet in her head and half of her body burnt. However, the family of her in-laws stuck to the story that this was a case of suicide. But what is more worrying is that despite the revelations made in the post-mortem report, the local police refused to register any F.IR or any Suo Moto action, even when one of Pushpa’s brothers approached to file a murder case against the in-laws family on October 6 on the ground that it was a suicide. The family of Pushpa alleged that her husband Manoj Bhalotia was having an extramarital affair with the niece of Om Prakash Bajoria, the President of Raniganj Chamber of Commerce. They accused Bajoria of using his political influence to quash the evidence to protect the prime suspects and conspirators of this murder. What makes the suicide story even more difficult to believe is that all the people who are said to be behind the ghastly death have fled their residences. However, the family of her in-laws stuck to the story that this was a case of suicide. But what is more worrying is that despite the revelations made in the post-mortem report, the local police refused to register any F.IR or any Suo Moto action, even when one of Pushpa’s brothers approached to file a murder case against the in-laws family on October 6 on the ground that it was a suicide. The family of Pushpa alleged that her husband Manoj Bhalotia was having an extramarital affair with the niece of Om Prakash Bajoria, the President of Raniganj Chamber of Commerce. They accused Bajoria of using his political influence to quash the evidence to protect the prime suspects and conspirators of this murder. What makes the suicide story even more difficult to believe is that all the people who are said to be behind the ghastly death have fled their residences. Pushpa Bhalotia, the daughter of Banwary Lal Agarwal, originally from Jharkhand’s Bokaro district, was married to Manoj Bhalotia of Ranjganj in West Bengal in 1995. She has two children who are now pursuing their studies in Australia. “Ever since their marriage, the couple would have issues and fight over petty things. There were times when we sent Pushpa back to her in-law’s house after convincing her that all would we well. But we never thought something like this would happen,” said Brahmanand Agarwal, one of her brothers. When the family saw the inaction of the West Bengal police over the murder, the family members along with some social organisations, Students’ union, Women activists, human rights activists, journalists, and advocates, arranged a Press Conference in Kolkata on November 23. All the participants who spoke sought a proper investigation. RTI activist Siddiqui has already forwarded a mail to the Home Ministry requesting for recommendation of CBI investigation and the copies of the same were sent to twelve more places including the West Bengal Commission for Women, Chief Minister of West Bengal. The Registrar of the Supreme Court of India and the Prime Minister and the President of India. Mustaquim Siddiqui, who has been working on the case for more than 50 days, said “The case has been fabricated by the police. If she tried to kill herself, she would have done so by a gunshot or by burning. How can one kill himself/herself with gunshot and fire at the same time?” He added, “The post-mortem report also said the bullet was not from a licensed gun. This also raises the question where she would get a smuggled gun to kill herself.” He also told to TwoCircles.net that the case has now turned to prove who is mightier as the two families belong to wealthy industrialist Marwari families. When Brahmanand Agarwal, the brother of the victim, was asked why they are considering the death as a murder case, he said, “ if the accused are not the culprits, then they should not have run away from their homes after October 5. Till now we are getting threats to withdraw the case from unknown numbers, who seemed to be from the accused family.” He added they are hopeful the police will conduct a thorough investigation and ensure justice to his sister.'



article_content = ''
#looping through the paragraphs and adding them to the variable
for p in paragraphs:  
    article_content += p

def _create_dictionary_table(text_string) -> dict:
   
    #removing stop words
    stop_words = set(stopwords.words("english"))
    
    words = word_tokenize(text_string)
    
    #reducing words to their root form
    stem = PorterStemmer()
    
    #creating dictionary for the word frequency table
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table


def _calculate_sentence_scores(sentences, frequency_table) -> dict:   

    #algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]

        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words

       

    return sentence_weight

def _calculate_average_score(sentence_weight) -> int:
   
    #calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    #getting sentence average value from source text
    average_score = (sum_values / len(sentence_weight))

    return average_score



def _run_article_summary(article):
    
    #creating a dictionary for the word frequency table
    frequency_table = _create_dictionary_table(article)
    #print(frequency_table)
    
    #tokenizing the sentences
    sentences = sent_tokenize(article)
    #print(sentences)
    
    #algorithm for scoring a sentence by its words
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)
    #print(sentence_scores)
    
    #getting the threshold
    threshold = _calculate_average_score(sentence_scores)
    #print(threshold)
    
    #producing the summary
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence[:7] in sentence_scores and sentence_scores[sentence[:7]] >= (threshold):
            article_summary += " " + sentence
            sentence_counter += 1

    
    return article_summary

summary_results = _run_article_summary(article_content)
#print(paragraphs)
words=paragraphs.split(' ')
for word in words:
    if word=='murder':
        print('dhara : Section 302')
        break
    if word=='rape':
        print('dhara : sections 375, 376, 376A')
        break
print('result : ',summary_results)
