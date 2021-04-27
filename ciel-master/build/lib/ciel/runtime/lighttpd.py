from cherrypy.process import plugins
import subprocess
import os.path
import tempfile


class LighttpdAdapter(plugins.SimplePlugin):

    def __init__(self, bus, static_content_root, local_port):
        self.local_port = local_port
        self.static_content_root = static_content_root
        self.lighty_ancillary_dir = tempfile.mkdtemp(prefix=os.getenv('TEMP', default='/tmp/ciel-lighttpd-'))
        self.lighty_conf = os.path.join(self.lighty_ancillary_dir, "ciel-lighttpd.conf")
        self.socket_path = os.path.join(self.lighty_ancillary_dir, "ciel-socket")
        self.bus = bus

    def subscribe(self):
        self.bus.subscribe("start", self.start, 75)
        self.bus.subscribe("stop", self.stop, 10)

    def start(self):
        with open(self.lighty_conf, "w") as conf_out:
            print >> conf_out, """"""

    def stop(self):
        try:
            self.lighty_proc.kill()
        except:
            pass
