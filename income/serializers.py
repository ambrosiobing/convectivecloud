from rest_framework import serializers
from income.models import Adult

class AdultSerializer(serializers.HyperlinkedModelSerializer):
    age = serializers.ChoiceField(
        choices=Adult.AGE_CHOICES
    )

    class Meta:
        model = Adult
        fields = (
            'age'
        )