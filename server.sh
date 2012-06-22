#! /bin/bash

start_servers() {
    echo "starting servers"
    CURRENT_PWD=`pwd`
    CATALINA_HOME="$CURRENT_PWD/system/server"
    system/server/bin/startup.sh
}

stop_servers() {
    echo "Stopping servers"
    CURRENT_PWD=`pwd`
    CATALINA_HOME="$CURRENT_PWD/system/server"
 
    system/server/bin/shutdown.sh
}

usage() {
    echo "$0 stop|start|restart"
}

[ $# -lt 1 ] && usage && exit 1
ACTION=$1

case "$ACTION" in
    "start") start_servers ;;
    "stop")  stop_servers ;;
    "restart")
        stop_servers
        sleep 1
        start_servers
        ;;
    *) echo "Uknown action $ACTION" && usage && exit 1
esac

exit 0
