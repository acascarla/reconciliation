from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reconciliation.models import Work
from reconciliation.serializers import WorkSerializer


class WorkView(APIView):

    def get(self, request):
        """
        Returns a single Work and it's data filtered by it's ISWC.
        Params:
        - iswc (GET): string, required.
        """
        iswc = request.GET.get('iswc')
        if not iswc:
            return self._bad_request_response()
        try:
            response = self._work_response(iswc)
        except ObjectDoesNotExist:
            response = self._work_not_found_response()
        return response

    def _bad_request_response(self):
        return Response(
            {'error': 'must provide iwsc get param'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def _work_response(self, iswc):
        work = Work.objects.get(iswc=iswc)
        serialized = WorkSerializer(work)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def _work_not_found_response(self):
        return Response(
            {'error': 'work not found'}, status=status.HTTP_404_NOT_FOUND
        )
