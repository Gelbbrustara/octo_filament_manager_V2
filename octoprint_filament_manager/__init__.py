import octoprint.plugin
import os
import json

class FilamentManagerPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.SimpleApiPlugin):

    def __init__(self):
        self.filament_data_file = self._basefolder + "/filament_data.json"
        if not os.path.exists(self.filament_data_file):
            with open(self.filament_data_file, 'w') as f:
                json.dump({"prints": [], "filaments": []}, f)

    def on_after_startup(self):
        self._logger.info("Octo Filament Manager Plugin started")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False),
            dict(type="tab", custom_bindings=False)
        ]

    def get_assets(self):
        return {
            "js": ["js/filament_manager.js"],
            "css": ["css/filament_manager.css"]
        }

    def get_api_commands(self):
        return dict(
            add_print=["name", "color", "weight", "cost"],
            get_filament_data=[]
        )

    def on_api_command(self, command, data):
        if command == "add_print":
            return self.add_print(data)
        elif command == "get_filament_data":
            return self.get_filament_data()

    def add_print(self, data):
        with open(self.filament_data_file, 'r') as f:
            filament_data = json.load(f)

        new_print = {
            "name": data["name"],
            "color": data["color"],
            "weight": float(data["weight"]),
            "cost": float(data["cost"]),
            "date": data["date"]
        }

        filament_data["prints"].append(new_print)
        filament_data["prints"] = sorted(filament_data["prints"], key=lambda x: (x["color"], -x["date"]))

        with open(self.filament_data_file, 'w') as f:
            json.dump(filament_data, f)

        return flask.jsonify(filament_data)

    def get_filament_data(self):
        with open(self.filament_data_file, 'r') as f:
            filament_data = json.load(f)
        return flask.jsonify(filament_data)

__plugin_name__ = "Octo Filament Manager"
__plugin_version__ = "4.2.0"
__plugin_description__ = "A plugin to manage 3D printing filament usage"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = FilamentManagerPlugin()
