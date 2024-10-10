from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import RawPayload
from datetime import datetime

def send_response(message, success=True):
    return JsonResponse({
        'success': success,
        'message': message
    })

@require_GET
def rawdata(request):
    """This is a GET API to receive the raw data and store it into the raw payload table."""
    api_key = request.GET.get('api_key', None)
    
    if not api_key:
        return send_response("API KEY is required!", success=False)

    # Get the raw payload from the query string
    payload = request.META['QUERY_STRING']
    timestamp = datetime.now()

    try:
        # Create and save a new RawPayload instance
        raw_payload = RawPayload(timestamp=timestamp, payload=payload)
        raw_payload.save()
    except Exception as err:
        print(str(err))
        return send_response("Something went wrong!", success=False)

    return send_response("Data saved!")
