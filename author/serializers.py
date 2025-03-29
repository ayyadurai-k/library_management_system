from author.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def validate(self, data):
        if data["age"] < 20 or data["age"] > 60:
            raise serializers.ValidationError(
                "Age should be greater 20 and less than or equal to 60"
            )
        
        
        return data
