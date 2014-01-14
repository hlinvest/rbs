from django.conf.urls import patterns, include, url

from django.contrib import admin
urlpatterns = patterns('',
    (r'^$', 'rr.r.views.index'),
    (r'^reservation_day/$', 'rr.r.views.reservation_day'),
    (r'^reservation_day_result/$', 'rr.r.views.reservation_day_result'),
#    (r'^reservation_hour/$', 'rr.r.views.reservation_hour'),
    (r'^reservation_hour_result/$', 'rr.r.views.reservation_hour_result'),
#    (r'^reservation_table/$', 'rr.r.views.reservation_table'),
    (r'^reservation_table_result/$', 'rr.r.views.reservation_table_result'),
#    (r'^reservation_customer/$', 'rr.r.views.reservation_customer'),
    (r'^reservation_customer_result/$', 'rr.r.views.reservation_customer_result'),
    
    
    (r'^admin/typical_day/$', 'rr.r.views.admin_typical_day'),
    (r'^admin/typical_day_result/$', 'rr.r.views.admin_typical_day_result'),
    (r'^admin/typical_week/$', 'rr.r.views.admin_typical_week'),
    (r'^admin/typical_week_result/$', 'rr.r.views.admin_typical_week_result'),
    (r'^admin/table_map/$', 'rr.r.views.admin_table_map'),
    (r'^admin/table_map_result/$', 'rr.r.views.admin_table_map_result'),
    (r'^admin/', include(admin.site.urls)),
)