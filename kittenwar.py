"""
This example shows two ways to redirect flows to another server.
"""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    flow.request.host = "www.kittenwar.com"
