
Setting up project
------------------

1.Clone the project

    git clone https://github.com/pnija/newsapi.git

2.Create a virtual environment for the project anywhere in the system

    mkdir <folder_name>
    cd <folder_name>
    virtualenv <project_name>

    eg: mkdir ~/virtual
        cd ~/virtual
        virtualenv test_app

3.Activate the virtual environment

    source <path_to_virtualenv>/bin/activate
    eg: source ~/virtual/test_app/bin/activate

4.Enter to the project folder

5.Install the required packages into virtual environment

    pip install -r requirements.txt

6. Setup the db for project using postgres

    Create a db and modify the database configurations in settings.py with your local db configs

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<your_db_name>',
        'USER': '<your_postgres_user>',
        'PASSWORD': 'your_postgres_user_password',
        'HOST': '',
        'PORT': '',
    },
}

6. Migrate the project

    python manage.py makemigrations
    python manage.py migrate

7. Create admin privileged user

    python manage.py createsuperuser
    (Run the command and follow the prompt)

8. Now you can run your project using

    python manage.py runserver

API Details
-----------

The following are the endpoints available in the project

1. Language listing API
2. News creation API
3. News listing API

Language Listing API
....................

URL             : <domain>/languages
METHOD          : GET
INPUT           : NIL
STATUS CODE     : 200
SAMPLE RESPONSE :
                {
                "xtw": "Tawandê",
                "xtu": "Cuyamecalco Mixtec",
                "xtt": "Tacahua Mixtec",
                "xts": "Sindihui Mixtec",
                "xtr": "Early Tripuri"
                }

News creation API
.................

URL             : <domain>/news/
METHOD          : POST
INPUT           : headline, content, publication_date, language(code from language listing API)
STATUS CODE:    201
SAMPLE RESPONSE:
                {
                  "id": 5,
                  "created": "2016-07-01T08:53:43.909440Z",
                  "modified": "2016-07-01T08:53:43.909465Z",
                  "headline": "My headline",
                  "content": "Here goes the content",
                  "publication_date": "2016-07-01",
                  "language": "en"
                }


News listing API
.................

URL             : <domain>/news/
METHOD          : GET
INPUT           : language : language_code(code obtained from language listing API, Optional)
STATUS CODE:    200
SAMPLE RESPONSE:
                [
                      {
                        "id": 1,
                        "created": "2016-07-01T04:46:32.666884Z",
                        "modified": "2016-07-01T04:46:32.666908Z",
                        "headline": "Hyderabad: ISIS suspects stored explosives in kitchen, used basement for target practice",
                        "content": "Mohammed Ibrahim Yajdhani has emerged as the face of the Hyderabad ISIS module which was busted on Wednesday (June 29). An electronic engineer and resident of Chatta Bazar. Yazdani had completed his B. Tech (EEE) from Anwar-ul-Uloom Engineering College in Hyderabad. He worked in Saudi Arabia for three years. But came back to India sometime in 2014.\r\nThe eldest of the five Yajdhani brothers, Ibrahim (30) was currently jobless. Ibrahim along with his brother Mohammed Illiyas and their tenant Rizwan met many of the suspects in the local mosque. Radicalised online, Ibrahim was in constant touch with \"Saheb\" who is suspected to be Shafi Armar.",
                        "publication_date": "2016-07-01",
                        "language": "en"
                      },
                      {
                        "id": 4,
                        "created": "2016-07-01T05:18:26.550490Z",
                        "modified": "2016-07-01T05:18:26.550523Z",
                        "headline": "Are Fawad Khan and his wife Sadaf expecting their second child?",
                        "content": "Finding Mariya: Mother uses Facebook to help her adoptive Indian daughter find her birth sister\r\nNeed motivation to leave the bed? You got to listen to this African drum jam session\r\nAwwperation Tiger: Video captures rare Sumatran tiger cubs at London zoo\r\nJust Urdu it: Hilarious Game of Thrones parody account will leave you in splits",
                        "publication_date": "2016-07-01",
                        "language": "bn"
                      },
                      {
                        "id": 3,
                        "created": "2016-07-01T05:02:40.280283Z",
                        "modified": "2016-07-01T05:02:40.280307Z",
                        "headline": "PM Narendra Modi reviews performance of ministries",
                        "content": "NEW DELHI: Amid talks of a Cabinet reshuffle, Prime Minister Narendra Modi on Thursday reviewed the performance of various ministries in spending budgetary allocations and implementing schemes in the past two years and asked his colleagues to ensure schemes be tailored to benefit masses.",
                        "publication_date": "2016-06-30",
                        "language": "la"
                      }
                ]
