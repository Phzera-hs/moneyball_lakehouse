import sys
import os
from pathlib import Path
import requests
import pandas

try:
    current_dir = Path(__file__).resolve().parent
except NameError:
    current_dir = Path(os.getcwd())

base_dir = current_dir.parent

if str(base_dir) not in sys.path:
    sys.path.append(str(base_dir))

from utils import get_key_env as gke

api = gke.get_api_key()
urllist = ["/v4/competitions/BSA/teams", "/v4/competitions/BSA/standings", "/v4/competitions/BSA/matches"]

header = {

}

