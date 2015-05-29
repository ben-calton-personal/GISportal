/*------------------------------------*\
    Configuration
    This file is for the configuration
    of the GIS Portal.

    browseCategories - Used to define
    which categories to be shown in the
    browse panel. This is currently
    limited to 2.
\*------------------------------------*/

gisportal.config = {
   siteMode: "production", //(development|production)
   browseCategories : {
      "indicator_type" : "Indicator Type",
      "data_provider" : "Data Provider",
      "model": "Model Name",
      "data_type" : "Data Type",
      "interval": "Interval",
      "region" : "Region"
   },
   browseMode : 'selectlist',                       // (tabs|selectlist) tabs (default) = original method of 3 tabs; selectlist = makes all available categories selectable from a drop down list
   defaultCategory: '',                     // only used when browseMode = selectlist; any key value from browseCategories
   //  Skip start screen only is the user has a saved state, requires T&C
   autoResumeSavedState: false,
   // Always skip the welcome page, also skips T&C
   skipWelcomePage: false,
   // Do we require terms and conditions agreement to use the port
   requiresTermsAndCondictions: true,
   paths: {
    graphServer: 'https://wci.earth2observe.eu/plotting',
    middlewarePath: '/service'
   },
   countryBorder : {
      'defaultLayer' : 'countries_all_white',      // (countries_all_white|countries_all_black|countries_all_blue)
      'alwaysVisible' : true                      // (true|false)  > If true the defaultLayer will be visible at page load
   },
   defaultBaseMap: 'EOX',

   // Should layers auto scale by default
   autoScale: true,
   requiresTermsAndCondictions: true,
   
   // Deny access to older browsers
   // none=Allow, advisory=Tell them only, strict=Stop them
   browserRestristion: "strict" //(none|advisory|strict)
   
};
