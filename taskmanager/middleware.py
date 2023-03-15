import logging
from taskmanager.models import Task

logger = logging.getLogger(__name__)

def simple_middleware(get_response):
    def middleware(request):
        # Код должен быть выполнен для каждого запроса до view
        if request.method == "POST":
            post_is_active = bool(request.POST.get('is_active', False))
            task_active = bool(Task.objects.filter(name=request.POST.get('name', None))[0].is_active)
            if task_active != post_is_active:
                logger.info('<Task active changed detected>')
                # Здесь следует отправить уведомление пользователю в телеграм, пока просто логируется событие
        response = get_response(request)
        # Код должен быть выполнен для ответа после view
        return response
    return middleware
