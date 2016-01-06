$(function(){
    $('.addresspicker-widget').each(function(){
        var $widget = $(this),
            $latlng = $widget.find('.addresspicker-coords'),
            $zoom = $widget.find('.addresspicker-zoom'),
            $result = $widget.find('.addresspicker-result'),
            $map = $widget.find('.addresspicker-map'),
            $searchField = $widget.find('.addresspicker-search'),
            lat = $widget.find('.addresspicker-initial-lat').val(),
            lng = $widget.find('.addresspicker-initial-lng').val(),
            zoom = parseInt($widget.find('.addresspicker-initial-zoom').val()),
            addresspickerMap = $searchField.addresspicker({
                elements: {
                    map: $map,
                    latlng: $latlng,
                    zoom: $zoom,
                    result: $result
                },
                mapOptions: {
                    zoom: zoom,
                    center: new google.maps.LatLng(lat, lng)
                }
            }),
            marker = addresspickerMap.addresspicker("marker")
        marker.setVisible(true)
        addresspickerMap.addresspicker("updatePosition")
    })
})
