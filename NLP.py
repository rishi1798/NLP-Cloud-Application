import nlpcloud

class NLPApp:

    def __init__(self):
        self.__database={}
        self.__first_menu()

    def __first_menu(self):

        first_input=input("""
        Hi! Would you like to proceed?
        1. Not a member? Register
        2. Already a member? Login
        3. Glati se aa gaye? Exit
        """)
        
        if first_input == "1":
            self.__register()
        elif first_input == "2":
            self.__login()
        elif first_input == "3":
            exit()
        else:
            print("Enter choice between 1,2,3 only.")
            
            self.__first_menu()

    def __second_menu(self):

        first_input=input("""
        Hi! Would you like to proceed?
        1. NER
        2. Language Detection
        3. Sentiment Analysis
        4.Logout
        """)
        
        if first_input == "1":
            self.__NER()
        elif first_input == "2":
            self.__language_detection()
        elif first_input == "3":
            self.__sentiment_analysis()
        elif first_input == "4":
            exit()
        else:
            print("Enter choice between 1,2,3 only.")
            self.__second_menu()

    def __register(self):
            name=input("Enter your name:")
            email=input("Enter your email:")
            password=input("Enter your password:")

            if email in self.__database:
                print("Email already exists.Try with different Email")
                self.__register()
            else:
                self.__database[email] = [name,password]
                print("User registered successfully!!!")
            self.__first_menu()

    def __login(self):
        email=input("Enter your Email:")
        password=input("Enter your password:")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login successfully")
                self.__second_menu()
            else:
                print("Wrong password.Try again!!!!")
                self.__login()
        else:
            print("This email is not registered")
            self.__register()
            



    def __NER(self):

        # Named Entity Recognition

        # This function will tell u about the Entities in the paragraph.so i have put a default paragraph here u can give your choice paragraph and we have to give a search entity which here i have given as programming language and this NLP model will give us the programming language in the given para in the below format

        # {'entities': [{'start': 26,
            # 'end': 36,
            # 'type': 'programming languages',
            # 'text': 'javascript'},
            # {'start': 102,
            # 'end': 108,
            # 'type': 'programming languages',
            # 'text': 'python'},
            # {'start': 165, 'end': 167, 'type': 'programming languages', 'text': 'go'}]}


        para="John Doe started learning Javascript when he was 15 years old. After a couple of years he switched to Python and starter learning low level programming. He is now a Go expert at Google."

        search_item="programming languages"

        client = nlpcloud.Client("finetuned-gpt-neox-20b", "e8f66824e67132dadf33daa0067ebddd97872bc3", gpu=True, lang="en")

        response=client.entities(para, searched_entity=search_item)

        print(response)

    def __language_detection(self):

        # Here also u can put the paragraph of your choice and this function will tell about the Language used in the paragraph here output is :en and fr

        para="John Doe has been working for Microsoft in Seattle since 1999. Et il parle aussi un peu français."
        client = nlpcloud.Client("python-langdetect", "e8f66824e67132dadf33daa0067ebddd97872bc3", gpu=False)
        response=client.langdetection(para)
        
        for i in response['languages']: 
            print(list(i.keys())[0])


    def __sentiment_analysis(self):
        
        # You can put paragraph of your choice and from that paragraph this NLP model will tell you the emotions in the paragraph and their can be multiple emotions in the paragraph but in the code i have only shown the emotion who have the highest score or the emotion which is most strongly reflecting in the paragraph .


        # Sample output:
        # {'scored_labels': [{'label': 'sadness', 'score': 0.0001777907891664654},
            # {'label': 'joy', 'score': 0.9987751841545105},
            # {'label': 'love', 'score': 0.0004087708657607436},
            # {'label': 'anger', 'score': 0.00012217740004416555},
            # {'label': 'fear', 'score': 0.00011809932038886473},
            # {'label': 'surprise', 'score': 0.0003979843750130385}]}




        para = "This isn't just a beautifully crafted gangster film. Or an outstanding family portrait, for that matter. An amazing period piece. A character study. A lesson in filmmaking and an inspiration to generations of actors, directors, screenwriters and producers. For me, this is more: this is the definitive film. 10 stars out of 10."
                

        client = nlpcloud.Client("distilbert-base-uncased-emotion", "e8f66824e67132dadf33daa0067ebddd97872bc3", gpu=False, lang="en")
        response = client.sentiment(para)

        L = []
        for i in response['scored_labels']:
            L.append(i['score'])

        index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)


        print(response['scored_labels'][index]['label'])
        self.__second_menu()

if __name__=="__main__":
    obj=NLPApp()
