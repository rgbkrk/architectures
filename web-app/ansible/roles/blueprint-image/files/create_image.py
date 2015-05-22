import pyrax
import yaml
import sys

creds_yml = yaml.load(open("creds.yml"))
config_yml = yaml.load(open("vars.yml"))

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(creds_yml['username'], creds_yml['api_key'])

region = config_yml["region"] if config_yml["region"] else "IAD"
cs = pyrax.connect_to_cloudservers(region=region)

img_id = None

servers = cs.servers.list()
for server in servers:
  if server.name == 'blueprint':
    img_id = server.create_image("autoscale_blueprint")

if img_id is None:
  print "No server named `blueprint`"
  sys.Exit(1)

img = cs.images.get(img_id)
img = pyrax.utils.wait_until(img, "status", ["ACTIVE", "ERROR"], attempts=0)

output_file = "roles/blueprint-image/files/.img_id"

f = open(output_file, "w")
f.write(img_id)
f.close()
