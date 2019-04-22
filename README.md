# Spotify Weather App
 - Requirements:
    + Python 3.7
  - Libraries:
    + Beautiful Soup 4
    + Django
- Setup:
  + Make sure to have the latest version of PYTHON 3 installed.
    - Now make sure you have pipenv installed: ```pip3 install pipenv```
    - Now to install all the dependencies: ```pipenv install```
- Usage:
  + Run ``` pipenv run python3 mysite/manage.py runserver ```
  + Visit [http://127.0.0.1:8000/webapp/home](http://127.0.0.1:8000/webapp/home) in your browser
## Weather Backend:
- Usage:
  + ``` pipenv run python3 parse.py```
  + Enter a zipcode
  + Location, Weather Description, Temperature in F and C, mood string will be displayed in a dictionary
- Notes: 
  + Still needs to be integrated with other parts of website. So far all that this does is take in user input and print to a terminal without saving any data. 
  + Updated to only be 3 individual functions that return a dictionary of data weather data from the website

## Links:
- Playlists:
  + [Windy](https://open.spotify.com/user/125001372/playlist/1mQvg5NX8hwvETI3Ud6pws?si=QF1obWvpSRCzV_JixWEuRw)
  + [Cloudy](https://open.spotify.com/user/125001372/playlist/2I7TZYJy5qLtfowMCTLIkP?si=m22x99xNS_KiMS6oLDB9BQ)
  + [Rainy](https://open.spotify.com/user/125001372/playlist/6N3EWQRQCMtrTeO6KSK0wR?si=BnofNgGNRfiFNYlWqPNkQQ)
  + [Sunny](https://open.spotify.com/user/125001372/playlist/4kIXGUdLiKqDnyPKHjtGy4?si=Xx_OT0qsQoejiLDhPnUi_w)
