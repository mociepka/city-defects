var App = App || {};

App.Defect = Backbone.Model.extend({
    initialize: function(opts) {
        this.point = new google.maps.LatLng(opts.lat, opts.lng);
        this.marker = new google.maps.Marker({
                position : this.point,
                //icon: '/static/store_locator/' + opts.type + 'marker.png'
        });
    }
});

App.Defects = Backbone.Collection.extend({
    model: App.Defect
});

App.MapView = Backbone.View.extend({
    initialize : function(opts) {
        var that = this;
        this.map = new google.maps.Map(this.el, {
            center : new google.maps.LatLng(this.$el.data('lat'), this.$el.data('lng')),
            zoom : this.$el.data('zoom'),
            mapTypeId : google.maps.MapTypeId.ROADMAP
        });
        this.collection.each(function(defect) {
            defect.marker.setMap(that.map);
        });
    }
});
