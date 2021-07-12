# -*- coding: utf-8 -*-
import subprocess, shlex


cmd = shlex.split("./alexa_remote_control.sh -e \"speak:私は実はバイリンガルなの。おはようは英語でGood moringなの知ってた？\"")
res = subprocess.call(cmd)
