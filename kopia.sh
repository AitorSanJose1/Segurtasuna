#!/bin/bash

rsync -av --link-dest=/var/tmp/Backups/$(date --date=yesterday +"%F") /home/aitor/Escritorio/Uni/Lab1 /var/tmp/Backups/$(date '+%F')
