from rest_framework import serializers
from myglory.models import GloryHero


class GloryHeroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GloryHero
        fields = "__all__"