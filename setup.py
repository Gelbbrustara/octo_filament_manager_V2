# coding=utf-8

########################################################################################################################
# Do not forget to adjust the following variables to your own plugin.

# The plugin's identifier, has to be unique
plugin_identifier = "filament_manager"

# The plugin's python package, should be "octoprint_<plugin identifier>", has to be unique
plugin_package = "octoprint_filament_manager"

# The plugin's human readable name. Can be overwritten within OctoPrint's internal data via __plugin_name__
plugin_name = "OctoPrint-Filament-Manager"

# The plugin's version. Can be overwritten within OctoPrint's internal data via __plugin_version__
plugin_version = "4.2.1"

# The plugin's description. Can be overwritten within OctoPrint's internal data via __plugin_description__
plugin_description = """A plugin to manage 3D printing filament usage"""

# The plugin's author. Can be overwritten within OctoPrint's internal data via __plugin_author__
plugin_author = "Your Name"

# The plugin's author's mail address.
plugin_author_email = "you@example.com"

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data via __plugin_url__
plugin_url = "https://github.com/Gelbbrustara/octo_filament_manager_V2"

# The plugin's license. Can be overwritten within OctoPrint's internal data via __plugin_license__
plugin_license = "AGPLv3"

# Any additional requirements besides OctoPrint should be listed here
plugin_requires = []

### --------------------------------------------------------------------------------------------------------------------
# More advanced options that usually shouldn't be adjusted follow after this point
### --------------------------------------------------------------------------------------------------------------------

# The Python version your plugin is compatible with. For example, to restrict to only Python 3.7 and above, use
# python_requires=">=3.7". Leaving it empty means the plugin is compatible with all Python versions supported by OctoPrint.
plugin_pythoncompat = ">=3.7,<4"

## If your plugin requires dependency links (e.g. link to specific versions of a library hosted on a repository like
## GitHub or a private server), you can add them here. For example:
# dependency_links = ["https://github.com/SomeUser/SomeProject/archive/master.zip#egg=SomeProject-dev"]

########################################################################################################################

from setuptools import setup

try:
	import octoprint_setuptools
except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)

# Creating setup parameters for the plugin
setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
	pythoncompat=plugin_pythoncompat,
	# dependency_links=dependency_links
)

# Setup the plugin using the setup parameters
setup(**setup_parameters)
