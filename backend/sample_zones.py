import json

sample_zones = {
    "restricted": [
        [[28.614,77.209],[28.615,77.209],[28.615,77.210],[28.614,77.210]]
    ],
    "allowed": [
        [[28.613,77.208],[28.616,77.208],[28.616,77.211],[28.613,77.211]]
    ]
}

with open("backend/sample_zones.py", "w") as f:
    json.dump(sample_zones, f)
