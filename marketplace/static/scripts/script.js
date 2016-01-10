(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

$("#region_switcher").dropdown({
    onChange: function onChange(value, text, $selectedItem) {
        $("#region_switcher_form_location_id").val(value);
        $("#region_switcher_form").submit();
    } });

$('.ui.checkbox').checkbox();
$('.dropdown').dropdown();

$('.fancybox').fancybox();

},{}]},{},[1])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCJmcm9udGVuZC9zY3JpcHRzL3NjcmlwdC5qcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTs7O0FDQUEsQ0FBQyxDQUFDLGtCQUFrQixDQUFDLENBQUMsUUFBUSxDQUFDO0FBQzNCLFlBQVEsRUFBRSxrQkFBUyxLQUFLLEVBQUUsSUFBSSxFQUFFLGFBQWEsRUFBRTtBQUMzQyxTQUFDLENBQUMsbUNBQW1DLENBQUMsQ0FBQyxHQUFHLENBQUMsS0FBSyxDQUFDLENBQUM7QUFDbEQsU0FBQyxDQUFDLHVCQUF1QixDQUFDLENBQUMsTUFBTSxFQUFFLENBQUM7S0FDM0MsRUFBQyxDQUFDLENBQUM7O0FBRUosQ0FBQyxDQUFDLGNBQWMsQ0FBQyxDQUFDLFFBQVEsRUFBRSxDQUFDO0FBQzdCLENBQUMsQ0FBQyxXQUFXLENBQUMsQ0FBQyxRQUFRLEVBQUUsQ0FBQzs7QUFFMUIsQ0FBQyxDQUFDLFdBQVcsQ0FBQyxDQUFDLFFBQVEsRUFBRSxDQUFDIiwiZmlsZSI6ImdlbmVyYXRlZC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24gZSh0LG4scil7ZnVuY3Rpb24gcyhvLHUpe2lmKCFuW29dKXtpZighdFtvXSl7dmFyIGE9dHlwZW9mIHJlcXVpcmU9PVwiZnVuY3Rpb25cIiYmcmVxdWlyZTtpZighdSYmYSlyZXR1cm4gYShvLCEwKTtpZihpKXJldHVybiBpKG8sITApO3ZhciBmPW5ldyBFcnJvcihcIkNhbm5vdCBmaW5kIG1vZHVsZSAnXCIrbytcIidcIik7dGhyb3cgZi5jb2RlPVwiTU9EVUxFX05PVF9GT1VORFwiLGZ9dmFyIGw9bltvXT17ZXhwb3J0czp7fX07dFtvXVswXS5jYWxsKGwuZXhwb3J0cyxmdW5jdGlvbihlKXt2YXIgbj10W29dWzFdW2VdO3JldHVybiBzKG4/bjplKX0sbCxsLmV4cG9ydHMsZSx0LG4scil9cmV0dXJuIG5bb10uZXhwb3J0c312YXIgaT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2Zvcih2YXIgbz0wO288ci5sZW5ndGg7bysrKXMocltvXSk7cmV0dXJuIHN9KSIsIiQoXCIjcmVnaW9uX3N3aXRjaGVyXCIpLmRyb3Bkb3duKHtcbiAgICBvbkNoYW5nZTogZnVuY3Rpb24odmFsdWUsIHRleHQsICRzZWxlY3RlZEl0ZW0pIHtcbiAgICAgICAgJChcIiNyZWdpb25fc3dpdGNoZXJfZm9ybV9sb2NhdGlvbl9pZFwiKS52YWwodmFsdWUpO1xuICAgICAgICAkKFwiI3JlZ2lvbl9zd2l0Y2hlcl9mb3JtXCIpLnN1Ym1pdCgpO1xufX0pO1xuXG4kKCcudWkuY2hlY2tib3gnKS5jaGVja2JveCgpO1xuJCgnLmRyb3Bkb3duJykuZHJvcGRvd24oKTtcblxuJCgnLmZhbmN5Ym94JykuZmFuY3lib3goKTtcbiJdfQ==
