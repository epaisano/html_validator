#!/bin/python3


import re


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    thtml = _extract_tags(html)
    stack = []
    if len(html) > 0 and len(thtml) <= 1:
        return False
    for tag in range(len(thtml)):
        if "/" not in thtml[tag]:
            stack.append(thtml[tag])
        else:
            if len(stack) == 0:
                return False
            tmp=(-len(stack[-1])) + 1
            if thtml[tag][:tmp:-1] == stack[-1][:tmp:-1]:
                stack.pop()
            else:
                return False
    return (len(stack) == 0)


def _extract_tags(html):
    '''
    This function returns a list of all the html tags
    contained in the input string, stripping out all
    text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    html = re.findall("<([^ >]+)", html)
    return list(map(lambda tag: "<" + tag + ">", html))
