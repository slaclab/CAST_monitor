#!/bin/bash
# As there is no iocBoot directory for the timing python codes,
# we end up running this with IOC set to the name and
# HUTCH set to the lowercase hutch name
# py-fstiming-XXX, py-fstiming-tt-XXX, py-fstiming-pcav-XXX are py2.7
# py-fstiming-cast-XXX is py3
#source /reg/g/pcds/setup/epicsenv-7.0.2-2.0.sh


export PSPKG_ROOT=/reg/g/pcds/pkg_mgr
export PSPKG_RELEASE="las-0.0.2"
export EPICS_CA_MAX_ARRAY_BYTES=8000000
source ${PSPKG_ROOT}/etc/set_env.sh
source /reg/g/pcds/engineering_tools/latest-released/scripts/pcds_conda

cd /cds/group/laser/timing/CAST_monitor

echo "Starting up CAST Monitoring Script"

#case 

#script = run.py
#esac

echo "Running CAST Monitoring script"

python run.py || echo "Script exited with code $?"
