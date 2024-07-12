// filament_manager/static/js/filament_manager.js
$(function() {
    function updateFilamentList(filamentData) {
        var filamentList = $("#filament_list");
        filamentList.empty();
        filamentData.forEach(function(filament) {
            var filamentItem = $("<div>").addClass("filament-item");
            var filamentColor = $("<div>").addClass("filament-color").css("background-color", filament.color);
            var filamentName = $("<div>").addClass("filament-name").text(filament.name);
            var filamentBar = $("<div>").addClass("filament-bar").css("width", filament.usage + "%");
            filamentItem.append(filamentColor, filamentName, filamentBar);
            filamentList.append(filamentItem);
        });
    }

    function fetchFilamentData() {
        $.get("/plugin/filament_manager/get_filament_data", function(response) {
            updateFilamentList(response.filament_data);
        });
    }

    $("#add_filament_form").submit(function(event) {
        event.preventDefault();
        var formData = {
            name: $("#filament_name").val(),
            color: $("#filament_color").val(),
            usage: $("#filament_usage").val()
        };
        $.ajax({
            url: "/plugin/filament_manager/add_filament",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function(response) {
                if (response.success) {
                    fetchFilamentData();
                    $("#add_filament_form")[0].reset();
                }
            }
        });
    });

    fetchFilamentData();
});
