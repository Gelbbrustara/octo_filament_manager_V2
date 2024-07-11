# filament_manager/plugin.py
from octoprint.plugin import OctoPrintPlugin, template_plugin

class FilamentManagerPlugin(OctoPrintPlugin):
    def on_after_startup(self):
        self._logger.info("Filament Manager Plugin started!")

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False),
            dict(type="tab", custom_bindings=False),
            dict(type="generic", template="filament_manager.jinja2", custom_bindings=False),
        ]

    def get_assets(self):
        return dict(
            js=["js/filament_manager.js"],
            css=["css/filament_manager.css"],
        )

    def get_update_information(self):
        return dict(
            filament_manager=dict(
                displayName="Filament Manager Plugin",
                displayVersion=self._plugin_version,
                type="github_release",
                user="your_username",
                repo="your_repository",
                current=self._plugin_version,
                pip="https://github.com/your_username/your_repository/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Filament Manager"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = FilamentManagerPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
