sixieskel.pyramid
=================

This package contains a set of Pyramid application templates for quickly getting started on Pyramid applications.

 * `sfu_pyramid_basic` - A very basic template that doesn't make assumptions about the type of persistence that will be used.
 * `sfu_pyramid_alchemy` - Application template that provides some basic SQLAlchemy configuration.
 * `sfu_pyramid_zodb` - Application template setting up ZODB connections and imports.

Features in Common
==================

 * **TemplateAPI class** - A class that is meant to provide an API to various sections of the application within rendered templates.
 * **api** template variable - An instance of the TemplateAPI class that is provided to any renderer engine registered with Pyramid.
 * **register_api** subscriber function - A BeforeRender subscriber that attaches the `api` variable to template environments.
