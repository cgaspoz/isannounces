# Using "live" data in a DEV server #

1) Be sure to have this in your app.yaml:
```
builtins:
- remote_api: on 
```
2) Download production data:
```
appcfg.py -e userid@gmail.com download_data --url=http://isannouncedev.appspot.com/_ah/remote_api --filename=data.db
```
3) Import the data into the development server:
```
appcfg.py upload_data --url http://localhost:8080/_ah/remote_api --file=data.db
```
For the last step your dev server should be running, of course.