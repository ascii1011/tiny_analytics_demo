#!/bin/bash

echo ""
echo "# start teardown mongodb >>>>>>>>>>>>>"

echo ""
echo "ls -alht ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data"
ls -alht ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data

echo ""
echo "removing special files..."
rm -f ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/.bash_history
rm -f ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/WiredTiger

echo ""
echo "removing directories..."
rm -rf ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/.mongodb
rm -rf ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/diagnostic.data
rm -rf ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/journal

echo ""
echo "removing all other files *.*"
rm -f ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data/*.*


echo ""
echo "ls -alht ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data"
ls -alht ~/dev/mnt_data/tiny_analytics_platform/min_custom/mongodb/data

echo ""
echo "<<<<<<<<<<< end teardown mongodb"
echo ""