
dic = {'Hello': 'hi, bro',
       'How are you?': 'I am fine, thanks',
       'What are you doing?': 'I answering on your stupid questions (sarcasm)'}
comp = 'Compukhter'
user = 'Uzver'
def ask_user():

        print(comp + ': Please ask me ')
        while True:
            try:
                key_ask = input(user + ': ')
                if key_ask == 'bb':
                    print(comp + ': Good bay my friend! >> unexpected shutdown')
                    break
                else:
                    print(comp +': ' + dic.get(key_ask, 'I am not understand you!'))
            except(KeyboardInterrupt):
                print("BB bro... you kill me :(")
                break
ask_user()