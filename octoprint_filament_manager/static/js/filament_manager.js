$(function() {
    function FilamentManagerViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];
        self.filaments = ko.observableArray([]);
        self.prints = ko.observableArray([]);

        self.newPrintName = ko.observable("");
        self.newPrintColor = ko.observable("");
        self.newPrintWeight = ko.observable(0);
        self.newPrintCost = ko.observable(0);
        self.newPrintDate = ko.observable(new Date().toISOString().split('T')[0]);

        self.loadFilamentData = function() {
            $.ajax({
                url: API_BASEURL + "plugin/filament_manager",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({command: "get_filament_data"}),
                contentType: "application/json; charset=UTF-8"
            }).done(function(data) {
                self.filaments(data.filaments);
                self.prints(data.prints);
            });
        };

        self.addPrint = function() {
            $.ajax({
                url: API_BASEURL + "plugin/filament_manager",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    command: "add_print",
                    name: self.newPrintName(),
                    color: self.newPrintColor(),
                    weight: self.newPrintWeight(),
                    cost: self.newPrintCost(),
                    date: self.newPrintDate()
                }),
                contentType: "application/json; charset=UTF-8"
            }).done(function(data) {
                self.filaments(data.filaments);
                self.prints(data.prints);
            });
        };

        self.loadFilamentData();
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: FilamentManagerViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#navbar_plugin_filament_manager", "#settings_plugin_filament_manager", "#tab_plugin_filament_manager"]
    });
});
