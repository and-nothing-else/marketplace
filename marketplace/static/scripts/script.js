(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
'use strict';

$('.ui.checkbox').checkbox();
$('.dropdown').dropdown();

$("#region_switcher").dropdown({
    onChange: function onChange(value, text, $selectedItem) {
        $("#region_switcher_form_location_id").val(value);
        $("#region_switcher_form").submit();
    } });

$("#user_select_item_category").dropdown({
    onChange: function onChange(value, text, $selectedItem) {
        $('#button_next').attr("href", $selectedItem.data("next-url")).removeClass('disabled');
    } });

$('.fancybox').fancybox();
$('table.sortable').tablesort();

},{}]},{},[1])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCJmcm9udGVuZC9zY3JpcHRzL3NjcmlwdC5qcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7O0FDQUEsQ0FBQyxDQUFDLGNBQWMsQ0FBQyxDQUFDLFFBQVEsRUFBRSxDQUFDO0FBQzdCLENBQUMsQ0FBQyxXQUFXLENBQUMsQ0FBQyxRQUFRLEVBQUUsQ0FBQzs7QUFHMUIsQ0FBQyxDQUFDLGtCQUFrQixDQUFDLENBQUMsUUFBUSxDQUFDO0FBQzNCLFlBQVEsRUFBRSxrQkFBUyxLQUFLLEVBQUUsSUFBSSxFQUFFLGFBQWEsRUFBRTtBQUMzQyxTQUFDLENBQUMsbUNBQW1DLENBQUMsQ0FBQyxHQUFHLENBQUMsS0FBSyxDQUFDLENBQUM7QUFDbEQsU0FBQyxDQUFDLHVCQUF1QixDQUFDLENBQUMsTUFBTSxFQUFFLENBQUM7S0FDM0MsRUFBQyxDQUFDLENBQUM7O0FBR0osQ0FBQyxDQUFDLDRCQUE0QixDQUFDLENBQUMsUUFBUSxDQUFDO0FBQ3JDLFlBQVEsRUFBRSxrQkFBUyxLQUFLLEVBQUUsSUFBSSxFQUFFLGFBQWEsRUFBRTtBQUMzQyxTQUFDLENBQUMsY0FBYyxDQUFDLENBQ1osSUFBSSxDQUFDLE1BQU0sRUFBRSxhQUFhLENBQUMsSUFBSSxDQUFDLFVBQVUsQ0FBQyxDQUFDLENBQzVDLFdBQVcsQ0FBQyxVQUFVLENBQUMsQ0FBQztLQUNwQyxFQUFDLENBQUMsQ0FBQzs7QUFHSixDQUFDLENBQUMsV0FBVyxDQUFDLENBQUMsUUFBUSxFQUFFLENBQUM7QUFDMUIsQ0FBQyxDQUFDLGdCQUFnQixDQUFDLENBQUMsU0FBUyxFQUFFLENBQUMiLCJmaWxlIjoiZ2VuZXJhdGVkLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXNDb250ZW50IjpbIihmdW5jdGlvbiBlKHQsbixyKXtmdW5jdGlvbiBzKG8sdSl7aWYoIW5bb10pe2lmKCF0W29dKXt2YXIgYT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2lmKCF1JiZhKXJldHVybiBhKG8sITApO2lmKGkpcmV0dXJuIGkobywhMCk7dmFyIGY9bmV3IEVycm9yKFwiQ2Fubm90IGZpbmQgbW9kdWxlICdcIitvK1wiJ1wiKTt0aHJvdyBmLmNvZGU9XCJNT0RVTEVfTk9UX0ZPVU5EXCIsZn12YXIgbD1uW29dPXtleHBvcnRzOnt9fTt0W29dWzBdLmNhbGwobC5leHBvcnRzLGZ1bmN0aW9uKGUpe3ZhciBuPXRbb11bMV1bZV07cmV0dXJuIHMobj9uOmUpfSxsLGwuZXhwb3J0cyxlLHQsbixyKX1yZXR1cm4gbltvXS5leHBvcnRzfXZhciBpPXR5cGVvZiByZXF1aXJlPT1cImZ1bmN0aW9uXCImJnJlcXVpcmU7Zm9yKHZhciBvPTA7bzxyLmxlbmd0aDtvKyspcyhyW29dKTtyZXR1cm4gc30pIiwiJCgnLnVpLmNoZWNrYm94JykuY2hlY2tib3goKTtcbiQoJy5kcm9wZG93bicpLmRyb3Bkb3duKCk7XG5cblxuJChcIiNyZWdpb25fc3dpdGNoZXJcIikuZHJvcGRvd24oe1xuICAgIG9uQ2hhbmdlOiBmdW5jdGlvbih2YWx1ZSwgdGV4dCwgJHNlbGVjdGVkSXRlbSkge1xuICAgICAgICAkKFwiI3JlZ2lvbl9zd2l0Y2hlcl9mb3JtX2xvY2F0aW9uX2lkXCIpLnZhbCh2YWx1ZSk7XG4gICAgICAgICQoXCIjcmVnaW9uX3N3aXRjaGVyX2Zvcm1cIikuc3VibWl0KCk7XG59fSk7XG5cblxuJChcIiN1c2VyX3NlbGVjdF9pdGVtX2NhdGVnb3J5XCIpLmRyb3Bkb3duKHtcbiAgICBvbkNoYW5nZTogZnVuY3Rpb24odmFsdWUsIHRleHQsICRzZWxlY3RlZEl0ZW0pIHtcbiAgICAgICAgJCgnI2J1dHRvbl9uZXh0JylcbiAgICAgICAgICAgIC5hdHRyKFwiaHJlZlwiLCAkc2VsZWN0ZWRJdGVtLmRhdGEoXCJuZXh0LXVybFwiKSlcbiAgICAgICAgICAgIC5yZW1vdmVDbGFzcygnZGlzYWJsZWQnKTtcbn19KTtcblxuXG4kKCcuZmFuY3lib3gnKS5mYW5jeWJveCgpO1xuJCgndGFibGUuc29ydGFibGUnKS50YWJsZXNvcnQoKTtcbiJdfQ==
