# -*- coding: utf-8 -*-
"""
@author: Noemi E. Cazzaniga - 2020
@email: noemi.cazzaniga@polimi.it
"""


import functools
import requests
from pandasdmx import Request


def robust_pandasdmx_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        max_att = 4
        for att in range(max_att + 1):
            try:
                resp = func(*args, **kwargs)
                return resp
            except ValueError as value_error:
                print("\r{0}".format(value_error))
                raise
            except ConnectionError as connection_error:
                print("\r{0}".format(connection_error))
                raise
            except requests.Timeout:
                if att == max_att:
                    print("\nTimeout Error: did not get data in allotted time. Attempts: {0}".format(max_att + 1))
                    raise
            except requests.ConnectionError:
                print('conn error')
                if att == max_att:
                    print("\nConnection Error: check your internet connection. Attempts: {0}".format(max_att + 1))
                    raise
            except requests.HTTPError as e:
                print("\rHTTPError 404: {0} not found in the Eurostat server".format(e.args[0].split('/')[-2]))
                raise
            except Exception as e:
                try:
                    if e.args[1] == 500:
                        print("\rServer Error 500: {0} not found in the Eurostat server".format(e.args[2].split('/')[-2]))
                    else:
                        print("\r")
                except:
                    print("\r")
                raise
    return wrapper



def estat_proxy(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from urllib.request import _opener #load ex-novo the built/modified opener
        try:
            proxydic = _opener.handle_open['http'][[isinstance(el, ProxyHandler) for el in _opener.handle_open['http']].index(True)].proxies
        except:
            proxydic = None
        estat = Request('ESTAT', timeout = 100., proxies = proxydic)
        res = func(estat, *args, **kwargs)
        return res
    return wrapper
