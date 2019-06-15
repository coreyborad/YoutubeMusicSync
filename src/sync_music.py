import subprocess
import os
import sys
import json
import datetime
import shlex

class MusicSync(object):
    def __init__(self, playlist):
        self.playlistfile = playlist

    def _run_command(self, command):
        # Change command to list type if is string
        if type(command) is str:
            command = shlex.split(command)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, encoding='utf8', shell=False)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self._log(output.strip())
        rc = process.poll()
        return rc

    def _log(self, message):
        print("%s %s" % ('['+str(datetime.datetime.now())+']', message))

    def load(self):
        with open(self.playlistfile, "r") as f:
            self.playlists = json.load(f)

    def sync(self):
        self._log("Start sync")
        count = 0
        for url in self.playlists:
            command = [
                "/usr/local/bin/youtube-dl",
                "--ignore-errors",
                "--extract-audio",
                "--audio-format",
                "mp3",
                "-o",
                "/usr/src/music/%(title)s.mp3",
                "--download-archive",
                "/usr/src/app/archive_" + str(count) + ".txt",
                url
            ]
            self._log("Trace list : " + url)
            self._run_command(command)
            self._log("Finish list : " + url)
            count += 1

        self._log("Finish sync all playlist")
        

def main():
    sync = MusicSync(os.path.dirname(os.path.abspath(__file__))+"/playlist.json")
    sync.load()
    sync.sync()

if __name__ == "__main__":
    main()
