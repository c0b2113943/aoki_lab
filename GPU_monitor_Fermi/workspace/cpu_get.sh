#!/bin/bash

cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
echo " CPU Usage: $cpu_usage%"

ram_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
echo " RAM Usage: $ram_usage%"