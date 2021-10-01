import json
class JSONFile:
    def __init__(self, filename):
        self.filename = filename

    async def read(self):
        with open(self.filename, "r") as f:
            res = json.load(f)
        return res

    async def update(self, outfile):
        with open(self.filename, "w") as f:
            return json.dump(outfile, f)
