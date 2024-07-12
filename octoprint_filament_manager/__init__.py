# coding=utf-8
from __future__ import absolute_import

import threading

from flask import request, jsonify, make_response, url_for
from contextlib import contextmanager

from octoprint.settings import valid_boolean_trues
from octoprint.filemanager.destinations import FileDestinations
from octoprint.server.util.flask import restricted_access, get_json_command_from_request

import octoprint.plugin
from .ThreadPool import ThreadPool


class FilemanagerPlugin(octoprint.plugin.TemplatePlugin,
						octoprint.plugin.AssetPlugin,
						octoprint.plugin.BlueprintPlugin,
						octoprint.plugin.ShutdownPlugin,
						octoprint.plugin.SettingsPlugin):

	def initialize(self):
		self._worker_lock_mutex = threading.RLock()
		self._worker_locks = dict()

		self._workerProgress_lock_mutex = threading.RLock()
		self._workerProgress_locks = dict()

		self.workerPool = ThreadPool(5)
		self.workerBusy = 5 * [False]
		self.workerProgress = 5 * [dict(command="", progress=0, lastfile="")]

	def on_shutdown(self):
		if any(self.workerBusy):
			self._logger.warning("Some workers weren't ready, but OctoPrint got shutdown.")

	def get_assets(self):
		return dict(
			js=["js/filament_manager.js"],
			css=["css/filament_manager.css"],
		)

	def get_settings_defaults(self):
		return dict(
			enableCheckboxes=False
		)

	def get_template_configs(self):
		return [
			dict(type="tab", template="filament_manager.jinja2", custom_bindings=True),
		]


	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			filemanager=dict(
				displayName="Octo Filament Manager",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="Gelbbrustara",
				repo="octo_filament_manager_V2",
				current=self._plugin_version,

				stable_branch=dict(
					name="Stable",
					branch="master",
					comittish=[
						"master"
					]
				),
				prerelease_branches=[
					dict(
						name="Development",
						branch="devel",
						comittish=[
							"devel",
							"master"
						]
					)
				],

				# update method: pip
				pip="https://github.com/Gelbbrustara/octo_filament_manager_V2/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Octo-Filament-manager"
__plugin_pythoncompat__ = ">=2.7,<4"


def __plugin_load__():
	global __plugin_implementation__
	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}