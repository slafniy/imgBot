##### How to run as console app
- Set your params in cfg.yaml
- Run `img_bot.py`

Run `img_bot.py --help` to see all possible cmd parameters 

#### How to build container
Execute `./docker_build.sh`

#### How to run container
`sudo docker run -v /your/own/config/path.yaml:/opt/img-bot/cfg.yaml slafniy/img-bot`