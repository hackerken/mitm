import io
import re
from PIL import Image
from mitmproxy import http


def response(ctx, flow):
# Flip images using ImageMagick
	if re.match('image/',flow.response.headers["content-type"][0]):
		proc = subprocess.Popen('/usr/bin/convert -flip - -',
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,)
		flow.response.content=proc.communicate(flow.response.content)[0]
		proc.stdin.close()