from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
# bu serileştirmek diye türkçeleştirilmiş ama json veriyi yapıp çekmeye yarıyor
# tam olarak işlevi json yapmak sanırım