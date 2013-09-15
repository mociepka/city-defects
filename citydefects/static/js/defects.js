var App = App || {};

App.Defect = Backbone.Model.extend({
    url: '/api/defects/',
    initialize: function(opts) {
        this.point = new google.maps.LatLng(opts.lat, opts.lng);
        this.marker = new google.maps.Marker({
                position : this.point,
                //icon: '/static/store_locator/' + opts.type + 'marker.png'
        });
    }
});

App.Defects = Backbone.Collection.extend({
    url: '/api/defects/',
    model: App.Defect
});

App.DefectView = Backbone.View.extend({
    template: function(context) {
        return _.template($('#defect-tmpl').html())(context);
    },
    initialize : function(opts) {
        var that = this;
        google.maps.event.addListener(this.model.marker, 'click', function(e) {
            that.clickMarker(e);
        });
    },
    clickMarker: function(e) {
        this.render();
    },
    render: function() {
        this.$el.html(this.template({
            defect: this.model
        }));
        return this;
    },
});

App.MapView = Backbone.View.extend({
    defectsViews : undefined,
    initialize : function(opts) {
        var that = this;
        this.defectEl = opts.defectEl;
        this.defectsViews = {};
        this.map = new google.maps.Map(this.el, {
            center : new google.maps.LatLng(this.$el.data('lat'), this.$el.data('lng')),
            zoom : this.$el.data('zoom'),
            mapTypeId : google.maps.MapTypeId.ROADMAP
        });
        this.listenTo(this.collection, 'all', this.test);
        this.listenTo(this.collection, 'add', this.addDefect);
    },
    addDefect : function(defect, collection, options) {
        defect.marker.setMap(this.map);
        this.defectsViews[defect.cid] = new App.DefectView({
            model: defect,
            el: this.defectEl
        });
    },
    test: function() {
        console.log(arguments);
    },
});

App.HeaderView = Backbone.View.extend({
    initialize : function(opts) {
        var that = this;
        this.listenTo(this.collection, 'sync', this.render);
        this.listenTo(this.collection, 'error', this.error);
        this.listenTo(this.collection, 'all', this.test);
    },
    events : {
        'submit form': function(e) {
            this.collection.create({
                title: this.$('#id_title').val(),
                description: this.$('#id_description').val(),
                street: this.$('#id_street').val(),
                lat: this.$('#id_lat').val(),
                lng: this.$('#id_lng').val(),
                tags: this.$('#id_tags').val()
            });
            e.preventDefault();
        }
    },
    test: function() {
        console.log(arguments);
    },
    error: function(model, xhr, option) {
        if (xhr.status == 400) {
            this.errors = JSON.parse(xhr.responseText);
        } else if (xhr.status == 500) {
            this.errors = {};
            this.errors[App.NFE] = 'Server error';
        }
        this.render();
    },
    render: function() {
        var that = this;
        this.$('.form-group').removeClass('has-error');
        if (this.errors) {
            _.each(this.errors, function(error, name) {
                if (name == App.NFE) {
                    that.$('form').prepend('<p class="text-error">' + error + '</p>');
                } else {
                    var $field = this.$('#id_' + name).parents('.form-group');
                    $field.addClass('has-error');
                    $field.append('<span class="help-block">' + error + '</span>');
                }
            });
            this.errors = null;
        }
        return this;
    },
});

// set csrf token to header for saveing models
(function($){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
        }
    });
})(jQuery);
