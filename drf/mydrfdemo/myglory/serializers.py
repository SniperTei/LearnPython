from rest_framework import serializers
from myglory.models import GloryHero

class GloryHeroSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    proficiency = serializers.IntegerField()
    proficiency_level = serializers.CharField(max_length=20)
    image = serializers.CharField(max_length=100)
    speciality = serializers.CharField(max_length=20)
    strong_period = serializers.CharField(max_length=20)
    # 生存能力
    live_ability = serializers.IntegerField()
    # 输出强度
    damage_ability = serializers.IntegerField()
    # 上手难度
    difficulty = serializers.IntegerField()
    # 被动技能
    passive_skill = serializers.CharField(max_length=100)
    # 1技能
    skill_1 = serializers.CharField(max_length=100)
    # 2技能
    skill_2 = serializers.CharField(max_length=100)
    # 3技能
    skill_3 = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return GloryHero.objects.create(**validated_data)
    
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)
    class Meta:
        model = GloryHero
        fields = ('name', 'proficiency', 'proficiency_level', 'image', 'speciality', 'strong_period', 'live_ability', 'damage_ability', 'difficulty', 'passive_skill', 'skill_1', 'skill_2', 'skill_3')