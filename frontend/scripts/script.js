$('.ui.checkbox').checkbox();
$('.dropdown').dropdown();


$("#region_switcher").dropdown({
    onChange: function(value, text, $selectedItem) {
        $("#region_switcher_form_location_id").val(value);
        $("#region_switcher_form").submit();
}});


$("#user_select_item_category").dropdown({
    onChange: function(value, text, $selectedItem) {
        $('#button_next')
            .attr("href", $selectedItem.data("next-url"))
            .removeClass('disabled');
}});


$(".item_size").popup();


$('.fancybox').fancybox();
$('table.sortable').tablesort();

