odoo.define('clf_dashboard.trip_geo', function (require) {
    "use strict";

    const trip = require('clf_dashboard.DashboardRewrite');
    var core = require('web.core');
    var _t = core._t;
    // alert('hiiiiiiiiiiiiiii')
    trip.include({
        start_work_trip(){
            // alert('kkkkkkkk')
            var self = this;
            var options = {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            };
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(self.update_work_trip.bind(self), self._getPositionError, options);
            }
        },
        update_work_trip(position){
            var self = this;
            alert(position.coords.latitude)
            this._rpc({
                model: 'hr.employee',
                method: 'update_work_trip',
                args: [[self.login_employee.id],'start',this.$( ".reasons" ).val(), [position.coords.latitude, position.coords.longitude]],
            })
            .then(function(result) {
                var trip_state =self.login_employee.trip_state;
                var message = ''
                var action_client = {
                    type: "ir.actions.client",
                    name: _t('لوحة المعلومات'),
                    tag: 'hr_dashboard',
                };
                self.do_action(action_client, {clear_breadcrumbs: true});
                if (trip_state == 'start'){
                    message = 'تأمل لك رحلة سالمة'
                }
                else if (trip_state == 'end'){
                    message = 'ترحب بعودتك'
                }
                self.trigger_up('show_effect', {
                    message: ("شركة المدينة للمحاماة والاستشارات القانونية " + message),
                    type: 'rainbow_man'
                });
            });
        },
// end
        end_work_trip(){
            var self = this;
            var options = {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            };
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(self.update_end_work_trip.bind(self), self._getPositionError, options);
            }
        },
        update_end_work_trip(position){
            var self = this;
            this._rpc({
                model: 'hr.employee',
                method: 'update_work_trip',
                args: [[self.login_employee.id],'end',this.$( ".reasons" ).val(), [position.coords.latitude, position.coords.longitude]],
            })
            .then(function(result) {
                var trip_state =self.login_employee.trip_state;
                var message = ''
                var action_client = {
                    type: "ir.actions.client",
                    name: _t('لوحة المعلومات'),
                    tag: 'hr_dashboard',
                };
                self.do_action(action_client, {clear_breadcrumbs: true});
                if (trip_state == 'start'){
                    message = 'تأمل لك رحلة سالمة'
                }
                else if (trip_state == 'end'){
                    message = 'ترحب بعودتك'
                }
                self.trigger_up('show_effect', {
                    message: _t("شركة المدينة للمحاماة والاستشارات القانونية " + message),
                    type: 'rainbow_man'
                });
            });
        },

        _getPositionError(err) {
            alert("يجب أن تسمح بالوصول إلى موقعك")
        },
    });

});
