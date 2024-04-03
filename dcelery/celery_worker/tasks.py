from celery import shared_task
import requests
from django.core.cache import cache
from .models import ScrapeData
import logging

# Configure logger
logger = logging.getLogger(__name__)

@shared_task
def scrape_proxies():
    try:
        logger.info("Starting the scrape_proxies task")

        api_url = 'https://proxylist.geonode.com/api/proxy-list?limit=10&page=1&sort_by=lastChecked&sort_type=desc'

        current_page = cache.get('current_proxy_page', 1)

        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            for proxy in data.get('data', []):
                ip = proxy.get('ip')
                port = proxy.get('port')
                protocol = ','.join(proxy.get('protocols', []))
                country = proxy.get('country')
                uptime = proxy.get('upTime', '')

                logger.info(f"Saved proxy: {ip}:{port}:{protocol}:{country}:{uptime}")

                ScrapeData.objects.update_or_create(
                    ip=ip,
                    port=port,
                    defaults={'protocol': protocol, 'country': country, 'uptime': uptime}
                )
            cache.set('current_proxy_page', current_page + 1, None)
            
        else:
            logger.error(f"Failed to fetch data from the API with status code: {response.status_code}")

    except Exception as e:
        logger.error(f"Error occurred in scrape_proxies task: {e}")
        raise 