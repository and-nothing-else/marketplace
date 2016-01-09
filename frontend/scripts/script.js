$("#region_switcher").dropdown({
    onChange: function(value, text, $selectedItem) {
        $("#region_switcher_form_location_id").val(value);
        $("#region_switcher_form").submit();
}});

$('.ui.checkbox').checkbox();
$('.dropdown').dropdown();
