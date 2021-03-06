# Django - API

This is a Django viewSet API app that uses Auth tokens.

## Requirements

The app is contained in its own enviroment.
In cmd/powershell start enviroment with "scripts/activate" from main directory.

cd to 'django_rest' and run command "$ python manage.py runserver"

When the server is ready you can browse to '127.0.0.1:8000'

## Details

This was a hobby project to create a Django based API that uses Authorization tokens. Any user can browse the database via the HTML front-end. If a user would like to contribute to the database, they can register and get a Auth token from the front end or directly via the API.

<h3>Api Usage via Python</h3>
<br>
<h2>Requirements</h2>
<ol>
  <li>Requests Module (pip install requests)</li>
</ol>

<h2>Get current entries</h2>
<pre>
  url = 'http://127.0.0.1:8000/api/heroes/'
  headers = {'Authorization': 'Token {your token number here}'}
  response = requests.get(url, headers = headers)
  print(response.json())
</pre>

<h2>Add new entries</h2>
<pre>
  url = 'http://127.0.0.1:8000/api/heroes/'
  headers = {'Authorization': 'Token {your token number here}'}
  myobj = {'name':'Ironman',
          'alias':'Tony Stark'}

  requests.post(url, data=myobj, headers = headers)
</pre>
<h2>Get Auth Token</h2>
<pre>
  url = 'http://127.0.0.1:8000/api-token-auth/'
  credentials = {'username':'your username', 'password':'your password'}
  response = requests.post(url, data = credentials)
  print(response.json())
</pre>
