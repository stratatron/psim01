#!/bin/bash
#
# script for creating iscsi storage for gateway01
###########################################################
stmfadm list-lu  | awk '{ print $3 }' > luns.temp
	stmfadm delete-lu $LUN
	logger -p local5.debug deleting lun $LUN
	echo "deleting lun $LUN"
done < luns.temp
HG=$(stmfadm list-hg | awk '{ print $3 }')
if [ -n $HG ]
then
	stmfadm delete-hg $HG
	logger -p local5.debug deleting hg $HG
	echo "deleting hostgroup $HG"
fi
zfs destroy -r archivepool01/vols
logger -p local5.debug destroying archivepool01/vols
echo "destroying archivepool01/vols/"
zfs destroy -r archivepool02/vols
logger -p local5.debug destroying archivepool02/vols
echo "destroying archivepool02/vols"
