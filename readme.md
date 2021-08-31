#### How to build container
Execute `./docker_build.sh`

#### How to run container
Prepare YAML configuration file with the following:

    telegram-token: %your telegram bot token%
    google-api-key: %google api developer key%
    google-search-engine-id: %google search engine id%

And execute this:
`sudo docker run --network=host -v %path-to-config%:/app/cfg.yaml slafniy/img-bot cfg.yaml`