!function r(o,e,n){function t(c,u){if(!e[c]){if(!o[c]){var f="function"==typeof require&&require;if(!u&&f)return f(c,!0);if(i)return i(c,!0);var a=new Error("Cannot find module '"+c+"'");throw a.code="MODULE_NOT_FOUND",a}var s=e[c]={exports:{}};o[c][0].call(s.exports,function(r){var e=o[c][1][r];return t(e?e:r)},s,s.exports,r,o,e,n)}return e[c].exports}for(var i="function"==typeof require&&require,c=0;c<n.length;c++)t(n[c]);return t}({1:[function(r,o,e){"use strict";$(".ui.checkbox").checkbox(),$(".dropdown").dropdown(),$("#region_switcher").dropdown({onChange:function(r,o,e){$("#region_switcher_form_location_id").val(r),$("#region_switcher_form").submit()}}),$(".fancybox").fancybox(),$("table.sortable").tablesort()},{}]},{},[1]);