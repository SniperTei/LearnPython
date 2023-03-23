from rest_framework import serializers
from myglory.models import GloryHero

class GloryHeroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
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
    
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.proficiency = validated_data.get('proficiency', instance.proficiency)
    #     instance.proficiency_level = validated_data.get('proficiency_level', instance.proficiency_level)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.speciality = validated_data.get('speciality', instance.speciality)
    #     instance.strong_period = validated_data.get('strong_period', instance.strong_period)
    #     instance.live_ability = validated_data.get('live_ability', instance.live_ability)
    #     instance.damage_ability = validated_data.get('damage_ability', instance.damage_ability)
    #     instance.difficulty = validated_data.get('difficulty', instance.difficulty)
    #     instance.passive_skill = validated_data.get('passive_skill', instance.passive_skill)
    #     instance.skill_1 = validated_data.get('skill_1', instance.skill_1)
    #     instance.skill_2 = validated_data.get('skill_2', instance.skill_2)
    #     instance.skill_3 = validated_data.get('skill_3', instance.skill_3)
    #     instance.save()
    #     return instance
        
    
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)
    class Meta:
        model = GloryHero
        fields = ('id', 'name', 'proficiency', 'proficiency_level', 'image', 'speciality', 'strong_period', 'live_ability', 'damage_ability', 'difficulty', 'passive_skill', 'skill_1', 'skill_2', 'skill_3')