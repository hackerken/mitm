from mitmproxy import http
import re


def response(flow: http.HTTPFlow) -> None:
        allcontent = flow.response.text
        allcontent = re.sub(r'\bTrump\b', 'Drumpf', allcontent, flags=re.IGNORECASE)
        flow.response.text = allcontent
