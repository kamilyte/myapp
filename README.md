# README

## Run installations

### macOS
```
pip3 install Django
pip3 install google-search-results
```

### Other Systems

```
pip install Django
pip install google-search-results
```

## Run

### macOS
```
python3 manage.py runserver
```
### Other Systems
```
python manage.py runserver
```
Run the app in the browser on host: http://127.0.0.1:8000/

## Backend
The backend was build using Python with Django. 
In order to retrieve the searches, we first used the organic results from the Google Scholar API to search for the author's ID, by searching through the list of authors and finding the author's ID. Then this ID is passed as a parameter to the Author API which will retrieve all the articles that have the ID listed as an author and use these results to print out the title, authors, year and number of citations for each article. In order to retrieve all the available articles (due to the offset of 20), the API would be called multiple times, taking into account the offset values. 
The screenshots below show the input on the first three lines and the rest is the output.

Input author: George Azzopardi
<img width="1440" alt="Screenshot 2023-09-20 at 20 14 01" src="https://github.com/kamilyte/myapp/assets/104073317/6a88feae-da93-4006-b054-e48eec71752f">


<img width="1440" alt="Screenshot 2023-09-20 at 20 14 18" src="https://github.com/kamilyte/myapp/assets/104073317/78c868b2-e904-4b91-9698-cc05c1f0cc7c">

Input author: Arnold Meijster
<img width="1428" alt="Screenshot 2023-09-20 at 20 18 28" src="https://github.com/kamilyte/myapp/assets/104073317/74087c51-e2ba-4f11-b140-12848badd755">

Input author: Vasilios Andrikopoulos
<img width="1440" alt="Screenshot 2023-09-20 at 21 15 14" src="https://github.com/kamilyte/myapp/assets/104073317/1c800cc9-ed20-4eb9-a6d3-f30c274e7718">

<img width="1440" alt="Screenshot 2023-09-20 at 21 15 35" src="https://github.com/kamilyte/myapp/assets/104073317/c983d0fd-c461-4bbd-ac32-1a6a625dbfe8">

## Frontend
The frontend was built using basic html to present the data. The screenshots below show the input author and the relevant results. 

Input author: George Azzopardi
![WhatsApp Image 2023-09-20 at 21 57 58](https://github.com/kamilyte/myapp/assets/104073317/4fe1fe23-b4ba-48b4-9f4a-ccbd4926d782)
![WhatsApp Image 2023-09-20 at 21 58 30](https://github.com/kamilyte/myapp/assets/104073317/a4944236-d9c1-4c26-99bf-15b72456451b)
![WhatsApp Image 2023-09-20 at 21 58 45](https://github.com/kamilyte/myapp/assets/104073317/72ae1538-245f-4323-95a3-0e5dad425850)
![WhatsApp Image 2023-09-20 at 21 58 56](https://github.com/kamilyte/myapp/assets/104073317/44dba214-fc81-4d8b-8a99-0d6aea37d9ab)


Input author: Brian Setz

![WhatsApp Image 2023-09-20 at 21 59 18](https://github.com/kamilyte/myapp/assets/104073317/0c359230-898e-453d-9d2e-a9a40b1c4e8c)



Input author: Vasilios Andrikopoulos
![WhatsApp Image 2023-09-20 at 22 01 08](https://github.com/kamilyte/myapp/assets/104073317/8023dfd9-0277-4fdc-93f1-fcf0e5e14be1)
![WhatsApp Image 2023-09-20 at 22 01 27](https://github.com/kamilyte/myapp/assets/104073317/631384eb-bb78-4768-a593-2fbdc8051f83)

![WhatsApp Image 2023-09-20 at 22 01 38](https://github.com/kamilyte/myapp/assets/104073317/b8893520-7362-4943-adc1-5faaf973ce24)

Input author: Arnold Meijster

![WhatsApp Image 2023-09-20 at 22 02 26](https://github.com/kamilyte/myapp/assets/104073317/c1514de0-7cf4-40a4-8665-d8cc937fea67)


Input author: Daniel Feitosa
![WhatsApp Image 2023-09-20 at 21 59 49](https://github.com/kamilyte/myapp/assets/104073317/82681a47-2de8-4c85-b42d-0c6bbbc446c6)
![WhatsApp Image 2023-09-20 at 22 00 03](https://github.com/kamilyte/myapp/assets/104073317/8ab36256-c378-45e9-94fa-51641dba04a3)
