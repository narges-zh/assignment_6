words_bank=[]

def load_data():
        try:
            file=open('words_bank.txt','r')
            my_words=file.read().split('\n')
            for i in range(len(my_words)):
                if i%2==0:
                    dict={}
                    dict['english']=my_words[i]
                else:
                    dict['persian']=my_words[i]
                    words_bank.append(dict)

        except:
            print('cant find file!!!!')

def write_to_file():
    
       new_word=''
       for i in range(len(words_bank)):
           en=words_bank[i]['english']
           fa=words_bank[i]['persion']
           new_word='\n'+en+'\n'+fa
           file=open('words_bank.txt','a')
           myfile=file.write(new_word)


def add_word():
    f=0
    new_word_en=input('enter new word in english:')
    for i in range(len(words_bank)):
        if words_bank[i]['english']==new_word_en:
            print('exit')
            f=0
        else:
            new_word_fa=input('enter new word in persion:')
            dict={}
            dict['english']=new_word_en
            dict['persion']=new_word_fa
            words_bank.append(dict)
            load_data()
            break
        if f==0:
            break

def translate_en2fa():
    input_txt=input('enter ure txt:')
    user_words=input_txt.split(' ')
    output_text=""

    for user_word in user_words:
      for word in words_bank:
          if user_word==word['english']:
              output_text+=word['persian']+' '
              break
      else:
          output_text+=user_word+' '
    print(output_text)


def translate_fa2en():
    input_txt=input('enter ure txt:')
    user_words=input_txt.split(' ')
    output_text=""

    for user_word in user_words:
      for word in words_bank:
          if user_word==word['persian']:
              output_text+=word['english']+' '
              break
      else:
          output_text+=user_word+' '
    print(output_text)


def show_menu():
    print('1-add new word')
    print('2-translate english 2 persian')
    print('3-translate persian 2 english')
    print('4-exit')



while True:
    show_menu()
    load_data()
    choice=int(input('which one??'))
    if choice==1:
        add_word()
    elif choice==2:
        translate_en2fa()
    elif choice==3:
        translate_fa2en()
    elif choice==4:
        exit()
    else:
        print('try again!!!')


