import pyrax
import getopt
import sys
import os

try:
    opts, args = getopt.getopt(sys.argv[1:], "ud", ["up=", "down="])
except:
    print str(err)
    usage()
    sys.exit(2)

up_hook = None
down_hook = None

for o, a in opts:
    if o in ('-u', '--up'):
        up_hook = a
    elif o in ('-d', '--down'):
        down_hook = a

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)

cm = pyrax.cloud_monitoring

# Create CRITICAL notification
cr_n = cm.create_notification("webhook", label="critical", details={"url": up_hook})

# Create OK notification
ok_n = cm.create_notification("webhook", label="OK", details={"url": down_hook})

# Create notification plan
plan = cm.create_notification_plan(label="production", ok_state=ok_n, critical_state=cr_n)

f = open('.np_id', 'w')
f.write(plan.id)
f.close()
