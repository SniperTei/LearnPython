from django.db import models

# Create your models here.

class GloryHero(models.Model):
    id = models.AutoField(primary_key=True)
    # 英雄名
    name = models.CharField(max_length=20)
    # 熟练度
    proficiency = models.IntegerField()
    # 熟练度等级
    proficiency_level = models.CharField(max_length=20)
    # 英雄头像
    image = models.CharField(max_length=100)
    # 特长
    speciality = models.CharField(max_length=20)
    # 强势期
    strong_period = models.CharField(max_length=20)
    # 生存能力
    live_ability = models.IntegerField()
    # 输出强度
    damage_ability = models.IntegerField()
    # 上手难度
    difficulty = models.IntegerField()
    # 被动技能
    passive_skill = models.CharField(max_length=100)
    # 1技能
    skill_1 = models.CharField(max_length=100)
    # 2技能
    skill_2 = models.CharField(max_length=100)
    # 3技能
    skill_3 = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return GloryHero.objects.create(**validated_data)

    def __str__(self):
        return self.name