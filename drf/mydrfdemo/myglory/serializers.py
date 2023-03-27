from rest_framework import serializers
from myglory.models import GloryHero


class GloryHeroSerializer(serializers.ModelSerializer):
    
    # 校验熟练度字段
    def validate_proficiency(self, value):
        if value < 0 or value > 10000:
            raise serializers.ValidationError("熟练度必须在0~10000之间")
        return value
    
    class Meta:
        model = GloryHero
        fields = "__all__"