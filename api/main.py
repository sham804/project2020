import json
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Configure Django settings
settings.configure(
    DEBUG=False,
    ALLOWED_HOSTS=['*'],
    TEMPLATE_DIRS=['applications/templates'],
    STATIC_URL='/static/',
)

# Initialize the WSGI application
application = get_wsgi_application()

def handler(event, context):
    # Convert Vercel event format to WSGI format
    wsgi_env = {
        'REQUEST_METHOD': event['httpMethod'],
        'PATH_INFO': event['path'],
        'QUERY_STRING': event['queryStringParameters'],
        'wsgi.input': event['body'],
        'wsgi.url_scheme': 'https' if event['headers'].get('X-Forwarded-Proto', 'http') == 'https' else 'http',
    }

    # Call the WSGI application
    status, headers, body = application(wsgi_env, start_response)

    return {
        'statusCode': status,
        'headers': dict(headers),
        'body': body
    }

def start_response(status, headers):
    # This function handles the response headers
    pass
