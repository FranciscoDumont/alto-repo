#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import BaseFilter


class HappyFilter(BaseFilter):
    def filter(self, message):
        return "patron" in message.text or "decision" in message.text


