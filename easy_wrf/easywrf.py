import os

from jinja2 import Environment, FileSystemLoader


class Templates:
    def __init__(self):
        self.environment = self.get_jinja_environment()

    @staticmethod
    def get_jinja_environment():
        package_path = os.path.dirname(os.path.abspath(__file__))
        template_folder_path = os.path.join(package_path, 'templates')
        return Environment(loader=FileSystemLoader(template_folder_path))

    def modify_template_and_write_out(self, template_name, filename, variables):
        template = self.environment.get_template(template_name)

        content = template.render(variables)
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f'... wrote {filename}')


class Variables:
    def __init__(self, template, directory=None):
        """
        WRF and WPS need environmental variables set
        """
        self.conda_environment_path = os.path.dirname(os.path.dirname(os.__file__))
        if self.conda_environment_path[-3:] == 'lib':
            self.conda_environment_path = os.path.dirname(self.conda_environment_path)

        self.templates = template

        if directory is None:
            self.directory = os.path.dirname(os.path.abspath(__file__))

    def make_variable_script(self):
        filename = os.path.join(self.directory, 'set_variables.sh')
        self.templates.modify_template_and_write_out(template_name='set_variables_template.sh',
                                                     filename=filename,
                                                     variables={
                                                         'conda_environment_path': self.conda_environment_path})


class EasyWRF(Variables):
    def __init__(self, template, directory=None, version='4.2.2'):
        self.version = version

        self.conda_environment_path = None
        self.templates = None
        super().__init__(template, directory)

    def make_download_script(self):
        """
        Create the script to download WRF
        """
        filename = os.path.join(self.directory, 'download_wrf.sh')
        self.templates.modify_template_and_write_out(template_name='download_wrf_template.sh',
                                                     filename=filename,
                                                     variables={'version': self.version})

    def configure_wrf(self):
        """
        Some options in the WRF configure file need to be changed by hand
        """
        pass

    def make_install_script(self):
        """
        """
        pass


class EasyWPS:
    def __init__(self):
        pass


def _delete_file_if_exists(filename):
    if os.path.exists(filename):
        os.remove(filename)


def clean(working_directory):
    """
    Helper function to clean generated files
    """
    _delete_file_if_exists(os.path.join(working_directory, 'set_variables.sh'))
    _delete_file_if_exists(os.path.join(working_directory, 'download_wrf.sh'))
    _delete_file_if_exists(os.path.join(working_directory, 'download_wrfgobble.sh'))
    print('Cleaning Complete')


if __name__ == '__main__':
    templates = Templates()

    wrf = EasyWRF(template=templates, version='3.8.1')
    wrf.make_variable_script()
    wrf.make_download_script()

    # clean(os.path.dirname(os.path.abspath(__file__)))
