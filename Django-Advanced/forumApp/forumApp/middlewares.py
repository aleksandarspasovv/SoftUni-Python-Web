import time

from django.utils.deprecation import MiddlewareMixin


def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()

        print(f'Time of execution {end_time - start_time}')

        return response

    return middleware


class MeasureResponseTime(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_respond(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f'total time {total_time}')
        return response