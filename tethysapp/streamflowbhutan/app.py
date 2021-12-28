from tethys_sdk.base import TethysAppBase, url_map_maker


class Streamflowbhutan(TethysAppBase):
    """
    Tethys app class for Streamflowbhutan.
    """

    name = 'ECMWF Streamflow Prediction Tool - Bhutan'
    index = 'streamflowbhutan:home'
    icon = 'streamflowbhutan/images/icon.gif'
    package = 'streamflowbhutan'
    root_url = 'streamflowbhutan'
    color = '#16a085'
    description = ''
    tags = 'ECMWF Streamflow Prediction'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='streamflowbhutan',
                controller='streamflowbhutan.controllers.index'),
            UrlMap(
                name='chart',
                url='streamflowbhutan/chart',
                controller='streamflowbhutan.controllers.chart'),
            UrlMap(
                name='forecastpercent',
                url='streamflowbhutan/forecastpercent',
                controller='streamflowbhutan.controllers.forecastpercent'),
            UrlMap(
                name='getFeatures',
                url='streamflowbhutan/api/getFeatures',
                controller='streamflowbhutan.api.getFeatures'),
            UrlMap(
                name='getreturnPeriod',
                url='streamflowbhutan/api/getreturnPeriod',
                controller='streamflowbhutan.api.getreturnPeriod'),
            UrlMap(
                name='getHistoric',
                url='streamflowbhutan/api/getHistoric',
                controller='streamflowbhutan.api.getHistoric'),
            UrlMap(
                name='getFlowDurationCurve',
                url='streamflowbhutan/api/getFlowDurationCurve',
                controller='streamflowbhutan.api.getFlowDurationCurve'),
            UrlMap(
                name='getForecast',
                url='streamflowbhutan/api/getForecast',
                controller='streamflowbhutan.api.getForecast'),
            UrlMap(
                name='getForecastCSV',
                url='streamflowbhutan/getForecastCSV',
                controller='streamflowbhutan.controllers.getForecastCSV'),
            UrlMap(
                name='getHistoricCSV',
                url='streamflowbhutan/getHistoricCSV',
                controller='streamflowbhutan.controllers.getHistoricCSV'),
        )

        return url_maps
