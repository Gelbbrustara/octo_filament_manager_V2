import octoprint.plugin
import flask
import json
import os

class FilamentManagerPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.SimpleApiPlugin):

    def __init__(self):
        self.filament_data_file = os.path.join(self.get_plugin_data_folder(), "filament_data.json")

    def on_after_startup(self):
        self._logger.info("FilamentManagerPlugin started")

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

    def get_api_commands(self):
        return dict(
            add_filament=[],
            get_filament_data=[]
        )

    def on_api_command(self, command, data):
        import flask
        if command == "add_filament":
            return self.add_filament(data)
        elif command == "get_filament_data":
            return self.get_filament_data()

    def add_filament(self, data):
        filament_data = self.load_filament_data()
        filament_data.append(data)
        self.save_filament_data(filament_data)
        return flask.jsonify(filament_data)

    def get_filament_data(self):
        filament_data = self.load_filament_data()
        return flask.jsonify(filament_data)

    def load_filament_data(self):
        if not os.path.exists(self.filament_data_file):
            return []
        with open(self.filament_data_file, 'r') as f:
            return json.load(f)

    def save_filament_data(self, data):
        with open(self.filament_data_file, 'w') as f:
            json.dump(data, f)

__plugin_name__ = "OctoPrint-Filament-Manager"
__plugin_version__ = "4.2.0"
__plugin_description__ = "A plugin to manage 3D printing filament usage"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = FilamentManagerPlugin()
