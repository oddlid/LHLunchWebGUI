#!/bin/bash

_base=$(dirname $(realpath $0))
_pid="/tmp/dj-lhlunch.pid"
_log="/tmp/django-lhlunch.log"
_ip="0.0.0.0"
_port="8001"


uwsgi \
   --chdir=$_base \
   --socket="${_ip}:${_port}" \
   --master \
   --pidfile=$_pid \
   --daemonize=$_log \
   --processes=4 \
   --harakiri=20 \
   --limit-as=128 \
   --max-requests=5000 \
   --vacuum \
   --module=LHLunchWebGUI.wsgi:application \
   --env DJANGO_SETTINGS_MODULE=LHLunchWebGUI.settings
