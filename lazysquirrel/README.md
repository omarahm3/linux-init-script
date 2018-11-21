# Lazy Squirrel Initializer Script (LSIS)

This python script should help easily open your daily use programs or/and development servers on Linux systems (that's what I've tested it on, so far). In case of any power outage, or unexpected shutdown it will be painful to click and walk through your programs and run each and single one of them, so this should help you get it together at one place and RUN THEM ALL!

### Use it!

You'll only need to do two things

1. Change `config.json` file, and add your name, programs, and servers.

   ```json
   "configuration": {
       "owner": "Omar",
       "programs": [
           "google-chrome",
           "phpstorm",
           "slack",
           "vlc"
       ],
       "servers": [
           {
               "name": "MyProject",
               "path": "/dev/www/html/whatever-it-is",
               "command": "php bin/console server:run"
           }
       ]
   } 
   ```

   `path` should be the full path of the project.

   `command` well its obvious, this is the command that should run the project server.

   And oh, don't forget change your name :'D

2. Contribute, or report me if you feel that there is something needs to be changed or added.



