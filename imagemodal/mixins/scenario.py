"""
Mixin workbench behavior into XBlocks
"""
from glob import glob

from xblock.core import XBlock



def _read_file(file_path):
    with open(file_path) as file_input:
        file_contents = file_input.read()
    return file_contents


def _parse_title(file_path):
    title = file_path
    title = title.split('/')[-1]
    title = '.'.join(title.split('.')[:-1])
    title = ' '.join(title.split('-'))
    title = ' '.join([
        word.capitalize()
        for word in title.split(' ')
    ])
    return title


def _read_files(files):
    file_contents = [
        (
            _parse_title(file_path),
            _read_file(file_path),
        )
        for file_path in files
    ]
    return file_contents


def _find_files(directory):
    pattern = "{directory}/*.xml".format(
        directory=directory,
    )
    files = glob(pattern)
    return files


class ImageModalScenarioMixin(object):
    """
    Provide a default test workbench for the XBlock
    """

    @classmethod
    def workbench_scenarios(cls):
        """
        Gather scenarios to be displayed in the workbench
        """
        resource_dir = cls.get_resources_dir()
        resource_dir = resource_dir or '.'
        scenario_dir = resource_dir + '/scenarios'
        files = _find_files(scenario_dir)
        scenarios = _read_files(files)
        return scenarios
