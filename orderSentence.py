def order(sentence):
    newSentence = []
    sentenceList = sentence.split()
    lenSentenceList = len(sentenceList)    

    for x in range(1, (lenSentenceList+1)):
    
        for word in sentenceList:            

            index = 0
            while (index < len(word)):                
                
                if (word[index].isdigit() and int(word[index]) == x):                    

                    newSentence.append(word)
                index += 1
            
    print(newSentence)

sentence = "4with y2ou s6ad fa7ce hey1 th3ere t5he"
# "Thi1s is2 3a T4est"
order(sentence)
