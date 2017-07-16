#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class Regex(object):
    newline = re.compile(r'^$')
    heading = re.compile(r'^(?P<level>\*+)\s+(?P<title>.+)$')
    comment = re.compile(r'^(\s*)#(.*)$')
    bold = re.compile(r'\*(?P<text>[\S]+?)\*')
    # italic = re.compile(r'(\*\*|/)(?P<text>[\S]+?)(\*\*|/)')
    italic = re.compile(r'\*\*(?P<text>[\S]+?)\*\*')
    underlined = re.compile(r' _(?P<text>[\S]+?)_')
    code = re.compile(r'=(?P<text>[\S]+?)=')
    delete = re.compile(r'\+(?P<text>[\S]+?)\+')
    verbatim = re.compile(r'~(?P<text>[\S]+?)~')
    image = re.compile(r'\[\[(?P<src>.+?)\](?:\[(?P<alt>.+?)\])?\]')
    link = re.compile(r'\[\[(?P<href>https?://.+?)\](?:\[(?P<text>.+?)\])?\]')
    fn = re.compile(r'\[fn:(?P<text>.+?)\]')

    begin_example = re.compile(r'\s*#\+BEGIN_EXAMPLE$')
    end_example = re.compile(r'\s*#\+END_EXAMPLE$')

    begin_quote = re.compile(r'\s*#\+BEGIN_QUOTE$')
    end_quote = re.compile(r'\s*#\+END_QUOTE$')

    begin_src = re.compile(r'\s*#\+BEGIN_SRC\s+(?P<lang>.+)$')
    end_src = re.compile(r'\s*#\+END_SRC$')

    any_depth = re.compile(r'(?P<depth>\s*)(?P<title>.+)$')
    order_list = re.compile(r'(?P<depth>\s*)\d+(\.|\))\s+(?P<title>.+)$')
    unorder_list = re.compile(r'(?P<depth>\s*)(-|\+)\s+(?P<title>.+)$')

    table = re.compile(r'\s*\|(?P<cells>(.+\|)+)s*$')
    table_sep = re.compile(r'^(\s*)\|((?:\+|-)*?)\|?$')
    table_setting = re.compile(r'\s*#\+ATTR_HTML:\s*:class\s*(?P<cls>.+)$')

    attr = re.compile(r'^(\s*)#\+(.*)$')


class NotBeginError(Exception):
    pass


class InlineElement(object):
    label = '{text}'
    regex = None

    def __init__(self, text):
        self.text = text
        self.children = []

    def to_html(self):
        return self.parse(self.text)

    def parse(self, text):
        for t in self.regex.finditer(text):
            string = self.label.format(text=t.group('text'))
            text = self.regex.sub(string, text, 1)
        return text

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.text.strip())


class Fn(InlineElement):
    '''
    <sup><a id="fnr:{text}" class="footref" href="#fn.{text}"></a></sup>
    '''
    label = '<sup><a id="fnr:{text}" class="footref" href="#fn.{text}">{text}</a></sup>'
    regex = Regex.fn

class Underlined(InlineElement):
    label = '<span style="text-decoration:underline">{text}</span>'
    regex = Regex.underlined

class Bold(InlineElement):
    label = '<b>{text}</b>'
    regex = Regex.bold
