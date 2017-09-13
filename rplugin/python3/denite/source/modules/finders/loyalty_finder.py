import finder_utils

from loyalty_file import LoyaltyFile


class LoyaltyFinder:

    GLOB_PATTERN = 'app/loyalties/**/*.rb'

    def __init__(self, context):
        self.context = context
        self.root_path = context['__root_path']

    def find_files(self):
        files = finder_utils.glob_project(self.root_path, self.GLOB_PATTERN)
        return [LoyaltyFile(filename) for filename in files]
