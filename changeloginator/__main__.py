# Author:   Lonnie Souder
# Date:     01/04/2022
# Generates a changelog from git log with commits written in a specific format.

import sys
from changeloginator import app

if __name__ == '__main__':
    app.main(sys.argv)
