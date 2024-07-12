import octoprint.plugin

class FilamentManagerPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("Octo Filament Manager Plugin started")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return {
            "js": ["js/filament_manager.js"],
            "css": ["css/filament_manager.css"],
            "less": ["less/filament_manager.less"]
        }

__plugin_name__ = "Octo Filament Manager"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A plugin to manage 3D printing filament usage"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = FilamentManagerPlugin()
