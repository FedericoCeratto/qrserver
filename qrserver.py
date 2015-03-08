#!/usr/bin/env python2

from argparse import ArgumentParser
import bottle
import netifaces
import qrcode

served_filename = None


def print_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii()


def guess_server_ipaddr():
    for if_name in netifaces.interfaces():
        if not if_name.startswith(('eth', 'wlan')):
            continue

        addresses = netifaces.ifaddresses(if_name)
        if netifaces.AF_INET not in addresses:
            continue

        return addresses[netifaces.AF_INET][0]['addr']


@bottle.route('/<requested_filename>')
def serve_static(requested_filename):
    if requested_filename != served_filename:
        bottle.abort(401, "Sorry, access denied.")

    return bottle.static_file(requested_filename, root='.', download=True)


def main():
    global served_filename

    ap = ArgumentParser()
    ap.add_argument('filename', help="Filename or URL")
    ap.add_argument('--ipaddr', default=guess_server_ipaddr())
    ap.add_argument('--port', default=8080, type=int)
    args = ap.parse_args()

    if args.filename.startswith(('http://', 'https://')):
        print_qrcode(args.filename)
        return

    url = "http://%s:%d/%s" % (args.ipaddr, args.port, args.filename)
    print "\nURL: %s" % url
    print_qrcode(url)
    served_filename = args.filename

    bottle.run(host=args.ipaddr, port=args.port)


if __name__ == "__main__":
    main()
