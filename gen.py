#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import random
import time

words = {
    "codenames_adjective": [
        "loud",
        "red",
        "blue",
        "green",
        "yellow",
        "irate",
        "angry",
        "peeved",
        "happy",
        "slimy",
        "sleepy",
        "junior",
        "slicker",
        "united",
        "somber",
        "bizarre",
        "odd",
        "weird",
        "wrong",
        "latent",
        "chilly",
        "strange",
        "loud",
        "silent",
        "hopping",
        "orange",
        "violet",
        "violent"
    ],
    "codenames_noun": [
        "whisper",
        "felony",
        "moon",
        "sucker",
        "penguin",
        "waffle",
        "maestro",
        "night",
        "trinity",
        "deity",
        "monkey",
        "ark",
        "squirrel",
        "iron",
        "bounce",
        "farm",
        "chef",
        "trough",
        "net",
        "trawl",
        "glee",
        "water",
        "spork",
        "plow",
        "feed",
        "souffle",
        "route",
        "bagel",
        "montana",
        "analyst",
        "auto",
        "watch",
        "photo",
        "yard",
        "source",
        "monkey",
        "seagull",
        "toll",
        "spawn",
        "gopher",
        "chipmunk",
        "set",
        "calendar",
        "artist",
        "chaser",
        "scan",
        "tote",
        "beam",
        "entourage",
        "genesis",
        "walk",
        "spatula",
        "rage",
        "fire",
        "master"
    ],
    "codenames_suffix": [
        " 4000",
        "-II",
        " 2.0",
        " rev4",
        "-HX",
        " v9",
    ],
}

if __name__ == "__main__":
    random.seed(time.time())
    coin = random.randint(0, 1)
    adj = words["codenames_adjective"][random.randint(0, 26)]
    non = words["codenames_noun"][random.randint(0, 53)]
    suf = words["codenames_suffix"][random.randint(0, 5)]
    if coin:
        print "Project: " + adj.upper() + non.upper() + suf.upper()
    else:
        print "Project: " + adj.upper() + non.upper()
